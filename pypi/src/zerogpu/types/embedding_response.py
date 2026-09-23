import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embedding import Embedding
from .embedding_usage import EmbeddingUsage


class EmbeddingResponse(UniversalBaseModel):
    """
    OpenAI-compatible embedding list. `data[i].index` maps each vector back to its input.
    """

    object: typing.Optional[str] = None
    data: typing.Optional[typing.List[Embedding]] = None
    model: typing.Optional[str] = None
    usage: typing.Optional[EmbeddingUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

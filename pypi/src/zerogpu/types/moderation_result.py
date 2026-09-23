import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ModerationResult(UniversalBaseModel):
    """
    The verdict for one input. Category keys follow OpenAI's names, e.g. `harassment/threatening`.
    """

    flagged: typing.Optional[bool] = None
    categories: typing.Optional[typing.Dict[str, bool]] = None
    category_scores: typing.Optional[typing.Dict[str, float]] = None
    category_applied_input_types: typing.Optional[typing.Dict[str, typing.List[str]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

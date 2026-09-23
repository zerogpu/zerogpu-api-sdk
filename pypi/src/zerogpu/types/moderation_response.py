import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .moderation_result import ModerationResult


class ModerationResponse(UniversalBaseModel):
    """
    OpenAI-compatible moderations envelope. One `results` entry per input.
    """

    id: typing.Optional[str] = None
    model: typing.Optional[str] = None
    results: typing.Optional[typing.List[ModerationResult]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow

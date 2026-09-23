# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .chat_completion_response import ChatCompletionResponse
    from .chat_message import ChatMessage
    from .chat_message_role import ChatMessageRole
    from .embedding import Embedding
    from .embedding_response import EmbeddingResponse
    from .embedding_usage import EmbeddingUsage
    from .error_response import ErrorResponse
    from .input_message import InputMessage
    from .input_message_role import InputMessageRole
    from .moderation_response import ModerationResponse
    from .moderation_result import ModerationResult
    from .output_content_block import OutputContentBlock
    from .output_message import OutputMessage
    from .response import Response
    from .text_response_config import TextResponseConfig
    from .text_response_config_format import TextResponseConfigFormat
    from .token_usage import TokenUsage
    from .transcription_response import TranscriptionResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ChatCompletionResponse": ".chat_completion_response",
    "ChatMessage": ".chat_message",
    "ChatMessageRole": ".chat_message_role",
    "Embedding": ".embedding",
    "EmbeddingResponse": ".embedding_response",
    "EmbeddingUsage": ".embedding_usage",
    "ErrorResponse": ".error_response",
    "InputMessage": ".input_message",
    "InputMessageRole": ".input_message_role",
    "ModerationResponse": ".moderation_response",
    "ModerationResult": ".moderation_result",
    "OutputContentBlock": ".output_content_block",
    "OutputMessage": ".output_message",
    "Response": ".response",
    "TextResponseConfig": ".text_response_config",
    "TextResponseConfigFormat": ".text_response_config_format",
    "TokenUsage": ".token_usage",
    "TranscriptionResponse": ".transcription_response",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "ChatCompletionResponse",
    "ChatMessage",
    "ChatMessageRole",
    "Embedding",
    "EmbeddingResponse",
    "EmbeddingUsage",
    "ErrorResponse",
    "InputMessage",
    "InputMessageRole",
    "ModerationResponse",
    "ModerationResult",
    "OutputContentBlock",
    "OutputMessage",
    "Response",
    "TextResponseConfig",
    "TextResponseConfigFormat",
    "TokenUsage",
    "TranscriptionResponse",
]

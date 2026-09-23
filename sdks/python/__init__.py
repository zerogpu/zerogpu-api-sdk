# isort: skip_file

import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .audio import CreateTranscriptionResult, SpeechResponseFormat, TranscriptionResponseFormat
    from .client import AsyncZerogpuApi, ZerogpuApi
    from .embeddings import CreateEmbeddingRequestInput
    from .environment import ZerogpuApiEnvironment
    from .errors import BadRequestError, ForbiddenError, InternalServerError, MethodFailureError, UnauthorizedError
    from .moderations import CreateModerationRequestInput
    from .responses import CreateResponseRequestInput
    from .types import (
        ChatCompletionResponse,
        ChatMessage,
        ChatMessageRole,
        Embedding,
        EmbeddingResponse,
        EmbeddingUsage,
        ErrorResponse,
        InputMessage,
        InputMessageRole,
        ModerationResponse,
        ModerationResult,
        OutputContentBlock,
        OutputMessage,
        Response,
        TextResponseConfig,
        TextResponseConfigFormat,
        TokenUsage,
        TranscriptionResponse,
    )
    from . import audio, chat, embeddings, moderations, responses
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncZerogpuApi": ".client",
    "BadRequestError": ".errors",
    "ChatCompletionResponse": ".types",
    "ChatMessage": ".types",
    "ChatMessageRole": ".types",
    "CreateEmbeddingRequestInput": ".embeddings",
    "CreateModerationRequestInput": ".moderations",
    "CreateResponseRequestInput": ".responses",
    "CreateTranscriptionResult": ".audio",
    "Embedding": ".types",
    "EmbeddingResponse": ".types",
    "EmbeddingUsage": ".types",
    "ErrorResponse": ".types",
    "ForbiddenError": ".errors",
    "InputMessage": ".types",
    "InputMessageRole": ".types",
    "InternalServerError": ".errors",
    "MethodFailureError": ".errors",
    "ModerationResponse": ".types",
    "ModerationResult": ".types",
    "OutputContentBlock": ".types",
    "OutputMessage": ".types",
    "Response": ".types",
    "SpeechResponseFormat": ".audio",
    "TextResponseConfig": ".types",
    "TextResponseConfigFormat": ".types",
    "TokenUsage": ".types",
    "TranscriptionResponse": ".types",
    "TranscriptionResponseFormat": ".audio",
    "UnauthorizedError": ".errors",
    "ZerogpuApi": ".client",
    "ZerogpuApiEnvironment": ".environment",
    "audio": ".audio",
    "chat": ".chat",
    "embeddings": ".embeddings",
    "moderations": ".moderations",
    "responses": ".responses",
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
    "AsyncZerogpuApi",
    "BadRequestError",
    "ChatCompletionResponse",
    "ChatMessage",
    "ChatMessageRole",
    "CreateEmbeddingRequestInput",
    "CreateModerationRequestInput",
    "CreateResponseRequestInput",
    "CreateTranscriptionResult",
    "Embedding",
    "EmbeddingResponse",
    "EmbeddingUsage",
    "ErrorResponse",
    "ForbiddenError",
    "InputMessage",
    "InputMessageRole",
    "InternalServerError",
    "MethodFailureError",
    "ModerationResponse",
    "ModerationResult",
    "OutputContentBlock",
    "OutputMessage",
    "Response",
    "SpeechResponseFormat",
    "TextResponseConfig",
    "TextResponseConfigFormat",
    "TokenUsage",
    "TranscriptionResponse",
    "TranscriptionResponseFormat",
    "UnauthorizedError",
    "ZerogpuApi",
    "ZerogpuApiEnvironment",
    "audio",
    "chat",
    "embeddings",
    "moderations",
    "responses",
]

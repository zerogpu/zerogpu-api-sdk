import typing

from ...types.transcription_response import TranscriptionResponse

# `json` / `verbose_json` parse to TranscriptionResponse; `text`, `srt`, and `vtt` return the raw string.
CreateTranscriptionResult = typing.Union[TranscriptionResponse, str]

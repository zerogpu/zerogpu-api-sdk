import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAudioClient, RawAudioClient
from .types.create_transcription_result import CreateTranscriptionResult
from .types.speech_response_format import SpeechResponseFormat
from .types.transcription_response_format import TranscriptionResponseFormat

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AudioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAudioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAudioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAudioClient
        """
        return self._raw_client

    def create_transcription(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[TranscriptionResponseFormat] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        timestamp_granularities: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTranscriptionResult:
        """
        Transcribe audio into text with `whisper-tiny`. Files up to 25 MB and 10 minutes.

        Parameters
        ----------
        file : core.File
            The audio file to transcribe: bytes, an open binary file, or a `(filename, content)` tuple.

        model : typing.Optional[str]
            Model identifier. Defaults to `whisper-tiny`.

        language : typing.Optional[str]
            ISO-639-1 code, such as `en`. Detected automatically when omitted.

        prompt : typing.Optional[str]
            Text to guide spelling and style, such as names or jargon.

        response_format : typing.Optional[TranscriptionResponseFormat]
            `json` (default) and `verbose_json` return a `TranscriptionResponse`; `text`, `srt`, and `vtt` return a string.

        temperature : typing.Optional[float]
            Sampling temperature, 0 to 1.

        timestamp_granularities : typing.Optional[typing.Sequence[str]]
            `segment` (default), `word`, or both. Requires `verbose_json`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTranscriptionResult
            A `TranscriptionResponse` for JSON formats, otherwise the transcript as a string.

        Examples
        --------
        from zerogpu import ZerogpuApi

        client = ZerogpuApi(
            api_key="YOUR_API_KEY",
        )
        with open("speech.mp3", "rb") as f:
            client.audio.create_transcription(
                file=f,
            )
        """
        _response = self._raw_client.create_transcription(
            file=file,
            model=model,
            language=language,
            prompt=prompt,
            response_format=response_format,
            temperature=temperature,
            timestamp_granularities=timestamp_granularities,
            request_options=request_options,
        )
        return _response.data

    def create_speech(
        self,
        *,
        input: str,
        model: typing.Optional[str] = OMIT,
        voice: typing.Optional[str] = OMIT,
        response_format: typing.Optional[SpeechResponseFormat] = OMIT,
        seed: typing.Optional[int] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        repetition_penalty: typing.Optional[float] = OMIT,
        voice_sample: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bytes:
        """
        Generate speech from text with `chatterbox-nano`. Pass `voice_sample` to clone a voice.

        Parameters
        ----------
        input : str
            The text to speak, up to 2000 characters. Inline tags such as `[laugh]` add paralinguistic cues.

        model : typing.Optional[str]
            Model identifier. Defaults to `chatterbox-nano`.

        voice : typing.Optional[str]
            OpenAI voice names are accepted and all map to the built-in voice.

        response_format : typing.Optional[SpeechResponseFormat]
            `mp3` (default), `opus`, `aac`, `flac`, `wav`, or `pcm` (raw 16-bit little-endian mono at 24 kHz).

        seed : typing.Optional[int]
            Pins sampling for repeatable output (best-effort).

        temperature : typing.Optional[float]
            Sampling temperature, 0 to 2.

        top_p : typing.Optional[float]
            Nucleus sampling, 0 to 1.

        top_k : typing.Optional[int]
            Top-k sampling.

        repetition_penalty : typing.Optional[float]
            Penalty on repeated speech tokens, 1 to 4.

        voice_sample : typing.Optional[core.File]
            Reference clip to clone a voice from (up to 10 MB and 30 seconds). Overrides `voice`. Not stored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bytes
            The audio file, encoded as `response_format`.

        Examples
        --------
        from zerogpu import ZerogpuApi

        client = ZerogpuApi(
            api_key="YOUR_API_KEY",
        )
        audio = client.audio.create_speech(
            input="Hey, how are you today?",
        )
        """
        _response = self._raw_client.create_speech(
            input=input,
            model=model,
            voice=voice,
            response_format=response_format,
            seed=seed,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
            voice_sample=voice_sample,
            request_options=request_options,
        )
        return _response.data


class AsyncAudioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAudioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAudioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAudioClient
        """
        return self._raw_client

    async def create_transcription(
        self,
        *,
        file: core.File,
        model: typing.Optional[str] = OMIT,
        language: typing.Optional[str] = OMIT,
        prompt: typing.Optional[str] = OMIT,
        response_format: typing.Optional[TranscriptionResponseFormat] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        timestamp_granularities: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTranscriptionResult:
        """
        Transcribe audio into text with `whisper-tiny`. Files up to 25 MB and 10 minutes.

        Parameters
        ----------
        file : core.File
            The audio file to transcribe: bytes, an open binary file, or a `(filename, content)` tuple.

        model : typing.Optional[str]
            Model identifier. Defaults to `whisper-tiny`.

        language : typing.Optional[str]
            ISO-639-1 code, such as `en`. Detected automatically when omitted.

        prompt : typing.Optional[str]
            Text to guide spelling and style, such as names or jargon.

        response_format : typing.Optional[TranscriptionResponseFormat]
            `json` (default) and `verbose_json` return a `TranscriptionResponse`; `text`, `srt`, and `vtt` return a string.

        temperature : typing.Optional[float]
            Sampling temperature, 0 to 1.

        timestamp_granularities : typing.Optional[typing.Sequence[str]]
            `segment` (default), `word`, or both. Requires `verbose_json`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTranscriptionResult
            A `TranscriptionResponse` for JSON formats, otherwise the transcript as a string.

        Examples
        --------
        import asyncio

        from zerogpu import AsyncZerogpuApi

        client = AsyncZerogpuApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            with open("speech.mp3", "rb") as f:
                await client.audio.create_transcription(
                    file=f,
                )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_transcription(
            file=file,
            model=model,
            language=language,
            prompt=prompt,
            response_format=response_format,
            temperature=temperature,
            timestamp_granularities=timestamp_granularities,
            request_options=request_options,
        )
        return _response.data

    async def create_speech(
        self,
        *,
        input: str,
        model: typing.Optional[str] = OMIT,
        voice: typing.Optional[str] = OMIT,
        response_format: typing.Optional[SpeechResponseFormat] = OMIT,
        seed: typing.Optional[int] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        top_p: typing.Optional[float] = OMIT,
        top_k: typing.Optional[int] = OMIT,
        repetition_penalty: typing.Optional[float] = OMIT,
        voice_sample: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bytes:
        """
        Generate speech from text with `chatterbox-nano`. Pass `voice_sample` to clone a voice.

        Parameters
        ----------
        input : str
            The text to speak, up to 2000 characters. Inline tags such as `[laugh]` add paralinguistic cues.

        model : typing.Optional[str]
            Model identifier. Defaults to `chatterbox-nano`.

        voice : typing.Optional[str]
            OpenAI voice names are accepted and all map to the built-in voice.

        response_format : typing.Optional[SpeechResponseFormat]
            `mp3` (default), `opus`, `aac`, `flac`, `wav`, or `pcm` (raw 16-bit little-endian mono at 24 kHz).

        seed : typing.Optional[int]
            Pins sampling for repeatable output (best-effort).

        temperature : typing.Optional[float]
            Sampling temperature, 0 to 2.

        top_p : typing.Optional[float]
            Nucleus sampling, 0 to 1.

        top_k : typing.Optional[int]
            Top-k sampling.

        repetition_penalty : typing.Optional[float]
            Penalty on repeated speech tokens, 1 to 4.

        voice_sample : typing.Optional[core.File]
            Reference clip to clone a voice from (up to 10 MB and 30 seconds). Overrides `voice`. Not stored.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bytes
            The audio file, encoded as `response_format`.

        Examples
        --------
        import asyncio

        from zerogpu import AsyncZerogpuApi

        client = AsyncZerogpuApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            audio = await client.audio.create_speech(
                input="Hey, how are you today?",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_speech(
            input=input,
            model=model,
            voice=voice,
            response_format=response_format,
            seed=seed,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            repetition_penalty=repetition_penalty,
            voice_sample=voice_sample,
            request_options=request_options,
        )
        return _response.data

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.raise_error_response import raise_error_response
from ..core.request_options import RequestOptions
from ..types.transcription_response import TranscriptionResponse
from .types.create_transcription_result import CreateTranscriptionResult
from .types.speech_response_format import SpeechResponseFormat
from .types.transcription_response_format import TranscriptionResponseFormat
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


def _transcription_request(
    *,
    file: core.File,
    model: typing.Optional[str],
    language: typing.Optional[str],
    prompt: typing.Optional[str],
    response_format: typing.Optional[TranscriptionResponseFormat],
    temperature: typing.Optional[float],
    timestamp_granularities: typing.Optional[typing.Sequence[str]],
    request_options: typing.Optional[RequestOptions],
) -> typing.Dict[str, typing.Any]:
    return dict(
        method="POST",
        data={
            "model": model,
            "language": language,
            "prompt": prompt,
            "response_format": response_format,
            "temperature": temperature,
            "timestamp_granularities[]": timestamp_granularities,
        },
        files={"file": file},
        request_options=request_options,
        omit=OMIT,
    )


def _parse_transcription(response: typing.Any) -> CreateTranscriptionResult:
    if not 200 <= response.status_code < 300:
        raise_error_response(response)
    if "json" not in response.headers.get("content-type", ""):
        return response.text
    try:
        return typing.cast(TranscriptionResponse, parse_obj_as(type_=TranscriptionResponse, object_=response.json()))  # type: ignore
    except ValidationError as e:
        raise ParsingError(
            status_code=response.status_code, headers=dict(response.headers), body=response.json(), cause=e
        )


def _speech_request(
    *,
    input: str,
    model: typing.Optional[str],
    voice: typing.Optional[str],
    response_format: typing.Optional[SpeechResponseFormat],
    seed: typing.Optional[int],
    temperature: typing.Optional[float],
    top_p: typing.Optional[float],
    top_k: typing.Optional[int],
    repetition_penalty: typing.Optional[float],
    voice_sample: typing.Optional[core.File],
    request_options: typing.Optional[RequestOptions],
) -> typing.Dict[str, typing.Any]:
    body = {
        "model": model,
        "input": input,
        "voice": voice,
        "response_format": response_format,
        "seed": seed,
        "temperature": temperature,
        "top_p": top_p,
        "top_k": top_k,
        "repetition_penalty": repetition_penalty,
    }
    # A reference clip for voice cloning needs multipart; everything else is sent as JSON.
    if voice_sample is not OMIT and voice_sample is not None:
        return dict(method="POST", data=body, files={"voice_sample": voice_sample}, request_options=request_options, omit=OMIT)
    return dict(
        method="POST",
        json=body,
        headers={"content-type": "application/json"},
        request_options=request_options,
        omit=OMIT,
    )


def _parse_speech(response: typing.Any) -> bytes:
    if not 200 <= response.status_code < 300:
        raise_error_response(response)
    return response.content


class RawAudioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[CreateTranscriptionResult]:
        """
        Parameters are documented on `AudioClient.create_transcription`. The raw response exposes
        the `x-audio-duration-seconds` header.

        Returns
        -------
        HttpResponse[CreateTranscriptionResult]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "audio/transcriptions",
            **_transcription_request(
                file=file,
                model=model,
                language=language,
                prompt=prompt,
                response_format=response_format,
                temperature=temperature,
                timestamp_granularities=timestamp_granularities,
                request_options=request_options,
            ),
        )
        return HttpResponse(response=_response, data=_parse_transcription(_response))

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
    ) -> HttpResponse[bytes]:
        """
        Parameters are documented on `AudioClient.create_speech`. The raw response exposes the
        `x-audio-duration-seconds` and `content-type` headers.

        Returns
        -------
        HttpResponse[bytes]
            The audio file, encoded as `response_format`.
        """
        _response = self._client_wrapper.httpx_client.request(
            "audio/speech",
            **_speech_request(
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
            ),
        )
        return HttpResponse(response=_response, data=_parse_speech(_response))


class AsyncRawAudioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[CreateTranscriptionResult]:
        """
        Parameters are documented on `AsyncAudioClient.create_transcription`. The raw response
        exposes the `x-audio-duration-seconds` header.

        Returns
        -------
        AsyncHttpResponse[CreateTranscriptionResult]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "audio/transcriptions",
            **_transcription_request(
                file=file,
                model=model,
                language=language,
                prompt=prompt,
                response_format=response_format,
                temperature=temperature,
                timestamp_granularities=timestamp_granularities,
                request_options=request_options,
            ),
        )
        return AsyncHttpResponse(response=_response, data=_parse_transcription(_response))

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
    ) -> AsyncHttpResponse[bytes]:
        """
        Parameters are documented on `AsyncAudioClient.create_speech`. The raw response exposes the
        `x-audio-duration-seconds` and `content-type` headers.

        Returns
        -------
        AsyncHttpResponse[bytes]
            The audio file, encoded as `response_format`.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "audio/speech",
            **_speech_request(
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
            ),
        )
        return AsyncHttpResponse(response=_response, data=_parse_speech(_response))

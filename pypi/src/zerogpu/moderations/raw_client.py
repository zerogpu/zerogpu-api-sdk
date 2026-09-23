import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.raise_error_response import raise_error_response
from ..core.request_options import RequestOptions
from ..types.moderation_response import ModerationResponse
from .types.create_moderation_request_input import CreateModerationRequestInput
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


def _parse(response: typing.Any) -> ModerationResponse:
    if not 200 <= response.status_code < 300:
        raise_error_response(response)
    try:
        return typing.cast(ModerationResponse, parse_obj_as(type_=ModerationResponse, object_=response.json()))  # type: ignore
    except ValidationError as e:
        raise ParsingError(
            status_code=response.status_code, headers=dict(response.headers), body=response.json(), cause=e
        )


class RawModerationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_moderation(
        self,
        *,
        input: CreateModerationRequestInput,
        model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ModerationResponse]:
        """
        Parameters
        ----------
        input : CreateModerationRequestInput
            Text to classify. A single string, a list of strings (one result per element), or a list of
            content parts (`{"type": "text", "text": "..."}`) forming one multi-modal input.

        model : typing.Optional[str]
            Moderation model to use. Defaults to `zlm-v1-moderation-edge`; OpenAI ids
            (`omni-moderation-latest`, `text-moderation-stable`) are accepted and mapped to it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ModerationResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "moderations",
            method="POST",
            json={"model": model, "input": input},
            headers={"content-type": "application/json"},
            request_options=request_options,
            omit=OMIT,
        )
        return HttpResponse(response=_response, data=_parse(_response))


class AsyncRawModerationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_moderation(
        self,
        *,
        input: CreateModerationRequestInput,
        model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ModerationResponse]:
        """
        Parameters
        ----------
        input : CreateModerationRequestInput
            Text to classify. A single string, a list of strings (one result per element), or a list of
            content parts (`{"type": "text", "text": "..."}`) forming one multi-modal input.

        model : typing.Optional[str]
            Moderation model to use. Defaults to `zlm-v1-moderation-edge`; OpenAI ids
            (`omni-moderation-latest`, `text-moderation-stable`) are accepted and mapped to it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ModerationResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "moderations",
            method="POST",
            json={"model": model, "input": input},
            headers={"content-type": "application/json"},
            request_options=request_options,
            omit=OMIT,
        )
        return AsyncHttpResponse(response=_response, data=_parse(_response))

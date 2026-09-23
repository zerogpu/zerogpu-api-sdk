import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.raise_error_response import raise_error_response
from ..core.request_options import RequestOptions
from ..types.embedding_response import EmbeddingResponse
from .types.create_embedding_request_input import CreateEmbeddingRequestInput
from pydantic import ValidationError


def _parse(response: typing.Any) -> EmbeddingResponse:
    if not 200 <= response.status_code < 300:
        raise_error_response(response)
    try:
        return typing.cast(EmbeddingResponse, parse_obj_as(type_=EmbeddingResponse, object_=response.json()))  # type: ignore
    except ValidationError as e:
        raise ParsingError(
            status_code=response.status_code, headers=dict(response.headers), body=response.json(), cause=e
        )


class RawEmbeddingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_embedding(
        self,
        *,
        model: str,
        input: CreateEmbeddingRequestInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmbeddingResponse]:
        """
        Parameters
        ----------
        model : str
            Embedding model to use: `all-minilm-l6-v2` or `bge-small-en-v1.5`.

        input : CreateEmbeddingRequestInput
            Text to embed. A single string, or a list of strings (one vector per element).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmbeddingResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "embeddings",
            method="POST",
            json={"model": model, "input": input},
            headers={"content-type": "application/json"},
            request_options=request_options,
        )
        return HttpResponse(response=_response, data=_parse(_response))


class AsyncRawEmbeddingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_embedding(
        self,
        *,
        model: str,
        input: CreateEmbeddingRequestInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmbeddingResponse]:
        """
        Parameters
        ----------
        model : str
            Embedding model to use: `all-minilm-l6-v2` or `bge-small-en-v1.5`.

        input : CreateEmbeddingRequestInput
            Text to embed. A single string, or a list of strings (one vector per element).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmbeddingResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "embeddings",
            method="POST",
            json={"model": model, "input": input},
            headers={"content-type": "application/json"},
            request_options=request_options,
        )
        return AsyncHttpResponse(response=_response, data=_parse(_response))

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.embedding_response import EmbeddingResponse
from .raw_client import AsyncRawEmbeddingsClient, RawEmbeddingsClient
from .types.create_embedding_request_input import CreateEmbeddingRequestInput


class EmbeddingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEmbeddingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEmbeddingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEmbeddingsClient
        """
        return self._raw_client

    def create_embedding(
        self,
        *,
        model: str,
        input: CreateEmbeddingRequestInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmbeddingResponse:
        """
        Turn text into 384-dimensional vectors.

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
        EmbeddingResponse
            Success

        Examples
        --------
        from zerogpu import ZerogpuApi

        client = ZerogpuApi(
            api_key="YOUR_API_KEY",
        )
        client.embeddings.create_embedding(
            model="all-minilm-l6-v2",
            input="ZeroGPU runs inference at the edge.",
        )
        """
        return self._raw_client.create_embedding(model=model, input=input, request_options=request_options).data


class AsyncEmbeddingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEmbeddingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEmbeddingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEmbeddingsClient
        """
        return self._raw_client

    async def create_embedding(
        self,
        *,
        model: str,
        input: CreateEmbeddingRequestInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmbeddingResponse:
        """
        Turn text into 384-dimensional vectors.

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
        EmbeddingResponse
            Success

        Examples
        --------
        import asyncio

        from zerogpu import AsyncZerogpuApi

        client = AsyncZerogpuApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.embeddings.create_embedding(
                model="all-minilm-l6-v2",
                input="ZeroGPU runs inference at the edge.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_embedding(model=model, input=input, request_options=request_options)
        return _response.data

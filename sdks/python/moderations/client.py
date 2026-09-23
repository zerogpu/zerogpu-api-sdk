import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.moderation_response import ModerationResponse
from .raw_client import AsyncRawModerationsClient, RawModerationsClient
from .types.create_moderation_request_input import CreateModerationRequestInput

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ModerationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawModerationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawModerationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawModerationsClient
        """
        return self._raw_client

    def create_moderation(
        self,
        *,
        input: CreateModerationRequestInput,
        model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModerationResponse:
        """
        Classify text against OpenAI's 13 safety categories.

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
        ModerationResponse
            Success

        Examples
        --------
        from zerogpu import ZerogpuApi

        client = ZerogpuApi(
            api_key="YOUR_API_KEY",
        )
        client.moderations.create_moderation(
            input="I want to hurt them.",
        )
        """
        return self._raw_client.create_moderation(input=input, model=model, request_options=request_options).data


class AsyncModerationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawModerationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawModerationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawModerationsClient
        """
        return self._raw_client

    async def create_moderation(
        self,
        *,
        input: CreateModerationRequestInput,
        model: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ModerationResponse:
        """
        Classify text against OpenAI's 13 safety categories.

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
        ModerationResponse
            Success

        Examples
        --------
        import asyncio

        from zerogpu import AsyncZerogpuApi

        client = AsyncZerogpuApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.moderations.create_moderation(
                input="I want to hurt them.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_moderation(input=input, model=model, request_options=request_options)
        return _response.data

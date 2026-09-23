import type { BaseClientOptions, BaseRequestOptions } from "../../../../BaseClient.js";
import { type NormalizedClientOptionsWithAuth, normalizeClientOptionsWithAuth } from "../../../../BaseClient.js";
import { mergeHeaders } from "../../../../core/headers.js";
import * as core from "../../../../core/index.js";
import * as environments from "../../../../environments.js";
import { handleNonStatusCodeError } from "../../../../errors/handleNonStatusCodeError.js";
import { handleStatusCodeError } from "../../../../errors/handleStatusCodeError.js";
import type * as ZerogpuApi from "../../../index.js";

export declare namespace ModerationsClient {
    export type Options = BaseClientOptions;

    export interface RequestOptions extends BaseRequestOptions {}
}

export class ModerationsClient {
    protected readonly _options: NormalizedClientOptionsWithAuth<ModerationsClient.Options>;

    constructor(options: ModerationsClient.Options) {
        this._options = normalizeClientOptionsWithAuth(options);
    }

    /**
     * Classify text against OpenAI's 13 safety categories.
     *
     * @param {ZerogpuApi.CreateModerationRequest} request
     * @param {ModerationsClient.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @throws {@link ZerogpuApi.BadRequestError}
     * @throws {@link ZerogpuApi.UnauthorizedError}
     * @throws {@link ZerogpuApi.ForbiddenError}
     * @throws {@link ZerogpuApi.MethodFailureError}
     * @throws {@link ZerogpuApi.InternalServerError}
     *
     * @example
     *     await client.moderations.createModeration({
     *         input: "I want to hurt them."
     *     })
     */
    public createModeration(
        request: ZerogpuApi.CreateModerationRequest,
        requestOptions?: ModerationsClient.RequestOptions,
    ): core.HttpResponsePromise<ZerogpuApi.ModerationResponse> {
        return core.HttpResponsePromise.fromPromise(this.__createModeration(request, requestOptions));
    }

    private async __createModeration(
        request: ZerogpuApi.CreateModerationRequest,
        requestOptions?: ModerationsClient.RequestOptions,
    ): Promise<core.WithRawResponse<ZerogpuApi.ModerationResponse>> {
        const _authRequest: core.AuthRequest = await this._options.authProvider.getAuthRequest();
        const _headers: core.Fetcher.Args["headers"] = mergeHeaders(
            _authRequest.headers,
            this._options?.headers,
            requestOptions?.headers,
        );
        const _response = await core.fetcher({
            url: core.url.join(
                (await core.Supplier.get(this._options.baseUrl)) ??
                    (await core.Supplier.get(this._options.environment)) ??
                    environments.ZerogpuApiEnvironment.Production,
                "moderations",
            ),
            method: "POST",
            headers: _headers,
            contentType: "application/json",
            queryParameters: requestOptions?.queryParams,
            requestType: "json",
            body: request,
            timeoutMs: (requestOptions?.timeoutInSeconds ?? this._options?.timeoutInSeconds ?? 60) * 1000,
            maxRetries: requestOptions?.maxRetries ?? this._options?.maxRetries,
            abortSignal: requestOptions?.abortSignal,
            fetchFn: this._options?.fetch,
            logging: this._options.logging,
        });
        if (_response.ok) {
            return { data: _response.body as ZerogpuApi.ModerationResponse, rawResponse: _response.rawResponse };
        }

        if (_response.error.reason === "status-code") {
            handleStatusCodeError(_response.error, _response.rawResponse);
        }

        return handleNonStatusCodeError(_response.error, _response.rawResponse, "POST", "/moderations");
    }
}

import type { BaseClientOptions, BaseRequestOptions } from "../../../../BaseClient.js";
import { type NormalizedClientOptionsWithAuth, normalizeClientOptionsWithAuth } from "../../../../BaseClient.js";
import { mergeHeaders } from "../../../../core/headers.js";
import * as core from "../../../../core/index.js";
import * as environments from "../../../../environments.js";
import { handleNonStatusCodeError } from "../../../../errors/handleNonStatusCodeError.js";
import { handleStatusCodeError } from "../../../../errors/handleStatusCodeError.js";
import type * as ZerogpuApi from "../../../index.js";

export declare namespace EmbeddingsClient {
    export type Options = BaseClientOptions;

    export interface RequestOptions extends BaseRequestOptions {}
}

export class EmbeddingsClient {
    protected readonly _options: NormalizedClientOptionsWithAuth<EmbeddingsClient.Options>;

    constructor(options: EmbeddingsClient.Options) {
        this._options = normalizeClientOptionsWithAuth(options);
    }

    /**
     * Turn text into 384-dimensional vectors.
     *
     * @param {ZerogpuApi.CreateEmbeddingRequest} request
     * @param {EmbeddingsClient.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @throws {@link ZerogpuApi.BadRequestError}
     * @throws {@link ZerogpuApi.UnauthorizedError}
     * @throws {@link ZerogpuApi.ForbiddenError}
     * @throws {@link ZerogpuApi.MethodFailureError}
     * @throws {@link ZerogpuApi.InternalServerError}
     *
     * @example
     *     await client.embeddings.createEmbedding({
     *         model: "all-minilm-l6-v2",
     *         input: "ZeroGPU runs inference at the edge."
     *     })
     */
    public createEmbedding(
        request: ZerogpuApi.CreateEmbeddingRequest,
        requestOptions?: EmbeddingsClient.RequestOptions,
    ): core.HttpResponsePromise<ZerogpuApi.EmbeddingResponse> {
        return core.HttpResponsePromise.fromPromise(this.__createEmbedding(request, requestOptions));
    }

    private async __createEmbedding(
        request: ZerogpuApi.CreateEmbeddingRequest,
        requestOptions?: EmbeddingsClient.RequestOptions,
    ): Promise<core.WithRawResponse<ZerogpuApi.EmbeddingResponse>> {
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
                "embeddings",
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
            return { data: _response.body as ZerogpuApi.EmbeddingResponse, rawResponse: _response.rawResponse };
        }

        if (_response.error.reason === "status-code") {
            handleStatusCodeError(_response.error, _response.rawResponse);
        }

        return handleNonStatusCodeError(_response.error, _response.rawResponse, "POST", "/embeddings");
    }
}

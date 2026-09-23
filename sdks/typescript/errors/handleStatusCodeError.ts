import * as ZerogpuApi from "../api/index.js";
import type * as core from "../core/index.js";
import * as errors from "./index.js";

export function handleStatusCodeError(
    error: core.Fetcher.FailedStatusCodeError,
    rawResponse: core.RawResponse,
): never {
    switch (error.statusCode) {
        case 400:
            throw new ZerogpuApi.BadRequestError(error.body, rawResponse);
        case 401:
            throw new ZerogpuApi.UnauthorizedError(error.body, rawResponse);
        case 403:
            throw new ZerogpuApi.ForbiddenError(error.body, rawResponse);
        case 420:
            throw new ZerogpuApi.MethodFailureError(error.body as ZerogpuApi.ErrorResponse, rawResponse);
        case 500:
            throw new ZerogpuApi.InternalServerError(error.body, rawResponse);
        default:
            throw new errors.ZerogpuApiError({
                statusCode: error.statusCode,
                body: error.body,
                rawResponse: rawResponse,
            });
    }
}

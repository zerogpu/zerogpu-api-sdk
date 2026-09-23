import type * as ZerogpuApi from "../index.js";

export interface Response {
    id: string;
    object: string;
    /** Unix timestamp when the response was created */
    created_at?: number | undefined;
    model: string;
    output: ZerogpuApi.OutputMessage[];
    usage?: ZerogpuApi.TokenUsage | undefined;
}

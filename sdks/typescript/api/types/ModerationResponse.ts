import type * as ZerogpuApi from "../index.js";

/**
 * OpenAI-compatible moderations envelope. One `results` entry per input.
 */
export interface ModerationResponse {
    id?: string | undefined;
    model?: string | undefined;
    results?: ZerogpuApi.ModerationResult[] | undefined;
    /** Accepts any additional properties */
    [key: string]: any;
}

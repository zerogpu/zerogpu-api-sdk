import type * as ZerogpuApi from "../index.js";

/**
 * OpenAI-compatible embedding list. `data[i].index` maps each vector back to its input.
 */
export interface EmbeddingResponse {
    object?: string | undefined;
    data?: ZerogpuApi.Embedding[] | undefined;
    /** The resolved model id. */
    model?: string | undefined;
    usage?: ZerogpuApi.EmbeddingUsage | undefined;
}

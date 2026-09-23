/**
 * @example
 *     {
 *         model: "all-minilm-l6-v2",
 *         input: "ZeroGPU runs inference at the edge."
 *     }
 */
export interface CreateEmbeddingRequest {
    /** Embedding model to use: `all-minilm-l6-v2` or `bge-small-en-v1.5`. */
    model: string;
    /** Text to embed. A single string, or an array of strings (one vector per element). */
    input: CreateEmbeddingRequest.Input;
}

export namespace CreateEmbeddingRequest {
    export type Input = string | string[];
}

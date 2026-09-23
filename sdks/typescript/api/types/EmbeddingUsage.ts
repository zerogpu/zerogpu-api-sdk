/**
 * Embeddings are billed on input tokens only; there are no output tokens.
 */
export interface EmbeddingUsage {
    prompt_tokens?: number | undefined;
    total_tokens?: number | undefined;
}

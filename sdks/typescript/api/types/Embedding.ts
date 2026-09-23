export interface Embedding {
    object?: string | undefined;
    /** Position of the input this vector was produced from. */
    index?: number | undefined;
    /** The embedding vector. 384 dimensions for both models. */
    embedding?: number[] | undefined;
}

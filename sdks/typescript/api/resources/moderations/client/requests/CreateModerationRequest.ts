/**
 * @example
 *     {
 *         input: "I want to hurt them."
 *     }
 */
export interface CreateModerationRequest {
    /**
     * Moderation model to use. Defaults to `zlm-v1-moderation-edge`; OpenAI ids
     * (`omni-moderation-latest`, `text-moderation-stable`) are accepted and mapped to it.
     */
    model?: string;
    /**
     * Text to classify. A single string, an array of strings (one result per element), or an array of
     * content parts (`{ type: "text", text: "..." }`) forming one multi-modal input.
     */
    input: CreateModerationRequest.Input;
}

export namespace CreateModerationRequest {
    export type Input = string | string[] | Record<string, unknown>[];
}

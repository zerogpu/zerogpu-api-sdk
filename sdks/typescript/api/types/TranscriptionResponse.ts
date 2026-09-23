/**
 * `json` returns `{ text }`. `verbose_json` adds `task`, `language`, `duration`, and `segments` and/or `words`.
 */
export interface TranscriptionResponse {
    /** The transcript. */
    text: string;
    /** Accepts any additional properties */
    [key: string]: any;
}

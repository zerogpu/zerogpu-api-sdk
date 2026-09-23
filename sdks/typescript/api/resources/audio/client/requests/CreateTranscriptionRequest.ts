/**
 * @example
 *     {
 *         file: await fs.openAsBlob("speech.mp3"),
 *         filename: "speech.mp3"
 *     }
 */
export interface CreateTranscriptionRequest {
    /** The audio file to transcribe, up to 25 MB and 10 minutes. A `File` keeps its own name. */
    file: Blob | ArrayBuffer | Uint8Array;
    /** Filename sent with `file`, such as `speech.mp3`. Defaults to the `File` name, or `audio`. */
    filename?: string;
    /** Model identifier. Defaults to `whisper-tiny`. */
    model?: string;
    /** ISO-639-1 code, such as `en`. Detected automatically when omitted. */
    language?: string;
    /** Text to guide spelling and style, such as names or jargon. */
    prompt?: string;
    /** `json` (default) and `verbose_json` return a `TranscriptionResponse`; `text`, `srt`, and `vtt` return a string. */
    response_format?: CreateTranscriptionRequest.ResponseFormat;
    /** Sampling temperature, 0 to 1. */
    temperature?: number;
    /** `segment` (default), `word`, or both. Requires `verbose_json`. */
    timestamp_granularities?: ("segment" | "word")[];
}

export namespace CreateTranscriptionRequest {
    export type ResponseFormat = "json" | "text" | "srt" | "verbose_json" | "vtt";
}

/**
 * @example
 *     {
 *         input: "Hey, how are you today?"
 *     }
 */
export interface CreateSpeechRequest {
    /** The text to speak, up to 2000 characters. Inline tags such as `[laugh]` add paralinguistic cues. */
    input: string;
    /** Model identifier. Defaults to `chatterbox-nano`. */
    model?: string;
    /** OpenAI voice names are accepted and all map to the built-in voice. */
    voice?: string;
    /** `mp3` (default), `opus`, `aac`, `flac`, `wav`, or `pcm` (raw 16-bit little-endian mono at 24 kHz). */
    response_format?: CreateSpeechRequest.ResponseFormat;
    /** Pins sampling for repeatable output (best-effort). */
    seed?: number;
    /** Sampling temperature, 0 to 2. */
    temperature?: number;
    /** Nucleus sampling, 0 to 1. */
    top_p?: number;
    /** Top-k sampling. */
    top_k?: number;
    /** Penalty on repeated speech tokens, 1 to 4. */
    repetition_penalty?: number;
    /** Reference clip to clone a voice from, up to 10 MB and 30 seconds. Overrides `voice`. Not stored. */
    voice_sample?: Blob | ArrayBuffer | Uint8Array;
    /** Filename sent with `voice_sample`. Defaults to the `File` name, or `voice_sample`. */
    voice_sample_filename?: string;
}

export namespace CreateSpeechRequest {
    export type ResponseFormat = "mp3" | "opus" | "aac" | "flac" | "wav" | "pcm";
}

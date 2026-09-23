import type { BaseClientOptions, BaseRequestOptions } from "../../../../BaseClient.js";
import { type NormalizedClientOptionsWithAuth, normalizeClientOptionsWithAuth } from "../../../../BaseClient.js";
import { mergeHeaders } from "../../../../core/headers.js";
import * as core from "../../../../core/index.js";
import * as environments from "../../../../environments.js";
import { handleNonStatusCodeError } from "../../../../errors/handleNonStatusCodeError.js";
import { handleStatusCodeError } from "../../../../errors/handleStatusCodeError.js";
import type * as ZerogpuApi from "../../../index.js";

export declare namespace AudioClient {
    export type Options = BaseClientOptions;

    export interface RequestOptions extends BaseRequestOptions {}
}

export class AudioClient {
    protected readonly _options: NormalizedClientOptionsWithAuth<AudioClient.Options>;

    constructor(options: AudioClient.Options) {
        this._options = normalizeClientOptionsWithAuth(options);
    }

    /**
     * Transcribe audio into text with `whisper-tiny`. The raw response carries the
     * `x-audio-duration-seconds` header.
     *
     * @param {ZerogpuApi.CreateTranscriptionRequest} request
     * @param {AudioClient.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @returns A `TranscriptionResponse` for `json` and `verbose_json`, otherwise the transcript as a string.
     *
     * @throws {@link ZerogpuApi.BadRequestError}
     * @throws {@link ZerogpuApi.UnauthorizedError}
     * @throws {@link ZerogpuApi.ForbiddenError}
     * @throws {@link ZerogpuApi.InternalServerError}
     *
     * @example
     *     await client.audio.createTranscription({
     *         file: await fs.openAsBlob("speech.mp3"),
     *         filename: "speech.mp3"
     *     })
     */
    public createTranscription(
        request: ZerogpuApi.CreateTranscriptionRequest,
        requestOptions?: AudioClient.RequestOptions,
    ): core.HttpResponsePromise<ZerogpuApi.TranscriptionResponse | string> {
        return core.HttpResponsePromise.fromPromise(this.__createTranscription(request, requestOptions));
    }

    private async __createTranscription(
        request: ZerogpuApi.CreateTranscriptionRequest,
        requestOptions?: AudioClient.RequestOptions,
    ): Promise<core.WithRawResponse<ZerogpuApi.TranscriptionResponse | string>> {
        const { file, filename, timestamp_granularities, ...fields } = request;
        const _body = toFormData(fields);
        appendFile(_body, "file", file, filename ?? fileName(file) ?? "audio");
        for (const granularity of timestamp_granularities ?? []) {
            _body.append("timestamp_granularities[]", granularity);
        }
        const _response = await this._post("audio/transcriptions", _body, "text", requestOptions);
        if (_response.ok) {
            const _text = _response.body as string;
            const _isJson = _response.rawResponse.headers.get("content-type")?.includes("json") ?? false;
            return {
                data: _isJson ? (JSON.parse(_text) as ZerogpuApi.TranscriptionResponse) : _text,
                rawResponse: _response.rawResponse,
            };
        }

        if (_response.error.reason === "status-code") {
            handleStatusCodeError(_response.error, _response.rawResponse);
        }

        return handleNonStatusCodeError(_response.error, _response.rawResponse, "POST", "/audio/transcriptions");
    }

    /**
     * Generate speech from text with `chatterbox-nano`. Pass `voice_sample` to clone a voice.
     * The raw response carries the `x-audio-duration-seconds` and `content-type` headers.
     *
     * @param {ZerogpuApi.CreateSpeechRequest} request
     * @param {AudioClient.RequestOptions} requestOptions - Request-specific configuration.
     *
     * @throws {@link ZerogpuApi.BadRequestError}
     * @throws {@link ZerogpuApi.UnauthorizedError}
     * @throws {@link ZerogpuApi.ForbiddenError}
     * @throws {@link ZerogpuApi.InternalServerError}
     *
     * @example
     *     const audio = await client.audio.createSpeech({
     *         input: "Hey, how are you today?"
     *     })
     *     fs.writeFileSync("speech.mp3", Buffer.from(await audio.arrayBuffer()))
     */
    public createSpeech(
        request: ZerogpuApi.CreateSpeechRequest,
        requestOptions?: AudioClient.RequestOptions,
    ): core.HttpResponsePromise<core.BinaryResponse> {
        return core.HttpResponsePromise.fromPromise(this.__createSpeech(request, requestOptions));
    }

    private async __createSpeech(
        request: ZerogpuApi.CreateSpeechRequest,
        requestOptions?: AudioClient.RequestOptions,
    ): Promise<core.WithRawResponse<core.BinaryResponse>> {
        const { voice_sample, voice_sample_filename, ...fields } = request;
        // A reference clip for voice cloning needs multipart; everything else is sent as JSON.
        let _body: FormData | typeof fields = fields;
        if (voice_sample != null) {
            _body = toFormData(fields);
            appendFile(_body, "voice_sample", voice_sample, voice_sample_filename ?? fileName(voice_sample) ?? "voice_sample");
        }
        const _response = await this._post("audio/speech", _body, "binary-response", requestOptions);
        if (_response.ok) {
            return { data: _response.body as core.BinaryResponse, rawResponse: _response.rawResponse };
        }

        if (_response.error.reason === "status-code") {
            handleStatusCodeError(_response.error, _response.rawResponse);
        }

        return handleNonStatusCodeError(_response.error, _response.rawResponse, "POST", "/audio/speech");
    }

    private async _post(
        path: string,
        body: unknown,
        responseType: core.Fetcher.Args["responseType"],
        requestOptions?: AudioClient.RequestOptions,
    ) {
        const _isForm = body instanceof FormData;
        const _authRequest: core.AuthRequest = await this._options.authProvider.getAuthRequest();
        const _headers: core.Fetcher.Args["headers"] = mergeHeaders(
            _authRequest.headers,
            this._options?.headers,
            requestOptions?.headers,
        );
        return core.fetcher({
            url: core.url.join(
                (await core.Supplier.get(this._options.baseUrl)) ??
                    (await core.Supplier.get(this._options.environment)) ??
                    environments.ZerogpuApiEnvironment.Production,
                path,
            ),
            method: "POST",
            headers: _headers,
            // fetch sets the multipart boundary itself, so no content type for form bodies.
            contentType: _isForm ? undefined : "application/json",
            queryParameters: requestOptions?.queryParams,
            requestType: _isForm ? "file" : "json",
            responseType,
            body,
            timeoutMs: (requestOptions?.timeoutInSeconds ?? this._options?.timeoutInSeconds ?? 60) * 1000,
            maxRetries: requestOptions?.maxRetries ?? this._options?.maxRetries,
            abortSignal: requestOptions?.abortSignal,
            fetchFn: this._options?.fetch,
            logging: this._options.logging,
        });
    }
}

function toFormData(fields: Record<string, unknown>): FormData {
    const form = new FormData();
    for (const [key, value] of Object.entries(fields)) {
        if (value != null) {
            form.append(key, String(value));
        }
    }
    return form;
}

function fileName(file: Blob | ArrayBuffer | Uint8Array): string | undefined {
    return typeof File !== "undefined" && file instanceof File ? file.name : undefined;
}

function appendFile(form: FormData, name: string, file: Blob | ArrayBuffer | Uint8Array, filename: string): void {
    form.append(name, file instanceof Blob ? file : new Blob([file as BlobPart]), filename);
}

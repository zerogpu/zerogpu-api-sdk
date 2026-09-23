# zerogpu-api

Official ZeroGPU API client for Node.js and TypeScript. Covers responses, chat completions, moderations, embeddings, and audio (transcriptions and speech), authenticated with your API key (`x-api-key` header).

## Install

```bash
npm install zerogpu-api
```

## Quick start — Responses

`input` may be a **plain string** or an **array** of `{ role, content }` messages, depending on the model.

```ts
import { ZerogpuApiClient } from "zerogpu-api";

const client = new ZerogpuApiClient({
  apiKey: process.env.ZEROGPU_API_KEY!,
});

const response = await client.responses.createResponse({
  model: "zlm-v1-followup-questions-edge",
  input: "In one short sentence, what is a habit tracker?",
  text: { format: { type: "text" } },
});

console.log(response.output);
```

### Optional `metadata` (Responses)

Some models accept extra options on the responses route (e.g. PII `mask` / `usecase`):

```ts
await client.responses.createResponse({
  model: "gliner-multi-pii-v1",
  input: "Your text…",
  metadata: { mask: "label", usecase: "redact" },
});
```

## Chat completions

For models that use the chat-completions shape:

```ts
const completion = await client.chat.createChatCompletion({
  model: "gliner-multi-pii-v1",
  messages: [{ role: "user", content: "Your text…" }],
  metadata: { mask: "label", usecase: "redact" },
});

console.log(completion);
```

## Moderations

Classify text against OpenAI's 13 safety categories. `model` defaults to `zlm-v1-moderation-edge`.

```ts
const moderation = await client.moderations.createModeration({
  input: "I want to hurt them.",
});

console.log(moderation.results?.[0]?.flagged, moderation.results?.[0]?.categories);
```

## Embeddings

384-dimensional vectors from `all-minilm-l6-v2` or `bge-small-en-v1.5`. Pass an array to embed a batch.

```ts
const embeddings = await client.embeddings.createEmbedding({
  model: "all-minilm-l6-v2",
  input: ["first document", "second document"],
});

console.log(embeddings.data?.[0]?.embedding);
```

## Audio

Transcribe with `whisper-tiny`. `json` (default) and `verbose_json` return an object; `text`, `srt`, and `vtt` return a string.

```ts
import fs from "node:fs";

const transcript = await client.audio.createTranscription({
  file: await fs.openAsBlob("speech.mp3"),
  filename: "speech.mp3",
});

console.log(transcript);
```

Generate speech with `chatterbox-nano`. Pass `voice_sample` to clone a voice from a reference clip.

```ts
const audio = await client.audio.createSpeech({
  input: "Hey, how are you today?",
  response_format: "mp3",
});

fs.writeFileSync("speech.mp3", Buffer.from(await audio.arrayBuffer()));
```

## Environment variables

- `ZEROGPU_API_KEY`

The client always calls production `https://api.zerogpu.ai/v1`; there is no URL environment variable.

## API reference

- [ZeroGPU docs](https://docs.zerogpu.ai)
- [Responses](https://docs.zerogpu.ai/api-reference/endpoint/responses)
- [Chat completions](https://docs.zerogpu.ai/api-reference/endpoint/chat-completions)
- [Moderations](https://docs.zerogpu.ai/api-reference/moderations)
- [Embeddings](https://docs.zerogpu.ai/api-reference/embeddings)
- [Transcriptions](https://docs.zerogpu.ai/api-reference/audio-transcriptions)
- [Speech](https://docs.zerogpu.ai/api-reference/audio-speech)

## Maintainers

From this `npm/` directory:

```bash
npm install
npm run build
npm publish --access public
```

This package bundles the TypeScript SDK from `../sdks/typescript` via `tsup`.

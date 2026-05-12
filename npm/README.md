# zerogpu-api

Official ZeroGPU API client for Node.js and TypeScript. Covers **`POST /v1/responses`** and **`POST /v1/chat/completions`** with the same headers (`x-api-key`, `x-project-id`).

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
  projectId: process.env.ZEROGPU_PROJECT_ID!,
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

## Environment variables

- `ZEROGPU_API_KEY`
- `ZEROGPU_PROJECT_ID`
- `ZEROGPU_API_URL` — optional override only; if unset, the client uses production `https://api.zerogpu.ai/v1`

## API reference

- [ZeroGPU docs](https://docs.zerogpu.ai)
- [Responses](https://docs.zerogpu.ai/api-reference/endpoint/responses)
- [Chat completions](https://docs.zerogpu.ai/api-reference/endpoint/chat-completions)

## Maintainers

From this `npm/` directory:

```bash
npm install
npm run build
npm publish --access public
```

This package bundles the generated TypeScript SDK from `../sdks/typescript` via `tsup`.

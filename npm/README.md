# zerogpu-api

Official ZeroGPU API client for Node.js and modern runtimes.

## Install

```bash
npm install zerogpu-api
```

## Quick Start

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

## Environment Variables

- `ZEROGPU_API_KEY`
- `ZEROGPU_PROJECT_ID`
- `ZEROGPU_API_URL` is optional and override-only. If unset, the SDK always uses production: `https://api.zerogpu.ai/v1`

## API Reference

- [ZeroGPU docs](https://docs.zerogpu.ai)
- [Responses endpoint](https://docs.zerogpu.ai/api-reference/endpoint/responses)

## Maintainers

From this `npm/` directory:

```bash
npm install
npm run build
npm publish --access public
```

This package bundles the generated TypeScript SDK from `../sdks/typescript` via `tsup`.

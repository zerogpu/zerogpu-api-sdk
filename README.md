# ZeroGPU SDK

Official API clients for [ZeroGPU](https://zerogpu.ai), generated from the OpenAPI spec with [Fern](https://buildwithfern.com/). Human-facing API documentation lives at [docs.zerogpu.ai](https://docs.zerogpu.ai).

## Repository layout

| Path | Description |
|------|-------------|
| `specs/zerogpu.openapi.yaml` | Source of truth for `POST /v1/responses` |
| `fern/` | Fern config (`generators.yml`, `fern.config.json`) |
| `sdks/` | Generated clients (TypeScript, Python, Go, Ruby, Java, Rust, C#, PHP, Swift) |
| `typescript-smoke/` | Minimal script to verify the TypeScript client against the live API |

## Regenerate SDKs

Prerequisites: Node.js, [`fern-api`](https://buildwithfern.com/learn/sdks/overview/quickstart) CLI, and a Fern account (`fern login` or `FERN_TOKEN`).

```bash
cd fern
npx fern-api check
```

Generate one language (examples):

```bash
npx fern-api generate              # default group: TypeScript → ../sdks/typescript
npx fern-api generate --group python-sdk
npx fern-api generate --group go-sdk
```

See `fern/generators.yml` for all groups and output paths.

## Try the TypeScript client

From `typescript-smoke/` (see that folder’s header comment for env vars). Do not commit secrets.

```bash
cd typescript-smoke
npm install
export ZEROGPU_API_KEY=…
export ZEROGPU_PROJECT_ID=…
export ZEROGPU_MODEL=…   # model id from the ZeroGPU dashboard
npm run smoke
```

Optional: `ZEROGPU_API_URL` for dev vs prod (must match your key/project environment). The smoke loader also reads `../../Benchmark/.env` if you use the benchmark repo next to this one.

## API overview

- **Base URL:** `https://api.zerogpu.ai/v1` (production)
- **Endpoint:** `POST /responses`
- **Headers:** `x-api-key`, `x-project-id`, `content-type: application/json`

Details: [Responses API](https://docs.zerogpu.ai/api-reference/endpoint/responses).

## License

Add a `LICENSE` file at the repo root when you publish; generated SDKs follow your chosen license for distributed packages.

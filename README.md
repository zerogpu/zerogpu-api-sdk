<p align="center">
  <img src="https://zerogpu.ai/assets/zerogpu-icon-dark-DB2Jfxq2.png" alt="ZeroGPU" width="160"/>
</p>

<h1 align="center">ZeroGPU API SDKs</h1>

<p align="center">
  <strong>Official API clients for <a href="https://zerogpu.ai">ZeroGPU</a>.</strong><br/>
  Call <code>POST /v1/responses</code> and <code>POST /v1/chat/completions</code> with typed helpers — publishable packages on <a href="https://www.npmjs.com/package/zerogpu-api">npm</a> (<code>zerogpu-api</code>) and <a href="https://pypi.org/project/zerogpu-api/">PyPI</a> (<code>pip install zerogpu-api</code> → import <code>zerogpu</code>).
</p>

<p align="center">
  <a href="https://platform.zerogpu.ai">
    <img src="https://img.shields.io/badge/Platform-Dashboard-22c55e?style=for-the-badge" alt="Open ZeroGPU platform" />
  </a>
  &nbsp;
  <a href="https://www.zerogpu.ai">
    <img src="https://img.shields.io/badge/Main-Website-22c55e?style=for-the-badge" alt="Open ZeroGPU website" />
  </a>
  &nbsp;
  <a href="https://docs.zerogpu.ai">
    <img src="https://img.shields.io/badge/Docs-docs.zerogpu.ai-111827?style=for-the-badge" alt="ZeroGPU documentation" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/zerogpu/SDK/stargazers"><img src="https://img.shields.io/github/stars/zerogpu/SDK?style=flat-square" alt="GitHub stars" /></a>
  <a href="https://www.npmjs.com/package/zerogpu-api"><img src="https://img.shields.io/npm/v/zerogpu-api?style=flat-square" alt="npm version" /></a>
  <a href="https://pypi.org/project/zerogpu-api/"><img src="https://img.shields.io/pypi/v/zerogpu-api?style=flat-square" alt="PyPI version" /></a>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="License" />
  <a href="https://github.com/zerogpu/zerogpu-router"><img src="https://img.shields.io/badge/Related-Router-111827?style=flat-square" alt="ZeroGPU Router" /></a>
</p>

<p align="center">
  <img src="assets/zerogpu%20-%20sdk%20gif.gif" alt="ZeroGPU API SDKs — dashboard and integration preview" width="720"/>
</p>

---

**ZeroGPU API SDKs** are the official API client libraries for [ZeroGPU](https://zerogpu.ai). Use them to call `POST /v1/responses` with your API key.

**API reference and guides:** [docs.zerogpu.ai](https://docs.zerogpu.ai) (authentication, models, error codes).

## Packages

| Registry | Package | Source |
|----------|---------|--------|
| [npm](https://www.npmjs.com/package/zerogpu-api) | `zerogpu-api` | [`npm/`](./npm/) (bundles `sdks/typescript`) |
| [PyPI](https://pypi.org/project/zerogpu-api/) | `zerogpu-api` (import `zerogpu`) | [`pypi/`](./pypi/) (synced from `sdks/python`) |

## Quick start (local checkout)

Environment variables (same as the [dashboard](https://zerogpu.ai) snippets):

- `ZEROGPU_API_KEY`

Clients always use the production API base URL `https://api.zerogpu.ai/v1`. There is no environment variable to change it.

**Smoke tests** — one live `POST /v1/responses` per SDK (TypeScript and Python); see [`smoke/README.md`](./smoke/README.md). TypeScript example:

```bash
cd smoke/typescript
npm install
export ZEROGPU_API_KEY=…
export ZEROGPU_MODEL=…   # from your dashboard
npm run smoke
```

Do not commit secrets.

### `input` shape (OpenAPI + SDKs)

The OpenAPI spec models `input` as **either** a non-empty **string** **or** a non-empty **array** of `role` / `content` messages, matching what production accepts.

## `POST /v1/responses` (reminder)

- **Production base URL:** `https://api.zerogpu.ai/v1`
- **Path:** `/responses`
- **Headers:** `x-api-key`, `content-type: application/json`

Full spec: [Responses API](https://docs.zerogpu.ai/api-reference/endpoint/responses).

**Also supported:** `POST /v1/chat/completions` via `client.chat` (Python: `client.chat`) for models that use the chat-completions route. Optional **`metadata`** on `POST /v1/responses` is included in `CreateResponseRequest` for model-specific options (e.g. PII).

---

## For maintainers

The clients in `sdks/typescript` and `sdks/python` are maintained by hand. When the API changes, update `specs/zerogpu.openapi.yaml` and both clients together, then run `./scripts/sync-pypi-from-sdks.sh`.

### Publishing to npm and PyPI

| Path | Registry | Package name (change if taken) |
|------|----------|----------------------------------|
| [`npm/`](./npm/) | [npmjs.com](https://www.npmjs.com/) | `zerogpu-api` (see `npm/package.json`) |
| [`pypi/`](./pypi/) | [PyPI](https://pypi.org/) | `zerogpu-api` — `pip install zerogpu-api` imports **`zerogpu`** |

**npm**

```bash
cd npm
npm install
npm run build
npm publish --access public
```

**PyPI** — use a [venv](https://docs.python.org/3/library/venv.html) and [PyPI API token](https://pypi.org/manage/account/token/):

```bash
./scripts/sync-pypi-from-sdks.sh   # copy sdks/python into pypi/src/zerogpu
cd pypi
python -m venv .venv && . .venv/bin/activate
pip install build twine
python -m build
twine upload dist/*
```

## Repository layout

| Path | Description |
|------|-------------|
| `specs/zerogpu.openapi.yaml` | OpenAPI reference for the API |
| `sdks/` | TypeScript and Python client source |
| `npm/` | npm package (`tsup` bundles `sdks/typescript`) |
| `pypi/` | PyPI package (`src/zerogpu` synced from `sdks/python`) |
| `scripts/sync-pypi-from-sdks.sh` | Copy `sdks/python` into the PyPI package |
| `smoke/` | Live-request smoke tests for TypeScript and Python (see `smoke/README.md`) |

## License

Add a root `LICENSE` when you publish; align it with the npm and PyPI packages.

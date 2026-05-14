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

---

**ZeroGPU API SDKs** are the official API client libraries for [ZeroGPU](https://zerogpu.ai). Use them to call `POST /v1/responses` with your API key and project id.

**API reference and guides:** [docs.zerogpu.ai](https://docs.zerogpu.ai) (authentication, models, error codes).

## Languages

Clients live under `sdks/`:

| Directory | Language |
|-----------|----------|
| `sdks/typescript` | TypeScript / JavaScript |
| `sdks/python` | Python |
| `sdks/go` | Go |
| `sdks/ruby` | Ruby |
| `sdks/java` | Java |
| `sdks/rust` | Rust |
| `sdks/csharp` | C# / .NET |
| `sdks/php/sdk` | PHP |
| `sdks/swift/sdk` | Swift |

When you publish packages to npm, PyPI, crates.io, etc., point users at those registries and [docs.zerogpu.ai](https://docs.zerogpu.ai); most developers do not need the internals of the **ZeroGPU API SDKs** repository.

## Quick start (local checkout)

Environment variables (same as the [dashboard](https://zerogpu.ai) snippets):

- `ZEROGPU_API_KEY`
- `ZEROGPU_PROJECT_ID`

Clients always use the production API base URL `https://api.zerogpu.ai/v1`. There is no environment variable to change it.

**Smoke tests** — one live `POST /v1/responses` per generated SDK; see [`smoke/README.md`](./smoke/README.md). TypeScript example:

```bash
cd smoke/typescript
npm install
export ZEROGPU_API_KEY=…
export ZEROGPU_PROJECT_ID=…
export ZEROGPU_MODEL=…   # from your dashboard
npm run smoke
```

Go uses the repo [`go.work`](./go.work) so builds resolve the `sdk` module; from the **Fern SDK** directory run `go run -C smoke/go .` (after exporting the same variables).

Do not commit secrets.

### `input` shape (OpenAPI + SDKs)

The OpenAPI spec models `input` as **either** a non-empty **string** **or** a non-empty **array** of `role` / `content` messages, matching what production accepts. Regenerate clients with Fern after changing `specs/zerogpu.openapi.yaml`.

## `POST /v1/responses` (reminder)

- **Production base URL:** `https://api.zerogpu.ai/v1`
- **Path:** `/responses`
- **Headers:** `x-api-key`, `x-project-id`, `content-type: application/json`

Full spec: [Responses API](https://docs.zerogpu.ai/api-reference/endpoint/responses).

**Also supported in the generated clients:** `POST /v1/chat/completions` via `client.chat` (Python: `client.chat`) for models that use the chat-completions route. Optional **`metadata`** on `POST /v1/responses` is included in `CreateResponseRequest` for model-specific options (e.g. PII).

---

## For maintainers: regenerating clients

SDKs are generated from `specs/zerogpu.openapi.yaml` using [Fern](https://buildwithfern.com/). To update or rebuild:

1. Edit the OpenAPI file if the API changed.
2. Run `npx fern-api check` from the `fern/` directory (or repo root with paths adjusted).
3. Run `npx fern-api generate` (after `fern login` or with `FERN_TOKEN`). Generator groups and output paths are in `fern/generators.yml`.

See Fern’s [SDK quickstart](https://buildwithfern.com/learn/sdks/overview/quickstart) for CLI install details.

### Publishing to npm and PyPI (recommended)

**ZeroGPU API SDKs** ship **standalone packages** that do not rely on Fern’s paid registry flow:

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
./scripts/sync-pypi-from-sdks.sh   # after `fern generate` updates sdks/python
cd pypi
python -m venv .venv && . .venv/bin/activate
pip install build twine
python -m build
twine upload dist/*
```

After regenerating Python with Fern, run **`sync-pypi-from-sdks.sh`** so `pypi/src/zerogpu` stays in sync with `sdks/python`.

**Optional:** Fern can also publish directly from `generators.yml` ([npm](https://buildwithfern.com/learn/sdks/generators/typescript/publishing), [PyPI](https://buildwithfern.com/learn/sdks/generators/python/publishing)); you don’t need that if you use `npm/` and `pypi/` above.

## Repository layout

| Path | Description |
|------|-------------|
| `specs/zerogpu.openapi.yaml` | API definition used for generation |
| `fern/` | Fern configuration |
| `sdks/` | Generated output (do not hand-edit; regenerate) |
| `npm/` | npm package (`tsup` bundles `sdks/typescript`) |
| `pypi/` | PyPI package (`src/zerogpu` synced from `sdks/python`) |
| `scripts/sync-pypi-from-sdks.sh` | Refresh Python package after Fern regen |
| `go.work` | Go workspace linking `sdks/go` and `smoke/go` for smoke runs |
| `smoke/` | Live-request smoke tests per SDK (see `smoke/README.md`) |

## License

Add a root `LICENSE` when you publish; align it with packages you ship to npm, PyPI, etc.

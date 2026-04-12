# ZeroGPU SDK

Official API client libraries for [ZeroGPU](https://zerogpu.ai). Use them to call `POST /v1/responses` with your API key and project id.

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

When you publish packages to npm, PyPI, crates.io, etc., point users at those registries and [docs.zerogpu.ai](https://docs.zerogpu.ai); most developers do not need this repo’s internals.

## Quick start (local checkout)

Environment variables (same as the [dashboard](https://zerogpu.ai) snippets):

- `ZEROGPU_API_KEY`
- `ZEROGPU_PROJECT_ID`
- Optional: `ZEROGPU_API_URL` if you use a non-default API host (dev vs prod must match your credentials)

**Smoke test (TypeScript)** — verifies a live request with the generated client:

```bash
cd typescript-smoke
npm install
export ZEROGPU_API_KEY=…
export ZEROGPU_PROJECT_ID=…
export ZEROGPU_MODEL=…   # from your dashboard
npm run smoke
```

Do not commit secrets. See `typescript-smoke/smoke.ts` for optional `ZEROGPU_API_URL` behavior.

## `POST /v1/responses` (reminder)

- **Production base URL:** `https://api.zerogpu.ai/v1`
- **Path:** `/responses`
- **Headers:** `x-api-key`, `x-project-id`, `content-type: application/json`

Full spec: [Responses API](https://docs.zerogpu.ai/api-reference/endpoint/responses).

---

## For maintainers: regenerating clients

SDKs are generated from `specs/zerogpu.openapi.yaml` using [Fern](https://buildwithfern.com/). To update or rebuild:

1. Edit the OpenAPI file if the API changed.
2. Run `npx fern-api check` from the `fern/` directory (or repo root with paths adjusted).
3. Run `npx fern-api generate` (after `fern login` or with `FERN_TOKEN`). Generator groups and output paths are in `fern/generators.yml`.

See Fern’s [SDK quickstart](https://buildwithfern.com/learn/sdks/overview/quickstart) for CLI install details.

### Publishing to npm and PyPI

This repo currently uses **`output.location: local-file-system`** in `fern/generators.yml`, so `fern generate` writes into `sdks/` without creating a publishable **npm** or **PyPI** package manifest by itself. To publish through Fern’s pipeline, switch the **TypeScript** and **Python** groups to registry output and add metadata (package names must be unused on npmjs.org / PyPI).

**TypeScript → npm**

1. In `generators.yml`, for the TS group, set `output.location` to **`npm`**, add **`package-name`** (e.g. `@zerogpu/api`), optional **`config.namespaceExport`**, and a **`github`** block pointing at this repo (see Fern’s reference).
2. Authenticate: Fern recommends **OIDC** (“trusted publishing”) with `token: OIDC` on the npm output, or legacy **`token: ${NPM_TOKEN}`** and a GitHub secret.
3. Run `fern generate --group local` (or your TS group name) so Fern emits `package.json`, build steps, and usually a CI workflow, then follow releases as in Fern’s guide.

Full walkthrough: [Publishing to npm](https://buildwithfern.com/learn/sdks/generators/typescript/publishing).

**Python → PyPI**

1. Set **`output.location` to `pypi`**, **`package-name`** (e.g. `zerogpu`), optional **`config.client_class_name`**, **`github.repository`**, and **`token: ${PYPI_TOKEN}`** (PyPI API token in GitHub Actions secrets).
2. Run `fern generate --group python-sdk --version <semver>` with `FERN_TOKEN` (and `PYPI_TOKEN` in CI) set as Fern documents.

Full walkthrough: [Publishing to PyPI](https://buildwithfern.com/learn/sdks/generators/python/publishing).

**Without Fern’s registry mode:** you can hand-add **`package.json`** + a bundler (`tsup` / `tsc`) for TypeScript, or **`pyproject.toml`** + a `src/zerogpu` layout for Python, but that duplicates what Fern generates when `output.location` is `npm` / `pypi`—prefer the official config once you are ready to publish.

## Repository layout

| Path | Description |
|------|-------------|
| `specs/zerogpu.openapi.yaml` | API definition used for generation |
| `fern/` | Fern configuration |
| `sdks/` | Generated output (do not hand-edit; regenerate) |
| `typescript-smoke/` | Local smoke test for the TS client |

## License

Add a root `LICENSE` when you publish; align it with packages you ship to npm, PyPI, etc.

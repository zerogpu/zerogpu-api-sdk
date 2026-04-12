# zerogpu-api (npm)

Official ZeroGPU API client for Node.js and browsers (bundled TypeScript SDK).

## Install

```bash
npm install zerogpu-api
```

## Build (maintainers)

From this `npm/` directory:

```bash
npm install
npm run build
```

Output is in `dist/`. The entry bundles `../sdks/typescript` via `tsup`.

## Publish

```bash
npm publish --access public
```

Use an npm account with access to the package name (or a scoped name like `@your-org/zerogpu-api` — update `package.json`).

See the repo root `README.md` for API docs and env vars.

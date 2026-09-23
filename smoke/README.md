# SDK smoke tests

Each subdirectory runs **one live** `POST /v1/responses` call against production (`https://api.zerogpu.ai/v1`) using the generated client in `../sdks/<language>/`.

## Credentials

Set (or put in `smoke/<lang>/.env` or repo-root `Benchmark/.env` where supported):

| Variable | Required |
|----------|----------|
| `ZEROGPU_API_KEY` | Yes |
| `ZEROGPU_MODEL` | Yes — dashboard model id |

Optional: `ZEROGPU_INPUT_TEXT` — override prompt (where implemented).

Python uses **`pypi/src/zerogpu`** (same as the PyPI package). After editing `sdks/python`, run `./scripts/sync-pypi-from-sdks.sh` so `pypi/` matches.

## Run one language

| SDK | Command (from repo root) |
|-----|----------------------------------|
| TypeScript | `cd smoke/typescript && npm install && npm run smoke` |
| Python | `cd smoke/python && pip install -r requirements.txt && python smoke.py` |

## Run all (best effort)

`./smoke/run-all.sh` runs each smoke whose toolchain is on `PATH`. Failures are reported at the end; exit code is non-zero if any run failed.

Missing toolchains are skipped.

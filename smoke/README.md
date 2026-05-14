# SDK smoke tests

Each subdirectory runs **one live** `POST /v1/responses` call against production (`https://api.zerogpu.ai/v1`) using the generated client in `../sdks/<language>/`.

## Credentials

Set (or put in `smoke/<lang>/.env` or repo-root `Benchmark/.env` where supported):

| Variable | Required |
|----------|----------|
| `ZEROGPU_API_KEY` | Yes |
| `ZEROGPU_PROJECT_ID` | Yes |
| `ZEROGPU_MODEL` | Yes — dashboard model id |

Optional: `ZEROGPU_INPUT_TEXT` — override prompt (where implemented).

Python uses **`pypi/src/zerogpu`** (same as the PyPI package). After `fern generate`, run `./scripts/sync-pypi-from-sdks.sh` so `pypi/` matches `sdks/python`.

## Run one language

| SDK | Command (from repo `Fern SDK/`) |
|-----|----------------------------------|
| TypeScript | `cd smoke/typescript && npm install && npm run smoke` |
| Python | `cd smoke/python && pip install -r requirements.txt && python smoke.py` |
| Go | `go run -C smoke/go .` (must run from **Fern SDK** root so [`go.work`](../go.work) applies) |
| Ruby | `cd smoke/ruby && bundle install && bundle exec ruby smoke.rb` (Ruby **≥ 3.3** per `sdks/ruby/zerogpu.gemspec`) |
| Rust | `cd smoke/rust && cargo run` |
| C# | `cd smoke/csharp && dotnet run` |
| PHP | `cd smoke/php && composer install && php smoke.php` |
| Swift | `cd smoke/swift && swift run zerogpu-sdk-smoke` |
| Java | `cd smoke/java && mvn -q exec:java` |

## Run all (best effort)

`./smoke/run-all.sh` runs each smoke whose toolchain is on `PATH`. Failures are reported at the end; exit code is non-zero if any run failed.

Install only the stacks you care about; missing tools are skipped.

**Go:** the repo root `go.work` file includes `./sdks/go` and `./smoke/go` so the smoke binary can import the `sdk` module. Do not delete `go.work` if you rely on `smoke/go`.

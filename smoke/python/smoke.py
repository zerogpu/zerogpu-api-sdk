"""Live smoke: one POST /v1/responses via PyPI-layout Python package (`pypi/src/zerogpu`)."""
from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
# Use the standalone package tree (import `zerogpu`), not raw `sdks/python` (flat Fern
# layout shadows the stdlib `types` module when placed first on sys.path).
PY_SRC = ROOT / "pypi" / "src"
sys.path.insert(0, str(PY_SRC))

for env_path in (
    Path(__file__).resolve().parent / ".env",
    Path(__file__).resolve().parents[3] / "Benchmark" / ".env",
):
    load_dotenv(env_path)


def main() -> None:
    from zerogpu import ZerogpuApi

    api_key = (os.environ.get("ZEROGPU_API_KEY") or "").strip()
    project_id = (os.environ.get("ZEROGPU_PROJECT_ID") or "").strip()
    model = (os.environ.get("ZEROGPU_MODEL") or "").strip()
    if not api_key or not project_id:
        print("Set ZEROGPU_API_KEY and ZEROGPU_PROJECT_ID", file=sys.stderr)
        sys.exit(1)
    if not model:
        print("Set ZEROGPU_MODEL", file=sys.stderr)
        sys.exit(1)

    prompt = (os.environ.get("ZEROGPU_INPUT_TEXT") or "").strip() or (
        "In one short sentence, what is a habit tracker?"
    )

    client = ZerogpuApi(project_id=project_id, api_key=api_key)
    res = client.responses.create_response(
        model=model,
        input=prompt,
        text={"format": {"type": "text"}},
    )
    print("id:", res.id)
    print("model:", res.model)
    print("usage:", res.usage)


if __name__ == "__main__":
    main()

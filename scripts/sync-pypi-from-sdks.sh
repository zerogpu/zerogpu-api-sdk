#!/usr/bin/env bash
# After regenerating sdks/python (e.g. fern generate), sync into the PyPI package tree.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
rm -rf "${ROOT}/pypi/src/zerogpu"
mkdir -p "${ROOT}/pypi/src/zerogpu"
cp -R "${ROOT}/sdks/python/"* "${ROOT}/pypi/src/zerogpu/"
find "${ROOT}/pypi/src/zerogpu" -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
echo "Synced sdks/python -> pypi/src/zerogpu"

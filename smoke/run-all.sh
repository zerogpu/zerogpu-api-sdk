#!/usr/bin/env bash
# Run every smoke test for which the host has the toolchain.
# Usage: from Fern SDK/: ./smoke/run-all.sh
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
FAIL=0
SKIPPED=0

section() {
  echo ""
  echo "========== $1 =========="
}

skip() {
  section "$1"
  echo "SKIP: $2"
}

if command -v node >/dev/null 2>&1; then
  section "typescript"
  if (cd "$ROOT/smoke/typescript" && npm install --silent && npm run smoke); then echo "OK: typescript"; else echo "FAIL: typescript"; FAIL=$((FAIL + 1)); fi
else
  skip "typescript" "node not found"
fi

if command -v python3 >/dev/null 2>&1; then
  section "python"
  if (cd "$ROOT/smoke/python" && python3 -m pip install -q -r requirements.txt && python3 smoke.py); then echo "OK: python"; else echo "FAIL: python"; FAIL=$((FAIL + 1)); fi
else
  skip "python" "python3 not found"
fi

echo ""
echo "Done. failures=$FAIL"
[[ "$FAIL" -eq 0 ]]

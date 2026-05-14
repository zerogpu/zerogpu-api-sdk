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

if command -v go >/dev/null 2>&1; then
  section "go"
  if (cd "$ROOT" && go run -C smoke/go .); then echo "OK: go"; else echo "FAIL: go"; FAIL=$((FAIL + 1)); fi
else
  skip "go" "go not found"
fi

if command -v bundle >/dev/null 2>&1; then
  section "ruby"
  if (cd "$ROOT/smoke/ruby" && bundle install --quiet && bundle exec ruby smoke.rb); then echo "OK: ruby"; else echo "FAIL: ruby"; FAIL=$((FAIL + 1)); fi
else
  skip "ruby" "bundle not found"
fi

if command -v cargo >/dev/null 2>&1; then
  section "rust"
  if (cd "$ROOT/smoke/rust" && cargo run -q); then echo "OK: rust"; else echo "FAIL: rust"; FAIL=$((FAIL + 1)); fi
else
  skip "rust" "cargo not found"
fi

if command -v dotnet >/dev/null 2>&1; then
  section "csharp"
  if (cd "$ROOT/smoke/csharp" && dotnet run); then echo "OK: csharp"; else echo "FAIL: csharp"; FAIL=$((FAIL + 1)); fi
else
  skip "csharp" "dotnet not found"
fi

if command -v composer >/dev/null 2>&1 && command -v php >/dev/null 2>&1; then
  section "php"
  if (cd "$ROOT/smoke/php" && composer install -q && php smoke.php); then echo "OK: php"; else echo "FAIL: php"; FAIL=$((FAIL + 1)); fi
else
  skip "php" "php or composer not found"
fi

if command -v swift >/dev/null 2>&1; then
  section "swift"
  if (cd "$ROOT/smoke/swift" && swift run -q zerogpu-sdk-smoke); then echo "OK: swift"; else echo "FAIL: swift"; FAIL=$((FAIL + 1)); fi
else
  skip "swift" "swift not found"
fi

if command -v mvn >/dev/null 2>&1; then
  section "java"
  if (cd "$ROOT/smoke/java" && mvn -q exec:java); then echo "OK: java"; else echo "FAIL: java"; FAIL=$((FAIL + 1)); fi
else
  skip "java" "mvn not found"
fi

echo ""
echo "Done. failures=$FAIL"
[[ "$FAIL" -eq 0 ]]

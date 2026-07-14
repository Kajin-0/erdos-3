#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_terminal_sink_ledger}"
IDENTITY_SHA256="1f25e54d10d73c0130535d12f264405f0e5adb954820725395deb7c86ac19bf9"
BELLMAN_SHA256="7da70d79f271080a66d3f8ed1aa517d95bf321eb5d618822440fefdfa8504e14"
THIRD_SHA256="efdd41c014104f328f28c3d13b097335fd2b1730859b74134344329251b135d0"
POTENTIAL_SHA256="0e1b81e3562990e6071db64c4d6544aab1bb0c78aaae08eee780f3f9d6f81063"
FOURTH_SHA256="2c2f2103de57bd8fdcc4c32448ea9e1cf662b325e590da5e1b0758c62298c9e5"
mkdir -p "$WORK"

IDENTITY_GENERATED="$WORK/retained_terminal_sink_identity_certificate.txt"
IDENTITY_RECORDED="$ROOT/data/retained_terminal_sink_identity_certificate_2026-07-13.txt"
LEDGER="$WORK/retained_terminal_sink_identity_ledger.jsonl"

python3 "$ROOT/src/run_exact_python.py" \
  "$ROOT/src/export_retained_terminal_sink_ledger.py" \
  "$IDENTITY_GENERATED" "$LEDGER"

cmp "$IDENTITY_RECORDED" "$IDENTITY_GENERATED"
IDENTITY_ACTUAL="$(sha256sum "$IDENTITY_GENERATED" | awk '{print $1}')"
if [[ "$IDENTITY_ACTUAL" != "$IDENTITY_SHA256" ]]; then
  echo "error: retained terminal sink identity certificate SHA-256 mismatch" >&2
  echo "expected=$IDENTITY_SHA256" >&2
  echo "actual=$IDENTITY_ACTUAL" >&2
  exit 1
fi

LEDGER_ROWS="$(wc -l < "$LEDGER" | tr -d ' ')"
if [[ "$LEDGER_ROWS" != "13" ]]; then
  echo "error: retained terminal sink ledger row-count mismatch: $LEDGER_ROWS" >&2
  exit 1
fi

BELLMAN_GENERATED="$WORK/two_generation_recursive_bellman_row_certificate.txt"
BELLMAN_RECORDED="$ROOT/data/two_generation_recursive_bellman_row_certificate_2026-07-13.txt"
python3 "$ROOT/src/run_exact_python.py" \
  "$ROOT/src/verify_two_generation_recursive_bellman_row.py" \
  "$BELLMAN_GENERATED"

cmp "$BELLMAN_RECORDED" "$BELLMAN_GENERATED"
BELLMAN_ACTUAL="$(sha256sum "$BELLMAN_GENERATED" | awk '{print $1}')"
if [[ "$BELLMAN_ACTUAL" != "$BELLMAN_SHA256" ]]; then
  echo "error: two-generation recursive Bellman certificate SHA-256 mismatch" >&2
  echo "expected=$BELLMAN_SHA256" >&2
  echo "actual=$BELLMAN_ACTUAL" >&2
  exit 1
fi

THIRD_GENERATED="$WORK/third_generation_recursive_frontier_certificate.txt"
THIRD_RECORDED="$ROOT/data/third_generation_recursive_frontier_certificate_2026-07-13.txt"
python3 "$ROOT/src/run_exact_python.py" \
  "$ROOT/src/verify_third_generation_recursive_frontier.py" \
  "$THIRD_GENERATED"

cmp "$THIRD_RECORDED" "$THIRD_GENERATED"
THIRD_ACTUAL="$(sha256sum "$THIRD_GENERATED" | awk '{print $1}')"
if [[ "$THIRD_ACTUAL" != "$THIRD_SHA256" ]]; then
  echo "error: third-generation recursive frontier certificate SHA-256 mismatch" >&2
  echo "expected=$THIRD_SHA256" >&2
  echo "actual=$THIRD_ACTUAL" >&2
  exit 1
fi

POTENTIAL_GENERATED="$WORK/generation_aware_retained_potentials_certificate.txt"
POTENTIAL_RECORDED="$ROOT/data/generation_aware_retained_potentials_certificate_2026-07-13.txt"
python3 "$ROOT/src/run_exact_python.py" \
  "$ROOT/src/verify_generation_aware_retained_potentials.py" \
  "$POTENTIAL_GENERATED"

cmp "$POTENTIAL_RECORDED" "$POTENTIAL_GENERATED"
POTENTIAL_ACTUAL="$(sha256sum "$POTENTIAL_GENERATED" | awk '{print $1}')"
if [[ "$POTENTIAL_ACTUAL" != "$POTENTIAL_SHA256" ]]; then
  echo "error: generation-aware retained potential certificate SHA-256 mismatch" >&2
  echo "expected=$POTENTIAL_SHA256" >&2
  echo "actual=$POTENTIAL_ACTUAL" >&2
  exit 1
fi

FOURTH_GENERATED="$WORK/fourth_generation_potential_frontier_certificate.txt"
FOURTH_RECORDED="$ROOT/data/fourth_generation_potential_frontier_certificate_2026-07-13.txt"
python3 "$ROOT/src/run_exact_python.py" \
  "$ROOT/src/verify_fourth_generation_potential_frontier.py" \
  "$FOURTH_GENERATED"

cmp "$FOURTH_RECORDED" "$FOURTH_GENERATED"
FOURTH_ACTUAL="$(sha256sum "$FOURTH_GENERATED" | awk '{print $1}')"
if [[ "$FOURTH_ACTUAL" != "$FOURTH_SHA256" ]]; then
  echo "error: fourth-generation provenance-reserve certificate SHA-256 mismatch" >&2
  echo "expected=$FOURTH_SHA256" >&2
  echo "actual=$FOURTH_ACTUAL" >&2
  exit 1
fi

echo "retained_terminal_sink_identity_sha256=$IDENTITY_ACTUAL"
echo "retained_terminal_sink_ledger_rows=$LEDGER_ROWS"
echo "two_generation_recursive_bellman_sha256=$BELLMAN_ACTUAL"
echo "third_generation_recursive_frontier_sha256=$THIRD_ACTUAL"
echo "generation_aware_retained_potentials_sha256=$POTENTIAL_ACTUAL"
echo "fourth_generation_potential_frontier_sha256=$FOURTH_ACTUAL"
echo "verified: terminal identities, third-generation candidate potentials, fourth-generation failure, and refined token survival"

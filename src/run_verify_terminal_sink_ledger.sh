#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_terminal_sink_ledger}"
EXPECTED_SHA256="1f25e54d10d73c0130535d12f264405f0e5adb954820725395deb7c86ac19bf9"
mkdir -p "$WORK"

GENERATED="$WORK/retained_terminal_sink_identity_certificate.txt"
RECORDED="$ROOT/data/retained_terminal_sink_identity_certificate_2026-07-13.txt"
LEDGER="$WORK/retained_terminal_sink_identity_ledger.jsonl"

python3 "$ROOT/src/run_exact_python.py" \
  "$ROOT/src/export_retained_terminal_sink_ledger.py" \
  "$GENERATED" "$LEDGER"

cmp "$RECORDED" "$GENERATED"
ACTUAL_SHA256="$(sha256sum "$GENERATED" | awk '{print $1}')"
if [[ "$ACTUAL_SHA256" != "$EXPECTED_SHA256" ]]; then
  echo "error: retained terminal sink identity certificate SHA-256 mismatch" >&2
  echo "expected=$EXPECTED_SHA256" >&2
  echo "actual=$ACTUAL_SHA256" >&2
  exit 1
fi

LEDGER_ROWS="$(wc -l < "$LEDGER" | tr -d ' ')"
if [[ "$LEDGER_ROWS" != "13" ]]; then
  echo "error: retained terminal sink ledger row-count mismatch: $LEDGER_ROWS" >&2
  exit 1
fi

echo "retained_terminal_sink_identity_sha256=$ACTUAL_SHA256"
echo "retained_terminal_sink_ledger_rows=$LEDGER_ROWS"
echo "verified: exact numerical and provenance identities for 13 retained terminal sinks"

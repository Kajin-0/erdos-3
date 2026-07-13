#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_transport_reserve}"
EXPECTED_SHA256="4928834ff35d05804882a9c1519185cec80e97fd0953ce186415b2ea746bf8f1"

mkdir -p "$WORK"
GENERATED="$WORK/transport_interval_capacity_certificate.txt"
RECORDED="$ROOT/data/transport_interval_capacity_certificate_2026-07-13.txt"

python3 "$ROOT/src/verify_transport_interval_capacity.py" "$GENERATED"
cmp "$RECORDED" "$GENERATED"

ACTUAL_SHA256="$(sha256sum "$GENERATED" | awk '{print $1}')"
if [[ "$ACTUAL_SHA256" != "$EXPECTED_SHA256" ]]; then
  echo "error: transport certificate SHA-256 mismatch" >&2
  echo "expected=$EXPECTED_SHA256" >&2
  echo "actual=$ACTUAL_SHA256" >&2
  exit 1
fi

python3 "$ROOT/src/branching_reserve_lp.py" self-test

echo "certificate_sha256=$ACTUAL_SHA256"
echo "verified: transport interval capacity and branching-reserve LP harness"

#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_transport_reserve}"

TRANSPORT_SHA256="4928834ff35d05804882a9c1519185cec80e97fd0953ce186415b2ea746bf8f1"
REPLAY_SHA256="9c76d18a0c90f2818a47d39ecb9e8067c3b0f5663bd1daf252356e765e6d781d"
NAIVE_NO_GO_SHA256="67a8f08bdaacb838a364079c9fe9e03f7fcf3ae8325ba4aee970c997791664b8"

mkdir -p "$WORK"

verify_sha256() {
  local path="$1"
  local expected="$2"
  local label="$3"
  local actual
  actual="$(sha256sum "$path" | awk '{print $1}')"
  if [[ "$actual" != "$expected" ]]; then
    echo "error: $label SHA-256 mismatch" >&2
    echo "expected=$expected" >&2
    echo "actual=$actual" >&2
    exit 1
  fi
  echo "$label_sha256=$actual" | sed "s/label_/${label}_/"
}

TRANSPORT_GENERATED="$WORK/transport_interval_capacity_certificate.txt"
TRANSPORT_RECORDED="$ROOT/data/transport_interval_capacity_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_transport_interval_capacity.py" \
  "$TRANSPORT_GENERATED"
cmp "$TRANSPORT_RECORDED" "$TRANSPORT_GENERATED"
verify_sha256 "$TRANSPORT_GENERATED" "$TRANSPORT_SHA256" "transport"

REPLAY_GENERATED="$WORK/replay_transition_catalog_certificate.txt"
REPLAY_RECORDED="$ROOT/data/replay_transition_catalog_certificate_2026-07-13.txt"
python3 "$ROOT/src/export_replay_transition_catalog.py" self-test \
  "$REPLAY_GENERATED"
cmp "$REPLAY_RECORDED" "$REPLAY_GENERATED"
verify_sha256 "$REPLAY_GENERATED" "$REPLAY_SHA256" "replay"

NAIVE_GENERATED="$WORK/naive_reserve_no_go_certificate.txt"
NAIVE_RECORDED="$ROOT/data/naive_reserve_no_go_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_naive_reserve_no_go.py" \
  "$NAIVE_GENERATED"
cmp "$NAIVE_RECORDED" "$NAIVE_GENERATED"
verify_sha256 "$NAIVE_GENERATED" "$NAIVE_NO_GO_SHA256" "naive_no_go"

python3 "$ROOT/src/certified_contaminated_states.py" > /dev/null
python3 "$ROOT/src/branching_reserve_lp.py" self-test

echo "verified: transport capacity, replay catalog, naive no-go, and LP harness"

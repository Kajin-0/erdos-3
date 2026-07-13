#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_transport_reserve}"

TRANSPORT_SHA256="4928834ff35d05804882a9c1519185cec80e97fd0953ce186415b2ea746bf8f1"
REPLAY_SHA256="9c76d18a0c90f2818a47d39ecb9e8067c3b0f5663bd1daf252356e765e6d781d"
NAIVE_NO_GO_SHA256="67a8f08bdaacb838a364079c9fe9e03f7fcf3ae8325ba4aee970c997791664b8"
S1_DAG_SHA256="e31c232158b2abed03ebf7ec12e60d44ef14cff9ae7e066afaa645c80dd9b639"
S1_ALL_SHA256="8a0726c30041eba72d047924922cfc7c1ba756c63d58da3a04d92f27919273cc"
S2_NOVEL_SHA256="c552a6146531e02b19a1416c8913287d1efa86a0520eab031899630f8ecd33d7"
S2_ZERO_SHA256="e5d7a3bbefea78c7c5eeb85ec9155e947d00443e8c279ba6cfc72978267bf972"

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
  echo "${label}_sha256=$actual"
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

S1_DAG_GENERATED="$WORK/s1_deletion_dag_adapter.json"
S1_DAG_RECORDED="$ROOT/data/s1_deletion_dag_adapter_certificate_2026-07-13.json"
python3 "$ROOT/src/verify_s1_deletion_dag_adapter.py" \
  "$S1_DAG_GENERATED"
cmp "$S1_DAG_RECORDED" "$S1_DAG_GENERATED"
verify_sha256 "$S1_DAG_GENERATED" "$S1_DAG_SHA256" "s1_dag"

S1_ALL_GENERATED="$WORK/s1_all_deletion_schedules_certificate.txt"
S1_ALL_RECORDED="$ROOT/data/s1_all_deletion_schedules_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_s1_all_deletion_schedules.py" \
  "$S1_ALL_GENERATED"
cmp "$S1_ALL_RECORDED" "$S1_ALL_GENERATED"
verify_sha256 "$S1_ALL_GENERATED" "$S1_ALL_SHA256" "s1_all"

S2_NOVEL_GENERATED="$WORK/s2_novel_fiber_reference_certificate.txt"
S2_NOVEL_RECORDED="$ROOT/data/s2_novel_fiber_reference_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_s2_novel_fiber_reference.py" \
  "$S2_NOVEL_GENERATED"
cmp "$S2_NOVEL_RECORDED" "$S2_NOVEL_GENERATED"
verify_sha256 "$S2_NOVEL_GENERATED" "$S2_NOVEL_SHA256" "s2_novel"

S2_ZERO_GENERATED="$WORK/s2_zero_novelty_schedule_certificate.txt"
S2_ZERO_RECORDED="$ROOT/data/s2_zero_novelty_schedule_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_s2_zero_novelty_schedule.py" \
  "$S2_ZERO_GENERATED"
cmp "$S2_ZERO_RECORDED" "$S2_ZERO_GENERATED"
verify_sha256 "$S2_ZERO_GENERATED" "$S2_ZERO_SHA256" "s2_zero"

python3 "$ROOT/src/certified_contaminated_states.py" > /dev/null
python3 "$ROOT/src/branching_reserve_lp.py" self-test

echo "verified: transport, replay, reserve diagnostics, S1/S2 DAG checks, and LP harness"

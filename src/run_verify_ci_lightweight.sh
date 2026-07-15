#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_ci_lightweight}"
mkdir -p "$WORK"

verify_sha256() {
  local path="$1" expected="$2" label="$3" actual
  actual="$(sha256sum "$path" | awk '{print $1}')"
  if [[ "$actual" != "$expected" ]]; then
    echo "error: $label SHA-256 mismatch" >&2
    echo "expected=$expected" >&2
    echo "actual=$actual" >&2
    exit 1
  fi
  echo "${label}_sha256=$actual"
}

run_check() {
  local label="$1" expected="$2" recorded="$3" generated="$4"
  shift 4
  echo "running_lightweight_check=$label"
  "$@"
  cmp "$recorded" "$generated"
  verify_sha256 "$generated" "$expected" "$label"
}

run_check transport \
  4928834ff35d05804882a9c1519185cec80e97fd0953ce186415b2ea746bf8f1 \
  "$ROOT/data/transport_interval_capacity_certificate_2026-07-13.txt" \
  "$WORK/transport_interval_capacity_certificate.txt" \
  python3 "$ROOT/src/verify_transport_interval_capacity.py" \
  "$WORK/transport_interval_capacity_certificate.txt"

run_check replay \
  9c76d18a0c90f2818a47d39ecb9e8067c3b0f5663bd1daf252356e765e6d781d \
  "$ROOT/data/replay_transition_catalog_certificate_2026-07-13.txt" \
  "$WORK/replay_transition_catalog_certificate.txt" \
  python3 "$ROOT/src/export_replay_transition_catalog.py" self-test \
  "$WORK/replay_transition_catalog_certificate.txt"

run_check naive_no_go \
  67a8f08bdaacb838a364079c9fe9e03f7fcf3ae8325ba4aee970c997791664b8 \
  "$ROOT/data/naive_reserve_no_go_certificate_2026-07-13.txt" \
  "$WORK/naive_reserve_no_go_certificate.txt" \
  python3 "$ROOT/src/verify_naive_reserve_no_go.py" \
  "$WORK/naive_reserve_no_go_certificate.txt"

run_check s1_dag \
  e31c232158b2abed03ebf7ec12e60d44ef14cff9ae7e066afaa645c80dd9b639 \
  "$ROOT/data/s1_deletion_dag_adapter_certificate_2026-07-13.json" \
  "$WORK/s1_deletion_dag_adapter.json" \
  python3 "$ROOT/src/verify_s1_deletion_dag_adapter.py" \
  "$WORK/s1_deletion_dag_adapter.json"

run_check s1_all \
  8a0726c30041eba72d047924922cfc7c1ba756c63d58da3a04d92f27919273cc \
  "$ROOT/data/s1_all_deletion_schedules_certificate_2026-07-13.txt" \
  "$WORK/s1_all_deletion_schedules_certificate.txt" \
  python3 "$ROOT/src/verify_s1_all_deletion_schedules.py" \
  "$WORK/s1_all_deletion_schedules_certificate.txt"

run_check s1_overlap \
  64d1680ce30699ef2c7ac53fa9b42e88e2085c442dd32ccd9178bf0c7be828aa \
  "$ROOT/data/s1_schedule_overlap_floor_certificate_2026-07-13.txt" \
  "$WORK/s1_schedule_overlap_floor_certificate.txt" \
  python3 "$ROOT/src/verify_s1_schedule_overlap_floor.py" \
  "$WORK/s1_schedule_overlap_floor_certificate.txt"

run_check s2_novel \
  c552a6146531e02b19a1416c8913287d1efa86a0520eab031899630f8ecd33d7 \
  "$ROOT/data/s2_novel_fiber_reference_certificate_2026-07-13.txt" \
  "$WORK/s2_novel_fiber_reference_certificate.txt" \
  python3 "$ROOT/src/verify_s2_novel_fiber_reference.py" \
  "$WORK/s2_novel_fiber_reference_certificate.txt"

run_check s2_zero \
  e5d7a3bbefea78c7c5eeb85ec9155e947d00443e8c279ba6cfc72978267bf972 \
  "$ROOT/data/s2_zero_novelty_schedule_certificate_2026-07-13.txt" \
  "$WORK/s2_zero_novelty_schedule_certificate.txt" \
  python3 "$ROOT/src/verify_s2_zero_novelty_schedule.py" \
  "$WORK/s2_zero_novelty_schedule_certificate.txt"

python3 "$ROOT/src/verify_sponsor_pair_transport_small_box.py"
python3 "$ROOT/src/verify_canonical_hole_witness_pair_small_box.py"
python3 "$ROOT/src/verify_completion_step_fiber_light_heavy.py"
python3 "$ROOT/src/certified_contaminated_states.py" > /dev/null
python3 "$ROOT/src/branching_reserve_lp.py" self-test

echo "verified: lightweight exact certificates, independent pair, hole-witness, and completion-fiber transfer checks, and LP harness"

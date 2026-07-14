#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_terminal_sink_ledger}"
IDENTITY_SHA256="1f25e54d10d73c0130535d12f264405f0e5adb954820725395deb7c86ac19bf9"
BELLMAN_SHA256="7da70d79f271080a66d3f8ed1aa517d95bf321eb5d618822440fefdfa8504e14"
THIRD_SHA256="efdd41c014104f328f28c3d13b097335fd2b1730859b74134344329251b135d0"
POTENTIAL_SHA256="0e1b81e3562990e6071db64c4d6544aab1bb0c78aaae08eee780f3f9d6f81063"
FOURTH_SHA256="2c2f2103de57bd8fdcc4c32448ea9e1cf662b325e590da5e1b0758c62298c9e5"
FIFTH_SHA256="74120626dcf65e06beae044f37ff570be8113c494ab81ad3bdeba3aa67378bfb"
POLICY_SHA256="996d444724e5081986509fe539542ab19508c648ca9f8158650b387b542d6769"
ROOT_TRANSFER_SHA256="460bbf1a5b21a662353041b8e576fc8809a4823553fa63cc8ae7dc9ce469564a"
PAIR_ENERGY_SHA256="8cbda92325c346cff0e203350f55aaedc976d3995f5b4c734c3f431775bd3d2f"
PAIR_OWNERSHIP_SHA256="d60a49d35355be9cc078bd81eb1013a6af27cc9096e083334081024ce4781b92"
RESIDUAL_SPONSOR_SHA256="28266cae2b603b7a2490d547ef96d429e06e31cba4706ccc1f0fe0dbdc7bc986"
mkdir -p "$WORK"

verify_certificate() {
  local script="$1"
  local recorded="$2"
  local generated="$3"
  local expected="$4"
  local label="$5"
  python3 "$ROOT/src/run_exact_python.py" "$ROOT/src/$script" "$generated"
  cmp "$ROOT/data/$recorded" "$generated"
  local actual
  actual="$(sha256sum "$generated" | awk '{print $1}')"
  if [[ "$actual" != "$expected" ]]; then
    echo "error: $label certificate SHA-256 mismatch" >&2
    echo "expected=$expected" >&2
    echo "actual=$actual" >&2
    exit 1
  fi
  echo "${label}_sha256=$actual"
}

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
  exit 1
fi
LEDGER_ROWS="$(wc -l < "$LEDGER" | tr -d ' ')"
if [[ "$LEDGER_ROWS" != "13" ]]; then
  echo "error: retained terminal sink ledger row-count mismatch: $LEDGER_ROWS" >&2
  exit 1
fi

echo "retained_terminal_sink_identity_sha256=$IDENTITY_ACTUAL"
echo "retained_terminal_sink_ledger_rows=$LEDGER_ROWS"
verify_certificate \
  "verify_two_generation_recursive_bellman_row.py" \
  "two_generation_recursive_bellman_row_certificate_2026-07-13.txt" \
  "$WORK/two_generation_recursive_bellman_row_certificate.txt" \
  "$BELLMAN_SHA256" \
  "two_generation_recursive_bellman"
verify_certificate \
  "verify_third_generation_recursive_frontier.py" \
  "third_generation_recursive_frontier_certificate_2026-07-13.txt" \
  "$WORK/third_generation_recursive_frontier_certificate.txt" \
  "$THIRD_SHA256" \
  "third_generation_recursive_frontier"
verify_certificate \
  "verify_generation_aware_retained_potentials.py" \
  "generation_aware_retained_potentials_certificate_2026-07-13.txt" \
  "$WORK/generation_aware_retained_potentials_certificate.txt" \
  "$POTENTIAL_SHA256" \
  "generation_aware_retained_potentials"
verify_certificate \
  "verify_fourth_generation_potential_frontier.py" \
  "fourth_generation_potential_frontier_certificate_2026-07-13.txt" \
  "$WORK/fourth_generation_potential_frontier_certificate.txt" \
  "$FOURTH_SHA256" \
  "fourth_generation_potential_frontier"
verify_certificate \
  "verify_fifth_generation_feature_frontier.py" \
  "fifth_generation_feature_frontier_certificate_2026-07-13.txt" \
  "$WORK/fifth_generation_feature_frontier_certificate.txt" \
  "$FIFTH_SHA256" \
  "fifth_generation_feature_frontier"
verify_certificate \
  "verify_fourth_to_fifth_policy_sensitivity.py" \
  "fourth_to_fifth_policy_sensitivity_certificate_2026-07-14.txt" \
  "$WORK/fourth_to_fifth_policy_sensitivity_certificate.txt" \
  "$POLICY_SHA256" \
  "fourth_to_fifth_policy_sensitivity"
verify_certificate \
  "verify_fourth_to_fifth_root_transfer.py" \
  "fourth_to_fifth_root_transfer_certificate_2026-07-14.txt" \
  "$WORK/fourth_to_fifth_root_transfer_certificate.txt" \
  "$ROOT_TRANSFER_SHA256" \
  "fourth_to_fifth_root_transfer"
verify_certificate \
  "verify_pair_energy_frontier.py" \
  "pair_energy_frontier_certificate_2026-07-14.txt" \
  "$WORK/pair_energy_frontier_certificate.txt" \
  "$PAIR_ENERGY_SHA256" \
  "pair_energy_frontier"
verify_certificate \
  "verify_pair_resource_ownership.py" \
  "pair_resource_ownership_certificate_2026-07-14.txt" \
  "$WORK/pair_resource_ownership_certificate.txt" \
  "$PAIR_OWNERSHIP_SHA256" \
  "pair_resource_ownership"
verify_certificate \
  "verify_residual_sponsor_backbone_split.py" \
  "residual_sponsor_backbone_split_certificate_2026-07-14.txt" \
  "$WORK/residual_sponsor_backbone_split_certificate.txt" \
  "$RESIDUAL_SPONSOR_SHA256" \
  "residual_sponsor_backbone_split"

echo "verified: terminal identities, recursive frontiers through generation five, local policy sensitivity, root-lineage transfer, affine pair-energy Bellman contraction, exact pair-resource ownership, and residual-sponsor backbone refinement"

#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_transition_frontier}"
EXACT_PYTHON="$ROOT/src/run_exact_python.py"
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
  echo "running_exact_check=$label"
  "$@"
  cmp "$recorded" "$generated"
  verify_sha256 "$generated" "$expected" "$label"
}

run_check simultaneous_transition \
  e8162ee59d496bec8fe2d4103edc8f79de9fbd42444ef37f41fc317aec13a14b \
  "$ROOT/data/simultaneous_deletion_transition_certificate_2026-07-13.txt" \
  "$WORK/simultaneous_deletion_transition_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/export_simultaneous_deletion_transition.py" self-test \
  "$WORK/simultaneous_deletion_transition_certificate.txt"

run_check occurrence_multiplicity \
  9774ea7c8cbd3626b3120ade6b48344008b5f1706b05e253923393cc8495e7e8 \
  "$ROOT/data/recursive_occurrence_multiplicity_certificate_2026-07-13.txt" \
  "$WORK/recursive_occurrence_multiplicity_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_recursive_occurrence_multiplicity.py" \
  "$WORK/recursive_occurrence_multiplicity_certificate.txt"

run_check simultaneous_s4_s5 \
  ada237c35a0980c15cecac51e30fd43ade50948067d6f421477af1bb79239756 \
  "$ROOT/data/simultaneous_transition_s4_s5_certificate_2026-07-13.txt" \
  "$WORK/simultaneous_transition_s4_s5_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_simultaneous_transition_s4_s5.py" \
  "$WORK/simultaneous_transition_s4_s5_certificate.txt"

run_check simultaneous_s6_s7 \
  4c1767a8c0b4e65b2deb4e576bfec6f8b74e6531f4ef12e4444fd53a9d0cb94c \
  "$ROOT/data/simultaneous_transition_s6_s7_certificate_2026-07-13.txt" \
  "$WORK/simultaneous_transition_s6_s7_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_simultaneous_transition_s6_s7.py" \
  "$WORK/simultaneous_transition_s6_s7_certificate.txt"

run_check terminal_fiber \
  ddedf75bd52a6cc67cef6ecb0a635b836e9a1c7c5094a860449dd35dd2651c18 \
  "$ROOT/data/terminal_fiber_incidence_certificate_2026-07-13.txt" \
  "$WORK/terminal_fiber_incidence_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_terminal_fiber_incidence.py" \
  "$WORK/terminal_fiber_incidence_certificate.txt"

run_check terminal_fiber_scc \
  3166cbb0801eb774e8b6691ace6a8612f5457a9415bd8ae3762a1260216d0fe2 \
  "$ROOT/data/terminal_fiber_scc_quotient_certificate_2026-07-13.txt" \
  "$WORK/terminal_fiber_scc_quotient_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/export_terminal_fiber_scc_quotient.py" self-test \
  "$WORK/terminal_fiber_scc_quotient_certificate.txt"

run_check terminal_fiber_spectral \
  aa753127d2d0adbcb124b0a9f6e5c053350d422cd66fe2a4c73d1045b2917bf4 \
  "$ROOT/data/terminal_fiber_scc_spectral_growth_certificate_2026-07-13.txt" \
  "$WORK/terminal_fiber_scc_spectral_growth_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_terminal_fiber_scc_spectral_growth.py" \
  "$WORK/terminal_fiber_scc_spectral_growth_certificate.txt"

run_check s7_scc_output_load \
  cb5dbba5f45c25b2c286fde17e9895d017abaa906f69f73255a5f0b5b62d081d \
  "$ROOT/data/s7_scc_output_load_certificate_2026-07-13.txt" \
  "$WORK/s7_scc_output_load_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_s7_scc_output_load.py" \
  "$WORK/s7_scc_output_load_certificate.txt"

run_check s7_scc_local_completion \
  0419cdeab12c1a8ab2f55e041a0259ffde77f90df7031be0736137502e6ff737 \
  "$ROOT/data/s7_scc_local_completion_credit_certificate_2026-07-13.txt" \
  "$WORK/s7_scc_local_completion_credit_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_s7_scc_local_completion_credit.py" \
  "$WORK/s7_scc_local_completion_credit_certificate.txt"

run_check s7_scc_small_affine \
  6a1073d6fd485c0a99526c59c32b5a0985220632e32e67fc8fed9d5b8c5234e0 \
  "$ROOT/data/s7_scc_small_state_affine_frontier_certificate_2026-07-13.txt" \
  "$WORK/s7_scc_small_state_affine_frontier_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_s7_scc_small_state_affine_frontier.py" \
  "$WORK/s7_scc_small_state_affine_frontier_certificate.txt"

run_check s7_scc_seed_regeneration \
  03da3a4d6a2a878b9ca3ba45d0862932ba06512a9697bd828f7fc73e5883421c \
  "$ROOT/data/s7_scc_seed_regeneration_certificate_2026-07-13.txt" \
  "$WORK/s7_scc_seed_regeneration_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_s7_scc_seed_regeneration.py" \
  "$WORK/s7_scc_seed_regeneration_certificate.txt"

run_check s7_seed_policy_dependence \
  8b7465459f04d07bd67a7f198b3947ca94756ce988c0c73f4e59a5fac6b4b336 \
  "$ROOT/data/s7_regenerative_seed_policy_dependence_certificate_2026-07-13.txt" \
  "$WORK/s7_regenerative_seed_policy_dependence_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_s7_regenerative_seed_policy_dependence.py" \
  "$WORK/s7_regenerative_seed_policy_dependence_certificate.txt"

run_check s7_policy_transition_tradeoff \
  e4313f37643ad729fb8faa160ae63d5d59d61c521b149258a6aa131485dec70d \
  "$ROOT/data/s7_policy_transition_tradeoff_certificate_2026-07-13.txt" \
  "$WORK/s7_policy_transition_tradeoff_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_s7_policy_transition_tradeoff.py" \
  "$WORK/s7_policy_transition_tradeoff_certificate.txt"

run_check s7_delayed_seed_policy \
  37ed54c207820478fb5b2b2843342b2aebd9b274b4dd5ef1e6cf79e3d627f4e9 \
  "$ROOT/data/s7_delayed_seed_policy_certificate_2026-07-13.txt" \
  "$WORK/s7_delayed_seed_policy_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_s7_delayed_seed_policy.py" \
  "$WORK/s7_delayed_seed_policy_certificate.txt"

run_check s7_policy_weight_regions \
  97f45313494b16f022f47f87ef1c788962011c76c349dc88faef1ba8e1838693 \
  "$ROOT/data/s7_policy_weight_regions_certificate_2026-07-13.txt" \
  "$WORK/s7_policy_weight_regions_certificate.txt" \
  python3 "$EXACT_PYTHON" "$ROOT/src/verify_s7_policy_weight_regions.py" \
  "$WORK/s7_policy_weight_regions_certificate.txt"

echo "verified: simultaneous transition, SCC, obstruction, regeneration, policy tradeoff, delayed policy, and exact weight regions through S7"

#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_transition_frontier}"

SIMULTANEOUS_TRANSITION_SHA256="e8162ee59d496bec8fe2d4103edc8f79de9fbd42444ef37f41fc317aec13a14b"
OCCURRENCE_MULTIPLICITY_SHA256="9774ea7c8cbd3626b3120ade6b48344008b5f1706b05e253923393cc8495e7e8"
SIMULTANEOUS_S4_S5_SHA256="ada237c35a0980c15cecac51e30fd43ade50948067d6f421477af1bb79239756"
SIMULTANEOUS_S6_S7_SHA256="4c1767a8c0b4e65b2deb4e576bfec6f8b74e6531f4ef12e4444fd53a9d0cb94c"
TERMINAL_FIBER_SHA256="ddedf75bd52a6cc67cef6ecb0a635b836e9a1c7c5094a860449dd35dd2651c18"
TERMINAL_FIBER_SCC_SHA256="3166cbb0801eb774e8b6691ace6a8612f5457a9415bd8ae3762a1260216d0fe2"
TERMINAL_FIBER_SPECTRAL_SHA256="aa753127d2d0adbcb124b0a9f6e5c053350d422cd66fe2a4c73d1045b2917bf4"
S7_SCC_OUTPUT_LOAD_SHA256="cb5dbba5f45c25b2c286fde17e9895d017abaa906f69f73255a5f0b5b62d081d"
S7_SCC_LOCAL_COMPLETION_SHA256="0419cdeab12c1a8ab2f55e041a0259ffde77f90df7031be0736137502e6ff737"

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

SIMULTANEOUS_TRANSITION_GENERATED="$WORK/simultaneous_deletion_transition_certificate.txt"
SIMULTANEOUS_TRANSITION_RECORDED="$ROOT/data/simultaneous_deletion_transition_certificate_2026-07-13.txt"
python3 "$ROOT/src/export_simultaneous_deletion_transition.py" self-test \
  "$SIMULTANEOUS_TRANSITION_GENERATED"
cmp "$SIMULTANEOUS_TRANSITION_RECORDED" "$SIMULTANEOUS_TRANSITION_GENERATED"
verify_sha256 "$SIMULTANEOUS_TRANSITION_GENERATED" "$SIMULTANEOUS_TRANSITION_SHA256" "simultaneous_transition"

OCCURRENCE_MULTIPLICITY_GENERATED="$WORK/recursive_occurrence_multiplicity_certificate.txt"
OCCURRENCE_MULTIPLICITY_RECORDED="$ROOT/data/recursive_occurrence_multiplicity_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_recursive_occurrence_multiplicity.py" \
  "$OCCURRENCE_MULTIPLICITY_GENERATED"
cmp "$OCCURRENCE_MULTIPLICITY_RECORDED" "$OCCURRENCE_MULTIPLICITY_GENERATED"
verify_sha256 "$OCCURRENCE_MULTIPLICITY_GENERATED" "$OCCURRENCE_MULTIPLICITY_SHA256" "occurrence_multiplicity"

SIMULTANEOUS_S4_S5_GENERATED="$WORK/simultaneous_transition_s4_s5_certificate.txt"
SIMULTANEOUS_S4_S5_RECORDED="$ROOT/data/simultaneous_transition_s4_s5_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_simultaneous_transition_s4_s5.py" \
  "$SIMULTANEOUS_S4_S5_GENERATED"
cmp "$SIMULTANEOUS_S4_S5_RECORDED" "$SIMULTANEOUS_S4_S5_GENERATED"
verify_sha256 "$SIMULTANEOUS_S4_S5_GENERATED" "$SIMULTANEOUS_S4_S5_SHA256" "simultaneous_s4_s5"

SIMULTANEOUS_S6_S7_GENERATED="$WORK/simultaneous_transition_s6_s7_certificate.txt"
SIMULTANEOUS_S6_S7_RECORDED="$ROOT/data/simultaneous_transition_s6_s7_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_simultaneous_transition_s6_s7.py" \
  "$SIMULTANEOUS_S6_S7_GENERATED"
cmp "$SIMULTANEOUS_S6_S7_RECORDED" "$SIMULTANEOUS_S6_S7_GENERATED"
verify_sha256 "$SIMULTANEOUS_S6_S7_GENERATED" "$SIMULTANEOUS_S6_S7_SHA256" "simultaneous_s6_s7"

TERMINAL_FIBER_GENERATED="$WORK/terminal_fiber_incidence_certificate.txt"
TERMINAL_FIBER_RECORDED="$ROOT/data/terminal_fiber_incidence_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_terminal_fiber_incidence.py" \
  "$TERMINAL_FIBER_GENERATED"
cmp "$TERMINAL_FIBER_RECORDED" "$TERMINAL_FIBER_GENERATED"
verify_sha256 "$TERMINAL_FIBER_GENERATED" "$TERMINAL_FIBER_SHA256" "terminal_fiber"

TERMINAL_FIBER_SCC_GENERATED="$WORK/terminal_fiber_scc_quotient_certificate.txt"
TERMINAL_FIBER_SCC_RECORDED="$ROOT/data/terminal_fiber_scc_quotient_certificate_2026-07-13.txt"
python3 "$ROOT/src/export_terminal_fiber_scc_quotient.py" self-test \
  "$TERMINAL_FIBER_SCC_GENERATED"
cmp "$TERMINAL_FIBER_SCC_RECORDED" "$TERMINAL_FIBER_SCC_GENERATED"
verify_sha256 "$TERMINAL_FIBER_SCC_GENERATED" "$TERMINAL_FIBER_SCC_SHA256" "terminal_fiber_scc"

TERMINAL_FIBER_SPECTRAL_GENERATED="$WORK/terminal_fiber_scc_spectral_growth_certificate.txt"
TERMINAL_FIBER_SPECTRAL_RECORDED="$ROOT/data/terminal_fiber_scc_spectral_growth_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_terminal_fiber_scc_spectral_growth.py" \
  "$TERMINAL_FIBER_SPECTRAL_GENERATED"
cmp "$TERMINAL_FIBER_SPECTRAL_RECORDED" "$TERMINAL_FIBER_SPECTRAL_GENERATED"
verify_sha256 "$TERMINAL_FIBER_SPECTRAL_GENERATED" "$TERMINAL_FIBER_SPECTRAL_SHA256" "terminal_fiber_spectral"

S7_SCC_OUTPUT_LOAD_GENERATED="$WORK/s7_scc_output_load_certificate.txt"
S7_SCC_OUTPUT_LOAD_RECORDED="$ROOT/data/s7_scc_output_load_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_s7_scc_output_load.py" \
  "$S7_SCC_OUTPUT_LOAD_GENERATED"
cmp "$S7_SCC_OUTPUT_LOAD_RECORDED" "$S7_SCC_OUTPUT_LOAD_GENERATED"
verify_sha256 "$S7_SCC_OUTPUT_LOAD_GENERATED" "$S7_SCC_OUTPUT_LOAD_SHA256" "s7_scc_output_load"

S7_SCC_LOCAL_COMPLETION_GENERATED="$WORK/s7_scc_local_completion_credit_certificate.txt"
S7_SCC_LOCAL_COMPLETION_RECORDED="$ROOT/data/s7_scc_local_completion_credit_certificate_2026-07-13.txt"
python3 "$ROOT/src/verify_s7_scc_local_completion_credit.py" \
  "$S7_SCC_LOCAL_COMPLETION_GENERATED"
cmp "$S7_SCC_LOCAL_COMPLETION_RECORDED" "$S7_SCC_LOCAL_COMPLETION_GENERATED"
verify_sha256 "$S7_SCC_LOCAL_COMPLETION_GENERATED" "$S7_SCC_LOCAL_COMPLETION_SHA256" "s7_scc_local_completion"

echo "verified: simultaneous transition, multiplicity, incidence, SCC, spectral, output-load, and local-completion frontier through S7"

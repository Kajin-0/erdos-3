#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_depth10_residual_multik_rectangle_profile}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-$(nproc)}"
EXPECTED_WITNESS_SHA256="e43df5b7621ead4ee9bd1b02d3c812114a7d9a60f9130de0b5f6ab8cad419929"

mkdir -p "$WORK"
bash "$ROOT/src/run_sample_depth10_lifted_s9_completion_residual.sh" "$WORK"

python3 "$ROOT/src/verify_four_ratio_rectangle_transport.py" \
  "$WORK/four_ratio_rectangle_transport_certificate.txt"

$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_depth10_residual_multik_rectangle_profile.cpp" \
  -o "$WORK/verify_depth10_residual_multik_rectangle_profile"

export OMP_NUM_THREADS="$THREADS"
SAMPLE="$WORK/depth10_lifted_completion_residual_equal_rank512.txt"
WITNESSES="$WORK/depth10_residual_multik_rectangle_witnesses512.txt"
"$WORK/verify_depth10_residual_multik_rectangle_profile" "$SAMPLE" "$WITNESSES"

ACTUAL_SHA256="$(sha256sum "$WITNESSES" | awk '{print $1}')"
if [[ "$ACTUAL_SHA256" != "$EXPECTED_WITNESS_SHA256" ]]; then
  echo "error: witness SHA-256 mismatch" >&2
  echo "expected=$EXPECTED_WITNESS_SHA256" >&2
  echo "actual=$ACTUAL_SHA256" >&2
  exit 1
fi

echo "witness_sha256=$ACTUAL_SHA256"
echo "verified: four-ratio rectangle profile for all 512 exact residual samples"

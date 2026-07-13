#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_depth10_residual_rectangle_profile}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-$(nproc)}"
EXPECTED_WITNESS_SHA256="8f29ae200d72925052cd08ac9df94f7d8bdec9d0d24067b42c6cb74b5f5c58ed"

mkdir -p "$WORK"
bash "$ROOT/src/run_sample_depth10_lifted_s9_completion_residual.sh" "$WORK"

$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_depth10_residual_rectangle_profile.cpp" \
  -o "$WORK/verify_depth10_residual_rectangle_profile"

export OMP_NUM_THREADS="$THREADS"
SAMPLE="$WORK/depth10_lifted_completion_residual_equal_rank512.txt"
WITNESSES="$WORK/depth10_residual_rectangle_witnesses284.txt"
"$WORK/verify_depth10_residual_rectangle_profile" "$SAMPLE" "$WITNESSES"

ACTUAL_SHA256="$(sha256sum "$WITNESSES" | awk '{print $1}')"
if [[ "$ACTUAL_SHA256" != "$EXPECTED_WITNESS_SHA256" ]]; then
  echo "error: witness SHA-256 mismatch" >&2
  echo "expected=$EXPECTED_WITNESS_SHA256" >&2
  echo "actual=$ACTUAL_SHA256" >&2
  exit 1
fi

echo "witness_sha256=$ACTUAL_SHA256"
echo "verified: residual equal-rank rectangle profile"

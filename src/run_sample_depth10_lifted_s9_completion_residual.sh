#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_depth10_lifted_residual_sample}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-$(nproc)}"

mkdir -p "$WORK"

# Regenerate and audit the certified lifted-completion objects.
bash "$ROOT/src/run_verify_depth10_lifted_s9_completion.sh" "$WORK"

$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/sample_depth10_lifted_s9_completion_residual.cpp" \
  -o "$WORK/sample_depth10_lifted_s9_completion_residual"

export OMP_NUM_THREADS="$THREADS"
"$WORK/sample_depth10_lifted_s9_completion_residual" \
  "$WORK/s9_completions.bin" \
  "$WORK/s9_completion_differences.bin" \
  "$WORK/depth10_lifted_completion_residual_equal_rank512.txt"

sha256sum "$WORK/depth10_lifted_completion_residual_equal_rank512.txt"
echo "generated: exact 512-point equal-rank sample of the 177844250-candidate residual"

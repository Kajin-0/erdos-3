#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_depth10_lifted_residual_sample}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-$(nproc)}"
EXPECTED_SHA256="cdee14adb2f1ca29b4bac2a32384adab2ff139b9955370168f522279f0f8a832"

mkdir -p "$WORK"

# Regenerate and audit the certified lifted-completion objects.
bash "$ROOT/src/run_verify_depth10_lifted_s9_completion.sh" "$WORK"

$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/sample_depth10_lifted_s9_completion_residual.cpp" \
  -o "$WORK/sample_depth10_lifted_s9_completion_residual"

export OMP_NUM_THREADS="$THREADS"
OUTPUT="$WORK/depth10_lifted_completion_residual_equal_rank512.txt"
"$WORK/sample_depth10_lifted_s9_completion_residual" \
  "$WORK/s9_completions.bin" \
  "$WORK/s9_completion_differences.bin" \
  "$OUTPUT"

ACTUAL_SHA256="$(sha256sum "$OUTPUT" | awk '{print $1}')"
if [[ "$ACTUAL_SHA256" != "$EXPECTED_SHA256" ]]; then
  echo "error: sample SHA-256 mismatch" >&2
  echo "expected=$EXPECTED_SHA256" >&2
  echo "actual=$ACTUAL_SHA256" >&2
  exit 1
fi

echo "sample_sha256=$ACTUAL_SHA256"
echo "verified: exact 512-point equal-rank sample of the 177844250-candidate residual"

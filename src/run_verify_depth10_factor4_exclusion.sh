#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_depth10_factor4_exclusion}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-$(nproc)}"

mkdir -p "$WORK"
S9_BIN="$WORK/verify_depth9_no_cheap_extension"
ANCHOR_BIN="$WORK/verify_depth10_factor4_anchor_reduction"
HOLE_BIN="$WORK/verify_depth10_factor4_hole_reduction"
MIXED_BIN="$WORK/verify_depth10_factor4_mixed_completion"

$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_depth9_no_cheap_extension.cpp" \
  -o "$S9_BIN"
$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_depth10_factor4_anchor_reduction.cpp" \
  -o "$ANCHOR_BIN"
$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_depth10_factor4_hole_reduction.cpp" \
  -o "$HOLE_BIN"
$CXX -O3 -std=c++17 \
  "$ROOT/src/verify_depth10_factor4_mixed_completion.cpp" \
  -o "$MIXED_BIN"

export OMP_NUM_THREADS="$THREADS"

# Regenerate the exact S9 signed completion set and its certified
# completion-to-base difference support.
"$S9_BIN" completions "$WORK/s9_completions.bin"
rm -f "$WORK"/s9_delta_chunk_*.bin
index=0
for start in 0 10000 20000 30000 40000 50000 60000 70000 80000; do
  end=$((start+10000))
  (( end > 88573 )) && end=88573
  "$S9_BIN" correlate \
    "$WORK/s9_completions.bin" \
    "$start" \
    "$end" \
    "$WORK/s9_delta_chunk_${index}.bin"
  index=$((index+1))
done
"$S9_BIN" reduce \
  "$WORK/s9_completion_differences.bin" \
  "$WORK"/s9_delta_chunk_*.bin

# Sequential exact reductions of the genuinely new S10 factor-four domain.
"$ANCHOR_BIN" \
  "$WORK/s9_completions.bin" \
  "$WORK/s9_completion_differences.bin" \
  "$WORK/residual_2520.txt"

"$HOLE_BIN" \
  "$WORK/residual_2520.txt" \
  "$WORK/residual_1866.txt"

"$MIXED_BIN" \
  "$WORK/s9_completions.bin" \
  "$WORK/s9_completion_differences.bin" \
  "$WORK/residual_1866.txt" \
  "$WORK/residual_893.txt"

python3 "$ROOT/src/verify_depth10_factor4_residual_witnesses.py" \
  "$WORK/residual_893.txt" \
  "$ROOT/data/depth10_factor4_residual_witnesses_2026-07-12.txt"

echo "verified: N_10_4=0"

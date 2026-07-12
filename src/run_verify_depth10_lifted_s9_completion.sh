#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_depth10_lifted_s9_completion}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-$(nproc)}"

mkdir -p "$WORK"
S9_BIN="$WORK/verify_depth9_no_cheap_extension"
S10_BIN="$WORK/verify_depth10_lifted_s9_completion"

$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_depth9_no_cheap_extension.cpp" \
  -o "$S9_BIN"
$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_depth10_lifted_s9_completion.cpp" \
  -o "$S10_BIN"

export OMP_NUM_THREADS="$THREADS"

# Regenerate only the S9 completion objects needed by the S10 lifting theorem.
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

"$S10_BIN" \
  "$WORK/s9_completions.bin" \
  "$WORK/s9_completion_differences.bin"

echo "verified: lifted S9 completion reduction for the S10 factor-four domain"

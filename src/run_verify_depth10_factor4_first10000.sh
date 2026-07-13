#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_depth10_factor4_first10000}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-$(nproc)}"

mkdir -p "$WORK"

"$ROOT/src/run_verify_depth10_factor4_first5000.sh" "$WORK/first5000"

$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_depth10_factor4_positions_5001_10000.cpp" \
  -o "$WORK/verify_positions_5001_10000"

OMP_NUM_THREADS="$THREADS" \
  "$WORK/verify_positions_5001_10000" \
  "$WORK/depth10_factor4_positions_5001_10000_witnesses.txt"

sha256sum "$WORK/depth10_factor4_positions_5001_10000_witnesses.txt"

echo "verified: first 10000 genuinely new S10 factor-four candidates"

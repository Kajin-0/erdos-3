#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_depth10_factor4_first1000}"
CXX="${CXX:-g++}"

mkdir -p "$WORK"

$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_depth10_factor4_first100.cpp" \
  -o "$WORK/verify_first100"

$CXX -O3 -std=c++17 \
  "$ROOT/src/verify_depth10_factor4_positions_101_1000.cpp" \
  -o "$WORK/verify_positions_101_1000"

"$WORK/verify_first100" \
  "$ROOT/data/depth10_factor4_first100_witnesses_2026-07-13.txt"

"$WORK/verify_positions_101_1000" \
  "$WORK/depth10_factor4_positions_101_1000_witnesses.txt"

sha256sum "$WORK/depth10_factor4_positions_101_1000_witnesses.txt"

echo "verified: first 1000 genuinely new S10 factor-four candidates"

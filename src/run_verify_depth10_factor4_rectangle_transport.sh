#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_rectangle_transport}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-$(nproc)}"

mkdir -p "$WORK"

python3 "$ROOT/src/verify_rectangle_transport_channel.py" \
  "$WORK/rectangle_transport_channel_certificate.txt"

sha256sum "$WORK/rectangle_transport_channel_certificate.txt"

$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_depth10_factor4_top_quartile_rectangle_profile.cpp" \
  -o "$WORK/verify_top_quartile_rectangle_profile"

OMP_NUM_THREADS="$THREADS" \
  "$WORK/verify_top_quartile_rectangle_profile" \
  "$ROOT/data/depth10_factor4_top_quartile128_witnesses_2026-07-13.txt"

sha256sum \
  "$ROOT/data/depth10_factor4_top_quartile128_witnesses_2026-07-13.txt"

echo "verified: exact k=4 rectangle transport and top-quartile S10 profile"

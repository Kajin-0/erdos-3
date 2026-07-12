#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-16}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

BIN="$TMP/verify_depth8_no_cheap_extension"
"$CXX" -O3 -fopenmp \
  "$ROOT/src/verify_depth8_no_cheap_extension.cpp" \
  -o "$BIN"

export OMP_NUM_THREADS="$THREADS"

"$BIN" --mode core \
  --write-remaining "$TMP/p0.txt"
"$BIN" --mode phase1 \
  --target-file "$TMP/p0.txt" \
  --write-remaining "$TMP/p1.txt"
"$BIN" --mode phase2 \
  --target-file "$TMP/p1.txt" \
  --write-remaining "$TMP/p2.txt"
"$BIN" --mode phase3 \
  --target-file "$TMP/p2.txt" \
  --write-remaining "$TMP/p3.txt"
"$BIN" --mode phase4 \
  --target-file "$TMP/p3.txt" \
  --write-remaining "$TMP/p4.txt"
"$BIN" --mode phase5 \
  --target-file "$TMP/p4.txt" \
  --write-remaining "$TMP/p5.txt"
"$BIN" --mode exceptions

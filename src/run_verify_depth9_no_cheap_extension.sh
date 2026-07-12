#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_depth9_no_cheap}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-$(nproc)}"
mkdir -p "$WORK"
BIN="$WORK/verify_depth9_no_cheap_extension"
$CXX -O3 -std=c++17 -fopenmp "$ROOT/src/verify_depth9_no_cheap_extension.cpp" -o "$BIN"
export OMP_NUM_THREADS="$THREADS"
$BIN state

$BIN completions "$WORK/completions.bin"
rm -f "$WORK"/delta_chunk_*.bin
index=0
for start in 0 10000 20000 30000 40000 50000 60000 70000 80000; do
  end=$((start+10000)); (( end > 88573 )) && end=88573
  $BIN correlate "$WORK/completions.bin" "$start" "$end" "$WORK/delta_chunk_${index}.bin"
  index=$((index+1))
done
$BIN reduce "$WORK/completion_differences.bin" "$WORK"/delta_chunk_*.bin
$BIN domains "$WORK/completion_differences.bin" "$WORK/residual.txt"
$BIN check "$WORK/residual.txt" 9238162 70446a8ae38a0994

rm -rf "$WORK/delta_chunks" && mkdir "$WORK/delta_chunks"
split -l 8 -d -a 3 "$ROOT/data/depth9_transverse_differences_2026-07-12.txt" "$WORK/delta_chunks/d"
phase=0
for delta_file in "$WORK"/delta_chunks/d*; do
  next="$WORK/transverse_${phase}.txt"
  $BIN transpose "$WORK/residual.txt" "$delta_file" "$next"
  mv "$next" "$WORK/residual.txt"
  phase=$((phase+1))
done
$BIN delta0 "$WORK/residual.txt" "$WORK/delta0.txt"
mv "$WORK/delta0.txt" "$WORK/residual.txt"
$BIN check "$WORK/residual.txt" 15471 7e4bdb962920ad1c

run_band(){ local mode="$1" lo="$2" hi="$3" count="$4" hash="$5"; "$BIN" "$mode" "$WORK/residual.txt" "$lo" "$hi" "$WORK/next.txt"; mv "$WORK/next.txt" "$WORK/residual.txt"; "$BIN" check "$WORK/residual.txt" "$count" "$hash"; }

run_band band 0 30 13875 41c6a37e7a5cbaab
run_band band 30 50 12802 ec0a0b218f60f39f
run_band band 50 70 12006 79f4ff6fd399deed
run_band band 70 100 9423 94b222cc89420cd5
run_band band 100 125 8227 8f79773d825b9b8a
run_band band 125 150 6440 f79d4ee35d208e25
run_band band 150 200 4672 6df246bbdabc0fb0
run_band band 200 250 3404 1cbb6debab4cde02
run_band band 250 275 2845 6ed3570c7680eb0d
run_band band 275 285 2821 b10da2c626f2b080
run_band band 285 290 2333 fde45d6fb8d07c0c
run_band band 290 295 2298 635f72bf3692dc1b
run_band band 295 300 2205 2c711b8a795edcfa
run_band band 300 325 1892 00bd37c3494a3ecc
run_band band 325 350 1770 67aed0b894ac5a24
run_band band 350 375 1508 e9be28f9da53ff3a
run_band band 375 385 1414 86933c6d3370ea7a
run_band band 385 392 1388 bec1ba5165d110ef
run_band band 392 400 1264 42dd3f7d6895a3f5
run_band band 400 425 1207 a24557aa6e8632ad
run_band band 425 431 1207 a24557aa6e8632ad
run_band target-band 431 432 909 7dc8d091009de569
run_band band 432 450 840 136f2a458c676de6
run_band band 450 500 711 fa2bfe93a59c5bfe
run_band band 500 525 595 2f4e4cd6705147b7
run_band band 525 550 492 e114910f199cb1b9
run_band band 550 575 477 2128c75550a09a72
run_band target-band 575 576 431 8e378645299ba92f
run_band band 576 600 395 ba63ef5afbe6d2fc
run_band band 600 625 374 ba54265a21527713
run_band band 625 637 366 9ecff648d87b7b2c
run_band band 637 647 366 9ecff648d87b7b2c
run_band target-band 647 648 271 07563416517037dc
run_band band 648 700 238 20b9228d90d62bf1
run_band band 700 800 149 b502761bc380af0a
run_band band 800 863 132 9569dfff7e7555fa
run_band target-band 863 864 93 f4fd09a42686a230
run_band band 864 1000 50 da6837c8df0b2088
run_band target-band 1000 1100 36 6012877f5b4ffce9
run_band target-band 1100 1200 24 d462e6e8b5860bab
run_band target-band 1200 1300 17 ce93f15b9842ca67
run_band target-band 1300 1500 15 dcab870e3567b681
run_band target-band 1500 2000 7 36448695e481d4d0
$BIN final "$WORK/residual.txt"
echo "verified: N_9_2=N_9_4=0"

#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_depth10_factor4_exclusion}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-$(nproc)}"

python3 "$ROOT/src/audit_depth10_factor4_anchor_reduction.py"

cat >&2 <<'EOF'
The depth-ten factor-four pipeline is currently exploratory, not a proof.

Blocking issues:
  1. verify_depth10_factor4_anchor_reduction.cpp removes candidates without
     constructing or checking a valid four-term-progression witness.
  2. only 720 of the required 893 terminal witness records are committed.

See docs/depth-ten-factor-four-exclusion-audit.md.
Set ERDOS_ALLOW_UNCERTIFIED_DEPTH10_FACTOR4=1 only to reproduce the
exploratory intermediate counts. No N_10_4 theorem may be inferred.
EOF

if [[ "${ERDOS_ALLOW_UNCERTIFIED_DEPTH10_FACTOR4:-0}" != "1" ]]; then
  exit 2
fi

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

# Reproduce the exploratory reductions. The anchor stage is not currently a
# certified witness reduction; see the audit note referenced above.
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

# Assemble the witness fragments that currently exist. This intentionally
# fails the 893-record verifier until the missing 173 records are supplied.
cat \
  "$ROOT/data/depth10_factor4_residual_witnesses_2026-07-12.part00.txt" \
  "$ROOT/data/depth10_factor4_residual_witnesses_2026-07-12.part01.txt" \
  "$ROOT/data/depth10_factor4_residual_witnesses_2026-07-12.part02.txt" \
  "$ROOT/data/depth10_factor4_residual_witnesses_2026-07-12.part03.txt" \
  > "$WORK/depth10_factor4_residual_witnesses.partial.txt"

python3 "$ROOT/src/verify_depth10_factor4_residual_witnesses.py" \
  "$WORK/residual_893.txt" \
  "$WORK/depth10_factor4_residual_witnesses.partial.txt"

# This line is reachable only after both audit gaps are repaired.
echo "exploratory factor-four pipeline completed"

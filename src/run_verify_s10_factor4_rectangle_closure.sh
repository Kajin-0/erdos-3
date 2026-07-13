#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
WORK="${1:-${TMPDIR:-/tmp}/erdos_s10_factor4_rectangle_closure}"
CXX="${CXX:-g++}"
THREADS="${OMP_NUM_THREADS:-8}"

EXPECTED_UNION_SHA256="56c22b2bf90f99c42010d0e6b0b9a211040af04b54f87d46e8a9fb9336fa35a3"
EXPECTED_ZERO_SHA256="2847efd3228c8c175c8d3d944efc7680aa95a2ca4f60b9ab8d5df984decfc08d"
EXPECTED_TERMINAL_SHA256="56643ba1c0b36de464813470366cb74c66cc7ed21496dbb64578f56ec877198f"
EXPECTED_FINAL7_SHA256="447357ff5c38f927f9ed8ebacd9244ba273c5ff3c888b45566fc730064186ba6"

mkdir -p "$WORK"
BIN="$WORK/verify_b9_direct_rectangle_support"
$CXX -O3 -std=c++17 -fopenmp \
  "$ROOT/src/verify_b9_direct_rectangle_support.cpp" \
  -o "$BIN"

export OMP_NUM_THREADS="$THREADS"

"$BIN" special "$WORK/special.bin"
for bounds in \
  "0 16" \
  "16 32" \
  "32 64" \
  "64 128" \
  "128 256" \
  "256 300" \
  "300 350" \
  "350 400" \
  "400 450" \
  "450 512"
do
  read -r lower upper <<<"$bounds"
  "$BIN" band "$lower" "$upper" "$WORK/band_${lower}_${upper}.bin"
done

"$BIN" reduce \
  "$WORK/zeros2292.txt" \
  "$WORK/union_support.bin" \
  "$WORK/special.bin" \
  "$WORK"/band_*.bin

"$BIN" terminal \
  "$WORK/zeros2292.txt" \
  "$WORK/terminal_witnesses2285.txt"

FINAL7="$ROOT/data/b9_direct_rectangle_terminal7_witnesses_2026-07-13.txt"
"$BIN" final7 "$FINAL7"

check_sha256() {
  local expected="$1"
  local path="$2"
  local actual
  actual="$(sha256sum "$path" | awk '{print $1}')"
  if [[ "$actual" != "$expected" ]]; then
    echo "error: SHA-256 mismatch for $path" >&2
    echo "expected=$expected" >&2
    echo "actual=$actual" >&2
    exit 1
  fi
  echo "sha256[$path]=$actual"
}

check_sha256 "$EXPECTED_UNION_SHA256" "$WORK/union_support.bin"
check_sha256 "$EXPECTED_ZERO_SHA256" "$WORK/zeros2292.txt"
check_sha256 "$EXPECTED_TERMINAL_SHA256" "$WORK/terminal_witnesses2285.txt"
check_sha256 "$EXPECTED_FINAL7_SHA256" "$FINAL7"

python3 "$ROOT/src/verify_four_ratio_rectangle_transport.py" \
  "$WORK/four_ratio_rectangle_transport_certificate.txt"
python3 "$ROOT/src/verify_s10_factor4_rectangle_closure.py" \
  "$WORK/s10_factor4_rectangle_closure_certificate.txt"

python3 - <<'PY'
structural = 76581484
terminal = 2285
large_fiber = 7
umax = 76583776
assert structural + terminal + large_fiber == umax

inherited = 33026376
lifted_completion = 137142200
rectangle_residual = 177844250
total = 348012826
assert inherited + lifted_completion + rectangle_residual == total

print(f"verified_direct_B9_rectangle_support={umax}")
print(f"verified_S10_factor4_candidates={total}")
print("N_10_4=0")
PY

echo "verified: complete S10 factor-four exclusion by inheritance, lifted completion, and rectangle transport"

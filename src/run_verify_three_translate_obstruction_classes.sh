#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="${1:-${TMPDIR:-/tmp}/three_translate_obstruction_classes_certificate.txt}"

python3 "$ROOT/src/verify_three_translate_obstruction_classes.py" "$OUT"
sha256sum "$OUT"

echo "verified: exact three-translate obstruction classification and recurrence"

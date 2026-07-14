#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

bash -n \
  "$ROOT/src/stage_optional_probe_outputs.sh" \
  "$ROOT/src/run_atomic_python_probe.sh" \
  "$ROOT/src/assert_probe_status.sh" \
  "$ROOT/src/commit_probe_outputs.sh"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

# Safe staging: tracked deletion, never-created absence, and new addition.
repo="$work/repo"
mkdir -p "$repo/data"
git -C "$repo" init -q
git -C "$repo" config user.name test
git -C "$repo" config user.email test@example.invalid
printf 'ok\n' > "$repo/data/status.txt"
printf 'old\n' > "$repo/data/tracked.txt"
git -C "$repo" add data/status.txt data/tracked.txt
git -C "$repo" commit -qm initial

rm "$repo/data/tracked.txt"
(
  cd "$repo"
  bash "$ROOT/src/stage_optional_probe_outputs.sh" \
    data/status.txt data/tracked.txt data/never-created.txt
)
git -C "$repo" diff --cached --name-status | grep -Fx 'D	data/tracked.txt'
git -C "$repo" reset -q --hard HEAD

printf 'new\n' > "$repo/data/new.txt"
(
  cd "$repo"
  bash "$ROOT/src/stage_optional_probe_outputs.sh" \
    data/status.txt data/new.txt data/never-created.txt
)
git -C "$repo" diff --cached --name-status | grep -Fx 'A	data/new.txt'

# Atomic execution: successful outputs are moved into place.
cat > "$work/probe_ok.py" <<'PY'
import json
print(json.dumps({"ok": True}))
PY
cat > "$work/summary_ok.py" <<'PY'
import json
import sys
from pathlib import Path
payload = json.loads(Path(sys.argv[1]).read_text())
Path(sys.argv[2]).write_text(f"ok={str(payload['ok']).lower()}\n")
PY

(
  cd "$ROOT"
  GITHUB_SHA=test-source GITHUB_REF=refs/heads/main \
    bash src/run_atomic_python_probe.sh \
      helper_test_v1 \
      "$work/status-ok.txt" \
      "$work/stderr-ok.txt" \
      "$work/probe_ok.py" \
      "$work/probe.json" \
      "$work/summary_ok.py" \
      "$work/summary.txt"
)
grep -Fx 'probe_exit_status=0' "$work/status-ok.txt"
grep -Fx 'summary_exit_status=0' "$work/status-ok.txt"
grep -Fx 'ok=true' "$work/summary.txt"

# A failing probe may emit partial stdout, but no result file may survive.
cat > "$work/probe_fail.py" <<'PY'
import sys
print('{"partial":')
sys.exit(3)
PY
rm -f "$work/probe-fail.json" "$work/summary-fail.txt"
(
  cd "$ROOT"
  GITHUB_SHA=test-source GITHUB_REF=refs/heads/main \
    bash src/run_atomic_python_probe.sh \
      helper_test_failure_v1 \
      "$work/status-fail.txt" \
      "$work/stderr-fail.txt" \
      "$work/probe_fail.py" \
      "$work/probe-fail.json" \
      "$work/summary_ok.py" \
      "$work/summary-fail.txt"
)
[[ ! -e "$work/probe-fail.json" ]]
[[ ! -e "$work/summary-fail.txt" ]]
grep -Fx 'probe_exit_status=3' "$work/status-fail.txt"
if bash "$ROOT/src/assert_probe_status.sh" "$work/status-fail.txt"; then
  echo 'error: failing probe status was accepted' >&2
  exit 1
fi

echo 'probe workflow helper tests passed'

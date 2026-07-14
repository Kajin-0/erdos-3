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

expect_success() {
  local name="$1" file="$2"
  local out="$work/${name}.out" err="$work/${name}.err"
  local status
  set +e
  bash "$ROOT/src/assert_probe_status.sh" "$file" >"$out" 2>"$err"
  status=$?
  set -e
  if [[ "$status" -ne 0 ]]; then
    echo "error: $name expected exit 0, got $status" >&2
    cat "$err" >&2
    exit 1
  fi
}

expect_failure() {
  local name="$1" file="$2" pattern="$3"
  local out="$work/${name}.out" err="$work/${name}.err"
  local status
  set +e
  bash "$ROOT/src/assert_probe_status.sh" "$file" >"$out" 2>"$err"
  status=$?
  set -e
  if [[ "$status" -ne 1 ]]; then
    echo "error: $name expected exit 1, got $status" >&2
    cat "$err" >&2
    exit 1
  fi
  grep -Fq -- "$pattern" "$err"
  grep -Fq -- '--- preserved probe status ---' "$err"
}

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
git -C "$repo" diff --cached --name-status | grep -Fxq $'D\tdata/tracked.txt'
git -C "$repo" reset -q --hard HEAD

printf 'new\n' > "$repo/data/new.txt"
(
  cd "$repo"
  bash "$ROOT/src/stage_optional_probe_outputs.sh" \
    data/status.txt data/new.txt data/never-created.txt
)
git -C "$repo" diff --cached --name-status | grep -Fxq $'A\tdata/new.txt'

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
grep -Fqx 'probe_exit_status=0' "$work/status-ok.txt"
grep -Fqx 'summary_exit_status=0' "$work/status-ok.txt"
grep -Fqx 'ok=true' "$work/summary.txt"

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
grep -Fqx 'probe_exit_status=3' "$work/status-fail.txt"

# Case 1: successful outer status ignores a failed nested fixture.
cat > "$work/case1.txt" <<'EOF'
schema=outer_status_v1
lint_exit_status=0
helper_test_exit_status=0
--- helper tests ---
schema=helper_test_failure_v1
compile_exit_status=0
probe_exit_status=3
summary_exit_status=not_run
verifier_exit_status=not_applicable
EOF
expect_success case1 "$work/case1.txt"

# Case 2: failed outer status is not rescued by successful nested diagnostics.
cat > "$work/case2.txt" <<'EOF'
schema=outer_status_v1
lint_exit_status=1
helper_test_exit_status=0
--- helper tests ---
probe_exit_status=0
summary_exit_status=0
EOF
expect_failure case2 "$work/case2.txt" 'error: lint_exit_status=1'

# Case 3: ordinary successful probe status.
cat > "$work/case3.txt" <<'EOF'
schema=probe_status_v1
compile_exit_status=0
probe_exit_status=0
summary_exit_status=0
verifier_exit_status=not_applicable
--- stderr ---
EOF
expect_success case3 "$work/case3.txt"

# Case 4: ordinary failed probe status preserves full diagnostics.
cat > "$work/case4.txt" <<'EOF'
schema=probe_status_v1
compile_exit_status=0
probe_exit_status=7
summary_exit_status=not_run
verifier_exit_status=not_applicable
--- stderr ---
diagnostic body remains available
EOF
expect_failure case4 "$work/case4.txt" 'error: probe_exit_status=7'
grep -Fq 'diagnostic body remains available' "$work/case4.err"

# Case 5: missing top-level status fields fails even if diagnostics contain them.
cat > "$work/case5.txt" <<'EOF'
schema=outer_status_v1
source_commit=test-source
--- diagnostics ---
probe_exit_status=0
EOF
expect_failure case5 "$work/case5.txt" \
  'error: no top-level *_exit_status fields found'

# Case 6: capture and verify the expected negative fixture without log leakage.
expect_failure case6 "$work/status-fail.txt" 'error: probe_exit_status=3'
grep -Fq 'error: summary_exit_status=not_run' "$work/case6.err"

# Empty, not-run, unknown, and malformed top-level values must fail.
for spec in empty not_run unknown malformed; do
  case "$spec" in
    empty) line='probe_exit_status=' ;;
    not_run) line='probe_exit_status=not_run' ;;
    unknown) line='probe_exit_status=success' ;;
    malformed) line='probe_exit_status' ;;
  esac
  printf 'schema=invalid_status_v1\n%s\n' "$line" > "$work/invalid-$spec.txt"
  expect_failure "invalid-$spec" "$work/invalid-$spec.txt" 'error:'
done

echo 'probe workflow helper tests passed'

#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

bash -n \
  "$ROOT/src/stage_optional_probe_outputs.sh" \
  "$ROOT/src/run_atomic_python_probe.sh" \
  "$ROOT/src/run_atomic_documentation_patch.sh" \
  "$ROOT/src/assert_probe_status.sh" \
  "$ROOT/src/commit_probe_outputs.sh"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

expect_success() {
  local name="$1" file="$2"
  local out="$work/${name}.out" err="$work/${name}.err" status
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
  local out="$work/${name}.out" err="$work/${name}.err" status
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

# Atomic probe execution.
cat > "$work/probe_ok.py" <<'PY'
import json
print(json.dumps({"ok": True}))
PY
cat > "$work/summary_ok.py" <<'PY'
import json, sys
from pathlib import Path
payload = json.loads(Path(sys.argv[1]).read_text())
Path(sys.argv[2]).write_text(f"ok={str(payload['ok']).lower()}\n")
PY
(
  cd "$ROOT"
  GITHUB_SHA=test-source GITHUB_REF=refs/heads/main \
  GITHUB_RUN_ID=1 GITHUB_RUN_ATTEMPT=1 \
    bash src/run_atomic_python_probe.sh \
      helper_test_v1 "$work/status-ok.txt" "$work/stderr-ok.txt" \
      "$work/probe_ok.py" "$work/probe.json" \
      "$work/summary_ok.py" "$work/summary.txt"
)
grep -Fqx 'probe_exit_status=0' "$work/status-ok.txt"
grep -Fqx 'summary_exit_status=0' "$work/status-ok.txt"
grep -Fqx 'ok=true' "$work/summary.txt"

cat > "$work/probe_fail.py" <<'PY'
import sys
print('{"partial":')
sys.exit(3)
PY
rm -f "$work/probe-fail.json" "$work/summary-fail.txt"
(
  cd "$ROOT"
  GITHUB_SHA=test-source GITHUB_REF=refs/heads/main \
  GITHUB_RUN_ID=1 GITHUB_RUN_ATTEMPT=1 \
    bash src/run_atomic_python_probe.sh \
      helper_test_failure_v1 "$work/status-fail.txt" "$work/stderr-fail.txt" \
      "$work/probe_fail.py" "$work/probe-fail.json" \
      "$work/summary_ok.py" "$work/summary-fail.txt"
)
[[ ! -e "$work/probe-fail.json" ]]
[[ ! -e "$work/summary-fail.txt" ]]
grep -Fqx 'probe_exit_status=3' "$work/status-fail.txt"

# Status parser regression cases.
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
cat > "$work/case2.txt" <<'EOF'
schema=outer_status_v1
lint_exit_status=1
helper_test_exit_status=0
--- helper tests ---
probe_exit_status=0
summary_exit_status=0
EOF
expect_failure case2 "$work/case2.txt" 'error: lint_exit_status=1'
cat > "$work/case3.txt" <<'EOF'
schema=probe_status_v1
compile_exit_status=0
probe_exit_status=0
summary_exit_status=0
verifier_exit_status=not_applicable
--- stderr ---
EOF
expect_success case3 "$work/case3.txt"
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
cat > "$work/case5.txt" <<'EOF'
schema=outer_status_v1
source_commit=test-source
--- diagnostics ---
probe_exit_status=0
EOF
expect_failure case5 "$work/case5.txt" 'error: no top-level *_exit_status fields found'
expect_failure case6 "$work/status-fail.txt" 'error: probe_exit_status=3'
grep -Fq 'error: summary_exit_status=not_run' "$work/case6.err"
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

# Atomic documentation patch: successful idempotent output is promoted.
doc_repo="$work/doc-repo"
mkdir -p "$doc_repo/src" "$doc_repo/docs" "$doc_repo/data"
git -C "$doc_repo" init -q
git -C "$doc_repo" config user.name test
git -C "$doc_repo" config user.email test@example.invalid
printf 'old\n' > "$doc_repo/docs/target.md"
cat > "$doc_repo/src/patch_ok.py" <<'PY'
from pathlib import Path
Path('docs/target.md').write_text('canonical\n')
PY
cat > "$doc_repo/src/patch_fail.py" <<'PY'
from pathlib import Path
import sys
Path('docs/target.md').write_text('partial\n')
sys.exit(7)
PY
git -C "$doc_repo" add .
git -C "$doc_repo" commit -qm initial
(
  cd "$doc_repo"
  GITHUB_SHA=test-source GITHUB_REF=refs/heads/main \
  GITHUB_RUN_ID=2 GITHUB_RUN_ATTEMPT=1 \
    bash "$ROOT/src/run_atomic_documentation_patch.sh" \
      documentation_test_v1 data/doc-status.txt data/doc.err \
      src/patch_ok.py docs/target.md
)
grep -Fqx 'patch_exit_status=0' "$doc_repo/data/doc-status.txt"
grep -Fqx 'idempotence_exit_status=0' "$doc_repo/data/doc-status.txt"
grep -Fqx 'promotion_exit_status=0' "$doc_repo/data/doc-status.txt"
grep -Fqx 'canonical' "$doc_repo/docs/target.md"

# A failed documentation patch never promotes its partial worktree output.
printf 'stable\n' > "$doc_repo/docs/target.md"
git -C "$doc_repo" add docs/target.md
git -C "$doc_repo" commit -qm stable
(
  cd "$doc_repo"
  GITHUB_SHA=test-source GITHUB_REF=refs/heads/main \
  GITHUB_RUN_ID=3 GITHUB_RUN_ATTEMPT=1 \
    bash "$ROOT/src/run_atomic_documentation_patch.sh" \
      documentation_failure_v1 data/doc-fail-status.txt data/doc-fail.err \
      src/patch_fail.py docs/target.md
)
grep -Fqx 'patch_exit_status=7' "$doc_repo/data/doc-fail-status.txt"
grep -Fqx 'promotion_exit_status=not_run' "$doc_repo/data/doc-fail-status.txt"
grep -Fqx 'stable' "$doc_repo/docs/target.md"

# Linter architectural regressions: one-time files, duplicate ownership,
# duplicate trigger/output families, and noncanonical documentation writers.
PYTHONPATH="$ROOT/src" python3 - <<'PY'
from pathlib import Path
from lint_probe_workflows import lint_workflow_set

metadata = '''
          {
            echo "schema=test_v1"
            echo "patch_exit_status=$patch_status"
            echo "source_commit=${GITHUB_SHA}"
            echo "source_ref=${GITHUB_REF}"
            echo "workflow_run_id=${GITHUB_RUN_ID}"
            echo "workflow_run_attempt=${GITHUB_RUN_ATTEMPT}"
            echo "--- stderr ---"
          } > data/test_status.txt
'''

def writer(name: str, script: str, output: str, *, one_time: bool = False) -> tuple[Path, str]:
    filename = f"one-time-{name}.yml" if one_time else f"{name}.yml"
    text = f'''name: {name}
on:
  push:
    paths:
      - {script}
permissions:
  contents: write
concurrency:
  group: probe-result-writers-main
  cancel-in-progress: false
jobs:
  write:
    steps:
      - uses: actions/upload-artifact@v4
      - run: bash src/run_atomic_documentation_patch.sh test data/test_status.txt /tmp/test.err {script} {output}
      - run: bash src/commit_probe_outputs.sh message data/test_status.txt {output}
      - run: bash src/assert_probe_status.sh data/test_status.txt
{metadata}
'''
    return Path('.github/workflows') / filename, text

failures, _ = lint_workflow_set([writer('once', 'src/patch_a.py', 'README.md', one_time=True)])
assert any('one-time workflow files are prohibited' in item for item in failures), failures

left = writer('left', 'src/patch_same.py', 'README.md')
right = writer('right', 'src/patch_same.py', 'README.md')
failures, _ = lint_workflow_set([left, right])
joined = '\n'.join(failures)
assert 'duplicate writable ownership of src/patch_same.py' in joined, joined
assert '.github/workflows/left.yml' in joined and '.github/workflows/right.yml' in joined, joined
assert 'duplicate writable ownership of README.md' in joined, joined
assert 'duplicate writable trigger/output family' in joined, joined

bad_group_path, bad_group = writer('bad-group', 'src/patch_x.py', 'README.md')
bad_group = bad_group.replace('group: probe-result-writers-main', 'group: bespoke-writer')
failures, _ = lint_workflow_set([(bad_group_path, bad_group)])
assert any('must use exactly one concurrency group' in item for item in failures), failures

# A normal non-documentation status writer using the canonical helpers remains valid.
normal = '''name: normal
on: [push]
permissions:
  contents: write
concurrency:
  group: probe-result-writers-main
  cancel-in-progress: false
jobs:
  test:
    steps:
      - uses: actions/upload-artifact@v4
      - run: |
          {
            echo "schema=normal_v1"
            echo "probe_exit_status=$probe_status"
            echo "source_commit=${GITHUB_SHA}"
            echo "source_ref=${GITHUB_REF}"
            echo "workflow_run_id=${GITHUB_RUN_ID}"
            echo "workflow_run_attempt=${GITHUB_RUN_ATTEMPT}"
            echo "--- stderr ---"
          } > data/normal_status.txt
      - run: bash src/commit_probe_outputs.sh message data/normal_status.txt
      - run: bash src/assert_probe_status.sh data/normal_status.txt
'''
failures, _ = lint_workflow_set([(Path('.github/workflows/normal.yml'), normal)])
assert failures == [], failures
PY

echo 'probe workflow helper tests passed'

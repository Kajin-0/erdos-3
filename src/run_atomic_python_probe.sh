#!/usr/bin/env bash
set -uo pipefail

if [[ "$#" -ne 7 && "$#" -ne 9 ]]; then
  cat >&2 <<'EOF'
usage:
  run_atomic_python_probe.sh SCHEMA STATUS_FILE STDERR_FILE \
    PROBE_SCRIPT PROBE_OUTPUT SUMMARY_SCRIPT SUMMARY_OUTPUT \
    [VERIFIER_SCRIPT CERTIFICATE_OUTPUT]
EOF
  exit 2
fi

schema="$1"
status_file="$2"
stderr_file="$3"
probe_script="$4"
probe_output="$5"
summary_script="$6"
summary_output="$7"
verifier_script="${8:-}"
certificate_output="${9:-}"

mkdir -p "$(dirname "$status_file")" "$(dirname "$stderr_file")"
mkdir -p "$(dirname "$probe_output")" "$(dirname "$summary_output")"
if [[ -n "$certificate_output" ]]; then
  mkdir -p "$(dirname "$certificate_output")"
fi

tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT
probe_tmp="$tmpdir/probe.json"
summary_tmp="$tmpdir/summary.txt"
certificate_tmp="$tmpdir/certificate.txt"
status_tmp="$tmpdir/status.txt"

rm -f -- "$probe_output" "$summary_output"
if [[ -n "$certificate_output" ]]; then
  rm -f -- "$certificate_output"
fi
: > "$stderr_file"

compile_status=not_run
probe_status=not_run
summary_status=not_run
verifier_status=not_applicable

compile_files=("$probe_script" "$summary_script")
if [[ -n "$verifier_script" ]]; then
  compile_files+=("$verifier_script")
  verifier_status=not_run
fi

python3 -m py_compile "${compile_files[@]}" 2>"$stderr_file"
compile_status=$?

if [[ "$compile_status" == "0" ]]; then
  python3 src/run_exact_python.py "$probe_script" \
    >"$probe_tmp" 2>>"$stderr_file"
  probe_status=$?

  if [[ "$probe_status" == "0" ]]; then
    mv -- "$probe_tmp" "$probe_output"

    python3 "$summary_script" "$probe_output" "$summary_tmp" \
      2>>"$stderr_file"
    summary_status=$?
    if [[ "$summary_status" == "0" ]]; then
      mv -- "$summary_tmp" "$summary_output"
    fi

    if [[ -n "$verifier_script" ]]; then
      python3 src/run_exact_python.py "$verifier_script" "$certificate_tmp" \
        2>>"$stderr_file"
      verifier_status=$?
      if [[ "$verifier_status" == "0" ]]; then
        mv -- "$certificate_tmp" "$certificate_output"
      fi
    fi
  fi
fi

{
  echo "schema=$schema"
  echo "compile_exit_status=$compile_status"
  echo "probe_exit_status=$probe_status"
  echo "summary_exit_status=$summary_status"
  echo "verifier_exit_status=$verifier_status"
  echo "source_commit=${GITHUB_SHA:-unknown}"
  echo "source_ref=${GITHUB_REF:-unknown}"
  echo "workflow_run_id=${GITHUB_RUN_ID:-unknown}"
  echo "workflow_run_attempt=${GITHUB_RUN_ATTEMPT:-unknown}"
  echo "--- stderr ---"
  cat "$stderr_file"
} > "$status_tmp"
mv -- "$status_tmp" "$status_file"

# Diagnostics must always reach the recorder step. The workflow performs an
# explicit failure check only after the status and optional deletions are stored.
exit 0

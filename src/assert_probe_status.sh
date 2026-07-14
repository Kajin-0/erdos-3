#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -ne 1 ]]; then
  echo "usage: $0 STATUS_FILE" >&2
  exit 2
fi

status_file="$1"
if [[ ! -f "$status_file" ]]; then
  echo "error: probe status file is missing: $status_file" >&2
  exit 1
fi

found=0
failed=0
while IFS= read -r line || [[ -n "$line" ]]; do
  # The first diagnostic separator terminates the machine-readable header.
  # Legacy status files without a separator are parsed in full.
  if [[ "$line" == ---* ]]; then
    break
  fi

  if [[ "$line" == *_exit_status=* ]]; then
    key="${line%%=*}"
    value="${line#*=}"
    found=1

    if [[ ! "$key" =~ ^[A-Za-z_][A-Za-z0-9_]*_exit_status$ ]]; then
      echo "error: malformed status field: $line" >&2
      failed=1
      continue
    fi

    case "$value" in
      0|not_applicable) ;;
      *)
        echo "error: $key=$value" >&2
        failed=1
        ;;
    esac
  elif [[ "$line" == *_exit_status* ]]; then
    found=1
    echo "error: malformed status field: $line" >&2
    failed=1
  fi
done < "$status_file"

if [[ "$found" == "0" ]]; then
  echo "error: no top-level *_exit_status fields found in $status_file" >&2
  failed=1
fi

if [[ "$failed" != "0" ]]; then
  echo "--- preserved probe status ---" >&2
  cat "$status_file" >&2
  exit 1
fi

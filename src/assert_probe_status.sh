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
while IFS='=' read -r key value; do
  case "$key" in
    *_exit_status)
      found=1
      case "$value" in
        0|not_applicable) ;;
        *)
          echo "error: $key=$value" >&2
          failed=1
          ;;
      esac
      ;;
  esac
done < "$status_file"

if [[ "$found" == "0" ]]; then
  echo "error: no *_exit_status fields found in $status_file" >&2
  cat "$status_file" >&2
  exit 1
fi

if [[ "$failed" != "0" ]]; then
  echo "--- preserved probe status ---" >&2
  cat "$status_file" >&2
  exit 1
fi

#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -lt 1 ]]; then
  echo "usage: $0 STATUS_FILE [OPTIONAL_FILE ...]" >&2
  exit 2
fi

status_file="$1"
shift

if [[ ! -f "$status_file" ]]; then
  echo "error: required probe status file is missing: $status_file" >&2
  exit 1
fi

git add -- "$status_file"

for path in "$@"; do
  if [[ -e "$path" ]]; then
    git add -- "$path"
  elif git ls-files --error-unmatch -- "$path" >/dev/null 2>&1; then
    git rm --quiet -- "$path"
  fi
done

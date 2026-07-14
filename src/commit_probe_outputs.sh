#!/usr/bin/env bash
set -euo pipefail

if [[ "$#" -lt 2 ]]; then
  echo "usage: $0 COMMIT_MESSAGE STATUS_FILE [OPTIONAL_FILE ...]" >&2
  exit 2
fi

commit_message="$1"
status_file="$2"
shift 2
optional_files=("$@")

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

bash src/stage_optional_probe_outputs.sh "$status_file" "${optional_files[@]}"

if git diff --cached --quiet; then
  echo "No deterministic probe output change"
  exit 0
fi

git commit -m "$commit_message"

for attempt in 1 2 3; do
  git fetch origin main

  # Never rebase and publish a deterministic result across a source change.
  # Bot data-only commits are allowed; changes under src/ or workflow definitions
  # require a fresh run against the new source commit.
  if [[ -n "${GITHUB_SHA:-}" ]] && \
     ! git diff --quiet "$GITHUB_SHA" origin/main -- src .github/workflows; then
    echo "error: probe source changed after this run; refusing to publish stale output" >&2
    echo "source_commit=$GITHUB_SHA" >&2
    echo "current_main=$(git rev-parse origin/main)" >&2
    exit 1
  fi

  if ! git rebase origin/main; then
    if ! git rebase --abort; then
      echo "warning: failed to abort the unsuccessful generated-output rebase" >&2
    fi
    echo "error: generated-output commit could not be rebased cleanly" >&2
    exit 1
  fi

  if git push origin HEAD:main; then
    exit 0
  fi

  sleep $((attempt * 2))
done

echo "error: failed to push generated-output commit after three attempts" >&2
exit 1

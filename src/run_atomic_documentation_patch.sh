#!/usr/bin/env bash
set -uo pipefail

if [[ "$#" -lt 5 ]]; then
  cat >&2 <<'EOF'
usage:
  run_atomic_documentation_patch.sh SCHEMA STATUS_FILE STDERR_FILE \
    PATCH_ENTRY OUTPUT_FILE [OUTPUT_FILE ...]
EOF
  exit 2
fi

schema="$1"
status_file="$2"
stderr_file="$3"
patch_entry="$4"
shift 4
output_files=("$@")

repo_root="$(git rev-parse --show-toplevel)" || exit 2
mkdir -p "$(dirname "$status_file")" "$(dirname "$stderr_file")"
: > "$stderr_file"

tmpdir="$(mktemp -d)"
worktree="$tmpdir/worktree"
validated_dir="$tmpdir/validated"
first_hash="$tmpdir/first.sha256"
second_hash="$tmpdir/second.sha256"
status_tmp="$tmpdir/status.txt"
mkdir -p "$validated_dir"

compile_status=not_run
patch_status=not_run
idempotence_status=not_run
cleanup_status=not_run
promotion_status=not_run

if git -C "$repo_root" worktree add --detach "$worktree" HEAD \
    >>"$stderr_file" 2>&1; then
  python3 -W error -m py_compile "$worktree/$patch_entry" \
    2>>"$stderr_file"
  compile_status=$?

  if [[ "$compile_status" == "0" ]]; then
    (
      cd "$worktree"
      python3 "$patch_entry"
    ) 2>>"$stderr_file"
    patch_status=$?
  fi

  if [[ "$patch_status" == "0" ]]; then
    missing=0
    for path in "${output_files[@]}"; do
      if [[ ! -f "$worktree/$path" ]]; then
        echo "error: documentation patch did not produce $path" >>"$stderr_file"
        missing=1
      fi
    done
    if [[ "$missing" == "0" ]]; then
      (
        cd "$worktree"
        sha256sum -- "${output_files[@]}"
      ) >"$first_hash" 2>>"$stderr_file"
      first_hash_status=$?
      if [[ "$first_hash_status" == "0" ]]; then
        (
          cd "$worktree"
          python3 "$patch_entry"
        ) 2>>"$stderr_file"
        second_patch_status=$?
        if [[ "$second_patch_status" == "0" ]]; then
          (
            cd "$worktree"
            sha256sum -- "${output_files[@]}"
          ) >"$second_hash" 2>>"$stderr_file"
          second_hash_status=$?
          if [[ "$second_hash_status" == "0" ]]; then
            cmp "$first_hash" "$second_hash" 2>>"$stderr_file"
            idempotence_status=$?
          else
            idempotence_status=$second_hash_status
          fi
        else
          idempotence_status=$second_patch_status
        fi
      else
        idempotence_status=$first_hash_status
      fi
    else
      idempotence_status=1
    fi
  fi

  if [[ "$compile_status" == "0" && "$patch_status" == "0" && \
        "$idempotence_status" == "0" ]]; then
    copy_status=0
    for index in "${!output_files[@]}"; do
      path="${output_files[$index]}"
      if cp -- "$worktree/$path" "$validated_dir/$index" \
          2>>"$stderr_file"; then
        :
      else
        copy_status=$?
        break
      fi
    done
    if [[ "$copy_status" != "0" ]]; then
      idempotence_status=$copy_status
    fi
  fi
else
  worktree_status=$?
  echo "error: failed to create isolated documentation worktree" >>"$stderr_file"
  compile_status=$worktree_status
fi

if [[ -d "$worktree" ]]; then
  if git -C "$repo_root" worktree remove --force "$worktree" \
      >>"$stderr_file" 2>&1; then
    cleanup_status=0
  else
    cleanup_status=$?
  fi
else
  cleanup_status=0
fi

if [[ "$compile_status" == "0" && "$patch_status" == "0" && \
      "$idempotence_status" == "0" && "$cleanup_status" == "0" ]]; then
  promotion_status=0
  staged_temps=()
  backups=()
  existed=()

  for index in "${!output_files[@]}"; do
    destination="$repo_root/${output_files[$index]}"
    mkdir -p "$(dirname "$destination")"
    temp_destination="$(dirname "$destination")/.documentation-patch.$$.${index}.tmp"
    backup="$tmpdir/backup.${index}"

    if [[ -e "$destination" ]]; then
      if cp -- "$destination" "$backup" 2>>"$stderr_file"; then
        existed+=(1)
        backups+=("$backup")
      else
        promotion_status=$?
        break
      fi
    else
      existed+=(0)
      backups+=("")
    fi

    if cp -- "$validated_dir/$index" "$temp_destination" 2>>"$stderr_file"; then
      staged_temps+=("$temp_destination")
    else
      promotion_status=$?
      break
    fi
  done

  promoted_count=0
  if [[ "$promotion_status" == "0" ]]; then
    for index in "${!output_files[@]}"; do
      destination="$repo_root/${output_files[$index]}"
      if mv -- "${staged_temps[$index]}" "$destination" 2>>"$stderr_file"; then
        promoted_count=$((promoted_count + 1))
      else
        promotion_status=$?
        break
      fi
    done
  fi

  if [[ "$promotion_status" != "0" && "$promoted_count" -gt 0 ]]; then
    rollback_status=0
    for ((index = promoted_count - 1; index >= 0; index--)); do
      destination="$repo_root/${output_files[$index]}"
      if [[ "${existed[$index]}" == "1" ]]; then
        if cp -- "${backups[$index]}" "$destination" 2>>"$stderr_file"; then
          :
        else
          rollback_status=$?
        fi
      else
        if rm -f -- "$destination" 2>>"$stderr_file"; then
          :
        else
          rollback_status=$?
        fi
      fi
    done
    if [[ "$rollback_status" != "0" ]]; then
      echo "error: documentation-output rollback failed" >>"$stderr_file"
      promotion_status=$rollback_status
    fi
  fi

  for temp_path in "${staged_temps[@]:-}"; do
    if [[ -n "$temp_path" && -e "$temp_path" ]]; then
      rm -f -- "$temp_path"
    fi
  done
fi

{
  echo "schema=$schema"
  echo "compile_exit_status=$compile_status"
  echo "patch_exit_status=$patch_status"
  echo "idempotence_exit_status=$idempotence_status"
  echo "cleanup_exit_status=$cleanup_status"
  echo "promotion_exit_status=$promotion_status"
  echo "source_commit=${GITHUB_SHA:-unknown}"
  echo "source_ref=${GITHUB_REF:-unknown}"
  echo "workflow_run_id=${GITHUB_RUN_ID:-unknown}"
  echo "workflow_run_attempt=${GITHUB_RUN_ATTEMPT:-unknown}"
  echo "--- stderr ---"
  cat "$stderr_file"
} > "$status_tmp"
mv -- "$status_tmp" "$status_file"

rm -rf -- "$tmpdir"

# Diagnostics must always survive to artifact upload and commit. The workflow
# calls assert_probe_status.sh only after preservation.
exit 0

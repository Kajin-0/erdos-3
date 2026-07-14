#!/usr/bin/env python3
"""Reject unsafe deterministic-probe workflow and status-file patterns."""
from __future__ import annotations

from pathlib import Path
import re
import sys

WORKFLOW_DIR = Path(".github/workflows")
SRC_DIR = Path("src")
UNSAFE_STAGE = re.compile(r"\bgit\s+add\s+-A\s+(?:--\s+)?data/[^\s]+")
DIRECT_OPTIONAL_REDIRECT = re.compile(
    r">\s*data/[^\s]*(?:_probe\.json|_summary\.txt|_certificate[^\s]*\.txt)"
)
SUPPRESSED_FAILURE = re.compile(r"\|\|\s*true\b")
MACHINE_ECHO = re.compile(
    r"^\s*echo\s+(['\"])([A-Za-z_][A-Za-z0-9_]*)=.*\1\s*$"
)
SEPARATOR_ECHO = re.compile(r"^\s*echo\s+(['\"])---.*\1\s*$")
STATUS_FIELD_ECHO = re.compile(
    r"^\s*echo\s+(['\"])([A-Za-z_][A-Za-z0-9_]*_exit_status)=.*\1\s*$"
)
ASSERT_CALL = re.compile(
    r"(?m)^\s*(?:run:\s*)?.*\bbash\s+src/assert_probe_status\.sh\b"
)
PROBE_WRITER_MARKERS = (
    "_probe.json",
    "_summary.txt",
    "_status.txt",
)
SAFE_RECORDER_MARKERS = (
    "reusable-python-probe-recorder.yml",
    "src/stage_optional_probe_outputs.sh",
    "src/commit_probe_outputs.sh",
)
REQUIRED_STATUS_METADATA = (
    "schema",
    "source_commit",
    "source_ref",
    "workflow_run_id",
    "workflow_run_attempt",
)
FRAMEWORK_SCRIPTS = {
    "assert_probe_status.sh",
    "run_atomic_python_probe.sh",
    "stage_optional_probe_outputs.sh",
    "commit_probe_outputs.sh",
    "test_probe_workflow_helpers.sh",
}


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def status_blocks(text: str) -> list[tuple[int, list[str]]]:
    """Return shell brace blocks that emit one or more exit-status fields."""
    lines = text.splitlines()
    blocks: list[tuple[int, list[str]]] = []
    index = 0
    while index < len(lines):
        if lines[index].strip() != "{":
            index += 1
            continue
        end = index + 1
        while end < len(lines) and not re.match(r"^\s*}\s*>>?", lines[end]):
            end += 1
        if end >= len(lines):
            index += 1
            continue
        body = lines[index + 1 : end]
        if any("_exit_status=" in line for line in body):
            blocks.append((index + 1, body))
        index = end + 1
    return blocks


def lint_status_block(path: Path, start_line: int, body: list[str]) -> list[str]:
    failures: list[str] = []
    separator_index = next(
        (index for index, line in enumerate(body) if SEPARATOR_ECHO.match(line)),
        None,
    )
    header = body if separator_index is None else body[:separator_index]
    diagnostics = [] if separator_index is None else body[separator_index + 1 :]

    assignments: list[tuple[str, int]] = []
    status_fields = 0
    for offset, line in enumerate(header, start=1):
        stripped = line.strip()
        if not stripped:
            continue
        match = MACHINE_ECHO.match(line)
        if match is None:
            failures.append(
                f"{path}:{start_line + offset}: arbitrary output or command in "
                "machine-readable status header; move it after an echo "
                '"--- ... ---" separator'
            )
            continue
        key = match.group(2)
        assignments.append((key, start_line + offset))
        if key.endswith("_exit_status"):
            status_fields += 1

    if not assignments or assignments[0][0] != "schema":
        failures.append(
            f"{path}:{start_line}: status header must begin with a deterministic "
            "schema= field"
        )
    if status_fields == 0:
        failures.append(
            f"{path}:{start_line}: status header must contain at least one "
            "*_exit_status field"
        )

    keys = {key for key, _ in assignments}
    for key in REQUIRED_STATUS_METADATA:
        if key not in keys:
            failures.append(
                f"{path}:{start_line}: status header is missing required metadata "
                f"field {key}"
            )

    if separator_index is None:
        # Machine-only legacy files remain valid. Any non-assignment header line was
        # already rejected above, so diagnostics cannot silently enter the header.
        return failures

    for offset, line in enumerate(diagnostics, start=separator_index + 2):
        if STATUS_FIELD_ECHO.match(line):
            failures.append(
                f"{path}:{start_line + offset}: top-level status field appears after "
                "the diagnostic separator"
            )
    return failures


def lint_workflow(path: Path, text: str) -> list[str]:
    failures: list[str] = []
    for match in UNSAFE_STAGE.finditer(text):
        failures.append(
            f"{path}:{line_number(text, match.start())}: unsafe named optional "
            f"staging: {match.group(0)!r}"
        )

    is_probe_writer = (
        "contents: write" in text
        and any(marker in text for marker in PROBE_WRITER_MARKERS)
    )
    is_status_workflow = (
        "assert_probe_status.sh" in text
        or "_status.txt" in text
        or "reusable-python-probe-recorder.yml" in text
    )

    if is_probe_writer:
        if "group: probe-result-writers-main" not in text:
            failures.append(
                f"{path}: probe writer must use concurrency group "
                "probe-result-writers-main"
            )
        if not any(marker in text for marker in SAFE_RECORDER_MARKERS):
            failures.append(f"{path}: probe writer must use the shared hardened recorder")
        for match in DIRECT_OPTIONAL_REDIRECT.finditer(text):
            failures.append(
                f"{path}:{line_number(text, match.start())}: deterministic output must "
                f"be written atomically through a temporary file: {match.group(0)!r}"
            )

    if is_status_workflow:
        if "continue-on-error:" in text:
            failures.append(f"{path}: status workflows may not use continue-on-error")
        for match in SUPPRESSED_FAILURE.finditer(text):
            failures.append(
                f"{path}:{line_number(text, match.start())}: status workflows may not "
                "suppress failures with || true"
            )

    for start_line, body in status_blocks(text):
        failures.extend(lint_status_block(path, start_line, body))

    for assert_match in ASSERT_CALL.finditer(text):
        assert_pos = assert_match.start()
        upload_pos = text.rfind("actions/upload-artifact", 0, assert_pos)
        if upload_pos < 0:
            failures.append(
                f"{path}:{line_number(text, assert_pos)}: status assertion must run "
                "only after diagnostic artifacts are uploaded"
            )
        recorder_positions = [
            text.rfind(marker, 0, assert_pos)
            for marker in (
                "commit_probe_outputs.sh",
                "stage_optional_probe_outputs.sh",
            )
        ]
        if max(recorder_positions) < 0 and "contents: write" in text:
            failures.append(
                f"{path}:{line_number(text, assert_pos)}: writable status workflow "
                "must preserve or stage diagnostics before asserting status"
            )
    return failures


def main() -> int:
    failures: list[str] = []
    for path in sorted(WORKFLOW_DIR.glob("*.y*ml")):
        failures.extend(lint_workflow(path, path.read_text(encoding="utf-8")))

    for path in sorted(SRC_DIR.glob("*.sh")):
        text = path.read_text(encoding="utf-8")
        if path.name in FRAMEWORK_SCRIPTS:
            if "continue-on-error:" in text:
                failures.append(
                    f"{path}: framework scripts may not use continue-on-error"
                )
            for match in SUPPRESSED_FAILURE.finditer(text):
                failures.append(
                    f"{path}:{line_number(text, match.start())}: framework scripts "
                    "may not suppress failures with || true"
                )
        for start_line, body in status_blocks(text):
            failures.extend(lint_status_block(path, start_line, body))

    if failures:
        print("probe workflow lint failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("probe workflow lint passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

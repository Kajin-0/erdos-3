#!/usr/bin/env python3
"""Enforce the repository contract for writable GitHub Actions workflows."""
from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re
import sys
from typing import Iterable

WORKFLOW_DIR = Path('.github/workflows')
SRC_DIR = Path('src')
WRITER_GROUP = 'probe-result-writers-main'
REUSABLE_RECORDER = '.github/workflows/reusable-python-probe-recorder.yml'
DOC_HELPER = 'src/run_atomic_documentation_patch.sh'
COMMIT_HELPER = 'src/commit_probe_outputs.sh'
ONE_TIME_ALLOWLIST: frozenset[str] = frozenset()
CANONICAL_DOC_WORKFLOWS: frozenset[str] = frozenset()
AUTHORITATIVE_DOCS = frozenset({
    'README.md', 'docs/certainty-ledger.md', 'docs/current-proof-program.md',
    'docs/research-decision-history.md', 'docs/comprehensive-research-landscape.md',
})
FRAMEWORK_SCRIPTS = frozenset({
    'assert_probe_status.sh', 'run_atomic_python_probe.sh',
    'run_atomic_documentation_patch.sh', 'stage_optional_probe_outputs.sh',
    'commit_probe_outputs.sh', 'test_probe_workflow_helpers.sh',
})
REQUIRED_METADATA = ('schema', 'source_commit', 'source_ref', 'workflow_run_id', 'workflow_run_attempt')

UNSAFE_STAGE = re.compile(r'\bgit\s+add\s+-A\s+(?:--\s+)?data/[^\s]+')
DIRECT_OUTPUT = re.compile(r'>\s*data/[^\s]*(?:_probe\.json|_summary\.txt|_certificate[^\s]*\.txt)')
SUPPRESS = re.compile(r'\|\|\s*true\b')
MACHINE_ECHO = re.compile(r'^\s*echo\s+([\'\"])([A-Za-z_][A-Za-z0-9_]*)=.*\1\s*$')
SEPARATOR_ECHO = re.compile(r'^\s*echo\s+([\'\"])---.*\1\s*$')
STATUS_ECHO = re.compile(r'^\s*echo\s+([\'\"])([A-Za-z_][A-Za-z0-9_]*_exit_status)=.*\1\s*$')
ASSERT_CALL = re.compile(r'(?m)^\s*(?:run:\s*)?.*\bbash\s+src/assert_probe_status\.sh\b')
NAME = re.compile(r'(?m)^name:\s*(.+?)\s*$')
GROUP = re.compile(r'(?m)^\s*group:\s*([^\s#]+)')
PATCH = re.compile(r'\bsrc/(patch_[A-Za-z0-9_.-]+\.py)\b')
DATA_OUTPUT = re.compile(r'\bdata/[A-Za-z0-9_./${}-]+(?:\.json|\.txt|\.csv)\b')
SCHEMA = re.compile(r'echo\s+[\'\"]schema=([^\'\"$]+)')

@dataclass(frozen=True)
class Workflow:
    path: Path
    name: str
    text: str
    writable: bool
    delegated: bool
    status: bool
    writer: bool
    doc_patch: bool
    groups: tuple[str, ...]
    patch_scripts: frozenset[str]
    docs: frozenset[str]
    outputs: frozenset[str]
    triggers: frozenset[str]
    schemas: tuple[str, ...]
    artifact: bool
    commit_helper: str
    assertion: bool

def line_no(text: str, offset: int) -> int:
    return text.count('\n', 0, offset) + 1

def status_blocks(text: str) -> list[tuple[int, list[str]]]:
    lines = text.splitlines()
    result: list[tuple[int, list[str]]] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() != '{':
            i += 1
            continue
        end = i + 1
        while end < len(lines) and not re.match(r'^\s*}\s*>>?', lines[end]):
            end += 1
        if end < len(lines):
            body = lines[i + 1:end]
            if any('_exit_status=' in line for line in body):
                result.append((i + 1, body))
            i = end + 1
        else:
            i += 1
    return result

def lint_status_block(path: Path, start: int, body: list[str]) -> list[str]:
    failures: list[str] = []
    separator = next((i for i, line in enumerate(body) if SEPARATOR_ECHO.match(line)), None)
    header = body if separator is None else body[:separator]
    diagnostics = [] if separator is None else body[separator + 1:]
    assignments: list[str] = []
    status_count = 0
    for offset, line in enumerate(header, 1):
        if not line.strip():
            continue
        match = MACHINE_ECHO.match(line)
        if not match:
            failures.append(f'{path}:{start + offset}: arbitrary command in machine-readable status header')
            continue
        key = match.group(2)
        assignments.append(key)
        status_count += key.endswith('_exit_status')
    if not assignments or assignments[0] != 'schema':
        failures.append(f'{path}:{start}: status header must begin with schema=')
    if not status_count:
        failures.append(f'{path}:{start}: status header must contain at least one *_exit_status')
    for key in REQUIRED_METADATA:
        if key not in assignments:
            failures.append(f'{path}:{start}: status header missing {key}')
    if separator is not None:
        for offset, line in enumerate(diagnostics, separator + 2):
            if STATUS_ECHO.match(line):
                failures.append(f'{path}:{start + offset}: top-level status field after diagnostic separator')
    return failures

def list_values(text: str, key: str) -> frozenset[str]:
    values: set[str] = set()
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip() != f'{key}:':
            continue
        indent = len(line) - len(line.lstrip())
        for candidate in lines[i + 1:]:
            if not candidate.strip():
                continue
            candidate_indent = len(candidate) - len(candidate.lstrip())
            if candidate_indent <= indent:
                break
            stripped = candidate.strip()
            if stripped.startswith('-'):
                values.add(stripped[1:].strip().strip('\'\"'))
    return frozenset(value for value in values if value)

def inspect(path: Path, text: str) -> Workflow:
    name_match = NAME.search(text)
    name = name_match.group(1).strip('\'\"') if name_match else path.name
    writable = 'contents: write' in text
    delegated = f'uses: ./{REUSABLE_RECORDER}' in text or f'uses: {REUSABLE_RECORDER}' in text
    patch_scripts = frozenset(PATCH.findall(text))
    docs = frozenset(doc for doc in AUTHORITATIVE_DOCS if doc in text)
    doc_patch = writable and bool(patch_scripts or docs)
    outputs = set(DATA_OUTPUT.findall(text)) | set(docs)
    status = 'assert_probe_status.sh' in text or '_status.txt' in text or path.name == 'reusable-python-probe-recorder.yml'
    writer = writable and not delegated and bool(outputs or doc_patch or path.name == 'reusable-python-probe-recorder.yml')
    helper = ('commit_probe_outputs.sh' if COMMIT_HELPER in text else
              'stage_optional_probe_outputs.sh' if 'src/stage_optional_probe_outputs.sh' in text else 'none')
    return Workflow(
        path, name, text, writable, delegated, status, writer, doc_patch,
        tuple(GROUP.findall(text)), patch_scripts, docs, frozenset(outputs),
        list_values(text, 'paths'), tuple(SCHEMA.findall(text)),
        'actions/upload-artifact' in text, helper, 'assert_probe_status.sh' in text,
    )

def lint_one(info: Workflow) -> list[str]:
    path, text = info.path, info.text
    failures: list[str] = []
    if path.name.startswith('one-time-') and path.name not in ONE_TIME_ALLOWLIST:
        failures.append(f'{path}: one-time workflow files are prohibited after execution')
    for match in UNSAFE_STAGE.finditer(text):
        failures.append(f'{path}:{line_no(text, match.start())}: unsafe optional staging: {match.group(0)!r}')
    if info.writer:
        if info.groups != (WRITER_GROUP,):
            failures.append(f'{path}: writable writer must use exactly one concurrency group {WRITER_GROUP}; found {list(info.groups) or "none"}')
        if not any(marker in text for marker in (REUSABLE_RECORDER, 'src/stage_optional_probe_outputs.sh', COMMIT_HELPER)):
            failures.append(f'{path}: direct writer must use the shared recorder or commit helper')
        for match in DIRECT_OUTPUT.finditer(text):
            failures.append(f'{path}:{line_no(text, match.start())}: deterministic output must be written atomically')
    if info.doc_patch:
        if path.name not in CANONICAL_DOC_WORKFLOWS:
            failures.append(f'{path}: permanent documentation-patch workflow is not canonical; retain the script and delete the workflow')
        if DOC_HELPER not in text:
            failures.append(f'{path}: documentation writer must use {DOC_HELPER}')
        if COMMIT_HELPER not in text:
            failures.append(f'{path}: documentation writer must use {COMMIT_HELPER}')
    if info.status or info.writer or info.doc_patch:
        if 'continue-on-error:' in text:
            failures.append(f'{path}: status/result workflows may not use continue-on-error')
        for match in SUPPRESS.finditer(text):
            failures.append(f'{path}:{line_no(text, match.start())}: status/result workflows may not use || true')
    for start, body in status_blocks(text):
        failures.extend(lint_status_block(path, start, body))
    for match in ASSERT_CALL.finditer(text):
        pos = match.start()
        if text.rfind('actions/upload-artifact', 0, pos) < 0:
            failures.append(f'{path}:{line_no(text, pos)}: assertion precedes diagnostic artifact upload')
        if info.writable and max(text.rfind('commit_probe_outputs.sh', 0, pos), text.rfind('stage_optional_probe_outputs.sh', 0, pos)) < 0:
            failures.append(f'{path}:{line_no(text, pos)}: assertion precedes diagnostic preservation')
    return failures

def duplicate_failures(infos: Iterable[Workflow]) -> list[str]:
    failures: list[str] = []
    patches: dict[str, list[Path]] = defaultdict(list)
    docs: dict[str, list[Path]] = defaultdict(list)
    families: dict[tuple[frozenset[str], frozenset[str]], list[Path]] = defaultdict(list)
    for info in (item for item in infos if item.writable):
        for script in info.patch_scripts:
            patches[script].append(info.path)
        for doc in info.docs:
            docs[doc].append(info.path)
        if info.triggers and info.outputs:
            families[(info.triggers, info.outputs)].append(info.path)
    for label, owners in sorted(patches.items()):
        if len(owners) > 1:
            failures.append(f'duplicate writable ownership of src/{label}: {", ".join(map(str, sorted(owners)))}')
    for label, owners in sorted(docs.items()):
        if len(owners) > 1:
            failures.append(f'duplicate writable ownership of {label}: {", ".join(map(str, sorted(owners)))}')
    for (triggers, outputs), owners in sorted(families.items(), key=lambda item: tuple(map(str, sorted(item[1])))):
        if len(owners) > 1:
            failures.append('duplicate writable trigger/output family: ' + ', '.join(map(str, sorted(owners))) + f'; triggers={sorted(triggers)}; outputs={sorted(outputs)}')
    return failures

def lint_workflow_set(workflows: Iterable[tuple[Path, str]]) -> tuple[list[str], list[Workflow]]:
    infos = [inspect(path, text) for path, text in workflows]
    failures = [failure for info in infos for failure in lint_one(info)]
    failures.extend(duplicate_failures(infos))
    return failures, infos

def inventory(infos: Iterable[Workflow]) -> list[str]:
    lines = ['writable workflow inventory:', 'path | name | purpose | owned files | concurrency | schema | artifact | commit helper | final assertion']
    for info in sorted((item for item in infos if item.writable), key=lambda item: str(item.path)):
        purpose = ('documentation patch' if info.doc_patch else
                   'canonical reusable probe recorder' if info.path.name == 'reusable-python-probe-recorder.yml' else
                   'probe trigger delegating to reusable recorder' if info.delegated else
                   'status/result writer' if info.status else 'writable workflow')
        lines.append(' | '.join((
            str(info.path), info.name, purpose,
            ','.join(sorted(info.outputs)) or 'delegated/dynamic',
            ','.join(info.groups) or 'delegated/none',
            ','.join(info.schemas) or 'delegated/dynamic',
            'yes' if info.artifact else 'no', info.commit_helper,
            'yes' if info.assertion else 'no',
        )))
    return lines

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--inventory', action='store_true')
    args = parser.parse_args()
    workflow_files = [(path, path.read_text(encoding='utf-8')) for path in sorted(WORKFLOW_DIR.glob('*.y*ml'))]
    failures, infos = lint_workflow_set(workflow_files)
    for path in sorted(SRC_DIR.glob('*.sh')):
        text = path.read_text(encoding='utf-8')
        if path.name in FRAMEWORK_SCRIPTS:
            if 'continue-on-error:' in text:
                failures.append(f'{path}: framework scripts may not use continue-on-error')
            for match in SUPPRESS.finditer(text):
                failures.append(f'{path}:{line_no(text, match.start())}: framework scripts may not use || true')
        for start, body in status_blocks(text):
            failures.extend(lint_status_block(path, start, body))
    if args.inventory:
        print('\n'.join(inventory(infos)))
    if failures:
        print('probe workflow lint failed:', file=sys.stderr)
        for failure in failures:
            print(f'- {failure}', file=sys.stderr)
        return 1
    print('probe workflow lint passed')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

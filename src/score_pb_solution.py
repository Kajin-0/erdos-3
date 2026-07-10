#!/usr/bin/env python3
"""Parse a PB/MaxSAT solver assignment and score the selected digit set.

This is the bridge between external OPB solvers and the repo's harmonic scorer.
The expected model variables are the ones emitted by `src/cyclic_pb_encoder.py`:

    x0, x1, ..., x{b-1}

The parser accepts common assignment styles, including:

    v x0 -x1 x2 -x3
    x0=1 x1=0 x2=1
    x0 1
    x1 0

It then treats true variables as selected residues/digits, checks cyclic
modular k-AP-freeness, and computes the shifted Kempner sum

    H_shift(D,b) = sum_{n in K(D,b)} 1/(n+1).

This script deliberately does not trust solver output.  Every assignment is
rechecked before it is scored.  By default the assignment must explicitly assign
every model variable x0,...,x{b-1}; omitted variables are not silently treated as
false unless --allow-partial-assignment is supplied.
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from math import log
from pathlib import Path
from typing import Sequence

from shifted_kempner_sum import shifted_kempner_sum


SIGNED_VAR = re.compile(r"(?<![A-Za-z0-9_])(-?)x(\d+)(?![A-Za-z0-9_])")
EQ_VAR = re.compile(r"(?<![A-Za-z0-9_])x(\d+)\s*=\s*([01])")
PAIR_LINE = re.compile(r"^\s*x(\d+)\s+([01])\s*$")


@dataclass(frozen=True)
class ParsedAssignment:
    selected: tuple[int, ...]
    false_vars: tuple[int, ...]
    missing_vars: tuple[int, ...]
    status_lines: tuple[str, ...]
    objective_lines: tuple[str, ...]


class AssignmentParseError(ValueError):
    pass


def _assign_value(assignments: dict[int, int], idx: int, val: int, *, line: str) -> None:
    if val not in (0, 1):
        raise AssignmentParseError(f"invalid Boolean value for x{idx}: {val}")
    old = assignments.get(idx)
    if old is not None and old != val:
        raise AssignmentParseError(
            f"conflicting assignments for x{idx}: saw both {old} and {val}; line={line!r}"
        )
    assignments[idx] = val


def parse_assignment(
    text: str,
    base: int,
    *,
    require_complete: bool = True,
) -> ParsedAssignment:
    """Parse a solver assignment and validate model-variable coverage.

    Variables outside ``0 <= i < base`` are rejected.  In complete mode, every
    model variable x0,...,x{base-1} must appear explicitly as true or false.
    """
    assignments: dict[int, int] = {}
    status_lines: list[str] = []
    objective_lines: list[str] = []

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(("c", "*")):
            continue
        if line.startswith("s "):
            status_lines.append(line)
            continue
        if line.startswith("o "):
            objective_lines.append(line)
            continue

        pair = PAIR_LINE.match(line)
        if pair:
            idx = int(pair.group(1))
            val = int(pair.group(2))
            _assign_value(assignments, idx, val, line=line)
            continue

        matched_eq = False
        for idx_text, val_text in EQ_VAR.findall(line):
            matched_eq = True
            idx = int(idx_text)
            val = int(val_text)
            _assign_value(assignments, idx, val, line=line)

        # Signed variable format.  Skip equality lines already handled above;
        # otherwise `x3=0` would also look like a positive `x3` token.
        if matched_eq or "=" in line:
            continue
        for sign, idx_text in SIGNED_VAR.findall(line):
            idx = int(idx_text)
            val = 0 if sign == "-" else 1
            _assign_value(assignments, idx, val, line=line)

    out_of_range = sorted(idx for idx in assignments if idx < 0 or idx >= base)
    if out_of_range:
        raise AssignmentParseError(
            "assignment contains variables outside expected base "
            f"0..{base - 1}: {out_of_range}"
        )

    missing = tuple(idx for idx in range(base) if idx not in assignments)
    if require_complete and missing:
        raise AssignmentParseError(
            "incomplete solver assignment; missing variables: "
            + " ".join(f"x{i}" for i in missing)
        )

    selected = tuple(sorted(idx for idx, val in assignments.items() if val == 1))
    false_vars = tuple(sorted(idx for idx, val in assignments.items() if val == 0))
    return ParsedAssignment(
        selected=selected,
        false_vars=false_vars,
        missing_vars=missing,
        status_lines=tuple(status_lines),
        objective_lines=tuple(objective_lines),
    )


def parse_assignment_text(text: str, base: int) -> tuple[int, ...]:
    """Backward-compatible wrapper returning selected variables only.

    This uses complete-assignment validation.  Use ``parse_assignment`` directly
    when missing-variable diagnostics are needed.
    """
    return parse_assignment(text, base, require_complete=True).selected


def forbidden_masks_mod_b(b: int, k: int) -> list[int]:
    masks = set()
    for a in range(b):
        for d in range(1, b):
            residues = {(a + i * d) % b for i in range(k)}
            if len(residues) >= 2:
                masks.add(sum(1 << r for r in residues))
    return sorted(masks)


def is_modular_k_free(b: int, digits: Sequence[int], k: int) -> bool:
    mask = sum(1 << d for d in digits)
    return all((mask & f) != f for f in forbidden_masks_mod_b(b, k))


def check_size_bounds(
    digits: Sequence[int],
    *,
    expected_size: int | None,
    min_size: int | None,
    max_size: int | None,
) -> None:
    size = len(digits)
    if expected_size is not None and size != expected_size:
        raise SystemExit(f"parsed assignment size {size} != expected size {expected_size}")
    if min_size is not None and size < min_size:
        raise SystemExit(f"parsed assignment size {size} < min size {min_size}")
    if max_size is not None and size > max_size:
        raise SystemExit(f"parsed assignment size {size} > max size {max_size}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=int, required=True)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--solution", type=Path, required=True)
    parser.add_argument("--target", type=float, default=4.43975)
    parser.add_argument("--order", type=int, default=60)
    parser.add_argument("--tol", type=float, default=1e-15)
    parser.add_argument(
        "--allow-partial-assignment",
        action="store_true",
        help="allow omitted x_i variables and treat them as false for legacy solver outputs",
    )
    parser.add_argument("--expected-size", type=int, default=None)
    parser.add_argument("--min-size", type=int, default=None)
    parser.add_argument("--max-size", type=int, default=None)
    args = parser.parse_args()

    parsed = parse_assignment(
        args.solution.read_text(),
        args.base,
        require_complete=not args.allow_partial_assignment,
    )
    digits = parsed.selected
    if not digits:
        raise SystemExit("no true x_i variables were parsed from solver output")
    if 0 not in digits:
        raise SystemExit("parsed candidate does not contain digit 0; shifted scorer expects 0 in D")
    check_size_bounds(
        digits,
        expected_size=args.expected_size,
        min_size=args.min_size,
        max_size=args.max_size,
    )

    ap_free = is_modular_k_free(args.base, digits, args.k)
    score = shifted_kempner_sum(args.base, digits, order=args.order, tol=args.tol)

    print(f"base={args.base}")
    print(f"k={args.k}")
    print(f"digits={' '.join(map(str, digits))}")
    print(f"size={len(digits)}")
    print(f"assigned_true={len(parsed.selected)}")
    print(f"assigned_false={len(parsed.false_vars)}")
    print(f"missing_variables={len(parsed.missing_vars)}")
    if parsed.status_lines:
        print("solver_status_lines=" + " | ".join(parsed.status_lines))
    if parsed.objective_lines:
        print("solver_objective_lines=" + " | ".join(parsed.objective_lines))
    print(f"alpha={log(len(digits)) / log(args.base):.10f}")
    print(f"modular_k_free={int(ap_free)}")
    print(f"shifted_sum={score.shifted_sum:.12f}")
    print(f"target={args.target:.12f}")
    print(f"beats_target={int(ap_free and score.shifted_sum > args.target)}")


if __name__ == "__main__":
    main()

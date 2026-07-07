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
rechecked before it is scored.
"""
from __future__ import annotations

import argparse
import re
from math import log
from pathlib import Path
from typing import Sequence

from shifted_kempner_sum import shifted_kempner_sum


SIGNED_VAR = re.compile(r"(?<![A-Za-z0-9_])(-?)x(\d+)(?![A-Za-z0-9_])")
EQ_VAR = re.compile(r"(?<![A-Za-z0-9_])x(\d+)\s*=\s*([01])")
PAIR_LINE = re.compile(r"^\s*x(\d+)\s+([01])\s*$")


def parse_assignment_text(text: str, base: int) -> tuple[int, ...]:
    true_vars: set[int] = set()
    false_vars: set[int] = set()

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(("c", "*")):
            continue
        if line.startswith("s ") or line.startswith("o "):
            continue

        pair = PAIR_LINE.match(line)
        if pair:
            idx = int(pair.group(1))
            val = int(pair.group(2))
            if val:
                true_vars.add(idx)
                false_vars.discard(idx)
            else:
                false_vars.add(idx)
                true_vars.discard(idx)
            continue

        for idx_text, val_text in EQ_VAR.findall(line):
            idx = int(idx_text)
            val = int(val_text)
            if val:
                true_vars.add(idx)
                false_vars.discard(idx)
            else:
                false_vars.add(idx)
                true_vars.discard(idx)

        # Signed variable format.  Skip equality lines already handled above;
        # otherwise `x3=0` would also look like a positive `x3` token.
        if "=" in line:
            continue
        for sign, idx_text in SIGNED_VAR.findall(line):
            idx = int(idx_text)
            if sign == "-":
                false_vars.add(idx)
                true_vars.discard(idx)
            else:
                true_vars.add(idx)
                false_vars.discard(idx)

    selected = tuple(sorted(x for x in true_vars if 0 <= x < base))
    return selected


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=int, required=True)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--solution", type=Path, required=True)
    parser.add_argument("--target", type=float, default=4.43975)
    parser.add_argument("--order", type=int, default=60)
    parser.add_argument("--tol", type=float, default=1e-15)
    args = parser.parse_args()

    digits = parse_assignment_text(args.solution.read_text(), args.base)
    if not digits:
        raise SystemExit("no true x_i variables were parsed from solver output")
    if 0 not in digits:
        raise SystemExit("parsed candidate does not contain digit 0; shifted scorer expects 0 in D")

    ap_free = is_modular_k_free(args.base, digits, args.k)
    score = shifted_kempner_sum(args.base, digits, order=args.order, tol=args.tol)

    print(f"base={args.base}")
    print(f"k={args.k}")
    print(f"digits={' '.join(map(str, digits))}")
    print(f"size={len(digits)}")
    print(f"alpha={log(len(digits)) / log(args.base):.10f}")
    print(f"modular_k_free={int(ap_free)}")
    print(f"shifted_sum={score.shifted_sum:.12f}")
    print(f"target={args.target:.12f}")
    print(f"beats_target={int(ap_free and score.shifted_sum > args.target)}")


if __name__ == "__main__":
    main()

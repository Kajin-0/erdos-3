#!/usr/bin/env python3
"""Scan fixed-size digit-substitution neighborhoods around a benchmark set.

The current best public k=4 shifted Kempner benchmark is Walker's base-55 set.
This script tests whether small same-size substitutions can improve it.

A radius-r scan removes r nonzero digits from the benchmark and adds r missing
digits, preserving both zero and set size.  Each neighbor is checked for cyclic
modular k-AP-freeness.  AP-free neighbors are then scored by the shifted Kempner
harmonic scorer.

The first recorded result for Walker's base-55 set is strong local rigidity:
there are no AP-free radius-1 or radius-2 neighbors.
"""
from __future__ import annotations

import argparse
import csv
from itertools import combinations
from math import log
from pathlib import Path
from typing import Sequence

from shifted_kempner_sum import parse_digits, shifted_kempner_sum


def forbidden_masks_mod_b(b: int, k: int) -> list[int]:
    masks = set()
    for a in range(b):
        for d in range(1, b):
            residues = {(a + i * d) % b for i in range(k)}
            if len(residues) >= 2:
                masks.add(sum(1 << r for r in residues))
    return sorted(masks)


def mask_from_digits(digits: Sequence[int]) -> int:
    mask = 0
    for d in digits:
        mask |= 1 << d
    return mask


def digits_from_mask(mask: int, b: int) -> tuple[int, ...]:
    return tuple(i for i in range(b) if (mask >> i) & 1)


def is_free_mask(mask: int, forbidden: Sequence[int]) -> bool:
    return all((mask & f) != f for f in forbidden)


def scan_radius(
    base: int,
    k: int,
    digits: Sequence[int],
    radius: int,
    score_order: int,
    score_tol: float,
) -> dict[str, object]:
    D = set(digits)
    if 0 not in D:
        raise ValueError("benchmark digits must contain 0; scans preserve zero")

    forbidden = forbidden_masks_mod_b(base, k)
    start_mask = mask_from_digits(digits)
    start_score = shifted_kempner_sum(base, digits, order=score_order, tol=score_tol).shifted_sum

    removable = sorted(D - {0})
    addable = sorted(set(range(base)) - D)

    total_neighbors = 0
    ap_free_neighbors = 0
    scored_neighbors = 0
    best_score = start_score
    best_remove: tuple[int, ...] | None = None
    best_add: tuple[int, ...] | None = None
    best_digits = tuple(sorted(D))

    for rem in combinations(removable, radius):
        base_mask = start_mask
        for d in rem:
            base_mask &= ~(1 << d)
        for add in combinations(addable, radius):
            total_neighbors += 1
            candidate_mask = base_mask
            for d in add:
                candidate_mask |= 1 << d
            if not is_free_mask(candidate_mask, forbidden):
                continue
            ap_free_neighbors += 1
            cand_digits = digits_from_mask(candidate_mask, base)
            score = shifted_kempner_sum(base, cand_digits, order=score_order, tol=score_tol).shifted_sum
            scored_neighbors += 1
            if score > best_score:
                best_score = score
                best_remove = rem
                best_add = add
                best_digits = cand_digits

    return {
        "base": base,
        "k": k,
        "radius": radius,
        "size": len(D),
        "alpha": log(len(D)) / log(base),
        "start_score": start_score,
        "best_score": best_score,
        "improved": int(best_score > start_score),
        "total_neighbors": total_neighbors,
        "ap_free_neighbors": ap_free_neighbors,
        "scored_neighbors": scored_neighbors,
        "best_remove": "" if best_remove is None else " ".join(map(str, best_remove)),
        "best_add": "" if best_add is None else " ".join(map(str, best_add)),
        "best_digits": " ".join(map(str, best_digits)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=int, required=True)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--digits", required=True)
    parser.add_argument("--max-radius", type=int, default=2)
    parser.add_argument("--order", type=int, default=40)
    parser.add_argument("--tol", type=float, default=1e-12)
    parser.add_argument("--csv", type=Path, default=None)
    args = parser.parse_args()

    digits = parse_digits(args.digits)
    rows = []
    for radius in range(1, args.max_radius + 1):
        row = scan_radius(args.base, args.k, digits, radius, args.order, args.tol)
        rows.append(row)
        print(
            f"radius={radius} total={row['total_neighbors']} "
            f"ap_free={row['ap_free_neighbors']} improved={row['improved']} "
            f"best={row['best_score']:.12f}"
        )

    if args.csv:
        args.csv.parent.mkdir(parents=True, exist_ok=True)
        with args.csv.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
        print(f"wrote {args.csv}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate and score one cyclic digit-set candidate.

This is the end-to-end gate for proposed one-layer shifted Kempner candidates:

1. Parse a base-b digit set D.
2. Check the cyclic modular k-AP-free certificate.
3. Compute the shifted Kempner harmonic score

       H_shift(D,b) = sum_{n in K(D,b)} 1/(n+1).

A candidate only matters for the current k=4 benchmark if it is certified
4-AP-free and its shifted score exceeds Walker's public base-55 value 4.43975.
"""
from __future__ import annotations

import argparse
from math import log
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


def is_modular_k_free(b: int, digits: Sequence[int], k: int) -> bool:
    mask = sum(1 << d for d in digits)
    return all((mask & f) != f for f in forbidden_masks_mod_b(b, k))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=int, required=True)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--digits", required=True)
    parser.add_argument("--target", type=float, default=4.43975)
    parser.add_argument("--order", type=int, default=60)
    parser.add_argument("--tol", type=float, default=1e-15)
    args = parser.parse_args()

    digits = parse_digits(args.digits)
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

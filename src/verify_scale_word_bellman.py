#!/usr/bin/env python3
"""Verify the exact Bellman defect, block-ratio, and repayment identities."""
from __future__ import annotations

from fractions import Fraction


def next_size(size: int) -> int:
    return 3 * (size + 1)


def bellman(size: int, persistence: int, scale: int) -> Fraction:
    return Fraction(4 * persistence * (size + 1), scale)


def weight(size: int, persistence: int, scale: int) -> Fraction:
    return Fraction(persistence * size, scale)


def advance(size: int, persistence: int, scale: int, factor: int):
    return next_size(size), 2 * persistence, factor * scale


def endpoint_ratio(size: int, factors: tuple[int, ...]) -> Fraction:
    initial = bellman(size, 1, 1)
    state = (size, 1, 1)
    for factor in factors:
        state = advance(*state, factor)
    return bellman(*state) / initial


def main() -> None:
    for size in range(1, 100):
        for factor in (2, 4, 8, 16, 32):
            child = advance(size, 1, 1, factor)
            defect = bellman(size, 1, 1) - weight(size, 1, 1) - bellman(*child)
            expected = Fraction(3 * size + 4, 1) * (1 - Fraction(8, factor))
            if defect != expected:
                raise AssertionError("one-step Bellman defect mismatch")

        ratio_48 = endpoint_ratio(size, (4, 8))
        if ratio_48 != Fraction(9 * size + 13, 8 * (size + 1)):
            raise AssertionError("4,8 block mismatch")

        for word in ((4, 8, 8), (8, 4, 8), (8, 8, 4)):
            ratio = endpoint_ratio(size, word)
            if ratio != Fraction(27 * size + 40, 32 * (size + 1)):
                raise AssertionError("factor-four repayment block mismatch")

        for word in (
            (2, 8, 8, 8, 8),
            (8, 2, 8, 8, 8),
            (8, 8, 2, 8, 8),
            (8, 8, 8, 2, 8),
            (8, 8, 8, 8, 2),
        ):
            ratio = endpoint_ratio(size, word)
            if ratio != Fraction(243 * size + 364, 256 * (size + 1)):
                raise AssertionError("factor-two repayment block mismatch")

    if not all(endpoint_ratio(size, (4, 8)) > 1 for size in range(1, 1000)):
        raise AssertionError("one factor eight unexpectedly repays factor four")
    if not all(endpoint_ratio(size, (4, 8, 8)) < 1 for size in range(2, 1000)):
        raise AssertionError("two factor eights failed to repay factor four")
    if not all(endpoint_ratio(size, (2, 8, 8, 8, 8)) < 1 for size in range(9, 1000)):
        raise AssertionError("four factor eights failed to repay factor two")

    recorded = (4, 8, 4, 4, 8, 4, 8, 8, 8)
    if endpoint_ratio(12, recorded) != Fraction(2555, 2048):
        # B10/B1 = [4*1024*(265720)/L10] / [4*2*13/64].
        raise AssertionError("recorded branch endpoint ratio mismatch")

    print("verified: Bellman defect identity for dyadic factors 2 through 32")
    print("verified: endpoint ratio depends only on cumulative scale product")
    print("verified: one factor four plus two factor eights contracts for N>=2")
    print("verified: one factor two plus four factor eights contracts for N>=9")
    print("recorded_B10_over_B1=2555/2048")
    print("factor4_block_uniform_bound_N9=283/320")
    print("factor2_block_uniform_bound_N9=2551/2560")


if __name__ == "__main__":
    main()

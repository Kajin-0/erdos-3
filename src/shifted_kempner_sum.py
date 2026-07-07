#!/usr/bin/env python3
"""Score shifted Kempner harmonic sums for digit-restricted sets.

Walker reports harmonic sums for shifted Kempner sets.  If

    K(D,b) = {n >= 0 : every base-b digit of n lies in D},

then the shifted set scored here is

    K(D,b) + 1 = {n + 1 : n in K(D,b)}.

The scored quantity is therefore

    H_shift(D,b) = sum_{n in K(D,b)} 1/(n + 1).

This convention includes the contribution from n=0, namely 1/(0+1)=1, and
matches the public Walker k=4 values in `data/public_benchmarks.csv` to the
reported precision.

Method
------
For each number of suffix digits m, write an element of K(D,b) as

    n = a*b^m + r,

where a is a nonzero leading digit in D and r is an m-digit suffix using digits
from D, leading zeros allowed.  We need

    sum_r 1/(a*b^m + r + 1).

Set B=b^m and expand around the midpoint r=B/2:

    a*B + r + 1 = B*(a + 1/2 + 1/B) + (r - B/2).

Because |r-B/2| / (B*(a+1/2+1/B)) <= 1/3 for a>=1, the geometric expansion is
rapid.  Normalized suffix power moments are updated by a stable recurrence, so
we never enumerate all suffixes.

This is a compact Python scorer intended for candidate triage and benchmark
reproduction.  It is not a replacement for high-precision Baillie-Schmelzer
post-processing, but it is accurate enough for the public 5-decimal benchmarks.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from math import comb, log
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class ScoreResult:
    base: int
    digits: tuple[int, ...]
    shifted_sum: float
    alpha: float
    levels: int
    order: int


@dataclass(frozen=True)
class BenchmarkRow:
    benchmark_id: str
    k: int
    base: int | None
    digits: tuple[int, ...] | None
    reported_harmonic_sum: float | None


def parse_digits(text: str) -> tuple[int, ...]:
    return tuple(sorted({int(x) for x in text.replace(",", " ").split()}))


def parse_optional_digits(text: str) -> tuple[int, ...] | None:
    text = text.strip()
    if not text:
        return None
    return parse_digits(text)


def shifted_kempner_sum(
    base: int,
    digits: Sequence[int],
    order: int = 60,
    tol: float = 1e-15,
    max_levels: int = 500,
) -> ScoreResult:
    """Approximate sum_{n in K(D,b)} 1/(n+1)."""
    D = tuple(sorted(set(digits)))
    if 0 not in D:
        raise ValueError("digits must contain 0 for the shifted Kempner convention")
    if any(d < 0 or d >= base for d in D):
        raise ValueError("digits must lie in {0,...,base-1}")

    leading_digits = [d for d in D if d > 0]
    if not leading_digits:
        return ScoreResult(base, D, 1.0, 0.0, 0, order)

    # R[j] = sum_{r in R_m} (r / b^m)^j for current suffix length m.
    # For m=0, there is one suffix r=0.
    R = [0.0 for _ in range(order + 1)]
    R[0] = 1.0

    digit_power_sums = [sum(d**e for d in D) for e in range(order + 1)]

    total = 1.0  # contribution from n=0 in K(D,b), shifted to denominator 1
    levels_used = 0

    for m in range(max_levels):
        B = float(base**m)

        # C[s] = sum_r ((r/B) - 1/2)^s.
        central = []
        for s in range(order + 1):
            value = 0.0
            for j in range(s + 1):
                value += comb(s, j) * R[j] * ((-0.5) ** (s - j))
            central.append(value)

        shell = 0.0
        for a in leading_digits:
            center = a + 0.5 + 1.0 / B
            subtotal = 0.0
            for s, moment in enumerate(central):
                subtotal += ((-1.0) ** s) * moment / (center ** (s + 1))
            shell += subtotal / B

        total += shell
        levels_used = m + 1

        if abs(shell) < tol:
            break

        # Advance normalized raw suffix moments from length m to m+1.
        next_R = [0.0 for _ in range(order + 1)]
        for s in range(order + 1):
            accum = 0.0
            for j in range(s + 1):
                accum += comb(s, j) * digit_power_sums[s - j] * R[j]
            next_R[s] = accum / (base**s)
        R = next_R
    else:
        raise RuntimeError("max_levels reached before convergence")

    alpha = log(len(D)) / log(base) if len(D) > 1 else 0.0
    return ScoreResult(base, D, total, alpha, levels_used, order)


def load_benchmark_rows(path: Path) -> list[BenchmarkRow]:
    rows: list[BenchmarkRow] = []
    with path.open(newline="") as f:
        for row in csv.DictReader(f):
            base = int(row["base"]) if row["base"].strip() else None
            harmonic = float(row["harmonic_sum"]) if row["harmonic_sum"].strip() else None
            rows.append(
                BenchmarkRow(
                    benchmark_id=row["id"],
                    k=int(row["k"]),
                    base=base,
                    digits=parse_optional_digits(row["digits_or_layers"]),
                    reported_harmonic_sum=harmonic,
                )
            )
    return rows


def score_benchmarks(path: Path, order: int, tol: float) -> None:
    print("id,k,base,size,reported,computed,error,alpha,levels")
    for row in load_benchmark_rows(path):
        if row.base is None or row.digits is None:
            continue
        result = shifted_kempner_sum(row.base, row.digits, order=order, tol=tol)
        reported = row.reported_harmonic_sum
        error = "" if reported is None else f"{result.shifted_sum - reported:.10e}"
        reported_text = "" if reported is None else f"{reported:.10f}"
        print(
            f"{row.benchmark_id},{row.k},{row.base},{len(row.digits)},"
            f"{reported_text},{result.shifted_sum:.10f},{error},"
            f"{result.alpha:.10f},{result.levels}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=int, default=None)
    parser.add_argument("--digits", type=str, default=None)
    parser.add_argument("--benchmarks", type=Path, default=None)
    parser.add_argument("--order", type=int, default=60)
    parser.add_argument("--tol", type=float, default=1e-15)
    args = parser.parse_args()

    if args.benchmarks is not None:
        score_benchmarks(args.benchmarks, args.order, args.tol)
        return

    if args.base is None or args.digits is None:
        raise SystemExit("provide either --benchmarks or both --base and --digits")

    result = shifted_kempner_sum(args.base, parse_digits(args.digits), args.order, args.tol)
    print(f"base={result.base}")
    print(f"digits={' '.join(map(str, result.digits))}")
    print(f"size={len(result.digits)}")
    print(f"alpha={result.alpha:.10f}")
    print(f"shifted_sum={result.shifted_sum:.12f}")
    print(f"levels={result.levels}")
    print(f"order={result.order}")


if __name__ == "__main__":
    main()

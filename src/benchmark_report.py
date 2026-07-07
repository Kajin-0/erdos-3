#!/usr/bin/env python3
"""Validate and summarize public Erdős #3 benchmark entries.

This script is intentionally conservative.  It does not attempt to recompute
Walker's harmonic sums.  It validates the finite modular certificate when a
benchmark is a one-layer digit set, computes the density exponent, and reports
whether the entry is a k=4 target benchmark or only an adjacent reference.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from math import log
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class Benchmark:
    benchmark_id: str
    k: int
    base: int | None
    period: int | None
    kind: str
    digits: tuple[int, ...] | None
    harmonic_sum: float | None
    source: str
    notes: str


def parse_optional_int(text: str) -> int | None:
    return None if text.strip() == "" else int(text)


def parse_optional_float(text: str) -> float | None:
    return None if text.strip() == "" else float(text)


def parse_digits(text: str) -> tuple[int, ...] | None:
    text = text.strip()
    if not text:
        return None
    return tuple(int(x) for x in text.split())


def load_benchmarks(path: Path) -> list[Benchmark]:
    rows: list[Benchmark] = []
    with path.open(newline="") as f:
        for row in csv.DictReader(f):
            rows.append(
                Benchmark(
                    benchmark_id=row["id"],
                    k=int(row["k"]),
                    base=parse_optional_int(row["base"]),
                    period=parse_optional_int(row["period"]),
                    kind=row["kind"],
                    digits=parse_digits(row["digits_or_layers"]),
                    harmonic_sum=parse_optional_float(row["harmonic_sum"]),
                    source=row["source"],
                    notes=row["notes"],
                )
            )
    return rows


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


def density_exponent(base: int, digits: Sequence[int]) -> float:
    return log(len(digits)) / log(base)


def summarize(path: Path) -> None:
    rows = load_benchmarks(path)
    print("id,k,base,size,alpha,modular_k_free,harmonic_sum")
    for row in rows:
        if row.base is None or row.digits is None:
            print(
                f"{row.benchmark_id},{row.k},,,,{''},{row.harmonic_sum if row.harmonic_sum is not None else ''}"
            )
            continue
        alpha = density_exponent(row.base, row.digits)
        ok = is_modular_k_free(row.base, row.digits, row.k)
        print(
            f"{row.benchmark_id},{row.k},{row.base},{len(row.digits)},"
            f"{alpha:.10f},{int(ok)},{row.harmonic_sum if row.harmonic_sum is not None else ''}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmarks", type=Path, default=Path("data/public_benchmarks.csv"))
    args = parser.parse_args()
    summarize(args.benchmarks)


if __name__ == "__main__":
    main()

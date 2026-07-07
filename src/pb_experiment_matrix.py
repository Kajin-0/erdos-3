#!/usr/bin/env python3
"""Generate a reproducible PB/MaxSAT experiment matrix.

The goal is to avoid ad hoc solver runs.  This script emits a CSV of OPB model
commands around the known Walker base-55 benchmark.  Each row specifies:

- base b;
- target set size;
- objective proxy;
- OPB output path;
- command to generate the OPB model;
- command template to score a solver assignment.

The generated OPB files still need an external pseudo-Boolean optimizer.  Solver
outputs should be passed through `src/score_pb_solution.py` before any result is
accepted.
"""
from __future__ import annotations

import argparse
import csv
from math import exp, log
from pathlib import Path

TARGET_ALPHA = log(21) / log(55)
TARGET_SUM = 4.43975


def target_sizes_for_base(b: int, delta: int) -> list[int]:
    center = int(round(exp(TARGET_ALPHA * log(b))))
    sizes = sorted({max(2, center + d) for d in range(-delta, delta + 1)})
    return [s for s in sizes if s <= b]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b-min", type=int, default=45)
    parser.add_argument("--b-max", type=int, default=65)
    parser.add_argument("--size-delta", type=int, default=1)
    parser.add_argument(
        "--objectives",
        nargs="+",
        default=["harmonic_proxy", "low_digit", "cardinality"],
    )
    parser.add_argument("--models-dir", type=Path, default=Path("models"))
    parser.add_argument("--solutions-dir", type=Path, default=Path("solver_outputs"))
    parser.add_argument("--csv", type=Path, required=True)
    args = parser.parse_args()

    rows = []
    for b in range(args.b_min, args.b_max + 1):
        for size in target_sizes_for_base(b, args.size_delta):
            for objective in args.objectives:
                model = args.models_dir / f"cyclic_b{b}_k4_s{size}_{objective}.opb"
                solution = args.solutions_dir / f"cyclic_b{b}_k4_s{size}_{objective}.sol"
                rows.append(
                    {
                        "base": b,
                        "k": 4,
                        "size": size,
                        "target_alpha": f"{TARGET_ALPHA:.10f}",
                        "target_sum": f"{TARGET_SUM:.5f}",
                        "objective": objective,
                        "model_path": str(model),
                        "solution_path": str(solution),
                        "generate_model_cmd": (
                            "python src/cyclic_pb_encoder.py "
                            f"--base {b} --k 4 --min-size {size} --max-size {size} "
                            f"--objective {objective} --output {model}"
                        ),
                        "score_solution_cmd": (
                            "python src/score_pb_solution.py "
                            f"--base {b} --k 4 --solution {solution} --target {TARGET_SUM}"
                        ),
                    }
                )

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {args.csv} rows={len(rows)}")


if __name__ == "__main__":
    main()

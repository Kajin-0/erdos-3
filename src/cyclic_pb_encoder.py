#!/usr/bin/env python3
"""Generate OPB pseudo-Boolean models for cyclic 4-AP-free digit templates.

This is the first SAT/PB pivot after the literature audit.  Walker's public
`searchkfree` code already does substantial branch-and-bound search over modular
digit templates.  The purpose here is different: emit a standard optimization
model that can be handed to external PB/MaxSAT tooling.

Variables
---------
    x_d = 1  iff digit/residue d is selected, for d in Z/bZ.

Hard constraints
----------------
For every nontrivial cyclic k-term arithmetic progression mask M in Z/bZ,

    sum_{d in M} x_d <= |M|-1.

For k=4 this forbids every cyclic 4-AP from being fully selected.  The model can
also force x_0 = 1 and impose lower/upper size bounds.

Objective
---------
OPB is a minimization format.  We therefore minimize a negative weighted score:

    min: -w_0 x_0 - ... - w_{b-1} x_{b-1};

The default score favors smaller digits because shifted Kempner harmonic sums are
usually sensitive to low leading digits.  This is only a surrogate objective.  A
true Walker-style final score still requires harmonic post-processing.

Example
-------
    python src/cyclic_pb_encoder.py --base 55 --k 4 --min-size 21 \
        --objective harmonic_proxy --output models/cyclic_b55_k4.opb

Then solve the OPB file with an external pseudo-Boolean optimizer such as
RoundingSat, Sat4j PB, Open-WBO/PB front-ends, or another PB-capable solver.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


@dataclass(frozen=True)
class APConstraint:
    residues: tuple[int, ...]

    @property
    def rhs(self) -> int:
        return len(self.residues) - 1


def cyclic_ap_masks(base: int, k: int) -> list[APConstraint]:
    """Return unique nontrivial cyclic k-AP residue masks in Z/base Z."""
    masks: set[tuple[int, ...]] = set()
    for a in range(base):
        for d in range(1, base):
            residues = tuple(sorted({(a + i * d) % base for i in range(k)}))
            if len(residues) >= 2:
                masks.add(residues)
    return [APConstraint(m) for m in sorted(masks, key=lambda xs: (len(xs), xs))]


def objective_weights(base: int, mode: str) -> list[int]:
    """Integer objective weights for OPB output.

    The weights are deliberately simple and solver-friendly.  They should be
    interpreted as screening proxies, not exact harmonic sums.
    """
    if mode == "cardinality":
        return [1 for _ in range(base)]
    if mode == "low_digit":
        return [base - d for d in range(base)]
    if mode == "harmonic_proxy":
        # A mild low-digit bias.  Scaling by 1000 keeps integer OPB weights while
        # avoiding huge coefficient ranges.  Digit 0 receives the largest weight.
        return [1000 // (d + 1) for d in range(base)]
    raise ValueError(f"unknown objective mode: {mode}")


def term(coeff: int, var: str) -> str:
    return f"{coeff} {var}"


def write_opb(
    path: Path,
    base: int,
    k: int,
    objective: str,
    require_zero: bool,
    min_size: int | None,
    max_size: int | None,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    constraints = cyclic_ap_masks(base, k)
    weights = objective_weights(base, objective)
    variables = [f"x{d}" for d in range(base)]

    lines: list[str] = []
    lines.append(f"* cyclic {k}-AP-free digit-template PB model")
    lines.append(f"* base={base} variables={base} ap_constraints={len(constraints)}")
    lines.append(f"* objective={objective}; positive score is negated for OPB minimization")

    objective_terms = " ".join(term(-w, v) for w, v in zip(weights, variables) if w != 0)
    lines.append(f"min: {objective_terms};")

    if require_zero:
        lines.append("1 x0 >= 1;")

    if min_size is not None:
        lines.append(" ".join(term(1, v) for v in variables) + f" >= {min_size};")

    if max_size is not None:
        lines.append(" ".join(term(1, v) for v in variables) + f" <= {max_size};")

    for c in constraints:
        lhs = " ".join(term(1, f"x{d}") for d in c.residues)
        lines.append(f"{lhs} <= {c.rhs};")

    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", type=int, required=True)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument(
        "--objective",
        choices=["cardinality", "low_digit", "harmonic_proxy"],
        default="harmonic_proxy",
    )
    parser.add_argument("--require-zero", action="store_true", default=True)
    parser.add_argument("--allow-missing-zero", action="store_true")
    parser.add_argument("--min-size", type=int, default=None)
    parser.add_argument("--max-size", type=int, default=None)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    write_opb(
        path=args.output,
        base=args.base,
        k=args.k,
        objective=args.objective,
        require_zero=not args.allow_missing_zero,
        min_size=args.min_size,
        max_size=args.max_size,
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()

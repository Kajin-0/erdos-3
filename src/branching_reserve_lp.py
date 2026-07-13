#!/usr/bin/env python3
"""Export and verify exact branching-reserve inequalities.

Input is JSON Lines. Each non-comment row represents one parent transition:

{
  "name": "transition-name",
  "debt": "3/2",
  "error": "0",
  "parent": {"radius_deficit": "4", "support_holes": "2"},
  "children": [
    {
      "multiplicity": 1,
      "features": {"radius_deficit": "1", "support_holes": "1"}
    }
  ]
}

All numeric values may be integers or rational strings. The encoded target is

    debt + sum_child Phi(child) <= Phi(parent) + error,

with Phi(state) = sum_feature weight[feature] * feature(state).

The tool can export a CPLEX-LP feasibility problem or verify a supplied weight
vector using exact fractions. It does not claim that any listed feature family
is sufficient for the Erdős proof program.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Any
import argparse
import json
from math import lcm
import re


FeatureMap = dict[str, Fraction]


@dataclass(frozen=True)
class Constraint:
    name: str
    coefficients: FeatureMap
    rhs: Fraction

    def slack(self, weights: FeatureMap) -> Fraction:
        lhs = sum(
            coefficient * weights.get(feature, Fraction(0))
            for feature, coefficient in self.coefficients.items()
        )
        return lhs - self.rhs


def as_fraction(value: Any, field: str) -> Fraction:
    if isinstance(value, bool):
        raise ValueError(f"{field}: booleans are not numeric values")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError(
                f"{field}: invalid rational {value!r}"
            ) from exc
    raise ValueError(
        f"{field}: expected integer or rational string, "
        f"got {type(value).__name__}"
    )


def parse_features(raw: Any, field: str) -> FeatureMap:
    if not isinstance(raw, dict):
        raise ValueError(f"{field}: expected object")
    result: FeatureMap = {}
    for name, value in raw.items():
        if not isinstance(name, str) or not name:
            raise ValueError(
                f"{field}: feature names must be nonempty strings"
            )
        result[name] = as_fraction(value, f"{field}.{name}")
    return result


def add_scaled(
    target: FeatureMap,
    source: FeatureMap,
    scale: Fraction,
) -> None:
    for feature, value in source.items():
        target[feature] = (
            target.get(feature, Fraction(0)) + scale * value
        )
        if target[feature] == 0:
            del target[feature]


def parse_constraint(raw: Any, line_number: int) -> Constraint:
    if not isinstance(raw, dict):
        raise ValueError(f"line {line_number}: expected JSON object")
    name = raw.get("name", f"line-{line_number}")
    if not isinstance(name, str) or not name:
        raise ValueError(
            f"line {line_number}: name must be a nonempty string"
        )

    debt = as_fraction(raw.get("debt", 0), f"{name}.debt")
    error = as_fraction(raw.get("error", 0), f"{name}.error")
    parent = parse_features(
        raw.get("parent", {}),
        f"{name}.parent",
    )
    children = raw.get("children", [])
    if not isinstance(children, list):
        raise ValueError(f"{name}.children: expected array")

    coefficients = dict(parent)
    for index, child in enumerate(children):
        if not isinstance(child, dict):
            raise ValueError(
                f"{name}.children[{index}]: expected object"
            )
        multiplicity = as_fraction(
            child.get("multiplicity", 1),
            f"{name}.children[{index}].multiplicity",
        )
        if multiplicity < 0:
            raise ValueError(
                f"{name}.children[{index}].multiplicity "
                "must be nonnegative"
            )
        features = parse_features(
            child.get("features", {}),
            f"{name}.children[{index}].features",
        )
        add_scaled(coefficients, features, -multiplicity)

    # debt + child potential <= parent potential + error
    # (parent - child features) dot weights >= debt - error
    return Constraint(
        name=name,
        coefficients=coefficients,
        rhs=debt - error,
    )


def load_constraints(path: Path) -> list[Constraint]:
    constraints: list[Constraint] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    for line_number, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        try:
            raw = json.loads(stripped)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"line {line_number}: invalid JSON: {exc}"
            ) from exc
        constraints.append(
            parse_constraint(raw, line_number)
        )
    if not constraints:
        raise ValueError("input contains no constraints")
    return constraints


def load_weights(path: Path) -> FeatureMap:
    raw = json.loads(path.read_text(encoding="utf-8"))
    weights = parse_features(raw, "weights")
    negative = {
        name: value
        for name, value in weights.items()
        if value < 0
    }
    if negative:
        raise ValueError(
            f"weights must be nonnegative: {negative}"
        )
    return weights


def safe_name(name: str, prefix: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]", "_", name)
    if not cleaned or cleaned[0].isdigit():
        cleaned = f"_{cleaned}"
    return f"{prefix}{cleaned}"


def lp_number(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def lp_expression(
    coefficients: FeatureMap,
    variable_names: dict[str, str],
) -> str:
    terms: list[str] = []
    for feature in sorted(coefficients):
        coefficient = coefficients[feature]
        if coefficient == 0:
            continue
        variable = variable_names[feature]
        magnitude = abs(coefficient)
        atom = (
            variable
            if magnitude == 1
            else f"{lp_number(magnitude)} {variable}"
        )
        if not terms:
            terms.append(
                atom if coefficient > 0 else f"- {atom}"
            )
        else:
            terms.append(
                ("+ " if coefficient > 0 else "- ") + atom
            )
    return " ".join(terms) if terms else "0"


def export_lp(constraints: list[Constraint]) -> str:
    features = sorted(
        {
            feature
            for constraint in constraints
            for feature in constraint.coefficients
        }
    )
    variable_names = {
        feature: safe_name(feature, "w_")
        for feature in features
    }
    lines = ["Minimize", " obj: 0", "Subject To"]
    for index, constraint in enumerate(
        constraints,
        start=1,
    ):
        denominators = [constraint.rhs.denominator]
        denominators.extend(
            coefficient.denominator
            for coefficient in constraint.coefficients.values()
        )
        scale = lcm(*denominators)
        scaled_coefficients = {
            feature: coefficient * scale
            for feature, coefficient
            in constraint.coefficients.items()
        }
        scaled_rhs = constraint.rhs * scale
        assert scaled_rhs.denominator == 1
        assert all(
            value.denominator == 1
            for value in scaled_coefficients.values()
        )
        expression = lp_expression(
            scaled_coefficients,
            variable_names,
        )
        name = safe_name(
            constraint.name,
            f"c{index}_",
        )
        lines.append(
            f" {name}: {expression} >= {lp_number(scaled_rhs)}"
        )
    lines.append("Bounds")
    for feature in features:
        lines.append(
            f" {variable_names[feature]} >= 0"
        )
    lines.append("End")
    lines.append("")
    return "\n".join(lines)


def verify_weights(
    constraints: list[Constraint],
    weights: FeatureMap,
) -> tuple[bool, str]:
    unknown = sorted(
        set(weights)
        - {
            feature
            for constraint in constraints
            for feature in constraint.coefficients
        }
    )
    lines = []
    if unknown:
        lines.append(
            "unused_weights=" + ",".join(unknown)
        )

    valid = True
    minimum_slack: Fraction | None = None
    minimum_name = ""
    for constraint in constraints:
        slack = constraint.slack(weights)
        if minimum_slack is None or slack < minimum_slack:
            minimum_slack = slack
            minimum_name = constraint.name
        status = "PASS" if slack >= 0 else "FAIL"
        if slack < 0:
            valid = False
        lines.append(
            f"{status} {constraint.name} slack={slack}"
        )

    assert minimum_slack is not None
    lines.append(
        f"minimum_slack={minimum_slack} at={minimum_name}"
    )
    lines.append(f"constraints={len(constraints)}")
    lines.append(f"features={len(weights)}")
    lines.append(
        "result=" + ("FEASIBLE" if valid else "INFEASIBLE")
    )
    return valid, "\n".join(lines)


def self_test() -> None:
    rows = [
        {
            "name": "branch-aggregate",
            "debt": "3",
            "parent": {
                "radius_deficit": "5",
                "support_holes": "3",
            },
            "children": [
                {
                    "features": {
                        "radius_deficit": "1",
                        "support_holes": "1",
                    },
                    "multiplicity": 2,
                }
            ],
        },
        {
            "name": "error-allowance",
            "debt": "5/2",
            "error": "1/2",
            "parent": {"radius_deficit": "4"},
            "children": [
                {
                    "features": {
                        "radius_deficit": "2"
                    }
                }
            ],
        },
    ]
    constraints = [
        parse_constraint(row, index + 1)
        for index, row in enumerate(rows)
    ]
    weights = {
        "radius_deficit": Fraction(1),
        "support_holes": Fraction(1),
    }
    valid, report = verify_weights(
        constraints,
        weights,
    )
    assert valid
    assert "minimum_slack=0" in report
    lp = export_lp(constraints)
    assert "w_radius_deficit" in lp
    assert "w_support_holes" in lp
    assert "Subject To" in lp


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    export = subparsers.add_parser(
        "export",
        help="export exact constraints as CPLEX LP",
    )
    export.add_argument("input", type=Path)
    export.add_argument("output", type=Path)

    verify = subparsers.add_parser(
        "verify",
        help="verify nonnegative weights exactly",
    )
    verify.add_argument("input", type=Path)
    verify.add_argument("weights", type=Path)

    subparsers.add_parser(
        "self-test",
        help="run exact internal regression checks",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.command == "self-test":
        self_test()
        print(
            "verified: exact branching-reserve LP exporter "
            "and weight checker"
        )
        return 0

    constraints = load_constraints(args.input)
    if args.command == "export":
        args.output.write_text(
            export_lp(constraints),
            encoding="utf-8",
        )
        print(
            f"exported_constraints={len(constraints)}"
        )
        print(f"output={args.output}")
        return 0

    if args.command == "verify":
        weights = load_weights(args.weights)
        valid, report = verify_weights(
            constraints,
            weights,
        )
        print(report)
        return 0 if valid else 1

    raise AssertionError("unreachable")


if __name__ == "__main__":
    raise SystemExit(main())

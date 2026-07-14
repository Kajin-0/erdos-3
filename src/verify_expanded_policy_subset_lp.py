#!/usr/bin/env python3
"""Verify the expanded exact policy LP on the S1-S6 delay-subset lattice."""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

from branching_reserve_lp import export_lp, parse_constraint, verify_weights
from certified_contaminated_states import state_by_depth
from verify_two_coordinate_policy_family import (
    BASE_POLICIES,
    S7_EXTRA_POLICIES,
    REGENERATION_CHARGE,
    middle_fibers,
    policy_metrics,
    resolve_policy,
    fraction_text,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

SUBSET_STEPS = (5, 40, 30, 161, 142)
SUBSETS = tuple(
    subset
    for size in range(len(SUBSET_STEPS) + 1)
    for subset in combinations(SUBSET_STEPS, size)
)
CHOSEN = {
    1: "delay_none",
    2: "delay_5",
    3: "delay_5_161_142",
    4: "delay_5_40",
    5: "delay_5_40",
    6: "delay_5_40",
    7: "hybrid5",
}
WEIGHTS = {"lambda": Fraction(3), "gamma": Fraction(1, 10)}

EXPECTED_CONSTRAINTS = 198
EXPECTED_JSONL_BYTES = 417_334
EXPECTED_JSONL_SHA256 = "9181fd97362560cdb10001063df140b88465740f025620c3d2c4c92650d2d79f"
EXPECTED_LP_BYTES = 464_574
EXPECTED_LP_LINES = 206
EXPECTED_LP_SHA256 = "e1b0a00c2472110c9133cc79a844256211b5e0ed0e27c04acfc8f2a236026936"
EXPECTED_ACTIVE_COUNT = 47
EXPECTED_ACTIVE_SHA256 = "d6913498d788323c69bade7513294c758022f439108f535675cfe495c4814027"
STRICT_MINIMUM_NAME = "S3:delay_5_161_142<=delay_5_40"
STRICT_MINIMUM_HASH = "f63047846da4fbe9897d75156ec8ec2386709bc6a64d40c9305e7a03f7e2358c"
CERTIFICATE_SHA256 = "296e171145d54aed0425ffd14ea2065096106112c45094f0044e5962e3fe1829"


def policy_name(subset: tuple[int, ...]) -> str:
    if not subset:
        return "delay_none"
    return "delay_" + "_".join(map(str, subset))


def pairwise_harmonic(values: object) -> Fraction:
    terms = [Fraction(1, value) for value in values if value > 0]
    while len(terms) > 1:
        terms = [
            terms[index] + terms[index + 1]
            if index + 1 < len(terms)
            else terms[index]
            for index in range(0, len(terms), 2)
        ]
    return terms[0] if terms else Fraction()


def subset_metrics(depth: int, subset: tuple[int, ...]) -> dict[str, object]:
    state = state_by_depth(depth)
    selected, residual = resolve_policy(
        depth,
        frozenset(subset),
        False,
        False,
    )
    fibers = middle_fibers(selected)
    steps = set(fibers)
    return {
        "terminal_mass": pairwise_harmonic(steps),
        "occurrence_mass": sum(
            (pairwise_harmonic(values) for values in fibers.values()),
            Fraction(),
        ),
        "residual_error": Fraction(
            state.persistence * len(residual), state.scale
        ),
        "regeneration": False,
    }


def build_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for depth in range(1, 7):
        metrics = {
            policy_name(subset): subset_metrics(depth, subset)
            for subset in SUBSETS
        }
        chosen_name = CHOSEN[depth]
        chosen = metrics[chosen_name]
        for alternative_name in sorted(metrics):
            if alternative_name == chosen_name:
                continue
            alternative = metrics[alternative_name]
            delta_terminal = alternative["terminal_mass"] - chosen["terminal_mass"]
            delta_occurrence = alternative["occurrence_mass"] - chosen["occurrence_mass"]
            delta_error = alternative["residual_error"] - chosen["residual_error"]
            rows.append(
                {
                    "name": f"S{depth}:{chosen_name}<={alternative_name}",
                    "debt": fraction_text(-(delta_terminal + delta_error)),
                    "parent": {
                        "gamma": "0/1",
                        "lambda": fraction_text(delta_occurrence),
                    },
                    "children": [],
                }
            )

    policies7 = dict(BASE_POLICIES)
    policies7.update(S7_EXTRA_POLICIES)
    metrics7 = {
        name: policy_metrics(7, *arguments)
        for name, arguments in policies7.items()
    }
    chosen7 = metrics7[CHOSEN[7]]
    for alternative_name in sorted(metrics7):
        if alternative_name == CHOSEN[7]:
            continue
        alternative = metrics7[alternative_name]
        delta_terminal = alternative["terminal_mass"] - chosen7["terminal_mass"]
        delta_occurrence = alternative["occurrence_mass"] - chosen7["occurrence_mass"]
        delta_error = alternative["residual_error"] - chosen7["residual_error"]
        delta_regeneration = (
            REGENERATION_CHARGE
            if alternative["regeneration"]
            else Fraction()
        )
        rows.append(
            {
                "name": f"S7:{CHOSEN[7]}<={alternative_name}",
                "debt": fraction_text(-(delta_terminal + delta_error)),
                "parent": {
                    "gamma": fraction_text(delta_regeneration),
                    "lambda": fraction_text(delta_occurrence),
                },
                "children": [],
            }
        )
    return rows


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def build_certificate() -> str:
    rows = build_rows()
    if len(rows) != EXPECTED_CONSTRAINTS:
        raise AssertionError(f"constraint count mismatch: {len(rows)}")

    jsonl = "".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
        for row in rows
    )
    jsonl_bytes = len(jsonl.encode("utf-8"))
    jsonl_hash = hashlib.sha256(jsonl.encode("utf-8")).hexdigest()
    if jsonl_bytes != EXPECTED_JSONL_BYTES:
        raise AssertionError(f"JSONL byte-count mismatch: {jsonl_bytes}")
    if jsonl_hash != EXPECTED_JSONL_SHA256:
        raise AssertionError(f"JSONL hash mismatch: {jsonl_hash}")

    constraints = [
        parse_constraint(row, index)
        for index, row in enumerate(rows, start=1)
    ]
    valid, report = verify_weights(constraints, WEIGHTS)
    if not valid:
        raise AssertionError(report)

    slacks = [(constraint.slack(WEIGHTS), constraint.name) for constraint in constraints]
    active = tuple(name for slack, name in slacks if slack == 0)
    if len(active) != EXPECTED_ACTIVE_COUNT:
        raise AssertionError(f"active count mismatch: {len(active)}")
    active_payload = "\n".join(active) + "\n"
    active_hash = hashlib.sha256(active_payload.encode("utf-8")).hexdigest()
    if active_hash != EXPECTED_ACTIVE_SHA256:
        raise AssertionError(f"active hash mismatch: {active_hash}")

    strict_slack, strict_name = min(
        (slack, name) for slack, name in slacks if slack > 0
    )
    if strict_name != STRICT_MINIMUM_NAME:
        raise AssertionError(f"strict minimum mismatch: {strict_name}")
    if fraction_hash(strict_slack) != STRICT_MINIMUM_HASH:
        raise AssertionError("strict minimum hash mismatch")

    lp = export_lp(constraints)
    lp_bytes = len(lp.encode("utf-8"))
    lp_lines = len(lp.splitlines())
    lp_hash = hashlib.sha256(lp.encode("utf-8")).hexdigest()
    if lp_bytes != EXPECTED_LP_BYTES:
        raise AssertionError(f"LP byte-count mismatch: {lp_bytes}")
    if lp_lines != EXPECTED_LP_LINES:
        raise AssertionError(f"LP line-count mismatch: {lp_lines}")
    if lp_hash != EXPECTED_LP_SHA256:
        raise AssertionError(f"LP hash mismatch: {lp_hash}")

    lines = [
        "EXPANDED POLICY SUBSET-LATTICE LP",
        "",
        "subset_steps=5,40,30,161,142",
        "subsets_per_state_S1_S6=32",
        "S7_policy_family=current_13_policy_family",
        "features=lambda,gamma",
        "weights=lambda:3,gamma:1/10",
        f"constraints={len(constraints)}",
        f"jsonl_bytes={jsonl_bytes}",
        f"jsonl_sha256={jsonl_hash}",
        f"lp_bytes={lp_bytes}",
        f"lp_lines={lp_lines}",
        f"lp_sha256={lp_hash}",
        "",
        "result=FEASIBLE",
        f"active_equalities={len(active)}",
        f"active_equalities_sha256={active_hash}",
        f"strict_minimum_constraint={strict_name}",
        f"strict_minimum_slack_sha256={STRICT_MINIMUM_HASH}",
        f"strict_minimum_slack_numerator_digits={len(str(strict_slack.numerator))}",
        f"strict_minimum_slack_denominator_digits={len(str(strict_slack.denominator))}",
        "",
        "S1_chosen=delay_none",
        "S2_chosen=delay_5",
        "S3_chosen=delay_5_161_142",
        "S4_chosen=delay_5_40",
        "S5_chosen=delay_5_40",
        "S6_chosen=delay_5_40",
        "S7_chosen=hybrid5",
        "",
        (
            "conclusion: the exact witness lambda=3,gamma=1/10 remains feasible "
            "after expanding S1 through S6 to all 32"
        ),
        (
            "subsets of delay steps {5,40,30,161,142}. The expansion changes the "
            "unique S3 optimum to delay {5,161,142}."
        ),
        (
            "This is a finite policy-ranking LP and still does not encode retained "
            "simultaneous Bellman children."
        ),
        "",
    ]
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate


def main() -> int:
    if len(sys.argv) > 2:
        raise SystemExit("usage: verify_expanded_policy_subset_lp.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + hashlib.sha256(certificate.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

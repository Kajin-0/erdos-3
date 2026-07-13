#!/usr/bin/env python3
"""Export and verify the exact two-coordinate policy half-space system."""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from branching_reserve_lp import export_lp, parse_constraint, verify_weights
from verify_two_coordinate_policy_family import (
    BASE_POLICIES,
    S7_EXTRA_POLICIES,
    policy_metrics,
    fraction_text,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

CHOSEN = {
    1: "lex",
    2: "step5",
    3: "step540",
    4: "step540",
    5: "step540",
    6: "step540",
    7: "hybrid5",
}
WEIGHTS = {"lambda": Fraction(3), "gamma": Fraction(1, 10)}
REGENERATION_CHARGE = Fraction(36_953, 4_096)

EXPECTED_CONSTRAINTS = 60
EXPECTED_JSONL_BYTES = 293_294
EXPECTED_JSONL_SHA256 = "6e2aa22f5214450062e3805c883687a9fee55ff87ed998d65802db46a07bd89b"
EXPECTED_LP_BYTES = 348_333
EXPECTED_LP_LINES = 68
EXPECTED_LP_SHA256 = "62d24dd40f69e87d627d12b1a69645153903c2915895d44f6070cffe0d649667"
EXPECTED_ACTIVE = (
    "S1:lex<=q142",
    "S1:lex<=q161",
    "S1:lex<=q30",
    "S1:lex<=q40",
    "S1:lex<=step5",
    "S1:lex<=step540",
    "S1:lex<=step54030",
    "S2:step5<=step540",
)
STRICT_MINIMUM_NAME = "S1:lex<=reverse"
STRICT_MINIMUM_HASH = "496cf601dff1b45d679d3b660ec70a7a97de1503fbe13272de83a9fa7fb9a830"
S7_BOUNDARY_NAME = "S7:hybrid5<=step540"
S7_BOUNDARY_HASH = "f7aaa21925e0b9eba07695a3a189d0172914d6f431ff274ff0819b8d817d03f7"
CERTIFICATE_SHA256 = "7721d5c933fa04b3a2d9efec2ea29f1d0ebc540df6a602d78323bd390eb279d1"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def build_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for depth in range(1, 8):
        policies = dict(BASE_POLICIES)
        if depth == 7:
            policies.update(S7_EXTRA_POLICIES)
        metrics = {
            name: policy_metrics(depth, *arguments)
            for name, arguments in policies.items()
        }
        chosen_name = CHOSEN[depth]
        chosen = metrics[chosen_name]
        for alternative_name in sorted(policies):
            if alternative_name == chosen_name:
                continue
            alternative = metrics[alternative_name]
            delta_terminal = (
                alternative["terminal_mass"] - chosen["terminal_mass"]
            )
            delta_occurrence = (
                alternative["occurrence_mass"] - chosen["occurrence_mass"]
            )
            delta_error = (
                alternative["residual_error"] - chosen["residual_error"]
            )
            delta_regeneration = (
                REGENERATION_CHARGE
                if alternative["regeneration"]
                else Fraction()
            ) - (
                REGENERATION_CHARGE
                if chosen["regeneration"]
                else Fraction()
            )
            rows.append(
                {
                    "name": f"S{depth}:{chosen_name}<={alternative_name}",
                    "debt": fraction_text(-(delta_terminal + delta_error)),
                    "parent": {
                        "gamma": fraction_text(delta_regeneration),
                        "lambda": fraction_text(delta_occurrence),
                    },
                    "children": [],
                }
            )
    return rows


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
    if "minimum_slack=0 at=S1:lex<=q142" not in report:
        raise AssertionError("unexpected minimum-slack constraint")

    slacks = [(constraint.slack(WEIGHTS), constraint.name) for constraint in constraints]
    active = tuple(name for slack, name in slacks if slack == 0)
    if active != EXPECTED_ACTIVE:
        raise AssertionError(f"active equality mismatch: {active!r}")

    strict_slack, strict_name = min(
        (slack, name) for slack, name in slacks if slack > 0
    )
    if strict_name != STRICT_MINIMUM_NAME:
        raise AssertionError(f"strict minimum mismatch: {strict_name}")
    if fraction_hash(strict_slack) != STRICT_MINIMUM_HASH:
        raise AssertionError("strict minimum hash mismatch")

    s7_boundary = next(
        slack for slack, name in slacks if name == S7_BOUNDARY_NAME
    )
    if fraction_hash(s7_boundary) != S7_BOUNDARY_HASH:
        raise AssertionError("S7 boundary hash mismatch")

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
        "TWO-COORDINATE POLICY HALFSPACE LP",
        "",
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
        "minimum_slack=0",
        "minimum_constraint=S1:lex<=q142",
        "active_equalities=" + ",".join(active),
        f"strict_minimum_constraint={strict_name}",
        f"strict_minimum_slack_sha256={STRICT_MINIMUM_HASH}",
        f"strict_minimum_slack_numerator_digits={len(str(strict_slack.numerator))}",
        f"strict_minimum_slack_denominator_digits={len(str(strict_slack.denominator))}",
        f"S7_hybrid5_vs_step540_slack_sha256={S7_BOUNDARY_HASH}",
        f"S7_hybrid5_vs_step540_slack_numerator_digits={len(str(s7_boundary.numerator))}",
        f"S7_hybrid5_vs_step540_slack_denominator_digits={len(str(s7_boundary.denominator))}",
        "",
        (
            "conclusion: all 60 exact policy-comparison half-spaces are feasible "
            "at lambda=3 and gamma=1/10."
        ),
        (
            "The active equalities are S1 policy ties and the S2 step5/step540 "
            "tie. The smallest strict margin is"
        ),
        (
            "S1 lexicographic versus reverse; the active S7 continuation boundary "
            "is hybrid5 versus step540. This is an exact finite policy LP, not a "
            "retained-child Bellman LP."
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
        raise SystemExit("usage: verify_policy_halfspace_lp.py [OUTPUT]")
    certificate = build_certificate()
    if len(sys.argv) == 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + hashlib.sha256(certificate.encode("utf-8")).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Certify terminal-current absorption of S7 retained row-star branching."""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys

from probe_residual_sponsor_backbone_split import (
    affine_reference,
    build_split_occurrences,
    pair_weight,
    retain_occurrences,
)
from probe_sponsor_pair_transport_frontier import reconstruct_fourth_recursive, serialize_mass
from verify_retained_terminal_split import contains_three_term_ap

Pair = tuple[int, int]
Resource = tuple[int, int, int]


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate retained parent resource")
    return (left, right) if left < right else (right, left)


def canonical_hash(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit(
            "usage: probe_s7_terminal_current_branch_absorption.py OUTPUT_JSON"
        )

    parents = reconstruct_fourth_recursive()
    retained, metrics = retain_occurrences(build_split_occurrences(parents))
    if metrics["retained_states"] != 37:
        raise AssertionError("certified split retained frontier changed")

    owners: dict[Resource, list[dict[str, object]]] = defaultdict(list)
    state_rows: dict[int, dict[str, object]] = {}

    for state in retained:
        parent_class = int(state.representative.parent_class)
        reference = affine_reference(state)
        values = tuple(int(value) for value in state.values)
        roots = tuple(int(root) for root in state.representative.provenance)
        terminal = not contains_three_term_ap(values)
        source = str(state.representative.source)
        state_rows[state.index] = {
            "state_index": state.index,
            "parent_class": parent_class,
            "reference": reference,
            "values": values,
            "roots": roots,
            "terminal": terminal,
            "source": source,
        }

        for value, root in zip(values, roots, strict=True):
            pair = ordered_pair(reference, root)
            if pair[1] - pair[0] != value:
                raise AssertionError("terminal absorption current gap mismatch")
            resource = (parent_class, pair[0], pair[1])
            owners[resource].append(
                {
                    "state_index": state.index,
                    "reference": reference,
                    "child_pair": (0, value),
                    "resource_kind": "current",
                    "terminal": terminal,
                    "source": source,
                }
            )

        if terminal:
            continue
        for first, second in combinations(range(len(values)), 2):
            root_pair = ordered_pair(roots[first], roots[second])
            child_pair = ordered_pair(values[first], values[second])
            if root_pair[1] - root_pair[0] != child_pair[1] - child_pair[0]:
                raise AssertionError("terminal absorption latent gap mismatch")
            resource = (parent_class, root_pair[0], root_pair[1])
            owners[resource].append(
                {
                    "state_index": state.index,
                    "reference": reference,
                    "child_pair": child_pair,
                    "resource_kind": "latent",
                    "terminal": False,
                    "source": source,
                }
            )

    repeated = {resource: rows for resource, rows in owners.items() if len(rows) > 1}
    branching_mass = Fraction()
    terminal_covered_mass = Fraction()
    residual_mass = Fraction()
    covered_terminal_states: set[int] = set()
    repeated_rows: list[dict[str, object]] = []

    for resource, rows in sorted(repeated.items()):
        parent_class, left, right = resource
        gap = right - left
        excess_copies = len(rows) - 1
        terminal_current = [
            row
            for row in rows
            if bool(row["terminal"]) and row["resource_kind"] == "current"
        ]
        if len(terminal_current) > 1:
            raise AssertionError("one repeated resource has multiple terminal current owners")
        covered = 1 if terminal_current and excess_copies else 0
        branching_mass += Fraction(excess_copies, gap)
        terminal_covered_mass += Fraction(covered, gap)
        residual_mass += Fraction(excess_copies - covered, gap)
        if terminal_current:
            covered_terminal_states.add(int(terminal_current[0]["state_index"]))

        repeated_rows.append(
            {
                "resource": resource,
                "gap": gap,
                "multiplicity": len(rows),
                "terminal_current_covered": bool(covered),
                "owners": sorted(
                    rows,
                    key=lambda row: (
                        int(row["state_index"]),
                        str(row["resource_kind"]),
                    ),
                ),
            }
        )

    terminal_state_rows = [state_rows[index] for index in sorted(covered_terminal_states)]
    covered_terminal_state_mass = sum(
        (
            sum((Fraction(1, value) for value in row["values"]), Fraction())
            for row in terminal_state_rows
        ),
        Fraction(),
    )
    covered_terminal_current_mass = sum(
        (
            pair_weight((resource[1], resource[2]))
            for resource, rows in repeated.items()
            if any(
                bool(row["terminal"]) and row["resource_kind"] == "current"
                for row in rows
            )
        ),
        Fraction(),
    )

    expected_resources = [
        (65, 1455716, 1455863),
        (65, 1455716, 1455868),
        (65, 1455716, 1455869),
    ]
    if sorted(repeated) != expected_resources:
        raise AssertionError("S7 repeated parent-resource identity changed")
    if any(len(rows) != 2 for rows in repeated.values()):
        raise AssertionError("S7 repeated resource degree changed")
    if branching_mass != Fraction(22697, 1139544):
        raise AssertionError("S7 branching excess changed")
    if terminal_covered_mass != branching_mass or residual_mass:
        raise AssertionError("S7 terminal-current absorption no longer closes branching")
    if len(terminal_state_rows) != 1:
        raise AssertionError("S7 terminal coverage no longer uses one state")
    terminal_state = terminal_state_rows[0]
    if tuple(terminal_state["values"]) != (147, 152, 153):
        raise AssertionError("S7 covering terminal state changed")
    if covered_terminal_state_mass != branching_mass:
        raise AssertionError("covering terminal state mass differs from branching excess")
    if covered_terminal_current_mass != branching_mass:
        raise AssertionError("covered terminal current terms differ from branching excess")

    owner_profiles = defaultdict(int)
    for rows in repeated.values():
        profile = tuple(
            sorted(
                (
                    "terminal" if bool(row["terminal"]) else "recursive",
                    str(row["resource_kind"]),
                    str(row["source"]),
                )
                for row in rows
            )
        )
        owner_profiles[profile] += 1

    output = {
        "schema": "s7_terminal_current_branch_absorption_v1",
        "scope": "certified residual-sponsor split R4-to-F5 retained family",
        "generation_six_propagated": False,
        "counts": {
            "retained_states": len(retained),
            "parent_resources": len(owners),
            "repeated_parent_resources": len(repeated),
            "terminal_covered_resources": sum(
                any(
                    bool(row["terminal"]) and row["resource_kind"] == "current"
                    for row in rows
                )
                for rows in repeated.values()
            ),
            "covered_terminal_states": len(terminal_state_rows),
            "uncovered_excess_copies": 0,
        },
        "masses": {
            "branching_excess": serialize_mass(branching_mass),
            "terminal_covered_branching_mass": serialize_mass(terminal_covered_mass),
            "residual_branching_mass": serialize_mass(residual_mass),
            "covering_terminal_state_mass": serialize_mass(covered_terminal_state_mass),
            "covered_terminal_current_mass": serialize_mass(
                covered_terminal_current_mass
            ),
        },
        "covering_terminal_states": terminal_state_rows,
        "repeated_resources": repeated_rows,
        "owner_profiles": [
            {"profile": profile, "resources": count}
            for profile, count in sorted(owner_profiles.items())
        ],
        "checks": {
            "all_repeated_resources_terminal_covered": (
                terminal_covered_mass == branching_mass
            ),
            "zero_residual_branching": residual_mass == 0,
            "terminal_state_mass_identity": (
                covered_terminal_state_mass == branching_mass
            ),
            "terminal_current_injection": (
                covered_terminal_current_mass == terminal_covered_mass
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    Path(sys.argv[1]).write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

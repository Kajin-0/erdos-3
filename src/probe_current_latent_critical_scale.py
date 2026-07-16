#!/usr/bin/env python3
"""Test exact critical-scale packing of current-latent repeated resources."""
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
    retain_occurrences,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap


def ordered_pair(a: int, b: int) -> tuple[int, int]:
    if a == b:
        raise AssertionError("degenerate critical-scale resource")
    return (a, b) if a < b else (b, a)


def shell_base(values: tuple[int, ...]) -> int:
    if not values or min(values) <= 0:
        raise AssertionError("critical-scale state is not positive")
    base = 1 << (min(values).bit_length() - 1)
    if any(value < base or value >= 2 * base for value in values):
        raise AssertionError(f"state crosses its standard dyadic shell: {values}")
    return base


def fraction_row(value: Fraction) -> dict[str, str]:
    return {"fraction": str(value), "decimal": f"{float(value):.15f}"}


def transition_profile(name: str, parents: tuple[object, ...], children: tuple[object, ...]) -> dict[str, object]:
    parent_by_index = {int(parent.index): parent for parent in parents}
    owners: dict[tuple[int, int, int], list[dict[str, object]]] = defaultdict(list)

    for child in children:
        parent_class = int(child.representative.parent_class)
        if parent_class not in parent_by_index:
            raise AssertionError(f"{name}: child references unknown parent")
        values = tuple(int(value) for value in child.values)
        roots = tuple(int(root) for root in child.representative.provenance)
        reference = affine_reference(child)
        child_base = shell_base(values)
        terminal = not contains_three_term_ap(values)
        source = str(child.representative.source)

        for value, root in zip(values, roots, strict=True):
            pair = ordered_pair(reference, root)
            if pair[1] - pair[0] != value:
                raise AssertionError(f"{name}: current gap mismatch")
            owners[(parent_class, pair[0], pair[1])].append({
                "kind": "current", "state_index": int(child.index),
                "scale": child_base, "terminal": terminal,
                "source": source, "reference": reference,
            })

        if terminal:
            continue
        for i, j in combinations(range(len(values)), 2):
            pair = ordered_pair(roots[i], roots[j])
            child_pair = ordered_pair(values[i], values[j])
            if pair[1] - pair[0] != child_pair[1] - child_pair[0]:
                raise AssertionError(f"{name}: latent gap mismatch")
            owners[(parent_class, pair[0], pair[1])].append({
                "kind": "latent", "state_index": int(child.index),
                "scale": child_base, "terminal": False,
                "source": source, "reference": reference,
            })

    rows: list[dict[str, object]] = []
    maximum_ratio = Fraction()
    failures = 0
    recursive_current_rows = 0
    terminal_current_rows = 0

    for resource, resource_owners in sorted(owners.items()):
        current = [row for row in resource_owners if row["kind"] == "current"]
        latent = [row for row in resource_owners if row["kind"] == "latent"]
        if not current or not latent:
            continue
        if len(current) != 1 or len(latent) != 1:
            raise AssertionError(f"{name}: current-latent profile is not degree two")

        parent_class, left, right = resource
        parent = parent_by_index[parent_class]
        parent_values = tuple(int(value) for value in parent.values)
        parent_base = shell_base(parent_values)
        gap = right - left
        current_base = int(current[0]["scale"])
        latent_base = int(latent[0]["scale"])
        lhs = current_base + 2 * latent_base
        ratio = Fraction(lhs, parent_base)
        maximum_ratio = max(maximum_ratio, ratio)
        holds = lhs <= parent_base
        failures += not holds
        terminal_current_rows += bool(current[0]["terminal"])
        recursive_current_rows += not bool(current[0]["terminal"])

        if current_base > gap:
            raise AssertionError(f"{name}: current shell base exceeds current label")
        if gap >= latent_base:
            raise AssertionError(f"{name}: latent pair spans its full shell")

        rows.append({
            "resource": resource, "gap": gap,
            "parent_base": parent_base,
            "current_base": current_base,
            "latent_base": latent_base,
            "combined_scale": lhs,
            "ratio": fraction_row(ratio),
            "holds": holds,
            "current_owner": current[0],
            "latent_owner": latent[0],
        })

    return {
        "name": name,
        "counts": {
            "current_latent_resources": len(rows),
            "terminal_current_resources": terminal_current_rows,
            "recursive_current_resources": recursive_current_rows,
            "failed_resources": failures,
        },
        "maximum_ratio": fraction_row(maximum_ratio),
        "maximum_rows": [row for row in rows if Fraction(row["ratio"]["fraction"]) == maximum_ratio],
        "rows_hash": hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest(),
    }


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: probe_current_latent_critical_scale.py OUTPUT_JSON")

    retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(state for state in retained_second if contains_three_term_ap(state.values))
    _o3, retained_third, _m3, _r3 = propagate_recursive_states(recursive_second)
    recursive_third = tuple(state for state in retained_third if contains_three_term_ap(state.values))
    _o4, retained_fourth, _m4, _r4 = propagate_recursive_states(recursive_third)
    recursive_fourth = tuple(state for state in retained_fourth if contains_three_term_ap(state.values))
    retained_fifth, metrics = retain_occurrences(build_split_occurrences(recursive_fourth))
    if metrics["retained_states"] != 37:
        raise AssertionError("split fifth retained frontier changed")

    transitions = [
        transition_profile("historical_F1_to_F2", retained_first, retained_second),
        transition_profile("R2_to_F3", recursive_second, retained_third),
        transition_profile("R3_to_F4", recursive_third, retained_fourth),
        transition_profile("R4_to_F5_split", recursive_fourth, retained_fifth),
    ]
    total_rows = sum(int(row["counts"]["current_latent_resources"]) for row in transitions)
    failures = sum(int(row["counts"]["failed_resources"]) for row in transitions)
    maximum_ratio = max((Fraction(row["maximum_ratio"]["fraction"]) for row in transitions), default=Fraction())

    output = {
        "schema": "current_latent_critical_scale_v1",
        "scope": "four certified point-disjoint retained transitions; first is historical pre-terminal-stopping",
        "generation_six_propagated": False,
        "counts": {"resources": total_rows, "failures": failures},
        "maximum_ratio": fraction_row(maximum_ratio),
        "transitions": transitions,
        "checks": {
            "current_base_at_most_resource_gap": True,
            "latent_gap_strictly_below_latent_shell_base": True,
            "combined_current_latent_scale_at_most_parent": failures == 0,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    Path(sys.argv[1]).write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0 if failures == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Certify affine root-reference pivot structure at the R4->R5 frontier.

For a retained state, test whether every current point has the form

    u = p - r

for one common original-root reference r. For a minimum-anchor root a, a
backbone step should update the reference r -> a and send every recursive
survivor root p to

    u' = p - a.

This exposes the exact root-pivot geometry underlying the recorded harmonic
interval gains.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import sys

from probe_root_lineage_transfer_classification import (
    canonical_hash,
    serialize_mass,
    state_point_records,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    recursive_second = tuple(
        state for state in retained_second if contains_three_term_ap(state.values)
    )
    _occ3, retained_third, _metrics3, _rows3 = propagate_recursive_states(
        recursive_second
    )
    recursive_third = tuple(
        state for state in retained_third if contains_three_term_ap(state.values)
    )
    _occ4, retained_fourth, _metrics4, _rows4 = propagate_recursive_states(
        recursive_third
    )
    recursive_fourth = tuple(
        state for state in retained_fourth if contains_three_term_ap(state.values)
    )
    _occ5, retained_fifth, _metrics5, _rows5 = propagate_recursive_states(
        recursive_fourth
    )
    recursive_fifth = tuple(
        state for state in retained_fifth if contains_three_term_ap(state.values)
    )
    terminal_fifth = tuple(
        state for state in retained_fifth if not contains_three_term_ap(state.values)
    )

    first_root_universe = {
        root
        for state in retained_first
        for root in state.representative.provenance
    }
    points5r = state_point_records(recursive_fifth, require_unique_roots=True)
    points5t = state_point_records(terminal_fifth, require_unique_roots=True)
    roots5r = set(points5r)
    roots5t = set(points5t)

    state_rows: list[dict[str, object]] = []
    survivor_rows: list[dict[str, object]] = []
    references: list[int] = []
    anchors: list[int] = []
    gain = Fraction()

    for state in sorted(recursive_fourth, key=lambda item: item.index):
        values = tuple(state.values)
        representative = state.representative
        roots = tuple(representative.provenance)
        if len(values) != len(roots):
            raise AssertionError("point/provenance length mismatch")
        if len(set(roots)) != len(roots):
            raise AssertionError("R4 parent root repeated")

        offsets = {root - current for current, root in zip(values, roots, strict=True)}
        if len(offsets) != 1:
            raise AssertionError(f"parent class {state.index} is not affine")
        reference = next(iter(offsets))
        references.append(reference)

        minimum = min(values)
        anchor_position = values.index(minimum)
        anchor_root = roots[anchor_position]
        anchors.append(anchor_root)
        if anchor_root - reference != minimum:
            raise AssertionError("anchor/reference identity failed")
        if reference >= anchor_root:
            raise AssertionError("reference is not below anchor")
        if reference not in first_root_universe:
            raise AssertionError("reference is not an original first-frontier root")

        parent_roots = set(roots)
        surviving = parent_roots & roots5r
        terminalized = (parent_roots - surviving) & roots5t
        dropped = parent_roots - surviving - roots5t
        local_gain = Fraction()
        local_rows: list[dict[str, object]] = []

        point_by_root = {
            root: current for current, root in zip(values, roots, strict=True)
        }
        for root in sorted(surviving):
            parent_current = point_by_root[root]
            child = points5r[root][0]
            child_current = int(child["current"])
            if child["parent_class"] != state.index:
                raise AssertionError("survivor parent class mismatch")
            if child["source"] != "backbone":
                raise AssertionError("non-backbone survivor")
            if child["immediate"] != parent_current:
                raise AssertionError("immediate provenance mismatch")
            if parent_current != root - reference:
                raise AssertionError("parent affine identity failed")
            if child_current != root - anchor_root:
                raise AssertionError("child pivot identity failed")
            if not reference < anchor_root < root:
                raise AssertionError("root pivot order failed")
            if parent_current - child_current != minimum:
                raise AssertionError("translation length mismatch")

            interval_gain = Fraction(1, child_current) - Fraction(1, parent_current)
            algebraic_gain = Fraction(
                anchor_root - reference,
                (root - anchor_root) * (root - reference),
            )
            if interval_gain != algebraic_gain:
                raise AssertionError("pivot gain identity failed")
            local_gain += interval_gain
            survivor_row = {
                "root": root,
                "reference_root": reference,
                "anchor_root": anchor_root,
                "parent_current": parent_current,
                "child_current": child_current,
                "translation": minimum,
                "interval_gain": serialize_mass(interval_gain),
                "parent_state_class": state.index,
                "child_state_class": child["state_class"],
                "child_exponent": child["exponent"],
            }
            survivor_rows.append(survivor_row)
            local_rows.append(survivor_row)

        state_rows.append(
            {
                "parent_state_class": state.index,
                "parent_size": len(values),
                "reference_root": reference,
                "reference_in_first_root_universe": reference in first_root_universe,
                "reference_active_in_parent": reference in parent_roots,
                "minimum": minimum,
                "anchor_root": anchor_root,
                "anchor_in_first_root_universe": anchor_root in first_root_universe,
                "anchor_active_in_fifth": anchor_root in roots5r or anchor_root in roots5t,
                "surviving_roots": len(surviving),
                "terminalized_roots": len(terminalized),
                "dropped_roots": len(dropped),
                "local_interval_gain": serialize_mass(local_gain),
                "survivor_rows_sha256": canonical_hash(local_rows),
            }
        )
        gain += local_gain

    if len(survivor_rows) != 1015:
        raise AssertionError("survivor count changed")
    if len(set(references)) != len(references):
        raise AssertionError("reference root reused across R4 parent states")
    if len(set(anchors)) != len(anchors):
        raise AssertionError("anchor root reused across R4 parent states")
    if set(references) & set(anchors):
        raise AssertionError("R4 reference and anchor sets overlap")

    output = {
        "schema": "affine_root_pivot_probe_v1",
        "scope": "certified_baseline_R4_to_R5_recursive_transition",
        "counts": {
            "parent_states": len(state_rows),
            "affine_parent_states": len(state_rows),
            "distinct_reference_roots": len(set(references)),
            "reference_roots_in_first_root_universe": sum(
                row["reference_in_first_root_universe"] for row in state_rows
            ),
            "reference_roots_active_in_parent": sum(
                row["reference_active_in_parent"] for row in state_rows
            ),
            "distinct_anchor_roots": len(set(anchors)),
            "anchor_roots_in_first_root_universe": sum(
                row["anchor_in_first_root_universe"] for row in state_rows
            ),
            "anchor_roots_active_in_fifth": sum(
                row["anchor_active_in_fifth"] for row in state_rows
            ),
            "survivor_pivot_identities": len(survivor_rows),
        },
        "total_interval_gain": serialize_mass(gain),
        "state_rows": state_rows,
        "top_survivor_intervals": sorted(
            survivor_rows,
            key=lambda row: (
                -Fraction(row["interval_gain"]["fraction"]),
                row["root"],
            ),
        )[:25],
        "hashes": {
            "state_rows": canonical_hash(state_rows),
            "survivor_rows": canonical_hash(survivor_rows),
            "reference_roots": canonical_hash(sorted(references)),
            "anchor_roots": canonical_hash(sorted(anchors)),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

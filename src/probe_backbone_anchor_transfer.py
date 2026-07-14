#!/usr/bin/env python3
r"""Classify fourth-to-fifth transfer by the twelve recursive parent states.

The first root-lineage classification proved that every surviving root continues
through a backbone occurrence. This probe makes the resulting minimum-
translation mechanism explicit. For each fourth-generation recursive state S
with m=min(S), it records:

    full translation reserve
      H(S-m) - H(S\{m})
      = sum_{u in S, u>m} (1/(u-m)-1/u),

the retained recursive survivor gain, all exiting parent release, the fate of
the minimum-anchor root, and the local recursive mass balance.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
import hashlib
import json
import sys

from probe_root_lineage_transfer_classification import (
    canonical_hash,
    harmonic,
    raw_point_records,
    serialize_mass,
    state_point_records,
)
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def value_hash(values: tuple[int, ...]) -> str:
    payload = ",".join(str(value) for value in values)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def ratio_mass(numerator: Fraction, denominator: Fraction) -> dict[str, str] | None:
    if denominator == 0:
        return None
    return serialize_mass(numerator / denominator)


def main() -> int:
    _retained_first, retained_second = reconstruct_retained_families()
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
    occurrences5, retained_fifth, metrics5, _rows5 = propagate_recursive_states(
        recursive_fourth
    )
    terminal_fifth = tuple(
        state for state in retained_fifth if not contains_three_term_ap(state.values)
    )
    recursive_fifth = tuple(
        state for state in retained_fifth if contains_three_term_ap(state.values)
    )

    points4 = state_point_records(recursive_fourth, require_unique_roots=True)
    points5r = state_point_records(recursive_fifth, require_unique_roots=True)
    points5t = state_point_records(terminal_fifth, require_unique_roots=True)
    raw5 = raw_point_records(occurrences5)

    roots5r = set(points5r)
    roots5t = set(points5t)
    rows: list[dict[str, object]] = []
    anchor_roots: list[int] = []

    for state in sorted(recursive_fourth, key=lambda item: item.index):
        values = tuple(state.values)
        representative = state.representative
        root_by_value = dict(zip(values, representative.provenance, strict=True))
        minimum = min(values)
        anchor_root = root_by_value[minimum]
        anchor_roots.append(anchor_root)
        parent_roots = set(representative.provenance)
        if len(parent_roots) != len(values):
            raise AssertionError("fourth-generation parent root is repeated")

        surviving = parent_roots & roots5r
        terminalized = (parent_roots - surviving) & roots5t
        dropped = parent_roots - surviving - roots5t
        if surviving & terminalized:
            raise AssertionError("root splits within parent state")

        survivor_parent_mass = sum(
            (Fraction(1, points4[root][0]["current"]) for root in surviving),
            Fraction(),
        )
        survivor_child_mass = sum(
            (Fraction(1, points5r[root][0]["current"]) for root in surviving),
            Fraction(),
        )
        survivor_gain = survivor_child_mass - survivor_parent_mass
        terminal_parent_release = sum(
            (Fraction(1, points4[root][0]["current"]) for root in terminalized),
            Fraction(),
        )
        dropped_parent_release = sum(
            (Fraction(1, points4[root][0]["current"]) for root in dropped),
            Fraction(),
        )
        exit_release = terminal_parent_release + dropped_parent_release
        parent_mass = harmonic(values)
        local_recursive_net = survivor_child_mass - parent_mass
        if survivor_gain - exit_release != local_recursive_net:
            raise AssertionError(f"local transfer identity failed for {state.index}")

        gap_values = tuple(value - minimum for value in values if value > minimum)
        full_backbone_mass = harmonic(gap_values)
        full_parent_nonanchor_mass = parent_mass - Fraction(1, minimum)
        full_translation_gain = full_backbone_mass - full_parent_nonanchor_mass
        direct_full_gain = sum(
            (
                Fraction(1, value - minimum) - Fraction(1, value)
                for value in values
                if value > minimum
            ),
            Fraction(),
        )
        if full_translation_gain != direct_full_gain:
            raise AssertionError("full translation reserve identity failed")

        shell_drop_counts = Counter()
        child_source_counts = Counter()
        survivor_rows: list[tuple[int, int, int, str, int | None]] = []
        for root in sorted(surviving):
            parent = points4[root][0]
            child = points5r[root][0]
            if child["source"] != "backbone":
                raise AssertionError("non-backbone survivor detected")
            if child["parent_class"] != state.index:
                raise AssertionError("survivor assigned to wrong parent class")
            if child["immediate"] != parent["current"]:
                raise AssertionError("survivor immediate provenance mismatch")
            shell_drop = (
                int(parent["current"]).bit_length()
                - int(child["current"]).bit_length()
            )
            shell_drop_counts[shell_drop] += 1
            child_source_counts[str(child["source"])] += 1
            survivor_rows.append(
                (
                    root,
                    int(parent["current"]),
                    int(child["current"]),
                    str(child["source"]),
                    child["source_step"],
                )
            )

        anchor_raw_rows = raw5.get(anchor_root, [])
        if anchor_root in surviving or anchor_root in terminalized:
            anchor_fate = "retained"
        elif anchor_raw_rows:
            anchor_fate = "dropped_with_raw_output"
        else:
            anchor_fate = "dropped_no_raw_output"

        terminal_child_mass = sum(
            (Fraction(1, points5t[root][0]["current"]) for root in terminalized),
            Fraction(),
        )
        row = {
            "parent_state_class": state.index,
            "parent_representative": representative.index,
            "parent_source": representative.source,
            "parent_source_step": representative.source_step,
            "parent_exponent": representative.exponent,
            "parent_size": len(values),
            "parent_values_sha256": value_hash(values),
            "minimum": minimum,
            "anchor_root": anchor_root,
            "anchor_fate": anchor_fate,
            "anchor_raw_occurrences": len(anchor_raw_rows),
            "anchor_release": serialize_mass(Fraction(1, minimum)),
            "smallest_gaps": list(gap_values[:12]),
            "gap_values_sha256": value_hash(gap_values),
            "full_backbone_points": len(gap_values),
            "full_backbone_mass": serialize_mass(full_backbone_mass),
            "full_translation_gain": serialize_mass(full_translation_gain),
            "full_gain_over_anchor_release": ratio_mass(
                full_translation_gain, Fraction(1, minimum)
            ),
            "surviving_roots": len(surviving),
            "terminalized_roots": len(terminalized),
            "dropped_roots": len(dropped),
            "survivor_parent_mass": serialize_mass(survivor_parent_mass),
            "survivor_child_mass": serialize_mass(survivor_child_mass),
            "survivor_gain": serialize_mass(survivor_gain),
            "survivor_gain_over_anchor_release": ratio_mass(
                survivor_gain, Fraction(1, minimum)
            ),
            "retained_gain_fraction_of_full_translation": ratio_mass(
                survivor_gain, full_translation_gain
            ),
            "terminal_parent_release": serialize_mass(terminal_parent_release),
            "dropped_parent_release": serialize_mass(dropped_parent_release),
            "exit_release": serialize_mass(exit_release),
            "terminal_child_mass": serialize_mass(terminal_child_mass),
            "parent_mass": serialize_mass(parent_mass),
            "local_recursive_net": serialize_mass(local_recursive_net),
            "recursive_child_over_parent": ratio_mass(
                survivor_child_mass, parent_mass
            ),
            "shell_drop_counts": {
                str(shell): count for shell, count in sorted(shell_drop_counts.items())
            },
            "child_source_counts": dict(sorted(child_source_counts.items())),
            "survivor_rows_sha256": canonical_hash(survivor_rows),
        }
        rows.append(row)

    if len(anchor_roots) != len(set(anchor_roots)):
        raise AssertionError("minimum anchor root reused across parent states")
    if any(row["anchor_fate"] != "dropped_no_raw_output" for row in rows):
        raise AssertionError("not every parent minimum is a no-output dropped anchor")

    total_parent_mass = sum(
        (Fraction(row["parent_mass"]["fraction"]) for row in rows), Fraction()
    )
    total_full_translation_gain = sum(
        (Fraction(row["full_translation_gain"]["fraction"]) for row in rows),
        Fraction(),
    )
    total_anchor_release = sum(
        (Fraction(row["anchor_release"]["fraction"]) for row in rows), Fraction()
    )
    total_survivor_gain = sum(
        (Fraction(row["survivor_gain"]["fraction"]) for row in rows), Fraction()
    )
    total_exit_release = sum(
        (Fraction(row["exit_release"]["fraction"]) for row in rows), Fraction()
    )
    total_recursive_net = sum(
        (Fraction(row["local_recursive_net"]["fraction"]) for row in rows),
        Fraction(),
    )
    recursive_mass5 = sum((state.weight for state in recursive_fifth), Fraction())
    if total_parent_mass != sum(
        (state.weight for state in recursive_fourth), Fraction()
    ):
        raise AssertionError("parent mass aggregation failed")
    if total_survivor_gain - total_exit_release != total_recursive_net:
        raise AssertionError("aggregated local identities failed")
    if recursive_mass5 - total_parent_mass != total_recursive_net:
        raise AssertionError("recursive mass aggregation failed")

    expanding_rows = [
        row for row in rows if Fraction(row["local_recursive_net"]["fraction"]) > 0
    ]
    contracting_rows = [
        row for row in rows if Fraction(row["local_recursive_net"]["fraction"]) < 0
    ]
    neutral_rows = [
        row for row in rows if Fraction(row["local_recursive_net"]["fraction"]) == 0
    ]
    rows_by_gain = sorted(
        rows,
        key=lambda row: (
            -Fraction(row["survivor_gain"]["fraction"]),
            int(row["parent_state_class"]),
        ),
    )
    top_three_gain = sum(
        (Fraction(row["survivor_gain"]["fraction"]) for row in rows_by_gain[:3]),
        Fraction(),
    )

    canonical_rows = [
        {
            key: row[key]
            for key in (
                "parent_state_class",
                "parent_source",
                "parent_source_step",
                "parent_exponent",
                "parent_size",
                "parent_values_sha256",
                "minimum",
                "anchor_root",
                "anchor_fate",
                "anchor_raw_occurrences",
                "smallest_gaps",
                "gap_values_sha256",
                "full_backbone_points",
                "full_translation_gain",
                "surviving_roots",
                "terminalized_roots",
                "dropped_roots",
                "survivor_gain",
                "exit_release",
                "local_recursive_net",
                "shell_drop_counts",
                "child_source_counts",
                "survivor_rows_sha256",
            )
        }
        for row in rows
    ]

    output = {
        "schema": "backbone_anchor_transfer_probe_v1",
        "scope": "certified_baseline_fourth_to_fifth_transition",
        "counts": {
            "parent_states": len(rows),
            "minimum_anchor_roots": len(anchor_roots),
            "minimum_anchors_dropped_no_raw_output": sum(
                row["anchor_fate"] == "dropped_no_raw_output" for row in rows
            ),
            "expanding_parent_states": len(expanding_rows),
            "contracting_parent_states": len(contracting_rows),
            "neutral_parent_states": len(neutral_rows),
        },
        "masses": {
            "parent_recursive_mass": serialize_mass(total_parent_mass),
            "full_translation_gain": serialize_mass(total_full_translation_gain),
            "minimum_anchor_release": serialize_mass(total_anchor_release),
            "retained_survivor_gain": serialize_mass(total_survivor_gain),
            "exit_release": serialize_mass(total_exit_release),
            "recursive_net": serialize_mass(total_recursive_net),
            "recursive_fifth_mass": serialize_mass(recursive_mass5),
        },
        "ratios": {
            "full_translation_gain_over_anchor_release": ratio_mass(
                total_full_translation_gain, total_anchor_release
            ),
            "retained_gain_over_anchor_release": ratio_mass(
                total_survivor_gain, total_anchor_release
            ),
            "retained_gain_fraction_of_full_translation": ratio_mass(
                total_survivor_gain, total_full_translation_gain
            ),
            "top_three_parent_gain_share": ratio_mass(
                top_three_gain, total_survivor_gain
            ),
        },
        "expanding_parent_classes": [
            int(row["parent_state_class"]) for row in expanding_rows
        ],
        "contracting_parent_classes": [
            int(row["parent_state_class"]) for row in contracting_rows
        ],
        "neutral_parent_classes": [
            int(row["parent_state_class"]) for row in neutral_rows
        ],
        "rows": rows,
        "hashes": {
            "parent_state_rows": canonical_hash(canonical_rows),
            "anchor_roots": canonical_hash(sorted(anchor_roots)),
            "expanding_parent_classes": canonical_hash(
                sorted(int(row["parent_state_class"]) for row in expanding_rows)
            ),
        },
        "metrics5": metrics5,
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

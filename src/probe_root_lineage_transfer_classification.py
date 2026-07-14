#!/usr/bin/env python3
"""Classify the certified fourth-to-fifth root-lineage transfer exactly.

This probe refines the exact identity

    H5_rec - H4_rec = survivor_scale_gain - exiting_parent_release

without fitting a potential.  It classifies the 1,015 surviving unique root
lineages and the 702 exiting roots by retained-state source, shell drop,
source-step valuations, parent class, and raw-output/retention fate.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import sys
from typing import Iterable

from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def fraction_hash(value: Fraction) -> str:
    return hashlib.sha256(fraction_text(value).encode("utf-8")).hexdigest()


def decimal_text(value: Fraction, places: int = 12) -> str:
    sign = "-" if value < 0 else ""
    value = abs(value)
    scale = 10**places
    rounded = (value.numerator * scale * 2 + value.denominator) // (
        2 * value.denominator
    )
    whole, fractional = divmod(rounded, scale)
    return f"{sign}{whole}.{fractional:0{places}d}"


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def valuation(value: int, prime: int) -> int:
    if value <= 0:
        raise ValueError("valuation requires a positive integer")
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def state_point_records(
    states: tuple[object, ...],
    *,
    require_unique_roots: bool,
) -> dict[int, list[dict[str, object]]]:
    records: dict[int, list[dict[str, object]]] = defaultdict(list)
    for state in states:
        representative = state.representative
        for current, root, immediate in zip(
            state.values,
            representative.provenance,
            representative.immediate_provenance,
            strict=True,
        ):
            records[root].append(
                {
                    "current": current,
                    "root": root,
                    "immediate": immediate,
                    "state_class": state.index,
                    "parent_class": representative.parent_class,
                    "source": representative.source,
                    "source_step": representative.source_step,
                    "exponent": representative.exponent,
                }
            )
    if require_unique_roots:
        repeated = {
            root: rows for root, rows in records.items() if len(rows) != 1
        }
        if repeated:
            raise AssertionError(
                f"expected unique root records, found {len(repeated)} repeated roots"
            )
    return dict(records)


def raw_point_records(
    occurrences: tuple[object, ...],
) -> dict[int, list[dict[str, object]]]:
    records: dict[int, list[dict[str, object]]] = defaultdict(list)
    for occurrence in occurrences:
        for current, root, immediate in zip(
            occurrence.values,
            occurrence.provenance,
            occurrence.immediate_provenance,
            strict=True,
        ):
            records[root].append(
                {
                    "current": current,
                    "root": root,
                    "immediate": immediate,
                    "occurrence_index": occurrence.index,
                    "parent_class": occurrence.parent_class,
                    "source": occurrence.source,
                    "source_step": occurrence.source_step,
                    "exponent": occurrence.exponent,
                }
            )
    for rows in records.values():
        rows.sort(
            key=lambda row: (
                int(row["current"]),
                int(row["occurrence_index"]),
                str(row["source"]),
                -1 if row["source_step"] is None else int(row["source_step"]),
            )
        )
    return dict(records)


def serialize_mass(value: Fraction) -> dict[str, str]:
    return {
        "fraction": fraction_text(value),
        "decimal": decimal_text(value),
        "sha256": fraction_hash(value),
    }


def survivor_group_record(
    key_names: tuple[str, ...],
    key: tuple[object, ...],
    rows: list[dict[str, object]],
) -> dict[str, object]:
    parent_mass = sum(
        (Fraction(1, int(row["parent_current"])) for row in rows), Fraction()
    )
    child_mass = sum(
        (Fraction(1, int(row["child_current"])) for row in rows), Fraction()
    )
    gain = child_mass - parent_mass
    return {
        **dict(zip(key_names, key, strict=True)),
        "count": len(rows),
        "parent_mass": serialize_mass(parent_mass),
        "child_mass": serialize_mass(child_mass),
        "gain": serialize_mass(gain),
    }


def exit_group_record(
    key_names: tuple[str, ...],
    key: tuple[object, ...],
    rows: list[dict[str, object]],
) -> dict[str, object]:
    release = sum(
        (Fraction(1, int(row["parent_current"])) for row in rows), Fraction()
    )
    return {
        **dict(zip(key_names, key, strict=True)),
        "count": len(rows),
        "parent_release": serialize_mass(release),
    }


def grouped_survivors(
    rows: list[dict[str, object]],
    key_names: tuple[str, ...],
) -> list[dict[str, object]]:
    groups: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[tuple(row[name] for name in key_names)].append(row)
    result = [
        survivor_group_record(key_names, key, group_rows)
        for key, group_rows in groups.items()
    ]
    result.sort(
        key=lambda record: (
            -Fraction(record["gain"]["fraction"]),
            tuple(str(record[name]) for name in key_names),
        )
    )
    return result


def grouped_exits(
    rows: list[dict[str, object]],
    key_names: tuple[str, ...],
) -> list[dict[str, object]]:
    groups: dict[tuple[object, ...], list[dict[str, object]]] = defaultdict(list)
    for row in rows:
        groups[tuple(row[name] for name in key_names)].append(row)
    result = [
        exit_group_record(key_names, key, group_rows)
        for key, group_rows in groups.items()
    ]
    result.sort(
        key=lambda record: (
            -Fraction(record["parent_release"]["fraction"]),
            tuple(str(record[name]) for name in key_names),
        )
    )
    return result


def harmonic(values: Iterable[int]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def main() -> int:
    retained_first, retained_second = reconstruct_retained_families()
    del retained_first
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

    roots4 = set(points4)
    roots5r = set(points5r)
    roots5t = set(points5t)
    if not roots5r <= roots4 or not roots5t <= roots4:
        raise AssertionError("fifth retained family introduced new root provenance")

    surviving = roots4 & roots5r
    terminalized = (roots4 - surviving) & roots5t
    dropped = roots4 - surviving - roots5t
    split = roots5r & roots5t
    if split:
        raise AssertionError("root splits between recursive and terminal output")

    retained_fifth_union = {
        value for state in retained_fifth for value in state.values
    }

    survivor_rows: list[dict[str, object]] = []
    for root in sorted(surviving):
        parent = points4[root][0]
        child = points5r[root][0]
        parent_current = int(parent["current"])
        child_current = int(child["current"])
        if int(child["immediate"]) != parent_current:
            raise AssertionError(
                f"immediate provenance mismatch for root {root}: "
                f"{child['immediate']} != {parent_current}"
            )
        if child_current > parent_current:
            raise AssertionError(
                f"surviving lineage expands numerically for root {root}"
            )
        source_step = child["source_step"]
        if source_step is None:
            v2_step = None
            v3_step = None
            side_parity = None
            middle_color = None
        else:
            source_step = int(source_step)
            v2_step = valuation(source_step, 2)
            v3_step = valuation(source_step, 3)
            side_parity = v2_step % 2
            middle_color = (v2_step - v3_step) % 3

        parent_exponent = parent_current.bit_length() - 1
        child_exponent = child_current.bit_length() - 1
        if int(parent["exponent"]) != parent_exponent:
            raise AssertionError("parent shell exponent mismatch")
        if int(child["exponent"]) != child_exponent:
            raise AssertionError("child shell exponent mismatch")

        gain = Fraction(1, child_current) - Fraction(1, parent_current)
        survivor_rows.append(
            {
                "root": root,
                "parent_current": parent_current,
                "child_current": child_current,
                "gain": fraction_text(gain),
                "parent_state_class": int(parent["state_class"]),
                "parent_source": str(parent["source"]),
                "parent_source_step": parent["source_step"],
                "parent_exponent": parent_exponent,
                "child_state_class": int(child["state_class"]),
                "child_parent_class": int(child["parent_class"]),
                "child_source": str(child["source"]),
                "child_source_step": source_step,
                "child_exponent": child_exponent,
                "shell_drop": parent_exponent - child_exponent,
                "v2_source_step": v2_step,
                "v3_source_step": v3_step,
                "side_parity": side_parity,
                "middle_color": middle_color,
                "immediate_matches_parent": True,
            }
        )

    survivor_gain = sum(
        (Fraction(row["gain"]) for row in survivor_rows), Fraction()
    )
    parent_survivor_mass = sum(
        (Fraction(1, int(row["parent_current"])) for row in survivor_rows),
        Fraction(),
    )
    child_survivor_mass = sum(
        (Fraction(1, int(row["child_current"])) for row in survivor_rows),
        Fraction(),
    )
    if child_survivor_mass - parent_survivor_mass != survivor_gain:
        raise AssertionError("survivor gain decomposition failed")

    exit_rows: list[dict[str, object]] = []
    for root in sorted(roots4 - surviving):
        parent = points4[root][0]
        parent_current = int(parent["current"])
        raw_rows = raw5.get(root, [])
        raw_labels = sorted({int(row["current"]) for row in raw_rows})
        retained_overlap_labels = sorted(set(raw_labels) & retained_fifth_union)
        if root in terminalized:
            fate = "terminalized"
            terminal = points5t[root][0]
            terminal_current = int(terminal["current"])
            if int(terminal["immediate"]) != parent_current:
                raise AssertionError(
                    f"terminal immediate provenance mismatch for root {root}"
                )
        else:
            terminal_current = None
            if not raw_rows:
                fate = "dropped_no_raw_output"
            elif len(retained_overlap_labels) == len(raw_labels):
                fate = "dropped_raw_fully_numerically_covered"
            elif retained_overlap_labels:
                fate = "dropped_raw_partially_numerically_covered"
            else:
                fate = "dropped_raw_not_numerically_covered"

        raw_occurrence_mass = harmonic(int(row["current"]) for row in raw_rows)
        raw_union_mass = harmonic(raw_labels)
        exit_rows.append(
            {
                "root": root,
                "fate": fate,
                "parent_current": parent_current,
                "parent_state_class": int(parent["state_class"]),
                "parent_source": str(parent["source"]),
                "parent_source_step": parent["source_step"],
                "parent_exponent": parent_current.bit_length() - 1,
                "terminal_current": terminal_current,
                "raw_occurrence_count": len(raw_rows),
                "raw_distinct_labels": len(raw_labels),
                "raw_occurrence_mass": fraction_text(raw_occurrence_mass),
                "raw_union_mass": fraction_text(raw_union_mass),
                "retained_overlap_labels": len(retained_overlap_labels),
            }
        )

    exiting_release = sum(
        (Fraction(1, int(row["parent_current"])) for row in exit_rows),
        Fraction(),
    )
    recursive_mass4 = sum(
        (state.weight for state in recursive_fourth), Fraction()
    )
    recursive_mass5 = sum(
        (state.weight for state in recursive_fifth), Fraction()
    )
    if survivor_gain - exiting_release != recursive_mass5 - recursive_mass4:
        raise AssertionError("global root-transfer identity failed")

    sorted_individual = sorted(
        survivor_rows,
        key=lambda row: (-Fraction(row["gain"]), int(row["root"])),
    )
    concentration: dict[str, dict[str, str | int]] = {}
    for cutoff in (1, 5, 10, 25, 50, 100, 250, 500):
        selected_gain = sum(
            (Fraction(row["gain"]) for row in sorted_individual[:cutoff]),
            Fraction(),
        )
        concentration[f"top_{cutoff}"] = {
            "count": min(cutoff, len(sorted_individual)),
            "gain": fraction_text(selected_gain),
            "gain_decimal": decimal_text(selected_gain),
            "share": fraction_text(selected_gain / survivor_gain),
            "share_decimal": decimal_text(selected_gain / survivor_gain),
        }

    survivor_groups = {
        "child_source": grouped_survivors(
            survivor_rows, ("child_source",)
        ),
        "shell_drop": grouped_survivors(
            survivor_rows, ("shell_drop",)
        ),
        "child_source_shell_drop": grouped_survivors(
            survivor_rows, ("child_source", "shell_drop")
        ),
        "valuation_class": grouped_survivors(
            survivor_rows,
            ("child_source", "side_parity", "middle_color", "shell_drop"),
        ),
        "child_source_step": grouped_survivors(
            survivor_rows, ("child_source", "child_source_step")
        ),
        "parent_state_class": grouped_survivors(
            survivor_rows, ("parent_state_class",)
        ),
        "child_parent_class": grouped_survivors(
            survivor_rows, ("child_parent_class",)
        ),
    }
    exit_groups = {
        "fate": grouped_exits(exit_rows, ("fate",)),
        "fate_parent_source": grouped_exits(
            exit_rows, ("fate", "parent_source")
        ),
        "parent_state_class": grouped_exits(
            exit_rows, ("parent_state_class",)
        ),
    }

    canonical_survivor_rows = [
        {
            key: row[key]
            for key in (
                "root",
                "parent_current",
                "child_current",
                "gain",
                "parent_state_class",
                "parent_source",
                "parent_source_step",
                "parent_exponent",
                "child_state_class",
                "child_parent_class",
                "child_source",
                "child_source_step",
                "child_exponent",
                "shell_drop",
                "v2_source_step",
                "v3_source_step",
                "side_parity",
                "middle_color",
            )
        }
        for row in survivor_rows
    ]
    canonical_exit_rows = [
        {
            key: row[key]
            for key in (
                "root",
                "fate",
                "parent_current",
                "parent_state_class",
                "parent_source",
                "parent_source_step",
                "parent_exponent",
                "terminal_current",
                "raw_occurrence_count",
                "raw_distinct_labels",
                "raw_occurrence_mass",
                "raw_union_mass",
                "retained_overlap_labels",
            )
        }
        for row in exit_rows
    ]

    output = {
        "schema": "root_lineage_transfer_classification_probe_v1",
        "scope": "certified_baseline_fourth_to_fifth_transition",
        "policy": "local37_then_lexicographic_recursive_only",
        "retention": "global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "counts": {
            "fourth_recursive_roots": len(roots4),
            "surviving_roots": len(surviving),
            "terminalized_roots": len(terminalized),
            "dropped_roots": len(dropped),
            "split_roots": len(split),
            "survivor_immediate_provenance_matches": sum(
                bool(row["immediate_matches_parent"]) for row in survivor_rows
            ),
            "raw_fifth_occurrences": len(occurrences5),
            "retained_fifth_states": len(retained_fifth),
            "retained_fifth_points": len(retained_fifth_union),
        },
        "metrics5": metrics5,
        "masses": {
            "recursive_fourth": serialize_mass(recursive_mass4),
            "recursive_fifth": serialize_mass(recursive_mass5),
            "surviving_parent_mass": serialize_mass(parent_survivor_mass),
            "surviving_child_mass": serialize_mass(child_survivor_mass),
            "survivor_scale_gain": serialize_mass(survivor_gain),
            "exiting_parent_release": serialize_mass(exiting_release),
            "recursive_delta": serialize_mass(recursive_mass5 - recursive_mass4),
        },
        "identity": {
            "formula": "H5_recursive-H4_recursive=survivor_scale_gain-exiting_parent_release",
            "verified": survivor_gain - exiting_release
            == recursive_mass5 - recursive_mass4,
        },
        "survivor_gain_concentration": concentration,
        "survivor_groups": survivor_groups,
        "exit_groups": exit_groups,
        "top_individual_survivor_gains": sorted_individual[:25],
        "hashes": {
            "survivor_rows": canonical_hash(canonical_survivor_rows),
            "exit_rows": canonical_hash(canonical_exit_rows),
            "survivor_groups": canonical_hash(survivor_groups),
            "exit_groups": canonical_hash(exit_groups),
            "top_individual_survivor_gains": canonical_hash(
                [
                    {
                        key: row[key]
                        for key in (
                            "root",
                            "parent_current",
                            "child_current",
                            "gain",
                            "child_source",
                            "child_source_step",
                            "shell_drop",
                            "side_parity",
                            "middle_color",
                        )
                    }
                    for row in sorted_individual[:25]
                ]
            ),
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

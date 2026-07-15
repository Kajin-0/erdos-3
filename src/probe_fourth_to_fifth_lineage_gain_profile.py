#!/usr/bin/env python3
"""Classify the certified fourth-to-fifth root-lineage transfer exactly.

This is not a feature fit.  It decomposes the exact identity

    H5_rec - H4_rec = survivor_scale_gain - exiting_parent_release

by structural coordinates already present in the retained transition:
fourth parent class, fifth source type, source step, dyadic shell, and
immediate-provenance depth drop.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
import hashlib
import json
import sys

from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def fraction_text(value: Fraction) -> str:
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


def floor_log2_ratio(numerator: int, denominator: int) -> int:
    if numerator <= 0 or denominator <= 0:
        raise ValueError("floor_log2_ratio requires positive integers")
    if numerator >= denominator:
        exponent = numerator.bit_length() - denominator.bit_length()
        if numerator < (denominator << exponent):
            exponent -= 1
        return exponent
    exponent = denominator.bit_length() - numerator.bit_length()
    if (numerator << exponent) >= denominator:
        return -exponent
    return -(exponent + 1)


def recursive_families() -> tuple[tuple[object, ...], tuple[object, ...], tuple[object, ...]]:
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
    _occ5, retained_fifth, _metrics5, _rows5 = propagate_recursive_states(
        recursive_fourth
    )
    recursive_fifth = tuple(
        state for state in retained_fifth if contains_three_term_ap(state.values)
    )
    terminal_fifth = tuple(
        state for state in retained_fifth if not contains_three_term_ap(state.values)
    )
    return recursive_fourth, recursive_fifth, terminal_fifth


def summarize_group(rows: list[dict[str, object]]) -> dict[str, object]:
    parent_mass = sum((row["parent_mass"] for row in rows), Fraction())
    child_mass = sum((row["child_mass"] for row in rows), Fraction())
    gain = child_mass - parent_mass
    return {
        "count": len(rows),
        "parent_mass_decimal": decimal_text(parent_mass),
        "parent_mass_sha256": fraction_hash(parent_mass),
        "child_mass_decimal": decimal_text(child_mass),
        "child_mass_sha256": fraction_hash(child_mass),
        "gain_decimal": decimal_text(gain),
        "gain_sha256": fraction_hash(gain),
    }


def summarize_release(rows: list[dict[str, object]]) -> dict[str, object]:
    release = sum((row["parent_mass"] for row in rows), Fraction())
    return {
        "count": len(rows),
        "release_decimal": decimal_text(release),
        "release_sha256": fraction_hash(release),
    }


def main() -> int:
    recursive_fourth, recursive_fifth, terminal_fifth = recursive_families()

    fourth_by_root: dict[int, dict[str, object]] = {}
    fourth_state_by_index = {state.index: state for state in recursive_fourth}
    for state in recursive_fourth:
        for current, root, immediate in zip(
            state.values,
            state.representative.provenance,
            state.representative.immediate_provenance,
            strict=True,
        ):
            if root in fourth_by_root:
                raise AssertionError("fourth root provenance is not unique")
            fourth_by_root[root] = {
                "current": current,
                "state_index": state.index,
                "source": state.representative.source,
                "source_step": state.representative.source_step,
                "shell": state.representative.exponent,
                "immediate": immediate,
            }

    fifth_recursive_by_root: dict[int, dict[str, object]] = {}
    for state in recursive_fifth:
        for current, root, immediate in zip(
            state.values,
            state.representative.provenance,
            state.representative.immediate_provenance,
            strict=True,
        ):
            if root in fifth_recursive_by_root:
                raise AssertionError("fifth recursive root provenance is not unique")
            fifth_recursive_by_root[root] = {
                "current": current,
                "parent_class": state.representative.parent_class,
                "source": state.representative.source,
                "source_step": state.representative.source_step,
                "shell": state.representative.exponent,
                "immediate": immediate,
            }

    fifth_terminal_roots = {
        root
        for state in terminal_fifth
        for root in state.representative.provenance
    }
    roots4 = set(fourth_by_root)
    roots5r = set(fifth_recursive_by_root)
    if not roots5r <= roots4 or not fifth_terminal_roots <= roots4:
        raise AssertionError("fifth family introduced a new root")

    survivor_rows: list[dict[str, object]] = []
    for root in sorted(roots5r):
        parent = fourth_by_root[root]
        child = fifth_recursive_by_root[root]
        if child["parent_class"] != parent["state_index"]:
            raise AssertionError("surviving root changed parent class")
        u4 = int(parent["current"])
        u5 = int(child["current"])
        immediate = int(child["immediate"])
        if u5 > u4:
            raise AssertionError("surviving current label increased")
        if immediate < u5:
            raise AssertionError("immediate provenance is smaller than child label")
        survivor_rows.append(
            {
                "root": root,
                "parent_class": int(child["parent_class"]),
                "u4": u4,
                "u5": u5,
                "parent_mass": Fraction(1, u4),
                "child_mass": Fraction(1, u5),
                "source": str(child["source"]),
                "source_step": child["source_step"],
                "shell": int(child["shell"]),
                "immediate": immediate,
                "immediate_depth": floor_log2_ratio(immediate, u5),
                "root_depth": floor_log2_ratio(root, u5),
            }
        )

    exiting = roots4 - roots5r
    release_rows: list[dict[str, object]] = []
    for root in sorted(exiting):
        parent = fourth_by_root[root]
        release_rows.append(
            {
                "root": root,
                "parent_class": int(parent["state_index"]),
                "u4": int(parent["current"]),
                "parent_mass": Fraction(1, int(parent["current"])),
                "exit_type": (
                    "terminal" if root in fifth_terminal_roots else "dropped"
                ),
                "parent_source": str(parent["source"]),
                "parent_source_step": parent["source_step"],
                "parent_shell": int(parent["shell"]),
            }
        )

    survivor_gain = sum(
        (row["child_mass"] - row["parent_mass"] for row in survivor_rows),
        Fraction(),
    )
    exiting_release = sum(
        (row["parent_mass"] for row in release_rows), Fraction()
    )
    mass4 = sum((state.weight for state in recursive_fourth), Fraction())
    mass5 = sum((state.weight for state in recursive_fifth), Fraction())
    if survivor_gain - exiting_release != mass5 - mass4:
        raise AssertionError("lineage transfer identity failed")

    def grouped(rows: list[dict[str, object]], key: str) -> list[dict[str, object]]:
        buckets: dict[object, list[dict[str, object]]] = defaultdict(list)
        for row in rows:
            buckets[row[key]].append(row)
        result = []
        for value, members in buckets.items():
            summary = summarize_group(members)
            result.append({"key": value, **summary})
        return sorted(
            result,
            key=lambda row: (-float(row["gain_decimal"]), str(row["key"])),
        )

    def grouped_release(
        rows: list[dict[str, object]], key: str
    ) -> list[dict[str, object]]:
        buckets: dict[object, list[dict[str, object]]] = defaultdict(list)
        for row in rows:
            buckets[row[key]].append(row)
        result = []
        for value, members in buckets.items():
            result.append({"key": value, **summarize_release(members)})
        return sorted(
            result,
            key=lambda row: (-float(row["release_decimal"]), str(row["key"])),
        )

    parent_rows = grouped(survivor_rows, "parent_class")
    source_rows = grouped(survivor_rows, "source")
    shell_rows = grouped(survivor_rows, "shell")
    immediate_depth_rows = grouped(survivor_rows, "immediate_depth")
    root_depth_rows = grouped(survivor_rows, "root_depth")
    source_step_rows = grouped(survivor_rows, "source_step")
    release_parent_rows = grouped_release(release_rows, "parent_class")
    release_type_rows = grouped_release(release_rows, "exit_type")

    # Exact parent accounting: each fourth recursive parent class is represented.
    if set(row["key"] for row in parent_rows) != set(fourth_state_by_index):
        raise AssertionError("survivor parent-class support changed")

    top_source_steps = source_step_rows[:20]
    output = {
        "schema": "fourth_to_fifth_lineage_gain_profile_v1",
        "policy": "certified_baseline_lexicographic_descendants",
        "retention": "global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "counts": {
            "fourth_recursive_states": len(recursive_fourth),
            "fourth_recursive_roots": len(roots4),
            "surviving_roots": len(survivor_rows),
            "exiting_roots": len(release_rows),
            "terminal_exits": sum(row["exit_type"] == "terminal" for row in release_rows),
            "dropped_exits": sum(row["exit_type"] == "dropped" for row in release_rows),
            "survivor_parent_classes": len(parent_rows),
            "survivor_sources": len(source_rows),
            "survivor_shells": len(shell_rows),
            "survivor_immediate_depth_classes": len(immediate_depth_rows),
            "survivor_source_steps": len(source_step_rows),
        },
        "identity": {
            "formula": "H5_recursive-H4_recursive=survivor_scale_gain-exiting_parent_release",
            "verified": survivor_gain - exiting_release == mass5 - mass4,
            "survivor_scale_gain_decimal": decimal_text(survivor_gain),
            "survivor_scale_gain_sha256": fraction_hash(survivor_gain),
            "exiting_parent_release_decimal": decimal_text(exiting_release),
            "exiting_parent_release_sha256": fraction_hash(exiting_release),
            "recursive_delta_decimal": decimal_text(mass5 - mass4),
            "recursive_delta_sha256": fraction_hash(mass5 - mass4),
        },
        "survivor_gain_by_parent_class": parent_rows,
        "survivor_gain_by_source": source_rows,
        "survivor_gain_by_shell": shell_rows,
        "survivor_gain_by_immediate_depth": immediate_depth_rows,
        "survivor_gain_by_root_depth": root_depth_rows,
        "top_survivor_gain_source_steps": top_source_steps,
        "exit_release_by_parent_class": release_parent_rows,
        "exit_release_by_type": release_type_rows,
        "hashes": {
            "all_survivor_rows": canonical_hash(
                [
                    {
                        key: (fraction_text(value) if isinstance(value, Fraction) else value)
                        for key, value in row.items()
                    }
                    for row in survivor_rows
                ]
            ),
            "all_release_rows": canonical_hash(
                [
                    {
                        key: (fraction_text(value) if isinstance(value, Fraction) else value)
                        for key, value in row.items()
                    }
                    for row in release_rows
                ]
            ),
            "all_source_step_rows": canonical_hash(source_step_rows),
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

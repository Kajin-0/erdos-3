#!/usr/bin/env python3
"""Decompose the fourth-to-fifth recursive mass change by root lineage.

This probe does not fit a potential.  It records the exact state-independent
root-lineage identity on the certified baseline transition.  Because root
provenance is unique in both the fourth and fifth recursive families, the mass
change decomposes into:

    H5_rec - H4_rec
      = sum_surviving_roots (1/u5 - 1/u4)
        - sum_exiting_roots 1/u4.

Exiting roots are further classified by whether they appear in a fifth-generation
terminal retained state or disappear from the retained family entirely.
"""
from __future__ import annotations

from collections import Counter, defaultdict
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


def compact_bracket(value: Fraction, denominator: int = 1_000_000) -> list[str]:
    lower_numerator = (value.numerator * denominator) // value.denominator
    return [
        fraction_text(Fraction(lower_numerator, denominator)),
        fraction_text(Fraction(lower_numerator + 1, denominator)),
    ]


def root_map(states: tuple[object, ...]) -> dict[int, list[int]]:
    result: dict[int, list[int]] = defaultdict(list)
    for state in states:
        for current, root in zip(
            state.values, state.representative.provenance, strict=True
        ):
            result[root].append(current)
    return {root: sorted(values) for root, values in result.items()}


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


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
    _occ5, retained_fifth, metrics5, _rows5 = propagate_recursive_states(
        recursive_fourth
    )
    terminal_fifth = tuple(
        state for state in retained_fifth if not contains_three_term_ap(state.values)
    )
    recursive_fifth = tuple(
        state for state in retained_fifth if contains_three_term_ap(state.values)
    )

    map4 = root_map(recursive_fourth)
    map5r = root_map(recursive_fifth)
    map5t = root_map(terminal_fifth)
    if any(len(values) != 1 for values in map4.values()):
        raise AssertionError("fourth recursive root provenance is not unique")
    if any(len(values) != 1 for values in map5r.values()):
        raise AssertionError("fifth recursive root provenance is not unique")
    if not set(map5r) <= set(map4):
        raise AssertionError("fifth recursive family introduced a new root")
    if not set(map5t) <= set(map4):
        raise AssertionError("fifth terminal family introduced a new root")

    roots4 = set(map4)
    roots5r = set(map5r)
    roots5t = set(map5t)
    surviving = roots4 & roots5r
    terminalized = roots4 & roots5t
    split = surviving & terminalized
    exiting = roots4 - surviving
    exiting_to_terminal = exiting & terminalized
    exiting_dropped = exiting - terminalized

    survivor_gain = Fraction()
    survivor_rows: list[tuple[int, int, int]] = []
    for root in sorted(surviving):
        parent = map4[root][0]
        child = map5r[root][0]
        if child > parent:
            raise AssertionError(
                f"surviving root expands numerically: p={root}, u4={parent}, u5={child}"
            )
        survivor_gain += Fraction(1, child) - Fraction(1, parent)
        survivor_rows.append((root, parent, child))

    exiting_release = sum(
        (Fraction(1, map4[root][0]) for root in exiting), Fraction()
    )
    terminal_exit_release = sum(
        (Fraction(1, map4[root][0]) for root in exiting_to_terminal),
        Fraction(),
    )
    dropped_exit_release = sum(
        (Fraction(1, map4[root][0]) for root in exiting_dropped),
        Fraction(),
    )
    if terminal_exit_release + dropped_exit_release != exiting_release:
        raise AssertionError("exit-release partition failed")

    mass4 = sum((state.weight for state in recursive_fourth), Fraction())
    mass5r = sum((state.weight for state in recursive_fifth), Fraction())
    mass5t = sum((state.weight for state in terminal_fifth), Fraction())
    delta = mass5r - mass4
    if survivor_gain - exiting_release != delta:
        raise AssertionError("root-transfer identity failed")

    terminal_current_mass_by_root = {
        root: sum((Fraction(1, value) for value in values), Fraction())
        for root, values in map5t.items()
    }
    terminal_mass_from_exiting_roots = sum(
        (terminal_current_mass_by_root[root] for root in exiting_to_terminal),
        Fraction(),
    )
    terminal_mass_from_split_roots = sum(
        (terminal_current_mass_by_root[root] for root in split), Fraction()
    )
    if terminal_mass_from_exiting_roots + terminal_mass_from_split_roots != mass5t:
        raise AssertionError("terminal root partition failed")

    root_multiplicity5_all = Counter(
        root
        for state in retained_fifth
        for root in state.representative.provenance
    )
    output = {
        "schema": "fourth_to_fifth_root_transfer_probe_v1",
        "policy": "certified_baseline_lexicographic_descendants",
        "retention": "global_exact_duplicate_quotient_plus_maximum_harmonic_same_shell_independent_set",
        "counts": {
            "fourth_recursive_roots": len(roots4),
            "fifth_recursive_roots": len(roots5r),
            "fifth_terminal_root_labels": len(roots5t),
            "surviving_recursive_roots": len(surviving),
            "exiting_recursive_roots": len(exiting),
            "exiting_to_terminal_roots": len(exiting_to_terminal),
            "exiting_dropped_roots": len(exiting_dropped),
            "split_recursive_and_terminal_roots": len(split),
            "fifth_all_repeated_root_labels": sum(
                multiplicity > 1 for multiplicity in root_multiplicity5_all.values()
            ),
            "fifth_all_max_root_multiplicity": max(
                root_multiplicity5_all.values(), default=0
            ),
        },
        "metrics5": metrics5,
        "masses": {
            "fourth_recursive": fraction_text(mass4),
            "fifth_recursive": fraction_text(mass5r),
            "fifth_terminal": fraction_text(mass5t),
            "survivor_scale_gain": fraction_text(survivor_gain),
            "exiting_parent_release": fraction_text(exiting_release),
            "terminal_exit_parent_release": fraction_text(terminal_exit_release),
            "dropped_exit_parent_release": fraction_text(dropped_exit_release),
            "terminal_mass_from_exiting_roots": fraction_text(
                terminal_mass_from_exiting_roots
            ),
            "terminal_mass_from_split_roots": fraction_text(
                terminal_mass_from_split_roots
            ),
            "recursive_delta": fraction_text(delta),
        },
        "mass_decimals": {
            "fourth_recursive": decimal_text(mass4),
            "fifth_recursive": decimal_text(mass5r),
            "fifth_terminal": decimal_text(mass5t),
            "survivor_scale_gain": decimal_text(survivor_gain),
            "exiting_parent_release": decimal_text(exiting_release),
            "terminal_exit_parent_release": decimal_text(terminal_exit_release),
            "dropped_exit_parent_release": decimal_text(dropped_exit_release),
            "terminal_mass_from_exiting_roots": decimal_text(
                terminal_mass_from_exiting_roots
            ),
            "terminal_mass_from_split_roots": decimal_text(
                terminal_mass_from_split_roots
            ),
            "recursive_delta": decimal_text(delta),
        },
        "mass_hashes": {
            "fourth_recursive": fraction_hash(mass4),
            "fifth_recursive": fraction_hash(mass5r),
            "fifth_terminal": fraction_hash(mass5t),
            "survivor_scale_gain": fraction_hash(survivor_gain),
            "exiting_parent_release": fraction_hash(exiting_release),
            "terminal_exit_parent_release": fraction_hash(terminal_exit_release),
            "dropped_exit_parent_release": fraction_hash(dropped_exit_release),
            "terminal_mass_from_exiting_roots": fraction_hash(
                terminal_mass_from_exiting_roots
            ),
            "terminal_mass_from_split_roots": fraction_hash(
                terminal_mass_from_split_roots
            ),
            "recursive_delta": fraction_hash(delta),
        },
        "ratios": {
            "survivor_gain_over_exit_release": {
                "decimal": decimal_text(survivor_gain / exiting_release),
                "bracket_millionth": compact_bracket(
                    survivor_gain / exiting_release
                ),
                "sha256": fraction_hash(survivor_gain / exiting_release),
            },
            "recursive_fifth_over_fourth": {
                "decimal": decimal_text(mass5r / mass4),
                "bracket_millionth": compact_bracket(mass5r / mass4),
                "sha256": fraction_hash(mass5r / mass4),
            },
        },
        "identity": {
            "formula": "H5_recursive-H4_recursive=survivor_scale_gain-exiting_parent_release",
            "verified": survivor_gain - exiting_release == delta,
        },
        "hashes": {
            "surviving_root_rows": canonical_hash(survivor_rows),
            "exiting_roots": canonical_hash(sorted(exiting)),
            "exiting_to_terminal_roots": canonical_hash(
                sorted(exiting_to_terminal)
            ),
            "exiting_dropped_roots": canonical_hash(sorted(exiting_dropped)),
            "split_roots": canonical_hash(sorted(split)),
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

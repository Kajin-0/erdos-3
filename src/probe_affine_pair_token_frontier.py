#!/usr/bin/env python3
"""Classify affine coverage and coarse root-pair token reuse through F1..F5.

For a point with current label u and original root provenance p, the affine
reference candidate is r=p-u.  A state is affine when every point has the same
reference r and root provenance is pointwise distinct.

The coarse token (u,p) is then the root-pair token (r,p).  This probe records:
- affine versus non-affine state coverage;
- whether affine references belong to the first retained root universe;
- current-generation token occurrence/union mass;
- cross-generation first-appearance and reused pair-token mass;
- terminal versus recursive token reuse.

No sixth generation is constructed.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
import sys

from probe_root_lineage_transfer_classification import canonical_hash, serialize_mass
from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

Token = tuple[int, int]


def state_affine_record(state: object, first_root_universe: set[int]) -> dict[str, object]:
    values = tuple(state.values)
    roots = tuple(state.representative.provenance)
    immediate = tuple(state.representative.immediate_provenance)
    if len(values) != len(roots) or len(values) != len(immediate):
        raise AssertionError("state point/provenance length mismatch")
    distinct_roots = len(set(roots))
    offsets = {root - value for value, root in zip(values, roots, strict=True)}
    affine = distinct_roots == len(roots) and len(offsets) == 1
    reference = next(iter(offsets)) if affine else None
    return {
        "state_class": state.index,
        "representative": state.representative.index,
        "source": state.representative.source,
        "source_step": state.representative.source_step,
        "exponent": state.representative.exponent,
        "terminal": not contains_three_term_ap(values),
        "size": len(values),
        "distinct_roots": distinct_roots,
        "affine": affine,
        "reference_root": reference,
        "reference_in_first_root_universe": (
            reference in first_root_universe if reference is not None else False
        ),
        "reference_active_in_state": (
            reference in roots if reference is not None else False
        ),
        "tokens_sha256": canonical_hash(
            sorted((value, root, imm) for value, root, imm in zip(values, roots, immediate, strict=True))
        ),
    }


def family_tokens(states: tuple[object, ...]) -> list[tuple[int, int, int, bool, int]]:
    rows: list[tuple[int, int, int, bool, int]] = []
    for state in states:
        terminal = not contains_three_term_ap(state.values)
        for value, root, immediate in zip(
            state.values,
            state.representative.provenance,
            state.representative.immediate_provenance,
            strict=True,
        ):
            rows.append((value, root, immediate, terminal, state.index))
    return rows


def token_mass(tokens: set[Token]) -> Fraction:
    return sum((Fraction(1, value) for value, _root in tokens), Fraction())


def family_record(
    name: str,
    states: tuple[object, ...],
    first_root_universe: set[int],
    seen_tokens: set[Token],
) -> tuple[dict[str, object], set[Token]]:
    state_rows = [
        state_affine_record(state, first_root_universe)
        for state in sorted(states, key=lambda item: item.index)
    ]
    points = family_tokens(states)
    token_counts: Counter[Token] = Counter((value, root) for value, root, _i, _t, _s in points)
    token_immediates: dict[Token, set[int]] = defaultdict(set)
    token_types: dict[Token, set[bool]] = defaultdict(set)
    for value, root, immediate, terminal, _state_class in points:
        token_immediates[(value, root)].add(immediate)
        token_types[(value, root)].add(terminal)

    current_tokens = set(token_counts)
    first_tokens = current_tokens - seen_tokens
    reused_tokens = current_tokens & seen_tokens
    occurrence_mass = sum((Fraction(1, value) for value, _r, _i, _t, _s in points), Fraction())
    union_mass = token_mass(current_tokens)
    duplicate_occurrence_mass = occurrence_mass - union_mass
    first_mass = token_mass(first_tokens)
    reused_mass = token_mass(reused_tokens)
    if first_mass + reused_mass != union_mass:
        raise AssertionError("first/reused token decomposition failed")

    terminal_tokens = {
        token for token, types in token_types.items() if True in types
    }
    recursive_tokens = {
        token for token, types in token_types.items() if False in types
    }
    mixed_type_tokens = terminal_tokens & recursive_tokens

    record = {
        "name": name,
        "states": len(states),
        "points": len(points),
        "terminal_states": sum(row["terminal"] for row in state_rows),
        "recursive_states": sum(not row["terminal"] for row in state_rows),
        "affine_states": sum(row["affine"] for row in state_rows),
        "nonaffine_states": sum(not row["affine"] for row in state_rows),
        "affine_terminal_states": sum(row["affine"] and row["terminal"] for row in state_rows),
        "affine_recursive_states": sum(row["affine"] and not row["terminal"] for row in state_rows),
        "affine_references_in_first_root_universe": sum(
            row["affine"] and row["reference_in_first_root_universe"] for row in state_rows
        ),
        "affine_references_active_in_state": sum(
            row["affine"] and row["reference_active_in_state"] for row in state_rows
        ),
        "token_occurrences": sum(token_counts.values()),
        "distinct_tokens": len(current_tokens),
        "duplicate_token_classes": sum(count > 1 for count in token_counts.values()),
        "maximum_token_multiplicity": max(token_counts.values(), default=0),
        "tokens_with_multiple_immediate_provenance": sum(
            len(values) > 1 for values in token_immediates.values()
        ),
        "terminal_tokens": len(terminal_tokens),
        "recursive_tokens": len(recursive_tokens),
        "terminal_recursive_token_overlap": len(mixed_type_tokens),
        "first_appearance_tokens": len(first_tokens),
        "reused_prior_tokens": len(reused_tokens),
        "occurrence_mass": serialize_mass(occurrence_mass),
        "union_token_mass": serialize_mass(union_mass),
        "duplicate_occurrence_mass": serialize_mass(duplicate_occurrence_mass),
        "first_appearance_mass": serialize_mass(first_mass),
        "reused_prior_mass": serialize_mass(reused_mass),
        "state_rows": state_rows,
        "hashes": {
            "state_rows": canonical_hash(state_rows),
            "token_counts": canonical_hash(
                [(value, root, count) for (value, root), count in sorted(token_counts.items())]
            ),
            "first_tokens": canonical_hash(sorted(first_tokens)),
            "reused_tokens": canonical_hash(sorted(reused_tokens)),
            "token_immediates": canonical_hash(
                [
                    (value, root, sorted(immediates))
                    for (value, root), immediates in sorted(token_immediates.items())
                ]
            ),
        },
    }
    return record, seen_tokens | current_tokens


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

    families = [
        ("F1_retained", retained_first),
        ("F2_retained", retained_second),
        ("F3_retained", retained_third),
        ("F4_retained", retained_fourth),
        ("F5_retained", retained_fifth),
    ]
    first_root_universe = {
        root
        for state in retained_first
        for root in state.representative.provenance
    }
    seen_tokens: set[Token] = set()
    records: list[dict[str, object]] = []
    for name, states in families:
        record, seen_tokens = family_record(
            name,
            states,
            first_root_universe,
            seen_tokens,
        )
        records.append(record)

    cumulative_first_mass = sum(
        (Fraction(record["first_appearance_mass"]["fraction"]) for record in records),
        Fraction(),
    )
    cumulative_occurrence_mass = sum(
        (Fraction(record["occurrence_mass"]["fraction"]) for record in records),
        Fraction(),
    )
    cumulative_reuse_mass = cumulative_occurrence_mass - cumulative_first_mass
    if cumulative_reuse_mass != sum(
        (
            Fraction(record["duplicate_occurrence_mass"]["fraction"])
            + Fraction(record["reused_prior_mass"]["fraction"])
            for record in records
        ),
        Fraction(),
    ):
        raise AssertionError("cumulative pair-reuse decomposition failed")

    output = {
        "schema": "affine_pair_token_frontier_probe_v1",
        "scope": "certified_retained_families_F1_through_F5",
        "generation_six_propagated": False,
        "first_root_universe": {
            "roots": len(first_root_universe),
            "sha256": canonical_hash(sorted(first_root_universe)),
        },
        "families": records,
        "cumulative": {
            "occurrence_mass": serialize_mass(cumulative_occurrence_mass),
            "first_appearance_mass": serialize_mass(cumulative_first_mass),
            "pair_reuse_mass": serialize_mass(cumulative_reuse_mass),
            "distinct_tokens": len(seen_tokens),
            "tokens_sha256": canonical_hash(sorted(seen_tokens)),
        },
        "hashes": {
            "family_summaries": canonical_hash(
                [
                    {
                        key: record[key]
                        for key in (
                            "name",
                            "states",
                            "points",
                            "terminal_states",
                            "recursive_states",
                            "affine_states",
                            "nonaffine_states",
                            "affine_terminal_states",
                            "affine_recursive_states",
                            "affine_references_in_first_root_universe",
                            "affine_references_active_in_state",
                            "token_occurrences",
                            "distinct_tokens",
                            "duplicate_token_classes",
                            "maximum_token_multiplicity",
                            "tokens_with_multiple_immediate_provenance",
                            "terminal_tokens",
                            "recursive_tokens",
                            "terminal_recursive_token_overlap",
                            "first_appearance_tokens",
                            "reused_prior_tokens",
                            "occurrence_mass",
                            "union_token_mass",
                            "duplicate_occurrence_mass",
                            "first_appearance_mass",
                            "reused_prior_mass",
                            "hashes",
                        )
                    }
                    for record in records
                ]
            ),
            "affine_state_rows": canonical_hash(
                [(record["name"], record["state_rows"]) for record in records]
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

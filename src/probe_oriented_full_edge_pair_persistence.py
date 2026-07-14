#!/usr/bin/env python3
"""Exhaustively profile latent-pair persistence in oriented full-edge branching.

The original full-edge incidence theorem is numerical and local.  Recursive
pair containment additionally needs every child to have one fixed affine
orientation.  Split middle children by the parity-selected left/right side,
reconstruct their parent-root subsets, and measure current and latent physical
pair reuse over every four-AP-free subset of [1,14].
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import hashlib
import json
import sys

from verify_full_edge_coordinated_branching import (
    canonical_hash,
    contains_four_ap,
    harmonic,
    ordered_pair,
    pair_weight,
    three_aps,
    valuation,
    verify_child,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

LIMIT = 14
ChildKey = tuple[str, int, int | None]
Pair = tuple[int, int]
RIGHT_TYPES = {"side_first", "middle_right", "double_first"}
LEFT_TYPES = {"side_last", "middle_left", "double_last"}


def fraction_record(value: Fraction) -> dict[str, object]:
    text = f"{value.numerator}/{value.denominator}"
    return {
        "fraction": text,
        "decimal": f"{float(value):.12f}",
        "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def pair_energy(values: frozenset[int] | set[int]) -> Fraction:
    return sum(
        (Fraction(1, right - left) for left, right in combinations(sorted(values), 2)),
        Fraction(),
    )


def oriented_family(values: frozenset[int]) -> tuple[
    dict[ChildKey, frozenset[int]],
    dict[ChildKey, frozenset[int]],
    dict[ChildKey, int],
    list[dict[str, object]],
]:
    children: dict[ChildKey, set[int]] = defaultdict(set)
    roots: dict[ChildKey, set[int]] = defaultdict(set)
    references: dict[ChildKey, int] = {}
    seen: dict[tuple[ChildKey, int], dict[str, object]] = {}
    occurrences: list[dict[str, object]] = []

    for left, middle, right, step in three_aps(values):
        color = (valuation(step, 2) - valuation(step, 3)) % 3
        if valuation(step, 2) % 2 == 0:
            rows = (
                (("side_first", left, None), step, middle, left, (left, middle)),
                (("middle_right", middle, color), step, right, middle, (middle, right)),
                (("double_first", left, None), 2 * step, right, left, (left, right)),
            )
        else:
            rows = (
                (("side_last", right, None), step, middle, right, (middle, right)),
                (("middle_left", middle, color), step, left, middle, (left, middle)),
                (("double_last", right, None), 2 * step, left, right, (left, right)),
            )

        for key, token, root, reference, raw_pair in rows:
            pair = ordered_pair(*raw_pair)
            if abs(root - reference) != token:
                raise AssertionError("oriented affine token/root mismatch")
            if pair_weight(pair) != Fraction(1, token):
                raise AssertionError("oriented pair/token weight mismatch")
            if key in references and references[key] != reference:
                raise AssertionError("child key has inconsistent reference root")
            references[key] = reference
            identity = (key, token)
            record = {
                "progression": [left, middle, right, step],
                "child_key": list(key),
                "token": token,
                "root": root,
                "reference": reference,
                "pair": list(pair),
            }
            if identity in seen:
                raise AssertionError(f"duplicate oriented child token: {identity}")
            seen[identity] = record
            children[key].add(token)
            roots[key].add(root)
            occurrences.append(record)

    frozen_children = {key: frozenset(tokens) for key, tokens in children.items()}
    frozen_roots = {key: frozenset(items) for key, items in roots.items()}
    for key in frozen_children:
        if len(frozen_children[key]) != len(frozen_roots[key]):
            raise AssertionError("token/root cardinality mismatch")
    return frozen_children, frozen_roots, references, occurrences


def verify_root_geometry(
    values: frozenset[int],
    key: ChildKey,
    child_roots: frozenset[int],
    reference: int,
) -> None:
    kind = key[0]
    for root in child_roots:
        if kind in RIGHT_TYPES and not reference < root:
            raise AssertionError("right-oriented child root is not right of reference")
        if kind in LEFT_TYPES and not reference > root:
            raise AssertionError("left-oriented child root is not left of reference")
        if kind in {"side_first", "side_last"}:
            completion = 2 * root - reference
            if completion not in values:
                raise AssertionError("side child lacks outward reflection completion")
        elif kind in {"middle_right", "middle_left"}:
            completion = 2 * reference - root
            if completion not in values:
                raise AssertionError("middle child lacks inward reflection completion")
        elif kind in {"double_first", "double_last"}:
            if (reference + root) % 2:
                raise AssertionError("doubled-side midpoint is not integral")
            midpoint = (reference + root) // 2
            if midpoint not in values:
                raise AssertionError("doubled-side child lacks midpoint completion")
        else:
            raise AssertionError(f"unknown child kind {kind}")


def forbidden_reference_gap(kind: str, pair_gap: int) -> int:
    return 2 * pair_gap if kind.startswith("double_") else pair_gap


def subset_profile(values: frozenset[int]) -> dict[str, object]:
    children, roots, references, occurrences = oriented_family(values)
    for key, tokens in children.items():
        verify_child(key, tokens)
        verify_root_geometry(values, key, roots[key], references[key])

    if len(occurrences) != 3 * len(three_aps(values)):
        raise AssertionError("oriented family lost a progression membership")
    current_mass = sum((Fraction(1, int(row["token"])) for row in occurrences), Fraction())
    load = sum((Fraction(1, step) for *_points, step in three_aps(values)), Fraction())
    if current_mass != Fraction(5, 2) * load:
        raise AssertionError("oriented full-edge mass identity failed")

    recursive_keys = tuple(key for key, tokens in children.items() if three_aps(tokens))
    latent_occurrences: dict[Pair, list[tuple[ChildKey, int]]] = defaultdict(list)
    for key in recursive_keys:
        reference = references[key]
        for pair in combinations(sorted(roots[key]), 2):
            latent_occurrences[pair].append((key, reference))

    for pair, rows in latent_occurrences.items():
        left, right = pair
        if any(left < reference < right for _key, reference in rows):
            raise AssertionError("persistent pair reference lies inside pair interval")
        by_kind: dict[str, set[int]] = defaultdict(set)
        for key, reference in rows:
            by_kind[key[0]].add(reference)
        gap = right - left
        for kind, refs in by_kind.items():
            forbidden = forbidden_reference_gap(kind, gap)
            if any(reference + forbidden in refs for reference in refs):
                raise AssertionError(
                    f"forbidden same-type reference gap survived: {pair}, {kind}, {refs}"
                )

    latent_counts = Counter({pair: len(rows) for pair, rows in latent_occurrences.items()})
    latent_occurrence_mass = sum(
        (pair_weight(pair) * count for pair, count in latent_counts.items()), Fraction()
    )
    latent_union_mass = sum((pair_weight(pair) for pair in latent_counts), Fraction())

    current_counts = Counter(tuple(row["pair"]) for row in occurrences)
    total_counts = current_counts.copy()
    total_counts.update(latent_counts)
    total_occurrence_mass = sum(
        (pair_weight(pair) * count for pair, count in total_counts.items()), Fraction()
    )
    total_union_mass = sum((pair_weight(pair) for pair in total_counts), Fraction())
    parent_energy = pair_energy(values)
    if any(pair[0] not in values or pair[1] not in values for pair in total_counts):
        raise AssertionError("child resource escaped parent pair universe")
    if total_union_mass > parent_energy:
        raise AssertionError("child resource union exceeds parent pair universe")

    maximum_latent = max(latent_counts.values(), default=0)
    maximum_total = max(total_counts.values(), default=0)
    maximum_reference_count = max(
        (len({reference for _key, reference in rows}) for rows in latent_occurrences.values()),
        default=0,
    )
    worst_pairs = []
    for pair in sorted(latent_occurrences):
        rows = latent_occurrences[pair]
        if len(rows) != maximum_latent:
            continue
        worst_pairs.append(
            {
                "pair": list(pair),
                "gap": pair[1] - pair[0],
                "occurrences": [
                    {"child_key": list(key), "reference": reference}
                    for key, reference in sorted(rows)
                ],
            }
        )

    return {
        "values": list(values),
        "three_aps": len(three_aps(values)),
        "children": len(children),
        "recursive_children": len(recursive_keys),
        "current_occurrences": len(occurrences),
        "latent_pair_occurrences": sum(latent_counts.values()),
        "latent_pair_union": len(latent_counts),
        "maximum_latent_pair_multiplicity": maximum_latent,
        "maximum_total_resource_multiplicity": maximum_total,
        "maximum_reference_count": maximum_reference_count,
        "parent_pair_energy": fraction_record(parent_energy),
        "current_mass": fraction_record(current_mass),
        "latent_occurrence_mass": fraction_record(latent_occurrence_mass),
        "latent_union_mass": fraction_record(latent_union_mass),
        "total_occurrence_mass": fraction_record(total_occurrence_mass),
        "total_union_mass": fraction_record(total_union_mass),
        "worst_pairs": worst_pairs,
        "children_sha256": canonical_hash(
            [
                [list(key), sorted(children[key]), sorted(roots[key]), references[key]]
                for key in sorted(children)
            ]
        ),
    }


def ratio(numerator: Fraction, denominator: Fraction) -> Fraction:
    return numerator / denominator if denominator else Fraction()


def main() -> int:
    interval = tuple(range(1, LIMIT + 1))
    metrics = Counter()
    extrema: dict[str, tuple[Fraction, dict[str, object]]] = {}
    multiplicity_witness: dict[str, object] | None = None
    records_hash = hashlib.sha256()

    for mask in range(1 << LIMIT):
        values = frozenset(
            interval[index] for index in range(LIMIT) if mask & (1 << index)
        )
        if contains_four_ap(values):
            continue
        profile = subset_profile(values)
        records_hash.update(
            (json.dumps(profile, sort_keys=True, separators=(",", ":")) + "\n").encode(
                "utf-8"
            )
        )
        metrics["four_ap_free_subsets"] += 1
        metrics["subsets_with_recursive_children"] += int(profile["recursive_children"] > 0)
        metrics["three_aps"] += int(profile["three_aps"])
        metrics["children"] += int(profile["children"])
        metrics["recursive_children"] += int(profile["recursive_children"])
        metrics["latent_pair_occurrences"] += int(profile["latent_pair_occurrences"])
        metrics["latent_pair_union"] += int(profile["latent_pair_union"])
        metrics["maximum_latent_pair_multiplicity"] = max(
            metrics["maximum_latent_pair_multiplicity"],
            int(profile["maximum_latent_pair_multiplicity"]),
        )
        metrics["maximum_total_resource_multiplicity"] = max(
            metrics["maximum_total_resource_multiplicity"],
            int(profile["maximum_total_resource_multiplicity"]),
        )
        metrics["maximum_reference_count"] = max(
            metrics["maximum_reference_count"], int(profile["maximum_reference_count"])
        )
        if int(profile["maximum_latent_pair_multiplicity"]) == metrics[
            "maximum_latent_pair_multiplicity"
        ]:
            multiplicity_witness = profile

        parent = Fraction(profile["parent_pair_energy"]["fraction"])
        candidates = {
            "latent_occurrence_over_parent_energy": ratio(
                Fraction(profile["latent_occurrence_mass"]["fraction"]), parent
            ),
            "total_occurrence_over_parent_energy": ratio(
                Fraction(profile["total_occurrence_mass"]["fraction"]), parent
            ),
            "latent_occurrence_over_latent_union": ratio(
                Fraction(profile["latent_occurrence_mass"]["fraction"]),
                Fraction(profile["latent_union_mass"]["fraction"]),
            ),
        }
        for name, value in candidates.items():
            if name not in extrema or value > extrema[name][0]:
                extrema[name] = (value, profile)

    output = {
        "schema": "oriented_full_edge_pair_persistence_probe_v1",
        "interval": [1, LIMIT],
        "metrics": dict(metrics),
        "extrema": {
            name: {
                "ratio": fraction_record(value),
                "values": profile["values"],
                "recursive_children": profile["recursive_children"],
                "maximum_latent_pair_multiplicity": profile[
                    "maximum_latent_pair_multiplicity"
                ],
                "parent_pair_energy": profile["parent_pair_energy"],
                "latent_occurrence_mass": profile["latent_occurrence_mass"],
                "latent_union_mass": profile["latent_union_mass"],
                "total_occurrence_mass": profile["total_occurrence_mass"],
            }
            for name, (value, profile) in sorted(extrema.items())
        },
        "maximum_multiplicity_witness": multiplicity_witness,
        "verified": {
            "middle_children_split_by_orientation": True,
            "all_children_four_ap_free": True,
            "all_children_have_disjoint_first_three_dilates": True,
            "all_child_resources_contained_in_parent_pairs": True,
            "all_persistent_pair_references_outside_pair_interval": True,
            "same_type_side_middle_reference_gap_D_forbidden": True,
            "same_type_doubled_reference_gap_2D_forbidden": True,
        },
        "records_sha256": records_hash.hexdigest(),
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

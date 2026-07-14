#!/usr/bin/env python3
"""Profile pair persistence after mandatory dyadic shelling.

Full-edge children are not recursive objects until each numerical child is
resolved into standard dyadic shells.  Reconstruct oriented affine root sets,
partition every child by floor-log-two, and measure latent physical-pair reuse
only among shells that still contain a three-term progression.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import hashlib
import json
import sys

from probe_oriented_full_edge_pair_persistence import (
    LEFT_TYPES,
    RIGHT_TYPES,
    fraction_record,
    oriented_family,
    pair_energy,
    verify_root_geometry,
)
from verify_full_edge_coordinated_branching import (
    canonical_hash,
    contains_four_ap,
    pair_weight,
    three_aps,
    verify_child,
)

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

LIMIT = 20
ShellKey = tuple[str, int, int | None, int]
Pair = tuple[int, int]


def exponent(token: int) -> int:
    if token <= 0:
        raise ValueError("dyadic exponent requires a positive token")
    return token.bit_length() - 1


def shelled_family(values: frozenset[int]) -> tuple[
    dict[ShellKey, frozenset[int]],
    dict[ShellKey, frozenset[int]],
    dict[ShellKey, int],
    list[dict[str, object]],
]:
    children, _roots, references, occurrences = oriented_family(values)
    shell_tokens: dict[ShellKey, set[int]] = defaultdict(set)
    shell_roots: dict[ShellKey, set[int]] = defaultdict(set)
    shell_references: dict[ShellKey, int] = {}

    for key, tokens in children.items():
        kind, reference, color = key
        for token in tokens:
            shell_key: ShellKey = (kind, reference, color, exponent(token))
            if kind in RIGHT_TYPES:
                root = reference + token
            elif kind in LEFT_TYPES:
                root = reference - token
            else:
                raise AssertionError(f"unknown oriented kind {kind}")
            shell_tokens[shell_key].add(token)
            shell_roots[shell_key].add(root)
            shell_references[shell_key] = reference

    frozen_tokens = {key: frozenset(tokens) for key, tokens in shell_tokens.items()}
    frozen_roots = {key: frozenset(roots) for key, roots in shell_roots.items()}
    for key, tokens in frozen_tokens.items():
        if len(tokens) != len(frozen_roots[key]):
            raise AssertionError("dyadic shell token/root cardinality mismatch")
        lower = 1 << key[3]
        if not all(lower <= token < 2 * lower for token in tokens):
            raise AssertionError("token escaped its standard dyadic shell")
        verify_child(key, tokens)
        unshelled_key = key[:3]
        verify_root_geometry(values, unshelled_key, frozen_roots[key], references[unshelled_key])
    return frozen_tokens, frozen_roots, shell_references, occurrences


def subset_profile(values: frozenset[int]) -> dict[str, object]:
    shells, roots, references, occurrences = shelled_family(values)
    recursive_keys = tuple(key for key, tokens in shells.items() if three_aps(tokens))

    latent_rows: dict[Pair, list[tuple[ShellKey, int]]] = defaultdict(list)
    for key in recursive_keys:
        reference = references[key]
        for pair in combinations(sorted(roots[key]), 2):
            latent_rows[pair].append((key, reference))

    latent_counts = Counter({pair: len(rows) for pair, rows in latent_rows.items()})
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
    if total_union_mass > parent_energy:
        raise AssertionError("shelled child resource union exceeds parent pair universe")

    maximum_latent = max(latent_counts.values(), default=0)
    maximum_reference_count = max(
        (len({reference for _key, reference in rows}) for rows in latent_rows.values()),
        default=0,
    )
    reused = []
    for pair in sorted(latent_rows):
        rows = latent_rows[pair]
        if len(rows) <= 1:
            continue
        reused.append(
            {
                "pair": list(pair),
                "gap": pair[1] - pair[0],
                "occurrences": [
                    {"shell_key": list(key), "reference": reference}
                    for key, reference in sorted(rows)
                ],
            }
        )

    return {
        "values": list(values),
        "shells": len(shells),
        "recursive_shells": len(recursive_keys),
        "recursive_shell_keys": [list(key) for key in sorted(recursive_keys)],
        "latent_pair_occurrences": sum(latent_counts.values()),
        "latent_pair_union": len(latent_counts),
        "maximum_latent_pair_multiplicity": maximum_latent,
        "maximum_reference_count": maximum_reference_count,
        "parent_pair_energy": fraction_record(parent_energy),
        "latent_occurrence_mass": fraction_record(latent_occurrence_mass),
        "latent_union_mass": fraction_record(latent_union_mass),
        "total_occurrence_mass": fraction_record(total_occurrence_mass),
        "total_union_mass": fraction_record(total_union_mass),
        "reused_latent_pairs": reused,
        "shell_family_sha256": canonical_hash(
            [
                [list(key), sorted(shells[key]), sorted(roots[key]), references[key]]
                for key in sorted(shells)
            ]
        ),
    }


def ratio(numerator: Fraction, denominator: Fraction) -> Fraction:
    return numerator / denominator if denominator else Fraction()


def main() -> int:
    interval = tuple(range(1, LIMIT + 1))
    metrics = Counter()
    records_hash = hashlib.sha256()
    first_reuse: dict[str, object] | None = None
    extrema: dict[str, tuple[Fraction, dict[str, object]]] = {}

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
        metrics["subsets_with_recursive_shells"] += int(profile["recursive_shells"] > 0)
        metrics["shells"] += int(profile["shells"])
        metrics["recursive_shells"] += int(profile["recursive_shells"])
        metrics["latent_pair_occurrences"] += int(profile["latent_pair_occurrences"])
        metrics["latent_pair_union"] += int(profile["latent_pair_union"])
        metrics["maximum_latent_pair_multiplicity"] = max(
            metrics["maximum_latent_pair_multiplicity"],
            int(profile["maximum_latent_pair_multiplicity"]),
        )
        metrics["maximum_reference_count"] = max(
            metrics["maximum_reference_count"], int(profile["maximum_reference_count"])
        )
        if profile["reused_latent_pairs"] and first_reuse is None:
            first_reuse = profile

        parent = Fraction(profile["parent_pair_energy"]["fraction"])
        candidates = {
            "latent_occurrence_over_parent_energy": ratio(
                Fraction(profile["latent_occurrence_mass"]["fraction"]), parent
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
        "schema": "shelled_oriented_full_edge_pair_persistence_probe_v1",
        "interval": [1, LIMIT],
        "metrics": dict(metrics),
        "extrema": {
            name: {
                "ratio": fraction_record(value),
                "values": profile["values"],
                "recursive_shells": profile["recursive_shells"],
                "latent_pair_occurrences": profile["latent_pair_occurrences"],
                "latent_pair_union": profile["latent_pair_union"],
            }
            for name, (value, profile) in sorted(extrema.items())
        },
        "first_reuse_witness": first_reuse,
        "verified": {
            "mandatory_standard_dyadic_shelling_applied": True,
            "all_recursive_objects_are_single_dyadic_shells": True,
            "all_shell_resources_contained_in_parent_pairs": True,
        },
        "records_sha256": records_hash.hexdigest(),
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

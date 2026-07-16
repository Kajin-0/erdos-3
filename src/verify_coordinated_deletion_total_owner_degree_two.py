#!/usr/bin/env python3
"""Verify total current-plus-latent owner degree at most two."""
from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations
import hashlib
import json

from search_lexicographic_reserve_pseudoforest_small_box import (
    contains_four_ap,
    ordered_pair,
    retained_family,
)
from verify_retained_terminal_split import contains_three_term_ap

Resource = tuple[int, int]


def owner_profile(parent: tuple[int, ...]) -> dict[str, object]:
    retained = retained_family(parent)
    owners: dict[Resource, list[str]] = defaultdict(list)

    for state in retained:
        values = tuple(int(value) for value in state.values)
        roots = tuple(int(root) for root in state.representative.provenance)
        references = {
            root - value for value, root in zip(values, roots, strict=True)
        }
        if len(references) != 1:
            raise AssertionError("total-owner retained child is not affine")
        reference = references.pop()
        terminal = not contains_three_term_ap(values)

        for root in roots:
            owners[ordered_pair(reference, root)].append("current")

        if terminal:
            continue
        for left, right in combinations(roots, 2):
            owners[ordered_pair(left, right)].append("latent")

    profile_histogram: Counter[tuple[int, int]] = Counter()
    repeated_resources = 0
    maximum_current = 0
    maximum_latent = 0
    maximum_total = 0
    for resource, roles in owners.items():
        current = roles.count("current")
        latent = roles.count("latent")
        total = len(roles)
        profile_histogram[(current, latent)] += 1
        repeated_resources += total > 1
        maximum_current = max(maximum_current, current)
        maximum_latent = max(maximum_latent, latent)
        maximum_total = max(maximum_total, total)
        if current > 1:
            raise AssertionError(
                f"multiple current owners for {parent}: {resource}, {roles}"
            )
        if latent > 2:
            raise AssertionError(
                f"latent degree exceeded two for {parent}: {resource}, {roles}"
            )
        if total > 2:
            raise AssertionError(
                f"total owner degree exceeded two for {parent}: {resource}, {roles}"
            )
        if current and latent > 1:
            raise AssertionError(
                f"current plus two latent owners for {parent}: {resource}, {roles}"
            )

    return {
        "retained_states": len(retained),
        "resources": len(owners),
        "repeated_resources": repeated_resources,
        "maximum_current_degree": maximum_current,
        "maximum_latent_degree": maximum_latent,
        "maximum_total_degree": maximum_total,
        "profiles": [
            {
                "current": current,
                "latent": latent,
                "resources": count,
            }
            for (current, latent), count in sorted(profile_histogram.items())
        ],
    }


def main() -> int:
    endpoint = 16
    values = tuple(range(1, endpoint + 1))
    parents_checked = 0
    aggregate_profiles: Counter[tuple[int, int]] = Counter()
    parents_with_repeated_resources = 0
    maximum_repeated_resources = 0

    for mask in range(1 << endpoint):
        parent = tuple(
            value for index, value in enumerate(values) if mask & (1 << index)
        )
        if len(parent) < 3 or contains_four_ap(parent):
            continue
        parents_checked += 1
        profile = owner_profile(parent)
        repeated = int(profile["repeated_resources"])
        parents_with_repeated_resources += repeated > 0
        maximum_repeated_resources = max(maximum_repeated_resources, repeated)
        for row in profile["profiles"]:
            aggregate_profiles[(int(row["current"]), int(row["latent"]))] += int(
                row["resources"]
            )

    clean_latent_parent = (
        1,
        4,
        5,
        6,
        20,
        21,
        22,
        26,
        27,
        28,
        32,
        33,
        34,
    )
    rank_two_parent = (
        1,
        9194,
        9200,
        9206,
        10595,
        10600,
        10605,
        11296,
        11300,
        11304,
        11599,
        11600,
        11601,
        11996,
        11997,
        11999,
        12000,
        12001,
        12004,
        12005,
        12006,
        12012,
        12046,
        12047,
        12049,
        12050,
        12051,
        12054,
        12055,
        12056,
        12062,
        12096,
        12097,
        12099,
        12100,
        12101,
        12104,
        12105,
        12106,
        12112,
    )

    if contains_four_ap(clean_latent_parent) or contains_four_ap(rank_two_parent):
        raise AssertionError("named total-owner verifier parent contains a four-AP")

    clean_profile = owner_profile(clean_latent_parent)
    rank_two_profile = owner_profile(rank_two_parent)
    if int(clean_profile["maximum_total_degree"]) != 2:
        raise AssertionError("clean latent witness lost its degree-two reuse")
    if int(rank_two_profile["maximum_total_degree"]) != 2:
        raise AssertionError("rank-two witness lost its degree-two reuse")

    output: dict[str, object] = {
        "schema": "coordinated_deletion_total_owner_degree_two_v1",
        "endpoint": endpoint,
        "counts": {
            "small_box_parents_checked": parents_checked,
            "small_box_parents_with_repeated_resources": parents_with_repeated_resources,
            "maximum_small_box_repeated_resources": maximum_repeated_resources,
        },
        "aggregate_profile_histogram": [
            {
                "current": current,
                "latent": latent,
                "resources": count,
            }
            for (current, latent), count in sorted(aggregate_profiles.items())
        ],
        "clean_latent_witness": clean_profile,
        "rank_two_witness": rank_two_profile,
        "checks": {
            "current_degree_at_most_one": True,
            "latent_degree_at_most_two": True,
            "total_owner_degree_at_most_two": True,
            "current_plus_two_latent_impossible": True,
            "named_latent_reuse_witnesses_reach_degree_two": True,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

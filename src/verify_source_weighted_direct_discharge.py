#!/usr/bin/env python3
"""Verify exact source-weighted direct discharge on the relative small box."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
import hashlib
import json

from verify_direct_maximal_pair_discharge import (
    Pair,
    classify_pair,
    completion_candidates,
    contains_four_ap,
    four_aps,
    harmonic,
    is_relative_maximal,
    pair_weight,
    three_aps,
)


def gap_base(pair: Pair) -> int:
    gap = pair[1] - pair[0]
    return 1 << (gap.bit_length() - 1)


def main() -> int:
    universe = set(range(1, 13))
    progressions = four_aps(1, 12)
    maximal_parents = [
        {value for value in universe if (mask >> (value - 1)) & 1}
        for mask in range(1 << len(universe))
    ]
    maximal_parents = [
        parent
        for parent in maximal_parents
        if is_relative_maximal(parent, universe, progressions)
    ]
    if len(maximal_parents) != 58:
        raise AssertionError("source-weighted relative-maximal parent count changed")

    counts = Counter()
    total_entering = Fraction()
    total_source_outgoing = Fraction()
    total_full_capacity_outgoing = Fraction()
    total_light_source = Fraction()
    total_light_capacity = Fraction()
    total_heavy_source = Fraction()
    total_free_edge = Fraction()
    maximum_light_utilization = Fraction()
    profile_rows: list[object] = []

    for parent in maximal_parents:
        for base in (1, 2, 4, 8):
            shell = {value for value in parent if base <= value < 2 * base}
            eligible_pairs = [
                pair
                for pair in combinations(sorted(shell), 2)
                if completion_candidates(pair, universe)
            ]

            production = Fraction(5, 2) * sum(
                (
                    Fraction(1, middle - left)
                    for left, middle, _right in three_aps(shell)
                ),
                Fraction(),
            )

            for mask in range(1 << len(eligible_pairs)):
                activated = {
                    eligible_pairs[index]
                    for index in range(len(eligible_pairs))
                    if (mask >> index) & 1
                }
                counts["activated_families"] += 1

                local: set[Pair] = set()
                cross_rows: list[tuple[Pair, Pair]] = []
                hole_rows: list[
                    tuple[Pair, int, str, int, Fraction, Pair]
                ] = []

                for pair in activated:
                    kind, completion, role, step, coefficient, output = classify_pair(
                        parent, shell, pair, universe, progressions
                    )
                    if kind == "local":
                        local.add(pair)
                    elif kind == "cross":
                        assert output is not None
                        cross_rows.append((pair, output))
                    else:
                        assert output is not None
                        hole_rows.append(
                            (pair, completion, role, step, coefficient, output)
                        )

                local_mass = sum((pair_weight(pair) for pair in local), Fraction())
                if local_mass > production:
                    raise AssertionError("source-weighted local mass exceeds production")
                free_edge = production - local_mass

                cross_source = sum(
                    (pair_weight(source) for source, _target in cross_rows),
                    Fraction(),
                )
                cross_output = sum(
                    (pair_weight(source) for source, _target in cross_rows),
                    Fraction(),
                )
                if cross_source != cross_output:
                    raise AssertionError("source-weighted cross mass changed")
                for source, target in cross_rows:
                    if pair_weight(source) != pair_weight(target):
                        raise AssertionError("cross swap changed physical pair weight")
                    if gap_base(source) != gap_base(target):
                        raise AssertionError("cross swap changed dyadic gap base")

                grouped: dict[
                    tuple[Pair, int, str, Fraction],
                    list[tuple[Pair, int]],
                ] = defaultdict(list)
                roles_by_support: dict[
                    Pair, set[tuple[int, str, Fraction]]
                ] = defaultdict(set)
                for pair, completion, role, step, coefficient, support in hole_rows:
                    grouped[(support, completion, role, coefficient)].append(
                        (pair, step)
                    )
                    roles_by_support[support].add((completion, role, coefficient))

                reserve = set(activated) | {target for _source, target in cross_rows}
                support_light_load: dict[Pair, Fraction] = defaultdict(Fraction)
                light_source = Fraction()
                heavy_source = Fraction()

                for support, roles in roles_by_support.items():
                    multiplicity = len(roles)
                    threshold = (
                        Fraction()
                        if support in reserve
                        else pair_weight(support) / multiplicity
                    )
                    for completion, role, coefficient in roles:
                        rows = grouped[(support, completion, role, coefficient)]
                        steps = {step for _pair, step in rows}
                        load = coefficient * harmonic(steps)
                        source_mass = sum(
                            (pair_weight(pair) for pair, _step in rows),
                            Fraction(),
                        )
                        if load != source_mass:
                            raise AssertionError(
                                "role-fiber load differs from exact source mass"
                            )
                        if load <= threshold:
                            support_light_load[support] += load
                            light_source += load
                            source_moment = sum(
                                (
                                    pair_weight(pair) * gap_base(pair)
                                    for pair, _step in rows
                                ),
                                Fraction(),
                            )
                            output_moment = load * gap_base(support)
                            if output_moment > source_moment:
                                raise AssertionError(
                                    "source-weighted light dyadic-gap moment expanded"
                                )
                        else:
                            heavy_source += load

                for support, load in support_light_load.items():
                    if support in reserve:
                        raise AssertionError(
                            "source-weighted light support used reserved capacity"
                        )
                    if load > pair_weight(support):
                        raise AssertionError(
                            "source-weighted aggregate light load exceeds capacity"
                        )
                    if load:
                        maximum_light_utilization = max(
                            maximum_light_utilization,
                            load / pair_weight(support),
                        )

                light_capacity = sum(
                    (pair_weight(support) for support in support_light_load),
                    Fraction(),
                )
                hole_source = sum(
                    (pair_weight(pair) for pair, *_rest in hole_rows),
                    Fraction(),
                )
                if hole_source != light_source + heavy_source:
                    raise AssertionError("hole source partition failed")

                entering = sum(
                    (pair_weight(pair) for pair in activated), Fraction()
                )
                source_outgoing = cross_source + light_source + heavy_source
                if entering + free_edge != production + source_outgoing:
                    raise AssertionError(
                        "source-weighted production-compatible identity failed"
                    )

                full_capacity_outgoing = (
                    cross_source + light_capacity + heavy_source
                )
                if full_capacity_outgoing < source_outgoing:
                    raise AssertionError(
                        "full target capacity fell below source-weighted output"
                    )

                counts["local_pairs"] += len(local)
                counts["cross_pairs"] += len(cross_rows)
                counts["hole_pairs"] += len(hole_rows)
                counts["light_supports"] += len(support_light_load)
                counts["light_supports_partially_used"] += sum(
                    0 < load < pair_weight(support)
                    for support, load in support_light_load.items()
                )

                total_entering += entering
                total_source_outgoing += source_outgoing
                total_full_capacity_outgoing += full_capacity_outgoing
                total_light_source += light_source
                total_light_capacity += light_capacity
                total_heavy_source += heavy_source
                total_free_edge += free_edge
                profile_rows.append(
                    (
                        tuple(sorted(parent)),
                        base,
                        tuple(sorted(activated)),
                        str(entering),
                        str(free_edge),
                        str(cross_source),
                        str(light_source),
                        str(light_capacity),
                        str(heavy_source),
                    )
                )

    if counts["activated_families"] != 1769:
        raise AssertionError("source-weighted activated-family count changed")
    amplification = total_full_capacity_outgoing - total_source_outgoing
    if amplification < 0:
        raise AssertionError("negative full-capacity amplification")

    output: dict[str, object] = {
        "schema": "source_weighted_direct_discharge_small_box_v1",
        "relative_universe": [1, 12],
        "relative_maximal_parents": len(maximal_parents),
        "counts": dict(sorted(counts.items())),
        "masses": {
            "entering": str(total_entering),
            "free_edge": str(total_free_edge),
            "source_weighted_outgoing": str(total_source_outgoing),
            "full_capacity_outgoing": str(total_full_capacity_outgoing),
            "target_capacity_amplification": str(amplification),
            "light_source": str(total_light_source),
            "light_capacity": str(total_light_capacity),
            "heavy_source": str(total_heavy_source),
            "maximum_light_utilization": str(maximum_light_utilization),
        },
        "checks": {
            "raw_source_mass_conserved_with_free_tokens": True,
            "cross_gap_moment_preserved": True,
            "light_gap_moment_nonexpanding": True,
            "aggregate_light_load_within_capacity": True,
            "full_target_capacity_not_required": True,
        },
        "profile_sha256": hashlib.sha256(
            json.dumps(profile_rows, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

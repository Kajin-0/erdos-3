#!/usr/bin/env python3
"""Apply direct completion classification to the full activated S7 pair union."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

from probe_s7_hole_support_closure import (
    build_s7,
    canonical_pair,
    read_full_hole_map,
)
from probe_sponsor_pair_transport_frontier import pair_weight, serialize_mass
from verify_retained_terminal_split import contains_three_term_ap


Pair = tuple[int, int]


def completion_candidates(pair: Pair) -> tuple[tuple[int, str, int, Fraction], ...]:
    left, right = pair
    gap = right - left
    rows = [
        (left - gap, "right_adjacent", gap, Fraction(1)),
        (right + gap, "left_adjacent", gap, Fraction(1)),
    ]
    if gap % 2 == 0:
        rows.append((left + gap // 2, "outer", gap // 2, Fraction(1, 2)))
    if any(completion <= 0 for completion, _role, _step, _coefficient in rows):
        raise AssertionError("S7 shell pair has a nonpositive completion")
    return tuple(sorted(rows))


def harmonic(values: set[int] | tuple[int, ...]) -> Fraction:
    return sum((Fraction(1, value) for value in values), Fraction())


def pair_union_mass(values: set[Pair]) -> Fraction:
    return sum((pair_weight(pair) for pair in values), Fraction())


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_direct_pair_discharge.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    payment_path = Path(sys.argv[1])
    hole_map_path = Path(sys.argv[2])
    output_path = Path(sys.argv[3])

    payment = json.loads(payment_path.read_text(encoding="utf-8"))
    source_rows = payment.get("source_rows")
    if not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks source rows")

    s7 = build_s7()
    holes = read_full_hole_map(hole_map_path)
    lower, upper = 1_048_576, 2_097_151

    activated: set[Pair] = {
        tuple(int(value) for value in row["pair"])
        for row in source_rows
    }
    if len(activated) != 75_247:
        raise AssertionError("activated S7 pair union changed")
    if any(not set(pair) <= s7 for pair in activated):
        raise AssertionError("activated pair left S7")

    classes: dict[str, set[Pair]] = defaultdict(set)
    selected_holes: list[tuple[Pair, int, str, int, Fraction, Pair]] = []

    for pair in sorted(activated):
        candidates = completion_candidates(pair)
        roots = [row for row in candidates if row[0] in s7]
        if roots:
            classes["S7_edge_supported"].add(pair)
            continue

        certified = [row for row in candidates if row[0] in holes]
        if certified:
            completion, role, step, coefficient = min(certified)
            support = canonical_pair(*holes[completion])
            selected_holes.append(
                (pair, completion, role, step, coefficient, support)
            )
            classes["certified_S7_hole"].add(pair)
            continue

        if all(lower <= row[0] <= upper for row in candidates):
            classes["S7_admissible_extension"].add(pair)
        else:
            classes["ambient_outside_S7_shell"].add(pair)

    groups: dict[tuple[Pair, int, str, Fraction], set[int]] = defaultdict(set)
    roles_by_support: dict[Pair, set[tuple[int, str, Fraction]]] = defaultdict(set)
    for _pair, completion, role, step, coefficient, support in selected_holes:
        groups[(support, completion, role, coefficient)].add(step)
        roles_by_support[support].add((completion, role, coefficient))

    light_supports: set[Pair] = set()
    light_load = Fraction()
    heavy_load = Fraction()
    heavy_roles: list[dict[str, object]] = []
    maximum_roles = 0

    # Every entering activated pair is reserved.  The exact S7 diagnostic has no
    # certified cross-shell ambient-root set, so only the entering union is used.
    reserve = set(activated)

    for support, roles in sorted(roles_by_support.items()):
        multiplicity = len(roles)
        maximum_roles = max(maximum_roles, multiplicity)
        if multiplicity > 6:
            raise AssertionError("canonical support exceeds six role fibers")
        threshold = (
            Fraction()
            if support in reserve
            else pair_weight(support) / multiplicity
        )
        for completion, role, coefficient in sorted(roles):
            steps = groups[(support, completion, role, coefficient)]
            load = coefficient * harmonic(steps)
            if load <= threshold:
                light_supports.add(support)
                light_load += load
            else:
                heavy_load += load
                heavy_roles.append(
                    {
                        "support": support,
                        "completion": completion,
                        "role": role,
                        "coefficient": coefficient,
                        "steps": tuple(sorted(steps)),
                        "load": load,
                    }
                )

    if light_supports & reserve:
        raise AssertionError("direct light support overlaps entering pair union")
    light_capacity = pair_union_mass(light_supports)
    if light_load > light_capacity:
        raise AssertionError("direct light load exceeds support capacity")

    hole_target_mass = pair_union_mass(classes["certified_S7_hole"])
    grouped_hole_mass = sum(
        (
            coefficient * harmonic(steps)
            for (_support, _completion, _role, coefficient), steps in groups.items()
        ),
        Fraction(),
    )
    if grouped_hole_mass != hole_target_mass:
        raise AssertionError("direct S7 hole-fiber identity failed")
    if hole_target_mass > light_capacity + heavy_load:
        raise AssertionError("direct S7 hole transfer failed")

    terminal_shells = 0
    recursive_shells = 0
    terminal_mass = Fraction()
    recursive_mass = Fraction()
    shell_profile = Counter()

    for row in heavy_roles:
        coefficient = row["coefficient"]
        steps = row["steps"]
        assert isinstance(coefficient, Fraction)
        assert isinstance(steps, tuple)
        shells: dict[int, set[int]] = defaultdict(set)
        for step in steps:
            shell_base = 1 << (int(step).bit_length() - 1)
            shells[shell_base].add(int(step))
        for shell_base, shell_steps in shells.items():
            mass = coefficient * harmonic(shell_steps)
            shell_profile[shell_base] += 1
            if contains_three_term_ap(tuple(sorted(shell_steps))):
                recursive_shells += 1
                recursive_mass += mass
            else:
                terminal_shells += 1
                terminal_mass += mass

    if terminal_mass + recursive_mass != heavy_load:
        raise AssertionError("direct heavy terminal/recursive split failed")

    class_mass = {
        name: pair_union_mass(values)
        for name, values in classes.items()
    }
    activated_mass = pair_union_mass(activated)
    partition_mass = sum(class_mass.values(), Fraction())
    if partition_mass != activated_mass:
        raise AssertionError("direct completion classes do not partition activated mass")

    direct_rhs = (
        class_mass.get("S7_edge_supported", Fraction())
        + light_capacity
        + heavy_load
        + class_mass.get("S7_admissible_extension", Fraction())
        + class_mass.get("ambient_outside_S7_shell", Fraction())
    )
    if activated_mass > direct_rhs:
        raise AssertionError("finite S7 direct-discharge inequality failed")

    output = {
        "schema": "s7_direct_pair_discharge_profile_v1",
        "scope": "full activated physical pair union on the refined R4_to_F5 S7 frontier",
        "maximal_ambient_assumed": False,
        "generation_six_propagated": False,
        "counts": {
            "activated_pairs": len(activated),
            "S7_edge_supported_pairs": len(classes["S7_edge_supported"]),
            "certified_S7_hole_pairs": len(classes["certified_S7_hole"]),
            "S7_admissible_extension_pairs": len(
                classes["S7_admissible_extension"]
            ),
            "ambient_outside_S7_shell_pairs": len(
                classes["ambient_outside_S7_shell"]
            ),
            "canonical_supports": len(roles_by_support),
            "maximum_roles_per_support": maximum_roles,
            "light_support_pairs": len(light_supports),
            "heavy_role_fibers": len(heavy_roles),
            "terminal_heavy_shells": terminal_shells,
            "recursive_heavy_shells": recursive_shells,
        },
        "masses": {
            "activated_pair_union": serialize_mass(activated_mass),
            "S7_edge_supported": serialize_mass(
                class_mass.get("S7_edge_supported", Fraction())
            ),
            "certified_S7_hole": serialize_mass(hole_target_mass),
            "S7_admissible_extension": serialize_mass(
                class_mass.get("S7_admissible_extension", Fraction())
            ),
            "ambient_outside_S7_shell": serialize_mass(
                class_mass.get("ambient_outside_S7_shell", Fraction())
            ),
            "light_target_load": serialize_mass(light_load),
            "light_support_capacity": serialize_mass(light_capacity),
            "heavy_load": serialize_mass(heavy_load),
            "terminal_heavy_mass": serialize_mass(terminal_mass),
            "recursive_heavy_mass": serialize_mass(recursive_mass),
            "finite_direct_rhs": serialize_mass(direct_rhs),
            "finite_direct_slack": serialize_mass(direct_rhs - activated_mass),
        },
        "heavy_shell_profile": [
            {"shell_base": shell_base, "shells": shell_profile[shell_base]}
            for shell_base in sorted(shell_profile)
        ],
        "hashes": {
            "activated_pairs": hashlib.sha256(
                json.dumps(sorted(activated), separators=(",", ":")).encode("utf-8")
            ).hexdigest(),
            "selected_holes": hashlib.sha256(
                json.dumps(
                    [
                        (
                            pair,
                            completion,
                            role,
                            step,
                            str(coefficient),
                            support,
                        )
                        for pair, completion, role, step, coefficient, support
                        in selected_holes
                    ],
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest(),
            "light_supports": hashlib.sha256(
                json.dumps(sorted(light_supports), separators=(",", ":")).encode(
                    "utf-8"
                )
            ).hexdigest(),
        },
        "checks": {
            "activated_partition_identity": partition_mass == activated_mass,
            "hole_fiber_identity": grouped_hole_mass == hole_target_mass,
            "light_support_disjoint_from_entering": not (light_supports & reserve),
            "light_load_bounded_by_capacity": light_load <= light_capacity,
            "heavy_split_identity": terminal_mass + recursive_mass == heavy_load,
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    output_path.write_text(json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

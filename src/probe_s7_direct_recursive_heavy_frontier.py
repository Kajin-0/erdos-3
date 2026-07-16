#!/usr/bin/env python3
"""Profile the recursive heavy shells from direct S7 activated-pair discharge."""
from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import gcd
from pathlib import Path
import hashlib
import json
import sys

from probe_s7_direct_pair_discharge import completion_candidates, harmonic
from probe_s7_hole_support_closure import build_s7, canonical_pair, read_full_hole_map
from probe_sponsor_pair_transport_frontier import pair_weight, serialize_mass
from verify_retained_terminal_split import contains_three_term_ap
from verify_s7_regenerative_seed_policy_dependence import all_three_aps


Pair = tuple[int, int]


def pair_energy(values: tuple[int, ...]) -> Fraction:
    return sum(
        (Fraction(1, right - left) for left, right in combinations(values, 2)),
        Fraction(),
    )


def normalized_shape(values: tuple[int, ...]) -> tuple[int, ...]:
    minimum = values[0]
    shifts = tuple(value - minimum for value in values)
    common = 0
    for value in shifts[1:]:
        common = gcd(common, value)
    if common == 0:
        return tuple(0 for _ in values)
    return tuple(value // common for value in shifts)


def main() -> int:
    if len(sys.argv) != 4:
        raise SystemExit(
            "usage: probe_s7_direct_recursive_heavy_frontier.py "
            "TERMINAL_PAYMENT_JSON FULL_S7_HOLE_MAP_TSV OUTPUT_JSON"
        )

    payment = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    source_rows = payment.get("source_rows")
    if not isinstance(source_rows, list):
        raise AssertionError("terminal-payment payload lacks source rows")

    s7 = build_s7()
    holes = read_full_hole_map(Path(sys.argv[2]))
    activated: set[Pair] = {
        tuple(int(value) for value in row["pair"])
        for row in source_rows
    }
    if len(activated) != 75_247:
        raise AssertionError("activated S7 pair union changed")

    selected_holes: list[tuple[Pair, int, str, int, Fraction, Pair]] = []
    for pair in sorted(activated):
        candidates = completion_candidates(pair)
        if any(completion in s7 for completion, _role, _step, _alpha in candidates):
            continue
        certified = [
            row for row in candidates if row[0] in holes
        ]
        if not certified:
            continue
        completion, role, step, coefficient = min(certified)
        selected_holes.append(
            (
                pair,
                completion,
                role,
                step,
                coefficient,
                canonical_pair(*holes[completion]),
            )
        )

    groups: dict[tuple[Pair, int, str, Fraction], set[int]] = defaultdict(set)
    roles_by_support: dict[Pair, set[tuple[int, str, Fraction]]] = defaultdict(set)
    for _pair, completion, role, step, coefficient, support in selected_holes:
        groups[(support, completion, role, coefficient)].add(step)
        roles_by_support[support].add((completion, role, coefficient))

    recursive_rows: list[dict[str, object]] = []
    terminal_shells = 0
    for support, roles in sorted(roles_by_support.items()):
        multiplicity = len(roles)
        threshold = (
            Fraction()
            if support in activated
            else pair_weight(support) / multiplicity
        )
        for completion, role, coefficient in sorted(roles):
            steps = groups[(support, completion, role, coefficient)]
            role_load = coefficient * harmonic(steps)
            if role_load <= threshold:
                continue
            shells: dict[int, set[int]] = defaultdict(set)
            for step in steps:
                shell_base = 1 << (step.bit_length() - 1)
                shells[shell_base].add(step)
            for shell_base, shell_steps in sorted(shells.items()):
                state = tuple(sorted(shell_steps))
                if not contains_three_term_ap(state):
                    terminal_shells += 1
                    continue
                aps = tuple(all_three_aps(frozenset(state)))
                mass = coefficient * harmonic(state)
                energy = coefficient * pair_energy(state)
                recursive_rows.append(
                    {
                        "support": support,
                        "completion": completion,
                        "role": role,
                        "coefficient": coefficient,
                        "shell_base": shell_base,
                        "state": state,
                        "shape": normalized_shape(state),
                        "size": len(state),
                        "three_ap_count": len(aps),
                        "three_aps": aps,
                        "mass": mass,
                        "pair_energy": energy,
                    }
                )

    if len(recursive_rows) != 278:
        raise AssertionError(
            f"direct recursive heavy shell count changed: {len(recursive_rows)}"
        )
    if terminal_shells != 23_638:
        raise AssertionError("direct terminal heavy shell count changed")

    identity_rows: dict[
        tuple[int, str, tuple[int, ...]], list[dict[str, object]]
    ] = defaultdict(list)
    embedded_rows: dict[
        tuple[int, str, int, tuple[int, ...]], list[dict[str, object]]
    ] = defaultdict(list)
    for row in recursive_rows:
        coefficient = row["coefficient"]
        assert isinstance(coefficient, Fraction)
        state = row["state"]
        assert isinstance(state, tuple)
        identity = (int(row["shell_base"]), str(coefficient), state)
        embedded = (
            int(row["completion"]),
            str(row["role"]),
            int(row["shell_base"]),
            state,
        )
        identity_rows[identity].append(row)
        embedded_rows[embedded].append(row)

    occurrence_mass = sum((row["mass"] for row in recursive_rows), Fraction())
    occurrence_energy = sum(
        (row["pair_energy"] for row in recursive_rows), Fraction()
    )
    union_mass = sum(
        (members[0]["mass"] for members in identity_rows.values()), Fraction()
    )
    union_energy = sum(
        (members[0]["pair_energy"] for members in identity_rows.values()), Fraction()
    )

    if any(len(rows) != 1 for rows in embedded_rows.values()):
        raise AssertionError("one embedded recursive shell occurs more than once")

    size_profile = Counter(int(row["size"]) for row in recursive_rows)
    ap_profile = Counter(int(row["three_ap_count"]) for row in recursive_rows)
    shell_profile = Counter(int(row["shell_base"]) for row in recursive_rows)
    coefficient_profile = Counter(str(row["coefficient"]) for row in recursive_rows)
    multiplicity_profile = Counter(len(rows) for rows in identity_rows.values())
    shape_profile = Counter(tuple(row["shape"]) for row in recursive_rows)

    minimum_energy_surplus: Fraction | None = None
    minimum_surplus_row: dict[str, object] | None = None
    for row in recursive_rows:
        surplus = row["pair_energy"] - row["mass"]
        assert isinstance(surplus, Fraction)
        if minimum_energy_surplus is None or surplus < minimum_energy_surplus:
            minimum_energy_surplus = surplus
            minimum_surplus_row = row

    output = {
        "schema": "s7_direct_recursive_heavy_frontier_v1",
        "scope": "recursive heavy shells after direct S7 activated-pair discharge",
        "maximal_ambient_assumed": False,
        "generation_six_propagated": False,
        "counts": {
            "recursive_shell_occurrences": len(recursive_rows),
            "distinct_numerical_state_identities": len(identity_rows),
            "distinct_embedded_states": len(embedded_rows),
            "terminal_heavy_shells_excluded": terminal_shells,
            "maximum_numerical_state_multiplicity": max(multiplicity_profile),
            "maximum_state_size": max(size_profile),
            "maximum_three_ap_count": max(ap_profile),
            "distinct_normalized_shapes": len(shape_profile),
        },
        "masses": {
            "recursive_occurrence_mass": serialize_mass(occurrence_mass),
            "recursive_numerical_union_mass": serialize_mass(union_mass),
            "recursive_occurrence_pair_energy": serialize_mass(occurrence_energy),
            "recursive_numerical_union_pair_energy": serialize_mass(union_energy),
            "occurrence_pair_energy_surplus": serialize_mass(
                occurrence_energy - occurrence_mass
            ),
            "minimum_state_pair_energy_surplus": serialize_mass(
                minimum_energy_surplus or Fraction()
            ),
        },
        "profiles": {
            "size": [
                {"size": value, "shells": size_profile[value]}
                for value in sorted(size_profile)
            ],
            "three_ap_count": [
                {"three_aps": value, "shells": ap_profile[value]}
                for value in sorted(ap_profile)
            ],
            "shell_base": [
                {"shell_base": value, "shells": shell_profile[value]}
                for value in sorted(shell_profile)
            ],
            "coefficient": [
                {"coefficient": value, "shells": coefficient_profile[value]}
                for value in sorted(coefficient_profile)
            ],
            "multiplicity": [
                {"multiplicity": value, "states": multiplicity_profile[value]}
                for value in sorted(multiplicity_profile)
            ],
            "top_shapes": [
                {"shape": shape, "occurrences": count}
                for shape, count in sorted(
                    shape_profile.items(), key=lambda item: (-item[1], item[0])
                )[:20]
            ],
        },
        "minimum_surplus_witness": {
            "shell_base": minimum_surplus_row["shell_base"],
            "coefficient": str(minimum_surplus_row["coefficient"]),
            "state": minimum_surplus_row["state"],
            "mass": str(minimum_surplus_row["mass"]),
            "pair_energy": str(minimum_surplus_row["pair_energy"]),
        }
        if minimum_surplus_row is not None
        else None,
        "hashes": {
            "recursive_rows": hashlib.sha256(
                json.dumps(
                    [
                        (
                            row["support"],
                            row["completion"],
                            row["role"],
                            str(row["coefficient"]),
                            row["shell_base"],
                            row["state"],
                            row["shape"],
                            row["three_aps"],
                        )
                        for row in recursive_rows
                    ],
                    separators=(",", ":"),
                ).encode("utf-8")
            ).hexdigest(),
        },
        "checks": {
            "embedded_state_first_appearance": len(embedded_rows) == len(recursive_rows),
            "pair_energy_dominates_each_recursive_state": (
                minimum_energy_surplus is not None and minimum_energy_surplus >= 0
            ),
        },
    }
    canonical = json.dumps(output, sort_keys=True, separators=(",", ":"))
    output["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    Path(sys.argv[3]).write_text(
        json.dumps(output, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Verify exact-gap light-transition geometry and the two-syndetic bound."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json


Pair = tuple[int, int]


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate pair")
    return (left, right) if left < right else (right, left)


def canonical_pair(witness: tuple[int, int, int, int], missing: int) -> Pair:
    for index in range(3):
        if index != missing and index + 1 != missing:
            return witness[index], witness[index + 1]
    raise AssertionError("witness has no canonical adjacent pair")


def completion_candidates(pair: Pair) -> set[int]:
    left, right = pair
    gap = right - left
    rows = {left - gap, right + gap}
    if gap % 2 == 0:
        rows.add(left + gap // 2)
    return rows


def transition_profile() -> list[dict[str, object]]:
    # Use physical gap D=2 so all midpoint coordinates and the lattice unit
    # h=3D/2 are integral.
    gap = 2
    completion = 0
    lattice_unit = 3
    sources: dict[str, Pair] = {
        "right_adjacent": (completion + gap, completion + 2 * gap),
        "left_adjacent": (completion - 2 * gap, completion - gap),
        "outer": (completion - gap // 2, completion + gap // 2),
    }

    rows: list[dict[str, object]] = []
    nonterminal_shifts: list[int] = []
    for role, source in sources.items():
        for missing in range(4):
            start = completion - missing * gap
            witness = tuple(start + index * gap for index in range(4))
            roots = set(witness)
            roots.remove(completion)
            support = canonical_pair(witness, missing)
            if support[1] - support[0] != gap:
                raise AssertionError("canonical support changed exact gap")

            reserved_self = support == source
            guaranteed_roots = roots | set(source)
            local_completions = completion_candidates(support) & guaranteed_roots
            local_terminal = bool(local_completions)
            shift = Fraction(support[0] - source[0], lattice_unit)

            if not reserved_self and not local_terminal:
                if shift.denominator != 1 or abs(shift.numerator) not in {1, 2}:
                    raise AssertionError(
                        "nonterminal exact-gap transition left the +/-1,+/-2 lattice"
                    )
                nonterminal_shifts.append(shift.numerator)

            rows.append(
                {
                    "role": role,
                    "missing_index": missing,
                    "source": source,
                    "witness": witness,
                    "support": support,
                    "reserved_self": reserved_self,
                    "local_terminal": local_terminal,
                    "local_completion_roots": tuple(sorted(local_completions)),
                    "normalized_left_shift": str(shift),
                }
            )

    if sorted(nonterminal_shifts) != [-2, -1, 1, 2]:
        raise AssertionError(
            f"exact-gap nonterminal shift profile changed: {nonterminal_shifts}"
        )
    return rows


def contains_four_ap(bits: tuple[int, ...]) -> bool:
    occupied = {index for index, bit in enumerate(bits) if bit}
    if not occupied:
        return False
    upper = max(occupied)
    for left in occupied:
        for step in range(1, (upper - left) // 3 + 1):
            if all(left + index * step in occupied for index in range(4)):
                return True
    return False


def two_syndetic_profile() -> tuple[list[dict[str, int]], list[tuple[int, ...]]]:
    expected_counts = [1, 2, 3, 4, 6, 9, 8, 8, 12, 11, 9, 6, 3, 4, 3, 1, 0]
    sequences: list[tuple[int, ...]] = [(1,)]
    profile: list[dict[str, int]] = []
    final_nonempty: list[tuple[int, ...]] = []

    for length, expected in enumerate(expected_counts, start=1):
        if length == 1:
            current = sequences
        else:
            current = []
            for sequence in sequences:
                for bit in (0, 1):
                    if sequence[-1] == 0 and bit == 0:
                        continue
                    candidate = sequence + (bit,)
                    if not contains_four_ap(candidate):
                        current.append(candidate)
            sequences = current

        if len(current) != expected:
            raise AssertionError(
                f"two-syndetic profile changed at length {length}: {len(current)}"
            )
        profile.append(
            {
                "length": length,
                "valid_strings": len(current),
                "maximum_occupied": max((sum(row) for row in current), default=0),
            }
        )
        if current:
            final_nonempty = current

    if profile[-1]["valid_strings"] != 0:
        raise AssertionError("a valid two-syndetic length-17 string survived")
    if max(sum(row) for row in final_nonempty) != 9:
        raise AssertionError("maximum two-syndetic four-AP-free cardinality changed")
    return profile, final_nonempty


def main() -> int:
    transitions = transition_profile()
    profile, extremal = two_syndetic_profile()

    payload = {
        "schema": "exact_gap_light_persistence_v1",
        "normalized_physical_gap": 2,
        "normalized_lattice_unit": 3,
        "nonterminal_shift_set": [-2, -1, 1, 2],
        "maximum_nonterminal_pair_identities": 9,
        "maximum_episode_pair_identities_with_final_local_sink": 10,
        "transition_profile": transitions,
        "two_syndetic_profile": profile,
        "extremal_length_16_strings": [
            "".join(str(bit) for bit in row) for row in extremal
        ],
        "hashes": {
            "transition_profile": hashlib.sha256(
                json.dumps(transitions, sort_keys=True, separators=(",", ":")).encode(
                    "utf-8"
                )
            ).hexdigest(),
            "two_syndetic_profile": hashlib.sha256(
                json.dumps(profile, sort_keys=True, separators=(",", ":")).encode(
                    "utf-8"
                )
            ).hexdigest(),
        },
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    print(json.dumps(payload, sort_keys=True, indent=2))
    print("verified: exact-gap light-support persistence bound")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

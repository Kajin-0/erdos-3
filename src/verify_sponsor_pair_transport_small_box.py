#!/usr/bin/env python3
"""Independent exhaustive checks for sponsor-pair transport on small parents.

This verifier intentionally does not import the production transport probe.  It
reconstructs the lexicographic coordinated-deletion schedule, pair transport,
terminal completion map, source-weighted collision row, and residual-minimum
star charge directly for every four-AP-free subset of [1, 12].
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations

Pair = tuple[int, int]
Action = dict[str, int]


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 requires a positive integer")
    return (value & -value).bit_length() - 1


def ordered_pair(left: int, right: int) -> Pair:
    if left == right:
        raise AssertionError("degenerate pair")
    return (left, right) if left < right else (right, left)


def pair_weight(pair: Pair) -> Fraction:
    return Fraction(1, pair[1] - pair[0])


def three_aps(values: set[int]) -> tuple[tuple[int, int, int, int], ...]:
    if not values:
        return ()
    upper = max(values)
    rows: list[tuple[int, int, int, int]] = []
    for left in sorted(values):
        for step in range(1, (upper - left) // 2 + 1):
            middle = left + step
            right = left + 2 * step
            if middle in values and right in values:
                rows.append((step, left, middle, right))
    return tuple(sorted(rows))


def contains_four_ap(values: set[int]) -> bool:
    if not values:
        return False
    upper = max(values)
    for left in sorted(values):
        for step in range(1, (upper - left) // 3 + 1):
            if all(left + offset * step in values for offset in range(4)):
                return True
    return False


def build_schedule(values: set[int]) -> dict[str, object]:
    current = set(values)
    selected: list[Action] = []
    tau: dict[int, int] = {}
    actions: dict[int, Action] = {}

    for step, left, middle, right in three_aps(values):
        if not {left, middle, right} <= current:
            continue
        sponsor = left if v2(step) % 2 == 0 else right
        opposite = right if sponsor == left else left
        epsilon = 1 if middle > sponsor else -1
        action = {
            "rank": len(selected),
            "sponsor": sponsor,
            "middle": middle,
            "opposite": opposite,
            "q": step,
            "epsilon": epsilon,
        }
        selected.append(action)
        tau[sponsor] = action["rank"]
        actions[sponsor] = action
        current.remove(sponsor)

    if three_aps(current):
        raise AssertionError("lexicographic residual contains a three-AP")
    if set(tau) & current:
        raise AssertionError("residual/sponsor partition overlaps")
    if set(tau) | current != values:
        raise AssertionError("residual/sponsor partition is incomplete")

    return {
        "roots": set(values),
        "selected": tuple(selected),
        "tau": tau,
        "actions": actions,
        "residual": current,
        "sponsors": set(tau),
    }


def terminal_data(
    target: Pair,
    terminal_class: str,
    schedule: dict[str, object],
) -> tuple[int | None, tuple[int, int, int] | None]:
    tau: dict[int, int] = schedule["tau"]  # type: ignore[assignment]
    actions: dict[int, Action] = schedule["actions"]  # type: ignore[assignment]

    if terminal_class == "residual":
        left, right = target
        completion = 2 * right - left
        return completion, tuple(sorted((left, right, completion)))

    owners = [value for value in target if value in tau]
    if not owners:
        raise AssertionError("non-residual terminal target has no owner")
    sponsor = min(owners, key=lambda value: tau[value])
    other = target[1] if target[0] == sponsor else target[0]
    action = actions[sponsor]

    if terminal_class == "direct":
        middle = action["middle"]
        opposite = action["opposite"]
        if other == middle:
            completion = opposite
        elif other == opposite:
            completion = middle
        else:
            raise AssertionError("direct target is not a selected-action edge")
        return completion, tuple(sorted((sponsor, other, completion)))

    if terminal_class != "backward":
        raise AssertionError(f"unknown terminal class: {terminal_class}")
    completion = 2 * sponsor - other
    return completion, tuple(sorted((other, sponsor, completion)))


def transport(pair: Pair, schedule: dict[str, object]) -> dict[str, object]:
    tau: dict[int, int] = schedule["tau"]  # type: ignore[assignment]
    actions: dict[int, Action] = schedule["actions"]  # type: ignore[assignment]
    residual: set[int] = schedule["residual"]  # type: ignore[assignment]

    current = pair
    previous_rank = -1
    path: list[Pair] = []
    while True:
        left, right = current
        left_rank = tau.get(left)
        right_rank = tau.get(right)
        if left_rank is None and right_rank is None:
            if left not in residual or right not in residual:
                raise AssertionError("transport ended outside the residual")
            completion, witness = terminal_data(current, "residual", schedule)
            return {
                "terminal_class": "residual",
                "target": current,
                "completion": completion,
                "witness": witness,
                "path": tuple(path),
            }

        if right_rank is None or (
            left_rank is not None and left_rank < right_rank
        ):
            sponsor, other, rank = left, right, left_rank
        else:
            sponsor, other, rank = right, left, right_rank
        if rank is None or rank <= previous_rank:
            raise AssertionError("deletion rank did not increase")

        action = actions[sponsor]
        middle = action["middle"]
        opposite = action["opposite"]
        if other == middle or other == opposite:
            completion, witness = terminal_data(current, "direct", schedule)
            return {
                "terminal_class": "direct",
                "target": current,
                "completion": completion,
                "witness": witness,
                "path": tuple(path),
            }

        if abs(other - middle) > abs(other - sponsor):
            completion, witness = terminal_data(current, "backward", schedule)
            return {
                "terminal_class": "backward",
                "target": current,
                "completion": completion,
                "witness": witness,
                "path": tuple(path),
            }

        updated = ordered_pair(middle, other)
        if pair_weight(updated) < pair_weight(current):
            raise AssertionError("forward transport decreased pair weight")
        next_ranks = [tau[value] for value in updated if value in tau]
        if next_ranks and min(next_ranks) <= rank:
            raise AssertionError("forward transport did not raise minimum rank")
        path.append(updated)
        current = updated
        previous_rank = rank


def verify_completed_target_capacity(
    roots: set[int],
    target_results: dict[Pair, dict[str, object]],
) -> None:
    assigned: dict[tuple[int, int, int], set[Pair]] = defaultdict(set)
    completed_mass = Fraction()
    for target, result in target_results.items():
        completion = int(result["completion"])
        if result["terminal_class"] == "direct" or completion in roots:
            witness = result["witness"]
            if witness is None:
                raise AssertionError("completed target has no witness")
            witness_tuple = tuple(int(value) for value in witness)
            left, middle, right = witness_tuple
            if middle - left != right - middle or not set(witness_tuple) <= roots:
                raise AssertionError("invalid completed-target witness")
            if not set(target) <= set(witness_tuple):
                raise AssertionError("target is not an edge of its witness")
            assigned[witness_tuple].add(target)
            completed_mass += pair_weight(target)

    witness_capacity = Fraction()
    for witness, edges in assigned.items():
        step = witness[1] - witness[0]
        edge_mass = sum((pair_weight(edge) for edge in edges), Fraction())
        if edge_mass > Fraction(5, 2 * step):
            raise AssertionError("one three-AP exceeded its three-edge capacity")
        witness_capacity += Fraction(5, 2 * step)

    total_parent_capacity = Fraction(5, 2) * sum(
        (Fraction(1, step) for step, _left, _middle, _right in three_aps(roots)),
        Fraction(),
    )
    if completed_mass > witness_capacity or witness_capacity > total_parent_capacity:
        raise AssertionError("completed terminal target capacity failed")


def verify_collision_row(
    sources_by_target: dict[Pair, list[Pair]],
) -> None:
    initial_mass = Fraction()
    target_union_mass = Fraction()
    first_source_mass = Fraction()
    source_collision_mass = Fraction()
    terminal_collision_mass = Fraction()

    for target, sources in sources_by_target.items():
        weights = [pair_weight(source) for source in sources]
        maximum = max(weights)
        target_weight = pair_weight(target)
        if any(weight > target_weight for weight in weights):
            raise AssertionError("source weight exceeds terminal target weight")
        initial_mass += sum(weights, Fraction())
        target_union_mass += target_weight
        first_source_mass += maximum
        source_collision_mass += sum(weights, Fraction()) - maximum
        terminal_collision_mass += (len(sources) - 1) * target_weight

    if initial_mass != first_source_mass + source_collision_mass:
        raise AssertionError("source first-use/collision identity failed")
    if first_source_mass > target_union_mass:
        raise AssertionError("first-source mass exceeds target union")
    if source_collision_mass > terminal_collision_mass:
        raise AssertionError("source-weight collision does not refine terminal collision")
    if initial_mass > target_union_mass + source_collision_mass:
        raise AssertionError("source-weight transport inequality failed")


def verify_residual_minimum_star(values: set[int], schedule: dict[str, object]) -> None:
    if not values:
        return
    residual: set[int] = schedule["residual"]  # type: ignore[assignment]
    actions: dict[int, Action] = schedule["actions"]  # type: ignore[assignment]
    minimum = min(values)
    if minimum not in residual:
        return

    incidence = sum(
        (Fraction(1, action["q"]) for action in actions.values()), Fraction()
    )
    far_mass = Fraction()
    close_mass = Fraction()
    missing_mass = Fraction()
    close_charges: set[int] = set()

    for sponsor, action in actions.items():
        if action["epsilon"] != 1:
            continue
        result = transport(ordered_pair(minimum, sponsor), schedule)
        if result["terminal_class"] != "backward":
            raise AssertionError("left-sponsored residual-minimum star is not backward")

        gap = sponsor - minimum
        step = action["q"]
        if gap == step:
            raise AssertionError("equal-scale star creates a forbidden four-AP")
        if gap > step:
            far_mass += Fraction(1, gap)
            continue

        completion = 2 * sponsor - minimum
        if completion not in values:
            missing_mass += Fraction(1, gap)
            continue

        completion_action = actions.get(completion)
        if completion_action is None or completion_action["q"] > gap:
            raise AssertionError("close-star completion lacks an earlier charge")
        if completion in close_charges:
            raise AssertionError("close-star completion charge is not injective")
        close_charges.add(completion)
        close_mass += Fraction(1, gap)

    if far_mass > incidence or close_mass > incidence:
        raise AssertionError("residual-minimum star incidence charge failed")
    if far_mass + close_mass + missing_mass > 2 * incidence + missing_mass:
        raise AssertionError("residual-minimum star completion inequality failed")


def verify_parent(values: set[int]) -> tuple[int, int]:
    schedule = build_schedule(values)
    sponsors: set[int] = schedule["sponsors"]  # type: ignore[assignment]
    if not sponsors:
        return 0, 0

    sources = [
        pair
        for pair in combinations(sorted(values), 2)
        if set(pair) & sponsors
    ]
    sources_by_target: dict[Pair, list[Pair]] = defaultdict(list)
    target_results: dict[Pair, dict[str, object]] = {}
    for pair in sources:
        result = transport(pair, schedule)
        target: Pair = result["target"]  # type: ignore[assignment]
        sources_by_target[target].append(pair)
        previous = target_results.get(target)
        if previous is not None and (
            previous["terminal_class"] != result["terminal_class"]
            or previous["completion"] != result["completion"]
        ):
            raise AssertionError("one target has inconsistent terminal semantics")
        target_results[target] = result

    verify_collision_row(sources_by_target)
    verify_completed_target_capacity(values, target_results)
    verify_residual_minimum_star(values, schedule)
    return len(sources), len(target_results)


def main() -> int:
    universe = tuple(range(1, 13))
    checked_parents = 0
    scheduled_parents = 0
    activated_pairs = 0
    terminal_targets = 0

    for mask in range(1 << len(universe)):
        values = {
            universe[index]
            for index in range(len(universe))
            if (mask >> index) & 1
        }
        if contains_four_ap(values):
            continue
        checked_parents += 1
        sources, targets = verify_parent(values)
        if sources:
            scheduled_parents += 1
            activated_pairs += sources
            terminal_targets += targets

    print("sponsor_pair_transport_small_box_v1")
    print("universe=[1,12]")
    print(f"four_ap_free_parents={checked_parents}")
    print(f"parents_with_selected_actions={scheduled_parents}")
    print(f"activated_pair_checks={activated_pairs}")
    print(f"terminal_target_checks={terminal_targets}")
    print("source_weighted_collision=true")
    print("terminal_completion_capacity=true")
    print("residual_minimum_star_charge=true")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

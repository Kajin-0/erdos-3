#!/usr/bin/env python3
"""Resolve terminal-token collisions across second and third retained generations."""
from __future__ import annotations

import hashlib
import json
import sys

from probe_third_generation_recursive_frontier import propagate_recursive_states
from verify_retained_provenance_scale_profile import reconstruct_retained_families
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def point_records(states: tuple[object, ...], generation: int) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for state in states:
        representative = state.representative
        for value, root, immediate in zip(
            state.values,
            representative.provenance,
            representative.immediate_provenance,
            strict=True,
        ):
            records.append(
                {
                    "generation": generation,
                    "class_index": state.index,
                    "representative": representative.index,
                    "parent_class": representative.parent_class,
                    "source": representative.source,
                    "source_step": representative.source_step,
                    "exponent": representative.exponent,
                    "u": value,
                    "p": root,
                    "immediate": immediate,
                    "state_values": list(state.values),
                }
            )
    return records


def signature(record: dict[str, object], mode: str) -> tuple[object, ...]:
    if mode == "u_p":
        return (record["u"], record["p"])
    if mode == "u_p_immediate":
        return (record["u"], record["p"], record["immediate"])
    if mode == "u_p_source":
        return (
            record["u"],
            record["p"],
            record["source"],
            record["source_step"],
        )
    if mode == "u_p_immediate_source":
        return (
            record["u"],
            record["p"],
            record["immediate"],
            record["source"],
            record["source_step"],
        )
    raise ValueError(mode)


def collisions(
    earlier: list[dict[str, object]],
    later: list[dict[str, object]],
    mode: str,
) -> tuple[list[list[object]], list[dict[str, object]]]:
    earlier_map: dict[tuple[object, ...], list[dict[str, object]]] = {}
    later_map: dict[tuple[object, ...], list[dict[str, object]]] = {}
    for record in earlier:
        earlier_map.setdefault(signature(record, mode), []).append(record)
    for record in later:
        later_map.setdefault(signature(record, mode), []).append(record)
    shared = sorted(set(earlier_map) & set(later_map), key=repr)
    details = [
        {
            "signature": list(key),
            "earlier": earlier_map[key],
            "later": later_map[key],
        }
        for key in shared
    ]
    return [list(key) for key in shared], details


def main() -> int:
    _retained_first, retained_second = reconstruct_retained_families()
    terminal_second = tuple(
        state for state in retained_second
        if not contains_three_term_ap(state.values)
    )
    recursive_second = tuple(
        state for state in retained_second
        if contains_three_term_ap(state.values)
    )
    _occurrences, retained_third, _metrics, _child_rows = (
        propagate_recursive_states(recursive_second)
    )
    terminal_third = tuple(
        state for state in retained_third
        if not contains_three_term_ap(state.values)
    )
    recursive_third = tuple(
        state for state in retained_third
        if contains_three_term_ap(state.values)
    )

    second_records = point_records(terminal_second, 2)
    third_terminal_records = point_records(terminal_third, 3)
    third_recursive_records = point_records(recursive_third, 3)
    third_all_records = third_terminal_records + third_recursive_records

    modes = (
        "u_p",
        "u_p_immediate",
        "u_p_source",
        "u_p_immediate_source",
    )
    result: dict[str, object] = {
        "schema": "terminal_token_collision_signature_probe_v1",
        "second_terminal_records": len(second_records),
        "third_terminal_records": len(third_terminal_records),
        "third_recursive_records": len(third_recursive_records),
        "collisions": {},
    }
    collision_payload: dict[str, object] = {}
    for mode in modes:
        all_signatures, all_details = collisions(
            second_records, third_all_records, mode
        )
        terminal_signatures, terminal_details = collisions(
            second_records, third_terminal_records, mode
        )
        recursive_signatures, recursive_details = collisions(
            second_records, third_recursive_records, mode
        )
        collision_payload[mode] = {
            "all_count": len(all_signatures),
            "terminal_count": len(terminal_signatures),
            "recursive_count": len(recursive_signatures),
            "all_signatures": all_signatures,
            "terminal_signatures": terminal_signatures,
            "recursive_signatures": recursive_signatures,
            "details": all_details,
            "terminal_details": terminal_details,
            "recursive_details": recursive_details,
        }
    result["collisions"] = collision_payload
    canonical = json.dumps(result, sort_keys=True, separators=(",", ":"))
    result["probe_payload_sha256"] = hashlib.sha256(
        canonical.encode("utf-8")
    ).hexdigest()
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

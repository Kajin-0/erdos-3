#!/usr/bin/env python3
"""Compatibility entry point for first-frontier terminal correction.

First-generation retained classes use ShellOccurrence representatives, while
later generations use DescendantOccurrence representatives. Supply one
canonical signature that supports both representations.

The terminal-correction question needs retained-family and harmonic data, not a
quadratic latent-pair census. Replace that optional diagnostic with a linear
profile so this focused probe does not repeat the separate pair-resource run.
"""
from __future__ import annotations

from fractions import Fraction
import sys

import probe_first_frontier_terminal_correction as probe
from probe_root_lineage_transfer_classification import canonical_hash, serialize_mass
from verify_retained_terminal_split import contains_three_term_ap


def family_signature(states: tuple[object, ...]) -> str:
    rows = []
    for state in states:
        representative = state.representative
        provenance = tuple(representative.provenance)
        immediate = tuple(
            getattr(representative, "immediate_provenance", provenance)
        )
        rows.append(
            {
                "index": state.index,
                "values": list(state.values),
                "representative_type": type(representative).__name__,
                "representative_index": representative.index,
                "parent_class": getattr(representative, "parent_class", None),
                "source": representative.source,
                "source_step": representative.source_step,
                "exponent": representative.exponent,
                "provenance": list(provenance),
                "immediate": list(immediate),
            }
        )
    return canonical_hash(rows)


def lightweight_resource_profile(states: tuple[object, ...]) -> dict[str, object]:
    terminal = tuple(
        state for state in states if not contains_three_term_ap(state.values)
    )
    recursive = tuple(
        state for state in states if contains_three_term_ap(state.values)
    )
    terminal_mass = sum((state.weight for state in terminal), Fraction())
    recursive_mass = sum((state.weight for state in recursive), Fraction())
    return {
        "profile_scope": "linear_terminal_correction_only",
        "quadratic_pair_resource_profile_omitted": True,
        "states": len(states),
        "points": sum(len(state.values) for state in states),
        "terminal_states": len(terminal),
        "terminal_points": sum(len(state.values) for state in terminal),
        "recursive_states": len(recursive),
        "recursive_points": sum(len(state.values) for state in recursive),
        "terminal_mass": serialize_mass(terminal_mass),
        "recursive_mass": serialize_mass(recursive_mass),
        "total_mass": serialize_mass(terminal_mass + recursive_mass),
    }


probe.family_signature = family_signature
probe.resource_profile = lightweight_resource_profile


if __name__ == "__main__":
    raise SystemExit(probe.main())

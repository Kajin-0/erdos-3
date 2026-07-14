#!/usr/bin/env python3
"""Compatibility entry point for first-frontier terminal correction.

First-generation retained classes use ShellOccurrence representatives, while
later generations use DescendantOccurrence representatives.  Supply one
canonical signature that supports both representations, then run the original
exact probe unchanged.
"""
from __future__ import annotations

import sys

import probe_first_frontier_terminal_correction as probe
from probe_root_lineage_transfer_classification import canonical_hash


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


probe.family_signature = family_signature


if __name__ == "__main__":
    raise SystemExit(probe.main())

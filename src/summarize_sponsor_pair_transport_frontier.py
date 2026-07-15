#!/usr/bin/env python3
"""Write a compact deterministic summary of the sponsor-pair transport probe."""
from __future__ import annotations

from pathlib import Path
import json
import sys


def profile_line(row: dict[str, object]) -> str:
    initial = row["initial_mass"]["decimal"]  # type: ignore[index]
    target = row["target_occurrence_mass"]["decimal"]  # type: ignore[index]
    return f"{row['key']}|count={row['count']}|initial={initial}|target={target}"


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: summarize_sponsor_pair_transport_frontier.py INPUT OUTPUT")
    source = Path(sys.argv[1])
    target = Path(sys.argv[2])
    payload = json.loads(source.read_text(encoding="utf-8"))

    counts = payload["counts"]
    masses = payload["masses"]
    checks = payload["checks"]
    lines = [
        "sponsor_pair_transport_frontier_summary_v1",
        f"scope={payload['scope']}",
        f"generation_six_propagated={str(payload['generation_six_propagated']).lower()}",
        f"parent_states={counts['parent_states']}",
        f"split_retained_states={counts['split_retained_states']}",
        f"resource_occurrences={counts['resource_occurrences']}",
        f"distinct_resource_pairs={counts['distinct_resource_pairs']}",
        f"activated_distinct_pairs={counts['activated_distinct_pairs']}",
        f"inactive_residual_distinct_pairs={counts['inactive_residual_distinct_pairs']}",
        f"terminal_target_distinct_pairs={counts['terminal_target_distinct_pairs']}",
        f"terminal_collision_targets={counts['terminal_collision_targets']}",
        f"maximum_terminal_target_multiplicity={counts['maximum_terminal_target_multiplicity']}",
        f"maximum_transport_path_length={counts['maximum_transport_path_length']}",
        f"in_parent_completed_pairs={counts['in_parent_completed_pairs']}",
        f"parent_external_completion_pairs={counts['parent_external_completion_pairs']}",
        f"activated_initial_union_mass={masses['activated_initial_union']['decimal']}",
        f"terminal_target_occurrence_mass={masses['terminal_target_occurrence']['decimal']}",
        f"terminal_target_union_mass={masses['terminal_target_union']['decimal']}",
        f"transport_collision_mass={masses['transport_collision']['decimal']}",
        f"selected_action_incidence_bound={masses['selected_action_incidence_bound']['decimal']}",
        f"direct_target_union_mass={masses['direct_target_union']['decimal']}",
        f"transport_rhs={masses['transport_rhs']['decimal']}",
        f"transport_slack={masses['transport_slack']['decimal']}",
        f"transport_monotonicity={str(checks['transport_monotonicity']).lower()}",
        f"target_first_use_collision_partition={str(checks['target_first_use_collision_partition']).lower()}",
        f"direct_incidence_bound={str(checks['direct_incidence_bound']).lower()}",
        f"set_valued_transport_inequality={str(checks['set_valued_transport_inequality']).lower()}",
        "terminal_class_profile:",
    ]
    lines.extend(profile_line(row) for row in payload["terminal_class_profile"])
    lines.append("transport_path_profile:")
    lines.extend(profile_line(row) for row in payload["transport_path_profile"])
    lines.append("completion_profile:")
    lines.extend(profile_line(row) for row in payload["completion_profile"])
    lines.append(f"active_rows_sha256={payload['hashes']['active_rows']}")
    lines.append(
        f"terminal_target_counter_sha256={payload['hashes']['terminal_target_counter']}"
    )
    lines.append(f"probe_payload_sha256={payload['probe_payload_sha256']}")
    target.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

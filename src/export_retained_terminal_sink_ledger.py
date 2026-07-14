#!/usr/bin/env python3
"""Export exact numerical and provenance identities for retained terminal sinks."""
from __future__ import annotations

from pathlib import Path
from typing import Iterable
import hashlib
import json
import sys

from verify_retained_provenance_scale_profile import (
    build_ratio_rows,
    reconstruct_retained_families,
)
from verify_retained_terminal_split import contains_three_term_ap

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

EXPECTED_SECOND_RETAINED_FAMILY_SHA256 = (
    "dbb6d888c790cf5a67f2e3a6ed86400506c93baac3701f39d15d858c19b21596"
)
EXPECTED_FULL_RATIO_RECORD_BYTES = 1_287_870
EXPECTED_FULL_RATIO_RECORD_SHA256 = (
    "904b0b9f8906d196ea02369cb60153341eda5a562340ba8615dbcdb769dc92e3"
)
EXPECTED_TERMINAL_FAMILY_SHA256 = (
    "0aa2aca9246119f832bb3b58dcc090683c41fb85ed3c47d5c73d0b398dfc672e"
)
EXPECTED_COUNTS = {
    "retained_states": 27,
    "retained_points": 7_925,
    "terminal_states": 13,
    "terminal_points": 43,
    "recursive_states": 14,
    "recursive_points": 7_882,
}
CERTIFICATE_SHA256 = (
    "1f25e54d10d73c0130535d12f264405f0e5adb954820725395deb7c86ac19bf9"
)


def family_hash(states: Iterable[object]) -> str:
    payload = "".join(
        f"{state.index}:{','.join(map(str, state.values))}\n"
        for state in states
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def retained_family_hash(states: Iterable[object]) -> str:
    records = [
        {
            "class_index": state.index,
            "representative": state.representative.index,
            "parent_class": state.representative.parent_class,
            "source": state.representative.source,
            "source_step": state.representative.source_step,
            "exponent": state.representative.exponent,
            "values": list(state.values),
            "provenance": list(state.representative.provenance),
            "immediate_provenance": list(
                state.representative.immediate_provenance
            ),
        }
        for state in states
    ]
    payload = json.dumps(records, sort_keys=True, separators=(",", ":")) + "\n"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def build_ledger() -> tuple[str, str]:
    _retained_first, retained_second = reconstruct_retained_families()
    if retained_family_hash(retained_second) != EXPECTED_SECOND_RETAINED_FAMILY_SHA256:
        raise AssertionError("second-generation retained-family hash mismatch")

    terminal = tuple(
        state
        for state in retained_second
        if not contains_three_term_ap(state.values)
    )
    recursive = tuple(
        state
        for state in retained_second
        if contains_three_term_ap(state.values)
    )
    if family_hash(terminal) != EXPECTED_TERMINAL_FAMILY_SHA256:
        raise AssertionError("terminal-family hash mismatch")

    rows = build_ratio_rows(retained_second)
    ratio_payload = "".join(
        json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
        for row in rows
    )
    if len(ratio_payload.encode("utf-8")) != EXPECTED_FULL_RATIO_RECORD_BYTES:
        raise AssertionError("full ratio-record byte-count mismatch")
    if hashlib.sha256(ratio_payload.encode("utf-8")).hexdigest() != (
        EXPECTED_FULL_RATIO_RECORD_SHA256
    ):
        raise AssertionError("full ratio-record hash mismatch")

    observed = {
        "retained_states": len(retained_second),
        "retained_points": sum(len(state.values) for state in retained_second),
        "terminal_states": len(terminal),
        "terminal_points": sum(len(state.values) for state in terminal),
        "recursive_states": len(recursive),
        "recursive_points": sum(len(state.values) for state in recursive),
    }
    if observed != EXPECTED_COUNTS:
        raise AssertionError(f"terminal-ledger count mismatch: {observed!r}")

    rows_by_class: dict[int, list[dict[str, object]]] = {}
    for row in rows:
        rows_by_class.setdefault(int(row["class"]), []).append(row)

    terminal_values = {
        value for state in terminal for value in state.values
    }
    recursive_values = {
        value for state in recursive for value in state.values
    }
    if len(terminal_values) != EXPECTED_COUNTS["terminal_points"]:
        raise AssertionError("terminal numerical labels are not unique")
    if terminal_values & recursive_values:
        raise AssertionError("terminal and recursive numerical labels overlap")

    tokens: set[tuple[int, int]] = set()
    records: list[dict[str, object]] = []
    for state in terminal:
        representative = state.representative
        point_rows = rows_by_class.get(state.index, [])
        if [int(row["u"]) for row in point_rows] != list(state.values):
            raise AssertionError("terminal state and point rows are misaligned")
        for row in point_rows:
            token = (int(row["u"]), int(row["p"]))
            if token in tokens:
                raise AssertionError("duplicate terminal (u,p) token")
            tokens.add(token)
        records.append(
            {
                "class_index": state.index,
                "representative": representative.index,
                "parent_class": representative.parent_class,
                "source": representative.source,
                "source_step": representative.source_step,
                "exponent": representative.exponent,
                "values": list(state.values),
                "root_provenance": list(representative.provenance),
                "immediate_provenance": list(
                    representative.immediate_provenance
                ),
                "points": point_rows,
            }
        )

    if len(tokens) != EXPECTED_COUNTS["terminal_points"]:
        raise AssertionError("terminal token count mismatch")

    ledger_payload = "".join(
        json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
        for record in records
    )

    lines = [
        "RETAINED TERMINAL SINK IDENTITY LEDGER",
        "",
        (
            "source_second_generation_retained_family_sha256="
            f"{EXPECTED_SECOND_RETAINED_FAMILY_SHA256}"
        ),
        f"source_full_ratio_record_bytes={EXPECTED_FULL_RATIO_RECORD_BYTES}",
        f"source_full_ratio_record_sha256={EXPECTED_FULL_RATIO_RECORD_SHA256}",
        f"terminal_family_sha256={EXPECTED_TERMINAL_FAMILY_SHA256}",
        "",
        "terminal_sink_states=13",
        "terminal_sink_points=43",
        "recursive_states=14",
        "recursive_points=7882",
        "terminal_states_have_three_term_AP=False",
        "terminal_state_numerical_sets_pairwise_disjoint=True",
        "terminal_numerical_labels_disjoint_from_recursive_labels=True",
        "terminal_point_tokens_u_p_unique=True",
        "ledger_jsonl_rows=13",
        "ledger_schema=state_identity_plus_pointwise_root_and_immediate_provenance",
        "",
        (
            "conclusion: the certified second-generation retained family admits "
            "an exact 13-state terminal-sink identity ledger."
        ),
        (
            "Within this recorded family, all 43 terminal numerical labels and "
            "all (u,p) sink tokens are unique and can be charged once."
        ),
        (
            "This does not prove that an identical numerical or provenance-supported "
            "sink cannot be recreated in a different branch or later generation."
        ),
        "",
    ]
    certificate = "\n".join(lines)
    digest = hashlib.sha256(certificate.encode("utf-8")).hexdigest()
    if digest != CERTIFICATE_SHA256:
        raise AssertionError(f"certificate SHA-256 mismatch: {digest}")
    return certificate, ledger_payload


def main() -> int:
    if len(sys.argv) > 3:
        raise SystemExit(
            "usage: export_retained_terminal_sink_ledger.py "
            "[CERTIFICATE_OUTPUT] [LEDGER_JSONL_OUTPUT]"
        )
    certificate, ledger_payload = build_ledger()
    if len(sys.argv) >= 2:
        Path(sys.argv[1]).write_text(certificate, encoding="utf-8")
    if len(sys.argv) == 3:
        Path(sys.argv[2]).write_text(ledger_payload, encoding="utf-8")
    print(certificate, end="")
    print("certificate_sha256=" + CERTIFICATE_SHA256)
    print(
        "ledger_jsonl_sha256="
        + hashlib.sha256(ledger_payload.encode("utf-8")).hexdigest()
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

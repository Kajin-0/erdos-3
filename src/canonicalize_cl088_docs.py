#!/usr/bin/env python3
"""Remove legacy CL-088 duplicates and assert one canonical documentation state."""
from __future__ import annotations

from pathlib import Path

from patch_cl088_residual_sponsor_split import (
    CL088,
    CURRENT_HEADING,
    README_ITEM19,
    README_LINK,
    REF_LINES,
    canonicalize_current_program_text,
)

ROOT = Path(__file__).resolve().parents[1]
DECISION_HEADING = "### Residual-sponsor backbone refinement"
CERT_HEADING = "## 11. Certified retained-frontier result"


def canonicalize_current_program() -> None:
    path = ROOT / "docs/current-proof-program.md"
    text = canonicalize_current_program_text(path.read_text(encoding="utf-8"))
    path.write_text(text, encoding="utf-8")


def assert_count(path: str, needle: str, expected: int = 1) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    actual = text.count(needle)
    if actual != expected:
        raise AssertionError(f"{path}: expected {expected} copies of {needle!r}, found {actual}")


def main() -> int:
    canonicalize_current_program()
    assert_count("docs/certainty-ledger.md", CL088)
    for line in REF_LINES:
        assert_count("docs/certainty-ledger.md", line)
    assert_count("README.md", README_ITEM19)
    assert_count("README.md", README_LINK)
    assert_count("docs/current-proof-program.md", CURRENT_HEADING)
    assert_count("docs/research-decision-history.md", DECISION_HEADING)
    assert_count("docs/residual-sponsor-backbone-refinement.md", CERT_HEADING)
    current = (ROOT / "docs/current-proof-program.md").read_text(encoding="utf-8")
    if "\x08" in current:
        raise AssertionError("current proof program contains a backspace control character")
    print("CL-088 documentation canonicalized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

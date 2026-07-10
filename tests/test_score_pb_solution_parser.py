from __future__ import annotations

import pytest
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from score_pb_solution import AssignmentParseError, parse_assignment


def test_complete_signed_assignment_parses() -> None:
    parsed = parse_assignment("v x0 -x1 x2 -x3\n", base=4)

    assert parsed.selected == (0, 2)
    assert parsed.false_vars == (1, 3)
    assert parsed.missing_vars == ()


def test_incomplete_assignment_fails_by_default() -> None:
    with pytest.raises(AssignmentParseError, match="incomplete solver assignment"):
        parse_assignment("v x0 -x1\n", base=4)


def test_partial_assignment_mode_is_explicit() -> None:
    parsed = parse_assignment("v x0 -x1\n", base=4, require_complete=False)

    assert parsed.selected == (0,)
    assert parsed.false_vars == (1,)
    assert parsed.missing_vars == (2, 3)


def test_out_of_range_assignment_fails() -> None:
    with pytest.raises(AssignmentParseError, match="outside expected base"):
        parse_assignment("v x0 -x1 x4 -x2\n", base=4)


def test_conflicting_assignment_fails() -> None:
    with pytest.raises(AssignmentParseError, match="conflicting assignments"):
        parse_assignment("x0=1 x1=0\nx0 0\nx2=1\nx3=0\n", base=4)

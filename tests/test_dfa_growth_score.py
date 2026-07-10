#!/usr/bin/env python3
from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dfa_ap_cert import DFA  # noqa: E402
from dfa_growth_score import productive_states, score_dfa  # noqa: E402


class DfaGrowthScoreTests(unittest.TestCase):
    def test_rejecting_sink_does_not_control_growth(self) -> None:
        allowed = {0, 1, 2, 4, 5, 7}
        transitions = {
            "ok": {
                digit: ("ok" if digit in allowed else "dead")
                for digit in range(11)
            },
            "dead": {digit: "dead" for digit in range(11)},
        }
        dfa = DFA(
            base=11,
            states=("ok", "dead"),
            start="ok",
            accept=frozenset({"ok"}),
            transitions=transitions,
        )
        dfa.validate()

        self.assertEqual(productive_states(dfa), ("ok",))

        score = score_dfa(dfa, max_digits=3, power_iterations=50)
        self.assertAlmostEqual(score.spectral_radius, 6.0, places=12)
        self.assertAlmostEqual(
            score.alpha,
            math.log(6.0) / math.log(11.0),
            places=12,
        )
        self.assertEqual(score.accepted_counts, (1, 6, 36, 216))

    def test_no_productive_state_has_zero_growth(self) -> None:
        dfa = DFA(
            base=3,
            states=("start", "dead"),
            start="start",
            accept=frozenset(),
            transitions={
                "start": {0: "dead", 1: "dead", 2: "dead"},
                "dead": {0: "dead", 1: "dead", 2: "dead"},
            },
        )
        dfa.validate()

        self.assertEqual(productive_states(dfa), ())
        score = score_dfa(dfa, max_digits=2, power_iterations=20)
        self.assertEqual(score.spectral_radius, 0.0)
        self.assertEqual(score.alpha, float("-inf"))
        self.assertEqual(score.accepted_counts, (0, 0, 0))


if __name__ == "__main__":
    unittest.main()

from __future__ import annotations

import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from dfa_ap_cert import load_dfa
from dfa_growth_score import accepted_language_transition_matrix, score_dfa


def test_base11_digit_set_growth_ignores_dead_sink() -> None:
    dfa = load_dfa(ROOT / "examples" / "dfa" / "base11_digit_set.json")

    matrix, states = accepted_language_transition_matrix(dfa)
    score = score_dfa(dfa, max_digits=2, power_iterations=50)

    assert states == ("ok",)
    assert matrix == [[6]]
    assert score.productive_states == 1
    assert score.spectral_radius == 6
    assert math.isclose(score.alpha, math.log(6) / math.log(11), rel_tol=0.0, abs_tol=1e-12)
    assert score.accepted_counts[:4] == (1, 6, 36)


def test_all_digits_base3_growth_is_full_base() -> None:
    dfa = load_dfa(ROOT / "examples" / "dfa" / "all_digits_base3.json")

    _matrix, states = accepted_language_transition_matrix(dfa)
    score = score_dfa(dfa, max_digits=2, power_iterations=50)

    assert score.productive_states == len(states)
    assert math.isclose(score.spectral_radius, 3.0, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(score.alpha, 1.0, rel_tol=0.0, abs_tol=1e-12)

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from pb_manifest import build_manifest
from score_pb_solution import AssignmentParseError


def manifest_args(model: Path, solution: Path) -> dict[str, object]:
    return {
        "experiment_id": "test_b4_k4_s2",
        "repo_commit": "abc123",
        "model_path": model,
        "solution_path": solution,
        "base": 4,
        "k": 4,
        "objective": "harmonic_proxy",
        "require_zero": True,
        "expected_size": 2,
        "min_size": None,
        "max_size": None,
        "target": 4.43975,
        "order": 10,
        "tol": 1e-15,
        "allow_partial_assignment": False,
        "solver_name": "test-solver",
        "solver_version": "1.0",
        "solver_command": "test-solver model.opb",
        "solver_status": "SATISFIABLE",
        "wall_time_seconds": 1.25,
        "cpu_time_seconds": 1.0,
        "objective_value": -1500.0,
        "objective_bound": None,
        "optimality_gap": None,
        "generated_at_utc": "2026-07-10T00:00:00+00:00",
    }


def test_manifest_hashes_and_checks_complete_assignment(tmp_path: Path) -> None:
    model = tmp_path / "model.opb"
    solution = tmp_path / "solution.sol"
    model.write_text("* test model\nmin: -1 x0;\n")
    solution.write_text("s SATISFIABLE\nv x0 x1 -x2 -x3\n")

    manifest = build_manifest(**manifest_args(model, solution))

    assert manifest["model_sha256"] == hashlib.sha256(model.read_bytes()).hexdigest()
    assert manifest["solution_sha256"] == hashlib.sha256(solution.read_bytes()).hexdigest()
    assert manifest["solver"]["status"] == "SATISFIABLE"

    check = manifest["independent_check"]
    assert check["complete_assignment"] is True
    assert check["selected_digits"] == [0, 1]
    assert check["size_constraints_satisfied"] is True
    assert check["require_zero_satisfied"] is True
    assert check["modular_k_free"] is True
    assert isinstance(check["shifted_sum"], float)


def test_manifest_rejects_incomplete_sat_assignment(tmp_path: Path) -> None:
    model = tmp_path / "model.opb"
    solution = tmp_path / "solution.sol"
    model.write_text("* test model\n")
    solution.write_text("s SATISFIABLE\nv x0 -x1\n")

    with pytest.raises(AssignmentParseError, match="incomplete solver assignment"):
        build_manifest(**manifest_args(model, solution))


def test_unsat_manifest_does_not_claim_independent_assignment_check(tmp_path: Path) -> None:
    model = tmp_path / "model.opb"
    solution = tmp_path / "solution.sol"
    model.write_text("* test model\n")
    solution.write_text("s UNSATISFIABLE\n")

    args = manifest_args(model, solution)
    args["solver_status"] = "UNSATISFIABLE"
    manifest = build_manifest(**args)

    assert manifest["solver"]["status"] == "UNSATISFIABLE"
    assert manifest["independent_check"] is None

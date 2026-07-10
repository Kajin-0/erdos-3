#!/usr/bin/env python3
"""Generate a reproducibility manifest for a PB/MaxSAT experiment.

The manifest binds together:

- the exact OPB model and SHA-256 hash;
- the exact solver output and SHA-256 hash;
- solver identity, command, status, timing, and objective metadata;
- model parameters;
- an independent parse, cardinality check, cyclic AP check, and harmonic score.

JSON is used deliberately so the utility has no third-party YAML dependency.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from score_pb_solution import AssignmentParseError, is_modular_k_free, parse_assignment
from shifted_kempner_sum import shifted_kempner_sum

SOLVER_STATUSES = ("OPTIMUM", "SATISFIABLE", "UNSATISFIABLE", "UNKNOWN")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def size_constraints_satisfied(
    size: int,
    *,
    expected_size: int | None,
    min_size: int | None,
    max_size: int | None,
) -> bool:
    if expected_size is not None and size != expected_size:
        return False
    if min_size is not None and size < min_size:
        return False
    if max_size is not None and size > max_size:
        return False
    return True


def independent_check(
    solution_text: str,
    *,
    base: int,
    k: int,
    require_zero: bool,
    expected_size: int | None,
    min_size: int | None,
    max_size: int | None,
    target: float,
    order: int,
    tol: float,
    allow_partial_assignment: bool,
) -> dict[str, Any]:
    parsed = parse_assignment(
        solution_text,
        base,
        require_complete=not allow_partial_assignment,
    )
    digits = parsed.selected
    size_ok = size_constraints_satisfied(
        len(digits),
        expected_size=expected_size,
        min_size=min_size,
        max_size=max_size,
    )
    contains_zero = 0 in digits
    zero_ok = contains_zero or not require_zero
    modular_k_free = is_modular_k_free(base, digits, k)

    score_value: float | None = None
    beats_target = False
    if digits and contains_zero:
        score = shifted_kempner_sum(base, digits, order=order, tol=tol)
        score_value = score.shifted_sum
        beats_target = modular_k_free and size_ok and zero_ok and score_value > target

    return {
        "complete_assignment": len(parsed.missing_vars) == 0,
        "assigned_true": len(parsed.selected),
        "assigned_false": len(parsed.false_vars),
        "missing_variables": list(parsed.missing_vars),
        "selected_digits": list(digits),
        "size": len(digits),
        "size_constraints_satisfied": size_ok,
        "contains_zero": contains_zero,
        "require_zero_satisfied": zero_ok,
        "modular_k_free": modular_k_free,
        "shifted_sum": score_value,
        "target": target,
        "beats_target": beats_target,
        "solver_status_lines": list(parsed.status_lines),
        "solver_objective_lines": list(parsed.objective_lines),
    }


def build_manifest(
    *,
    experiment_id: str,
    repo_commit: str,
    model_path: Path,
    solution_path: Path,
    base: int,
    k: int,
    objective: str,
    require_zero: bool,
    expected_size: int | None,
    min_size: int | None,
    max_size: int | None,
    target: float,
    order: int,
    tol: float,
    allow_partial_assignment: bool,
    solver_name: str,
    solver_version: str,
    solver_command: str,
    solver_status: str,
    wall_time_seconds: float | None,
    cpu_time_seconds: float | None,
    objective_value: float | None,
    objective_bound: float | None,
    optimality_gap: float | None,
    generated_at_utc: str,
) -> dict[str, Any]:
    if solver_status not in SOLVER_STATUSES:
        raise ValueError(f"invalid solver status {solver_status!r}; expected one of {SOLVER_STATUSES}")
    if base < 2:
        raise ValueError("base must be at least 2")
    if k < 3:
        raise ValueError("k must be at least 3")

    manifest: dict[str, Any] = {
        "schema_version": 1,
        "experiment_id": experiment_id,
        "generated_at_utc": generated_at_utc,
        "repo_commit": repo_commit,
        "model_path": str(model_path),
        "model_sha256": sha256_file(model_path),
        "solution_path": str(solution_path),
        "solution_sha256": sha256_file(solution_path),
        "solver": {
            "name": solver_name,
            "version": solver_version,
            "command": solver_command,
            "wall_time_seconds": wall_time_seconds,
            "cpu_time_seconds": cpu_time_seconds,
            "status": solver_status,
            "objective_value": objective_value,
            "objective_bound": objective_bound,
            "optimality_gap": optimality_gap,
        },
        "model": {
            "base": base,
            "k": k,
            "objective": objective,
            "require_zero": require_zero,
            "expected_size": expected_size,
            "min_size": min_size,
            "max_size": max_size,
        },
    }

    if solver_status in ("OPTIMUM", "SATISFIABLE"):
        manifest["independent_check"] = independent_check(
            solution_path.read_text(),
            base=base,
            k=k,
            require_zero=require_zero,
            expected_size=expected_size,
            min_size=min_size,
            max_size=max_size,
            target=target,
            order=order,
            tol=tol,
            allow_partial_assignment=allow_partial_assignment,
        )
    else:
        manifest["independent_check"] = None

    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment-id", required=True)
    parser.add_argument("--repo-commit", required=True)
    parser.add_argument("--model", type=Path, required=True)
    parser.add_argument("--solution", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--base", type=int, required=True)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--objective", required=True)
    parser.add_argument("--allow-missing-zero", action="store_true")
    parser.add_argument("--allow-partial-assignment", action="store_true")
    parser.add_argument("--expected-size", type=int, default=None)
    parser.add_argument("--min-size", type=int, default=None)
    parser.add_argument("--max-size", type=int, default=None)
    parser.add_argument("--target", type=float, default=4.43975)
    parser.add_argument("--order", type=int, default=60)
    parser.add_argument("--tol", type=float, default=1e-15)
    parser.add_argument("--solver-name", required=True)
    parser.add_argument("--solver-version", required=True)
    parser.add_argument("--solver-command", required=True)
    parser.add_argument("--solver-status", choices=SOLVER_STATUSES, required=True)
    parser.add_argument("--wall-time-seconds", type=float, default=None)
    parser.add_argument("--cpu-time-seconds", type=float, default=None)
    parser.add_argument("--objective-value", type=float, default=None)
    parser.add_argument("--objective-bound", type=float, default=None)
    parser.add_argument("--optimality-gap", type=float, default=None)
    args = parser.parse_args()

    generated_at = datetime.now(timezone.utc).isoformat()
    try:
        manifest = build_manifest(
            experiment_id=args.experiment_id,
            repo_commit=args.repo_commit,
            model_path=args.model,
            solution_path=args.solution,
            base=args.base,
            k=args.k,
            objective=args.objective,
            require_zero=not args.allow_missing_zero,
            expected_size=args.expected_size,
            min_size=args.min_size,
            max_size=args.max_size,
            target=args.target,
            order=args.order,
            tol=args.tol,
            allow_partial_assignment=args.allow_partial_assignment,
            solver_name=args.solver_name,
            solver_version=args.solver_version,
            solver_command=args.solver_command,
            solver_status=args.solver_status,
            wall_time_seconds=args.wall_time_seconds,
            cpu_time_seconds=args.cpu_time_seconds,
            objective_value=args.objective_value,
            objective_bound=args.objective_bound,
            optimality_gap=args.optimality_gap,
            generated_at_utc=generated_at,
        )
    except AssignmentParseError as exc:
        raise SystemExit(f"invalid solver assignment: {exc}") from exc

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(f"wrote {args.output}")
    print(f"model_sha256={manifest['model_sha256']}")
    print(f"solution_sha256={manifest['solution_sha256']}")


if __name__ == "__main__":
    main()

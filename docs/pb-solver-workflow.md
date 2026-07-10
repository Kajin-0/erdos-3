# PB / MaxSAT solver workflow

## Purpose

The repo now has an end-to-end path for cyclic one-layer digit templates:

1. generate an OPB model;
2. solve it with an external PB/MaxSAT optimizer;
3. parse the solver assignment;
4. re-check cyclic `k`-AP-freeness;
5. compute the shifted Kempner harmonic sum;
6. compare against Walker's public `k=4` benchmark `4.43975`.

This avoids accepting density-only, proxy-only, or unverified solver output.

## Generate a model

Example for the Walker-scale base-55 profile:

```bash
python src/cyclic_pb_encoder.py \
  --base 55 \
  --k 4 \
  --min-size 21 \
  --max-size 21 \
  --objective harmonic_proxy \
  --output models/cyclic_b55_k4_s21_harmonic_proxy.opb
```

The hard constraints are cyclic AP blockers:

```math
\sum_{d\in M}x_d \le |M|-1,
```

where `M` is a nontrivial cyclic 4-AP residue mask in `Z/bZ`.

## Solve externally

Use any OPB-capable pseudo-Boolean optimizer.  The repo does not vendor a solver.  Candidate
solvers include RoundingSat, Sat4j PB, Open-WBO-compatible PB workflows, or other PB/MaxSAT
systems that can return variable assignments.

Save the solver output in a text file, for example:

```text
solver_outputs/cyclic_b55_k4_s21_harmonic_proxy.sol
```

## Score the solver output

```bash
python src/score_pb_solution.py \
  --base 55 \
  --k 4 \
  --solution solver_outputs/cyclic_b55_k4_s21_harmonic_proxy.sol \
  --expected-size 21 \
  --target 4.43975
```

The parser accepts common assignment styles such as:

```text
v x0 -x1 x2 -x3
x0=1 x1=0 x2=1
x0 1
x1 0
```

By default, the parser now requires every model variable

```text
x0, x1, ..., x{b-1}
```

to appear explicitly as true or false.  Omitted variables are not silently treated as false.
For legacy solver outputs, use

```bash
--allow-partial-assignment
```

but do not treat such a result as a publishable optimal certificate unless the omitted variables are
justified independently.

When the OPB model contains cardinality constraints, mirror them in the scorer with one of:

```bash
--expected-size 21
--min-size 20 --max-size 22
```

This catches assignments that may satisfy the parser but not the intended experiment profile.

## Reproducibility manifest

Every solver-backed claim should be accompanied by a manifest containing at least:

```yaml
experiment_id: cyclic_b55_k4_s21_harmonic_proxy
repo_commit: <git commit sha>
model_path: models/cyclic_b55_k4_s21_harmonic_proxy.opb
model_sha256: <sha256 of OPB model>
solution_path: solver_outputs/cyclic_b55_k4_s21_harmonic_proxy.sol
solution_sha256: <sha256 of solver output>
solver:
  name: <solver name>
  version: <solver version>
  command: <exact command line>
  wall_time_seconds: <wall time>
  cpu_time_seconds: <cpu time if known>
  status: <OPTIMUM | SATISFIABLE | UNSATISFIABLE | UNKNOWN>
  objective_value: <reported objective if present>
  objective_bound: <reported bound if present>
  optimality_gap: <gap if present>
model:
  base: 55
  k: 4
  objective: harmonic_proxy
  require_zero: true
  min_size: 21
  max_size: 21
independent_check:
  complete_assignment: true
  expected_size: 21
  modular_k_free: true
  shifted_sum: <computed shifted sum>
  beats_target_4_43975: <true | false>
```

Without this metadata, an external PB result should be treated as a candidate, not a certificate.

## Generate a focused experiment matrix

```bash
python src/pb_experiment_matrix.py \
  --b-min 45 \
  --b-max 65 \
  --size-delta 1 \
  --csv data/pb_experiment_matrix.csv
```

The recorded focused matrix is:

```text
data/pb_experiment_matrix_2026-07-07.csv
```

It contains commands for selected bases around the Walker base-55 benchmark and size profiles
near the exponent implied by `log(21)/log(55)`.

## Acceptance rule

A solver candidate is not interesting unless all conditions hold:

1. `score_pb_solution.py` parses a complete assignment, unless partial assignment is explicitly justified;
2. requested size constraints are mirrored with `--expected-size` or `--min-size`/`--max-size`;
3. `modular_k_free=1` from `score_pb_solution.py`;
4. `shifted_sum > 4.43975`;
5. the digit set is not a trivial restatement of an already recorded public benchmark.

A negative result is also useful only if the solver can certify unsatisfiability or optimality for a
specific base, size, and objective profile and the manifest records the solver status, objective
bound, and model hash.

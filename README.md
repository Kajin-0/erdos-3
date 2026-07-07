# Erdős Problem #3: harmonic AP search

This repository contains a concrete partial-progress attack on Erdős Problem #3:

> If `A ⊆ N` and `∑_{n∈A} 1/n = ∞`, must `A` contain arbitrarily long arithmetic progressions?

The full problem is open. The working target here is narrower: certified computational
search for large reciprocal-sum, 4-AP-free digit-restricted sets.

## Current pivot after literature audit

The audit changed the priority.  Alexander Walker's public work already covers the obvious
plain modular digit-set search.  The repo now pivots toward:

1. a machine-readable benchmark pack;
2. pseudo-Boolean / MaxSAT encoding for cyclic digit templates;
3. shifted Kempner harmonic scoring;
4. finite-state digit languages and carry-state automata.

The public `k=4` benchmark to beat is Walker's base-55 shifted Kempner example with harmonic
sum `4.43975`.

## Contents

- `src/modular_kempner_search.py` — branch-and-bound search for modular 4-free digit sets.
- `src/periodic_digit_ap.py` — finite automaton checker for one periodic digit system.
- `src/periodic_exhaustive_search.py` — exact period-2 threshold search engine.
- `src/periodic_stochastic_search.py` — stochastic witness-guided periodic search with exact certification.
- `src/benchmark_report.py` — validates public benchmark metadata and modular certificates.
- `src/shifted_kempner_sum.py` — scores shifted Kempner harmonic sums `K(D,b)+1`.
- `src/candidate_score.py` — certifies and scores a single proposed one-layer candidate.
- `src/cyclic_neighborhood_scan.py` — scans fixed-size digit-substitution neighborhoods.
- `src/cyclic_pb_encoder.py` — emits OPB pseudo-Boolean models for cyclic AP-free templates.
- `src/score_pb_solution.py` — parses external PB/MaxSAT assignments, re-certifies, and scores them.
- `src/pb_experiment_matrix.py` — generates reproducible PB/MaxSAT experiment matrices.
- `src/dfa_ap_cert.py` — exact 4-AP certifier for LSD-first regular digit languages.
- `src/dfa_growth_score.py` — growth-rate and truncated shifted-harmonic triage for DFA languages.
- `examples/dfa/base11_digit_set.json` — two-state DFA encoding Walker's base-11 digit set.
- `examples/dfa/all_digits_base3.json` — positive-control DFA that contains 4-APs.
- `data/public_benchmarks.csv` — known public benchmarks and provenance links.
- `data/benchmark_scores_2026-07-07.csv` — reproduction of Walker's public k=4 shifted sums.
- `data/walker55_neighborhood_scan_2026-07-07.csv` — radius-1/2 neighborhood scan of Walker's base-55 set.
- `data/pb_experiment_matrix_2026-07-07.csv` — focused PB experiment commands around Walker-scale bases.
- `data/small_base_run_2026-07-07.csv` — first reproducible small-base modular run.
- `data/period2_threshold_run_2026-07-07.csv` — exhaustive period-2 threshold run for bases 11–13.
- `data/stochastic_periodic_run_2026-07-07.csv` — first period-2/3 stochastic high-water-mark run.
- `docs/research-note.md` — current mathematical target, first observations, and next milestone.
- `docs/periodic-search-goal.md` — Walker base-55 benchmark target and first period-2 result.
- `docs/stochastic-search.md` — stochastic search algorithm, first results, and next SAT-style target.
- `docs/literature-audit-action-plan.md` — post-audit route and experiment queue.
- `docs/harmonic-search-status.md` — harmonic-aware scoring gate and local rigidity result.
- `docs/pb-solver-workflow.md` — end-to-end PB/MaxSAT workflow.
- `docs/regular-language-certifier.md` — DFA model, AP certificate, examples, and next search target.
- `docs/dfa-growth-triage.md` — DFA growth exponent and truncated shifted harmonic triage.

## Reproduce first modular run

```bash
python src/modular_kempner_search.py --verify-known --b-min 5 --b-max 34 --topn 1 \
  --csv data/small_base_run.csv
```

## Check Walker's base-11 set

```bash
python src/modular_kempner_search.py --verify-known --b-min 11 --b-max 11 --topn 1
```

## Test period-2 local augmentation of the base-11 set

```bash
python src/periodic_digit_ap.py \
  --base 11 \
  --digits "0,1,2,4,5,7" \
  --local-augment
```

Expected first observation: no one-digit period-2 augmentation of `{0,1,2,4,5,7}` preserves
4-AP-freeness under the automaton certificate.

## Reproduce the period-2 threshold run

```bash
python src/periodic_exhaustive_search.py \
  --b-min 11 \
  --b-max 13 \
  --csv data/period2_threshold_run.csv
```

This exhaustively checks all period-2 size profiles with

```math
\frac{\log |D_0|+\log |D_1|}{2\log b}>\frac{\log 21}{\log 55}.
```

Current result: no period-2 candidate beating the Walker base-55 density exponent was found
for bases 11, 12, or 13.

## Run stochastic period search

```bash
python src/periodic_stochastic_search.py \
  --b-min 14 \
  --b-max 18 \
  --periods 2 3 \
  --trials 20 \
  --csv data/stochastic_periodic_run.csv
```

Current result: the stochastic run did not beat the Walker base-55 exponent. The best candidate
in the recorded run was a period-3 base-11 system with exponent `log(6)/log(11) ≈ 0.74722`,
still below `log(21)/log(55) ≈ 0.75974`.

## Validate benchmark metadata

```bash
python src/benchmark_report.py --benchmarks data/public_benchmarks.csv
```

This checks one-layer digit benchmarks for modular `k`-AP-freeness and recomputes density
exponents.

## Reproduce shifted harmonic sums

```bash
python src/shifted_kempner_sum.py --benchmarks data/public_benchmarks.csv
```

The shifted convention is

```math
H_{shift}(D,b)=\sum_{n\in K(D,b)}\frac{1}{n+1}.
```

This reproduces Walker's public k=4 values to the reported 5-decimal precision:

- base 11: computed `4.4217475324`, reported `4.42175`;
- base 55: computed `4.4397533693`, reported `4.43975`.

## Score a proposed one-layer candidate

```bash
python src/candidate_score.py \
  --base 55 \
  --k 4 \
  --digits "0 1 2 4 5 9 10 11 14 16 17 18 21 24 30 37 39 41 42 45 47"
```

This checks cyclic modular `k`-AP-freeness, computes the shifted harmonic sum, and reports whether
the candidate beats `4.43975`.

## Scan Walker base-55 local neighborhood

```bash
python src/cyclic_neighborhood_scan.py \
  --base 55 \
  --k 4 \
  --digits "0 1 2 4 5 9 10 11 14 16 17 18 21 24 30 37 39 41 42 45 47" \
  --max-radius 2 \
  --csv data/walker55_neighborhood_scan.csv
```

Current result: the Walker base-55 set has no AP-free radius-1 or radius-2 same-size digit-substitution
neighbors.  The known benchmark is locally rigid under these small substitutions.

## Generate a cyclic PB model

```bash
python src/cyclic_pb_encoder.py \
  --base 55 \
  --k 4 \
  --min-size 21 \
  --max-size 21 \
  --objective harmonic_proxy \
  --output models/cyclic_b55_k4_s21_harmonic_proxy.opb
```

## Score an external PB solver solution

```bash
python src/score_pb_solution.py \
  --base 55 \
  --k 4 \
  --solution solver_outputs/cyclic_b55_k4_s21_harmonic_proxy.sol \
  --target 4.43975
```

This parses common solver assignment formats, rechecks cyclic modular `k`-AP-freeness, computes
the shifted harmonic score, and reports whether the solver output beats the target.

## Generate a PB experiment matrix

```bash
python src/pb_experiment_matrix.py \
  --b-min 45 \
  --b-max 65 \
  --size-delta 1 \
  --csv data/pb_experiment_matrix.csv
```

A focused recorded matrix is stored in `data/pb_experiment_matrix_2026-07-07.csv`.

## Certify a regular digit language

```bash
python src/dfa_ap_cert.py --dfa examples/dfa/base11_digit_set.json
```

Expected result: Walker's base-11 digit-set DFA is certified 4-AP-free.

```bash
python src/dfa_ap_cert.py --dfa examples/dfa/all_digits_base3.json --witness
```

Expected result: the all-digits base-3 DFA contains a nontrivial 4-AP and returns a witness.

## Triage a regular digit language

```bash
python src/dfa_growth_score.py \
  --dfa examples/dfa/base11_digit_set.json \
  --max-digits 6
```

This reports the DFA transition spectral radius, growth exponent, accepted counts by digit length,
and truncated shifted reciprocal sum over `n < b^M`.

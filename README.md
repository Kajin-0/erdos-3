# Erdős Problem #3: harmonic AP search

This repository contains a concrete partial-progress attack on Erdős Problem #3:

> If `A ⊆ N` and `∑_{n∈A} 1/n = ∞`, must `A` contain arbitrarily long arithmetic progressions?

The full problem is open. The repository keeps a permanent ledger of reliable partial results,
verified computations, and open bottlenecks so progress is not lost across long research sessions.

## Certainty ledger

The file

```text
docs/certainty-ledger.md
```

records claims that are safe to rely on.  Current high-certainty entries include:

- base-`b` automatic sets cannot be divergent reciprocal-sum counterexamples;
- any AP-free divergent candidate must be sparse in every fixed-ratio interval;
- the standard dyadic-block reduction to summability of `r_k(N)` bounds;
- the Walker base-55 local-rigidity computation in the cyclic digit-template model;
- the current open bottleneck: cross-block arithmetic constraints.

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

- `docs/certainty-ledger.md` — durable ledger of proved results, verified computations, and bottlenecks.
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
- `src/random_dfa_search.py` — random small-DFA candidate generator with exact AP certification.
- `src/dfa_canonicalize.py` — DFA minimization/canonicalization and SHA256 signatures.
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
- `docs/random-dfa-search.md` — random small-DFA search workflow and acceptance gates.
- `docs/dfa-canonicalization.md` — DFA minimization/canonicalization workflow.

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

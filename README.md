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
3. future carry-state automata and harmonic scoring.

The public `k=4` benchmark to beat is Walker's base-55 shifted Kempner example with harmonic
sum `4.43975`.

## Contents

- `src/modular_kempner_search.py` — branch-and-bound search for modular 4-free digit sets.
- `src/periodic_digit_ap.py` — finite automaton checker for one periodic digit system.
- `src/periodic_exhaustive_search.py` — exact period-2 threshold search engine.
- `src/periodic_stochastic_search.py` — stochastic witness-guided periodic search with exact certification.
- `src/benchmark_report.py` — validates public benchmark metadata and modular certificates.
- `src/cyclic_pb_encoder.py` — emits OPB pseudo-Boolean models for cyclic AP-free templates.
- `data/public_benchmarks.csv` — known public benchmarks and provenance links.
- `data/small_base_run_2026-07-07.csv` — first reproducible small-base modular run.
- `data/period2_threshold_run_2026-07-07.csv` — exhaustive period-2 threshold run for bases 11–13.
- `data/stochastic_periodic_run_2026-07-07.csv` — first period-2/3 stochastic high-water-mark run.
- `docs/research-note.md` — current mathematical target, first observations, and next milestone.
- `docs/periodic-search-goal.md` — Walker base-55 benchmark target and first period-2 result.
- `docs/stochastic-search.md` — stochastic search algorithm, first results, and next SAT-style target.
- `docs/literature-audit-action-plan.md` — post-audit route and experiment queue.

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
exponents. It does not recompute harmonic sums.

## Generate a cyclic PB model

```bash
python src/cyclic_pb_encoder.py \
  --base 55 \
  --k 4 \
  --min-size 21 \
  --objective harmonic_proxy \
  --output models/cyclic_b55_k4_min21.opb
```

The resulting OPB file can be passed to an external pseudo-Boolean optimizer.  Any solver output
must still be checked by the exact modular checker and then scored by harmonic post-processing.

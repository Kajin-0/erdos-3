# Erdős Problem #3: harmonic AP search

This repository contains a concrete partial-progress attack on Erdős Problem #3:

> If `A ⊆ N` and `∑_{n∈A} 1/n = ∞`, must `A` contain arbitrarily long arithmetic progressions?

The full problem is open. The working target here is narrower: certified computational
search for large reciprocal-sum, 4-AP-free digit-restricted sets.

## Contents

- `src/modular_kempner_search.py` — branch-and-bound search for modular 4-free digit sets.
- `src/periodic_digit_ap.py` — finite automaton checker for one periodic digit system.
- `src/periodic_exhaustive_search.py` — exact period-2 threshold search engine.
- `data/small_base_run_2026-07-07.csv` — first reproducible small-base modular run.
- `data/period2_threshold_run_2026-07-07.csv` — exhaustive period-2 threshold run for bases 11–13.
- `docs/research-note.md` — current mathematical target, first observations, and next milestone.
- `docs/periodic-search-goal.md` — Walker base-55 benchmark target and first period-2 result.

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

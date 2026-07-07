# Random small-DFA search

## Purpose

The repo now has a first executable search harness for the regular-language model class:

```text
src/random_dfa_search.py
```

This is not meant to prove optimality.  It is a candidate generator for small finite-state digit
languages that are not obviously plain one-layer digit sets.

## Pipeline

For each random DFA:

1. Generate a least-significant-digit-first DFA over base `b`.
2. Enforce zero-padding closure on accepting states.
3. Optionally skip trivial one-layer digit-set-like DFAs.
4. Run exact 4-AP certification using `src/dfa_ap_cert.py`.
5. If certified 4-AP-free, run growth/truncated harmonic triage using `src/dfa_growth_score.py`.
6. Save the top candidates by truncated shifted reciprocal sum.

## Example command

```bash
python src/random_dfa_search.py \
  --base 5 \
  --states 3 \
  --trials 1000 \
  --max-digits 6 \
  --keep 10 \
  --csv data/random_dfa_search.csv \
  --save-dir candidates/dfa
```

Each saved candidate can then be independently checked:

```bash
python src/dfa_ap_cert.py --dfa candidates/dfa/<candidate>.json
python src/dfa_growth_score.py --dfa candidates/dfa/<candidate>.json --max-digits 6
```

## Acceptance gates

A candidate is worth deeper analysis only if:

1. `dfa_ap_cert.py` reports `certified_4ap_free=1`;
2. `dfa_growth_score.py` reports a competitive growth exponent or truncated shifted sum;
3. the DFA is not just a disguised one-layer digit set;
4. the structure looks stable under reruns or appears in multiple nearby parameter regimes.

## Current limitation

The search is randomized and local.  It is useful for discovering examples, not for proving
nonexistence.  The next serious step after a promising hit is either:

1. DFA minimization/canonicalization;
2. exact transfer-operator harmonic scoring;
3. SAT/PB/SMT generation of small DFA transition tables under AP-free constraints.

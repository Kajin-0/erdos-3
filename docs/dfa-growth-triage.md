# DFA growth and truncated harmonic triage

## Purpose

The regular-language AP certifier answers:

```text
Does this DFA language contain a nontrivial 4-AP?
```

The next triage question is:

```text
Is this DFA language even large enough to be interesting?
```

The script

```text
src/dfa_growth_score.py
```

answers that second question approximately.  It does not replace a full transfer-operator harmonic
scorer, but it gives a cheap way to rank finite-state candidates before deeper analysis.

## Growth exponent

For a base-`b` DFA, define the digit-transition matrix `A` by

```math
A_{ij}=\#\{d\in\{0,\dots,b-1\}: q_i \xrightarrow{d} q_j\}.
```

The exponential language-growth exponent is estimated as

```math
\alpha=\frac{\log \rho(A)}{\log b},
```

where `rho(A)` is the Perron spectral radius.

A high-value regular-language candidate should have large `alpha`, but alpha alone is not the
objective.  The actual target remains shifted harmonic mass.

## Truncated shifted harmonic sum

For a maximum digit width `M`, the script computes

```math
H_M=\sum_{0\le n<b^M,\ n\ accepted}\frac{1}{n+1}.
```

For zero-padding-closed languages, this is a lower bound for the full shifted reciprocal sum.

## Example commands

Score the base-11 digit-set DFA:

```bash
python src/dfa_growth_score.py \
  --dfa examples/dfa/base11_digit_set.json \
  --max-digits 6
```

Score the positive-control all-digits DFA:

```bash
python src/dfa_growth_score.py \
  --dfa examples/dfa/all_digits_base3.json \
  --max-digits 6
```

## Interpretation

A regular-language candidate is worth deeper analysis only if it passes three gates:

1. `src/dfa_ap_cert.py` certifies it as 4-AP-free;
2. `src/dfa_growth_score.py` reports a competitive growth exponent or truncated harmonic score;
3. the language is not simply a disguised one-layer digit set already covered by Walker-style search.

## Current limitation

The truncated harmonic score enumerates all `n < b^M`, so it is only for small bases or small `M`.
The correct long-term scorer should use a transfer-operator / automaton moment method analogous to
`src/shifted_kempner_sum.py`, but generalized from one digit set to arbitrary DFA states.

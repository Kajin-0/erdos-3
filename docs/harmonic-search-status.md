# Harmonic-aware search status

## Why this file exists

The repository now has enough infrastructure to distinguish three different questions:

1. Is a digit set certified cyclic `k`-AP-free?
2. What is its shifted Kempner harmonic sum?
3. Does it beat Walker's public `k=4` target `4.43975`?

This prevents wasting time on density-only or proxy-only candidates.

## Candidate scoring gate

The script

```text
src/candidate_score.py
```

parses a base-`b` digit set, checks the cyclic modular `k`-AP certificate, computes

```math
H_{shift}(D,b)=\sum_{n\in K(D,b)}\frac{1}{n+1},
```

and reports whether the candidate beats the current target.

Example:

```bash
python src/candidate_score.py \
  --base 55 \
  --k 4 \
  --digits "0 1 2 4 5 9 10 11 14 16 17 18 21 24 30 37 39 41 42 45 47"
```

## Local rigidity of Walker's base-55 benchmark

The script

```text
src/cyclic_neighborhood_scan.py
```

scans fixed-size substitution neighborhoods.  A radius-`r` neighbor removes `r` nonzero digits
and adds `r` missing digits, preserving zero and preserving the digit-set size.

The first recorded result is stored in

```text
data/walker55_neighborhood_scan_2026-07-07.csv
```

For Walker's base-55 `k=4` benchmark:

| radius | total same-size neighbors checked | AP-free neighbors | improved harmonic score |
|---:|---:|---:|---:|
| 1 | 680 | 0 | no |
| 2 | 106590 | 0 | no |

Interpretation: the public benchmark is locally rigid under one- and two-digit substitutions.
This does not prove global optimality.  It says a successful search likely needs a larger structural
change, not a small perturbation of Walker's base-55 digit set.

## Next move

The next useful computational route is either:

1. external PB/MaxSAT search using `src/cyclic_pb_encoder.py`, followed by `src/candidate_score.py`; or
2. moving to finite-state regular languages / carry-state automata that are not equivalent to one-layer digit sets.

Plain local substitutions around the known base-55 benchmark are low value after this scan.

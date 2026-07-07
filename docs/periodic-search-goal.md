# Period-2 search toward the Walker base-55 benchmark

## Goal

The present computational target is to beat the fixed-digit Walker base-55 density exponent

```math
\alpha_{55}=\frac{\log 21}{\log 55}\approx 0.75974.
```

For a period-2 base-`b` digit system `(D0,D1)`, the comparable exponent is

```math
\alpha(D_0,D_1)=\frac{\log |D_0|+\log |D_1|}{2\log b}.
```

A candidate beats the density benchmark if

```math
\alpha(D_0,D_1)>\alpha_{55}.
```

The search in `src/periodic_exhaustive_search.py` exhaustively enumerates all period-2 size
profiles above this threshold for small bases, then all digit-set pairs containing zero for
each profile.

## AP certificate

The 4-term AP condition for `x0,x1,x2,x3` is equivalent to the two second-difference equations

```math
x_0-2x_1+x_2=0,
\qquad
x_1-2x_2+x_3=0.
```

Reading these equations in base `b` gives a finite automaton over two carry variables.
A periodic digit system is certified 4-AP-free if the automaton has no nontrivial path that
returns the carry pair to `(0,0)`.

## First exact run

The file `data/period2_threshold_run_2026-07-07.csv` records an exact period-2 threshold run for
bases

```math
11\le b\le 13.
```

For these bases, every period-2 size profile above the Walker base-55 exponent was exhausted.
No certified 4-AP-free system was found.

Summary:

| base | profiles above target | result |
|---:|---:|---|
| 11 | 47 | no hit |
| 12 | 58 | no hit |
| 13 | 68 | no hit |

This is a negative result, but it is useful: the easiest route to beating the base-55 benchmark
via small-base period-2 digit systems is blocked through base 13.

## Next computational step

Extend the exact search to larger bases using one of the following accelerations:

1. SAT/SMT encoding of the finite carry automaton obstruction.
2. Branch-and-bound over digit membership variables instead of full pair enumeration.
3. Period-3 beam search followed by exact automaton certification.
4. Direct harmonic-sum post-processing for high-exponent candidates, because exponent alone may
   not perfectly rank reciprocal sums.

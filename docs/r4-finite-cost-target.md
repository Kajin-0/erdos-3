# Finite cost target for the k=4 reciprocal-sum case

## Status

Working quantitative target derived from dyadic summability.

## Goal

To prove the `k=4` reciprocal-sum Erdős case, it is enough to prove a finite theorem of the following form.

There exist constants `C>0` and `eta>0` such that whenever

```math
N \ge \exp(C\alpha^{-1+\eta}),
```

every subset `A subset [N]` with `|A| >= alpha N` contains a nontrivial 4-term arithmetic progression.

Equivalently,

```math
r_4(N) \ll N(\log N)^{-1/(1-\eta)}.
```

Since

```math
\frac{1}{1-\eta}>1,
```

this implies

```math
\sum_j r_4(2^j)/2^j<\infty.
```

## Cost-function formulation

Let `C_4(alpha)` denote a threshold such that every subset of `[N]` of density at least `alpha`
contains a 4AP whenever

```math
N \ge \exp(C_4(\alpha)).
```

The reciprocal-sum target follows if

```math
C_4(\alpha) \ll \alpha^{-1+\eta}
```

for some `eta>0`.

A bound of the form

```math
C_4(\alpha) \ll \alpha^{-\theta}
```

corresponds to

```math
r_4(N) \ll N(\log N)^{-1/\theta}.
```

Therefore dyadic summability requires

```math
\theta<1.
```

## Relation to Green--Tao Part III

Green--Tao Part III proves a polylogarithmic bound

```math
r_4(N) \ll N(\log N)^{-c}
```

for some absolute `c>0`.  In cost-function language, this corresponds morally to

```math
C_4(\alpha) \ll \alpha^{-1/c}
```

up to losses hidden in the proof.

The reciprocal-sum problem requires improving the effective cost exponent to below `1`.

## What must improve

The proof audit should locate the dominant source of the effective `theta >= 1` barrier:

1. counting 4AP scarcity into a `U^3` obstruction;
2. inverse theorem quantitative dependence;
3. density increment strength;
4. Bohr/progression dimension growth;
5. radius or scale loss under iteration;
6. final iteration bookkeeping.

## Sharp research question

Can one force a 4AP at density `alpha` once

```math
N \ge \exp(C\alpha^{-1+\eta})
```

for some `eta>0`?

A positive answer proves the `k=4` reciprocal-sum case.

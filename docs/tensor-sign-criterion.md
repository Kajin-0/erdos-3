# Tensor-power sign criterion for four-balanced obstruction

## Status

Proof-audit criterion.  This note characterizes when a one-dimensional 4AP-free model tensors into an asymptotic negative four-balanced obstruction.

## Setup

Let `A subset F_p` have density

```math
alpha = |A|/p.
```

Let

```math
h = 1_A.
```

For `S subset {0,1,2,3}`, define

```math
lambda_S
= E_{x,d in F_p} prod_{i in S} h(x+id).
```

Write

```math
lambda_4 = lambda_{0123}.
```

For the four three-point patterns, define

```math
mu_i = lambda_{{0,1,2,3}\setminus {i}}.
```

Normalize by

```math
a = lambda_4/alpha^4,
qquad
r_i = mu_i/alpha^3.
```

## Tensor powers

Let

```math
B_n = A^n subset F_p^n,
qquad
alpha_n = alpha^n,
qquad
F_n = 1_{B_n} - alpha_n.
```

Because `1_{B_n}` is a tensor product, all progression averages factor.

The trilinear terms are

```math
T_{i,n} = mu_i^n - alpha^{3n}
        = alpha^{3n}(r_i^n-1).
```

The four-balanced term is

```math
Q_n = Lambda_4(F_n,F_n,F_n,F_n)
```

with

```math
Q_n/alpha_n^4 = a^n - sum_i r_i^n + 3.
```

## Asymptotic sign rule

The sign of `Q_n` for large `n` is controlled by the largest number among

```math
a,
 r_0,r_1,r_2,r_3,
 1.
```

If

```math
a > max_i r_i
qquad\text{and}\qquad a>1,
```

then `Q_n` is eventually positive.

If

```math
max_i r_i > max(a,1),
```

then `Q_n` is eventually negative.

If the maximum is tied, the sign depends on the number of maximal positive and negative contributions.

## Pure tensor enemy criterion

A tensor-power family would give an asymptotic pure four-balanced enemy if the base set satisfied:

```math
r_i >= 1 \quad\text{for every } i
```

so that all trilinear terms are nonnegative, and also

```math
max_i r_i > max(a,1),
```

so that `Q_n` is eventually negative.

Such a base example would produce tensor powers with

```math
Q_n < 0,
qquad
T_{i,n} >= 0 \quad\text{for all }i,
```

for all sufficiently large `n`.

## Small-prime computational check

Exhaustive search for `p <= 19` found no 4AP-free subset satisfying the pure tensor enemy criterion.

This does not prove nonexistence.  It only shows that the simplest tensor-power route does not produce the desired asymptotic obstruction at these primes.

## Relation to previous examples

The `F_11` example has `Q_n<0` for tensor powers, but it also has negative trilinear terms, so it is not pure.

The `F_17` example has `Q<0` and all `T_i>0` at level `n=1`, but its tensor powers have `Q_n>0` for every `n>=2`, because `a` dominates all `r_i`.

## Updated obstruction search

The clean product-construction obstruction would require finding a 4AP-free base set with

```math
r_i >= 1 \quad\forall i,
qquad
max_i r_i > max(a,1).
```

If no such base set exists in general, then any asymptotic pure four-balanced obstruction must be non-product or must arise only after localization/projection rather than direct tensoring.

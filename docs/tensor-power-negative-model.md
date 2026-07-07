# Tensor-power negative four-balanced model

## Status

Finite-field sanity check.  This tensors the small `F_11` example to an asymptotic family.  It is not a lower bound near the reciprocal-sum threshold, because its dimension is only logarithmic in `1/alpha`.

## Base example

Let

```math
A = {0,1,2,4,5,7} subset F_{11}
```

with

```math
alpha_0 = 6/11.
```

This set is 4AP-free in `F_11`.

For `n>=1`, define

```math
B_n = A^n subset F_{11}^n.
```

Then `B_n` is 4AP-free: a 4AP in `B_n` projects coordinatewise to a 4AP in `A`, so every coordinate of the common difference is zero.

The density is

```math
alpha_n = alpha_0^n = (6/11)^n.
```

Thus

```math
n = log(1/alpha_n)/log(11/6),
```

which is only logarithmic in `1/alpha_n`.

## Product factorization

Let `h=1_A` and `H=1_{B_n}`.  Since `H` is a tensor product, every 4AP average of products of `H` factorizes into the corresponding one-dimensional averages raised to the `n`th power.

For the base example, the relevant one-dimensional averages are:

```math
lambda_4 := Lambda_4(h,h,h,h) = 6/121,
```

```math
lambda_{012}=lambda_{123}=16/121,
qquad
lambda_{013}=lambda_{023}=21/121,
```

and every two-point average equals

```math
alpha_0^2 = 36/121.
```

## Four-balanced term for the tensor power

Let

```math
F_n = 1_{B_n} - alpha_n.
```

Then

```math
Q_n := Lambda_4(F_n,F_n,F_n,F_n)
```

is given by

```math
Q_n
= (6/121)^n
  - (6/11)^n * 2((16/121)^n + (21/121)^n)
  + 3(6/11)^{4n}.
```

Equivalently,

```math
Q_n / alpha_n^4
= 3 + (121/216)^n
    - 2(22/27)^n
    - 2(77/72)^n.
```

This is negative for every `n>=1`.  For large `n`, the negative term `-2(77/72)^n` dominates.

Thus negative four-balanced obstruction persists under tensor powers.

## Trilinear terms also persist

For the trilinear terms in the tensor power,

```math
T_{0,n}=T_{3,n}=(16/121)^n-(6/11)^{3n},
```

and

```math
T_{1,n}=T_{2,n}=(21/121)^n-(6/11)^{3n}.
```

Hence

```math
T_{0,n},T_{3,n}<0
```

for every `n>=1`.

So this tensor-power family does not isolate a pure four-balanced obstruction.  The negative four-balanced term coexists with negative trilinear terms at every tensor level.

## Relevance and limitation

This family proves that negative four-balanced obstruction can persist asymptotically for balanced indicators of 4AP-free sets.

However, it lives at the classical product-construction scale:

```math
n ~ log(1/alpha_n),
```

far below the desired forcing threshold

```math
n ~ alpha^{-1+delta}.
```

Therefore it does not threaten the proposed finite-field target.  Its value is diagnostic: any attempted positivity argument against negative four-balanced terms is false, but the remaining obstruction may still be convertible to trilinear structure in high-dimensional small-density regimes.

## Next research question

Can one construct a high-dimensional, small-density 4AP-free family near the scale

```math
n <= alpha^{-1+delta}
```

where

```math
Lambda_4(F,F,F,F) <= -c alpha^4
```

but all negative trilinear alternatives remain too small on low-codimension subspaces?

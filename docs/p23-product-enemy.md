# P23 product enemy for pure four-balanced obstruction

## Status

Computational counterexample to the candidate two-shadow domination conjecture.  This does not threaten the main reciprocal-sum target, because the tensor powers have dimension only logarithmic in inverse density.  It does show that direct tensor products can produce asymptotic pure four-balanced obstruction without negative trilinear terms.

## Exhaustive search result

An exhaustive backtracking search over nonempty subsets of `F_23` found:

```math
239614
```

4AP-free subsets.

Among these, exactly

```math
1518
```

satisfy the pure tensor enemy criterion

```math
E >= m^3/p,
qquad
I >= m^3/p,
qquad
max(E,I)>max(p,m^3/p).
```

Thus the candidate two-shadow domination conjecture is false at `p=23`.

## Explicit example

Let

```math
A={8,12,13,14,18,20,21,22} subset F_{23}.
```

Then

```math
m=8,
qquad
alpha=8/23.
```

A direct check over all `(x,d)` with `d != 0` shows that `A` contains no nontrivial 4AP.

The shadow counts are

```math
E=24,
qquad
I=23.
```

The random shadow scale is

```math
m^3/p = 512/23 = 22.2608...,
```

and

```math
max(E,I)=24>23=max(p,m^3/p).
```

So this set satisfies the pure tensor enemy criterion.

## Normalized tensor parameters

For this example,

```math
a = p^2/m^3 = 529/512,
```

```math
r_E = pE/m^3 = 23*24/512 = 69/64,
```

and

```math
r_I = pI/m^3 = 23*23/512 = 529/512.
```

Hence

```math
r_E>r_I=a>1.
```

## Tensor powers

Let

```math
B_n=A^n subset F_{23}^n,
qquad
alpha_n=(8/23)^n,
qquad
F_n=1_{B_n}-alpha_n.
```

Then `B_n` is 4AP-free for every `n`.

The tensor-power four-balanced term satisfies

```math
Q_n/alpha_n^4
= a^n-2r_E^n-2r_I^n+3.
```

Since `a=r_I`, this becomes

```math
Q_n/alpha_n^4
=3-2(69/64)^n-(529/512)^n.
```

This is negative for every `n>=1`.

The endpoint trilinear terms satisfy

```math
T_{0,n}=T_{3,n}=alpha_n^3((69/64)^n-1)>0,
```

and the interior trilinear terms satisfy

```math
T_{1,n}=T_{2,n}=alpha_n^3((529/512)^n-1)>0.
```

Thus this is an asymptotic pure four-balanced tensor obstruction:

```math
Q_n<0,
qquad
T_{i,n}>0 \quad\text{for all }i.
```

## Why this does not threaten the main target

The density of the tensor powers is

```math
alpha_n=(8/23)^n.
```

Therefore

```math
n = log(1/alpha_n)/log(23/8).
```

So the construction lives at the logarithmic product scale

```math
n ~ log(1/alpha_n),
```

far below the finite-field forcing scale sought for the reciprocal-sum route,

```math
n ~ alpha^{-1+delta}.
```

Thus it does not disprove the proposed finite-field target.  It only kills the hope that product constructions automatically force a negative trilinear obstruction whenever the four-balanced term is negative.

## Consequence for the proof search

The following candidate conjectures should now be marked false:

1. shadow-domination conjecture;
2. two-shadow domination conjecture;
3. direct tensor positivity/trilinear-conversion conjecture.

The remaining possible route is more subtle:

> Show that pure four-balanced tensor obstructions live only at product/logarithmic dimension scale, or that near the critical scale `n <= alpha^{-1+delta}` four-balanced negativity must localize into trilinear negativity or a large density increment.

## Next research question

Can one quantify why product pure four-balanced examples have only logarithmic dimension in `1/alpha`, and prove that any near-critical-dimensional pure four-balanced obstruction must have additional structure not present in the `F_23` tensor family?

# Quadratic correlation rank split

## Status

Proof-audit route split.  This note clarifies what a signed or unsigned quadratic correlation can and cannot buy.  A quadratic correlation is not automatically an affine-subspace density increment.  It becomes one only in the low-rank case; the high-rank case needs a direct recurrence/counting argument.

## Starting point

In the pure four-balanced branch one has

```math
Q=\Lambda_4(f,f,f,f) <= -c alpha^4,
```

with

```math
f=1_A-alpha.
```

By generalized von Neumann,

```math
||f||_{U^3} >= c alpha^4.
```

A generic finite-field `U^3` inverse theorem would give correlation with a quadratic phase:

```math
|E_x f(x)e_p(-q(x))| >= rho,
```

where `q:G -> F_p` is a quadratic polynomial and `rho` is some function of `alpha`.

## Correlation gives a quadratic-level density increment

Since `e_p(q(x))` takes only `p` values, a correlation of size `rho` implies that some quadratic level set

```math
V_t={x:q(x)=t}
```

has density increment of size at least

```math
c_p rho.
```

More precisely, after rotating the phase, the real part of the correlation is positive.  Averaging over the `p` fibers of `q`, at least one fiber must have

```math
E_{x in V_t} f(x) >= c_p rho,
```

provided the fiber has nonzero measure.  Thus

```math
|A cap V_t|/|V_t| >= alpha + c_p rho.
```

But `V_t` is generally a quadratic hypersurface, not an affine subspace.

Therefore this is not yet an induction-compatible density increment.

## Low-rank case

Suppose the quadratic phase has rank at most `R` in the sense that `q` depends on only `R` independent linear forms, up to affine-linear terms.

Then each relevant quadratic level set is a union of affine subspaces of codimension at most `R`.

A density increment on `V_t` then implies, by averaging over those affine pieces, a density increment on some affine subspace `W` with

```math
codim(W) <= R
```

and

```math
alpha_W >= alpha + c_p rho.
```

Thus the low-rank branch converts quadratic correlation into a usable affine density increment, but pays codimension `R`.

For the finite-field reciprocal-sum target, this branch is useful only if the rank/codimension cost and increment size satisfy the density-increment cost condition.  If

```math
rho ~ alpha^u,
qquad
R ~ alpha^{-v},
```

then a naive iteration has total exponent roughly

```math
v+u-1.
```

To beat the desired summability threshold, one needs

```math
v+u<2.
```

The borderline trilinear branch corresponds to `u=2`, `v=0`, giving equality rather than a win.

## High-rank case

If `q` has high rank, its level sets are not unions of low-codimension affine subspaces.  A density increment on `q(x)=t` cannot be directly fed into an affine-subspace induction.

The high-rank branch would instead need a direct counting statement, schematically:

> If `A` has increased density on a high-rank quadratic level set and is otherwise hyperplane-flat, then `A` contains a nontrivial 4AP.

This would use equidistribution/recurrence properties of high-rank quadratic forms rather than a plain density increment.

## Why sign might matter

The sign condition

```math
Q<0
```

is stronger than `||f||_{U^3}` being large.  It may force the quadratic structure to interact with the 4AP pattern with a definite orientation.

However, by itself, the sign does not automatically specify whether the quadratic phase is low-rank or high-rank, nor does it automatically produce an affine density increment stronger than the generic correlation scale.

Thus the sign is potentially useful only after one proves a one-sided recurrence or rank-split theorem.

## Updated route

The pure `U^3` branch should be split into two subcases:

1. **Low-rank quadratic branch.**  Convert to an affine-subspace density increment; track rank cost versus increment size.
2. **High-rank quadratic branch.**  Attempt direct 4AP recurrence/counting inside or relative to high-rank quadratic level sets.

This is more precise than the earlier target `large U3 => quadratic correlation`.

## Next research question

Can the negative four-balanced identity force either:

```math
rho >= alpha^{2-epsilon}
```

with low enough quadratic rank cost, or a high-rank quadratic recurrence contradiction?

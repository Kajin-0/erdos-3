# Minimal critical obstruction and hyperplane flatness

## Status

Proof-audit reduction.  This note records a scale-sensitive replacement for the false universal implication `Q<0 => some T_i<0`.  At the critical finite-field scale, a minimal counterexample must have no meaningful affine-hyperplane density increment.

## Target theorem form

Fix a prime `p>4` and an exponent

```math
theta = 1-delta < 1.
```

The desired finite-field forcing statement has the form:

```math
n >= C alpha^{-theta}
```

implies every subset `A subset F_p^n` of density `alpha` contains a nontrivial 4AP.

Equivalently, a counterexample is a 4AP-free set `A subset F_p^n` with density `alpha` and

```math
n >= C alpha^{-theta}.
```

## Minimal critical counterexample

Call a counterexample minimal if no affine hyperplane section is itself a counterexample for the same constant `C` and exponent `theta`.

Let `H subset F_p^n` be an affine hyperplane and let

```math
alpha_H = |A cap H|/|H|.
```

Then `A cap H` is also 4AP-free as a subset of `H ~= F_p^{n-1}`.

If

```math
n-1 >= C alpha_H^{-theta},
```

then `A cap H` is a lower-dimensional counterexample.  Therefore a minimal counterexample must satisfy

```math
alpha_H < (C/(n-1))^{1/theta}
```

for every affine hyperplane `H`.

## Near-threshold hyperplane flatness

Suppose the counterexample is near the critical boundary:

```math
n ~= C alpha^{-theta}.
```

Then

```math
(C/(n-1))^{1/theta}
= alpha (n/(n-1))^{1/theta}
= alpha (1 + 1/(n-1))^{1/theta}.
```

For large `n`, this is

```math
alpha (1 + 1/(theta n) + O(1/n^2)).
```

Thus a minimal near-threshold counterexample cannot have even a relative affine-hyperplane density increment much larger than

```math
1/(theta n).
```

In words: critical minimal obstructions must be hyperplane-density-flat.

## Why tensor products are nonminimal

For a fixed-base tensor product

```math
B_n=A^n subset F_p^{bn},
qquad
alpha_n=rho^n,
```

conditioning on one coordinate block lying in a favorable fiber usually increases density by a constant factor.

In the `F_23` product enemy, the base density is

```math
rho=8/23.
```

If one coordinate is fixed to a value in the base set, the remaining fiber has density

```math
rho^{n-1}=alpha_n/rho,
```

which is larger than the global density by the constant factor

```math
1/rho = 23/8.
```

This is far larger than the allowed minimal-counterexample increment scale

```math
1 + O(1/n).
```

Therefore tensor-product examples are strongly nonminimal at the critical scale.

## Interpretation

The `F_23` tensor enemy shows that pure four-balanced obstruction can exist with all trilinear terms positive.  But it also has obvious large hyperplane/fiber density increments.

A critical-scale proof should not try to rule out such product examples directly.  Instead it should pass to a denser lower-dimensional fiber until either:

1. the dimension scale is no longer critical; or
2. the remaining obstruction is hyperplane-flat.

The live enemy is therefore not a raw product tensor obstruction, but a hyperplane-flat pure four-balanced obstruction at dimension comparable to `alpha^{-theta}`.

## Updated proof target

A viable theorem can be reduced to the following scale-sensitive form:

> If `A subset F_p^n` is 4AP-free, has density `alpha`, satisfies `n >= C alpha^{-theta}`, and is hyperplane-flat in the sense that every affine hyperplane has density at most `alpha(1+O(1/n))`, then four-balanced negativity must force either a usable trilinear obstruction, a larger-codimension density increment, or a contradiction.

## Next research question

Can hyperplane-flatness be combined with the forced negative quartic 4AP identity to rule out pure four-balanced obstruction, or at least force a density increment on a codimension-`O(1)` affine subspace?

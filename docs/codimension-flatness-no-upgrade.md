# Codimension flatness does not upgrade the Fourier scale

## Status

Proof-audit negative result.  This note checks whether minimality on higher-codimension affine subspaces improves the hyperplane Fourier scale.  It does not: raw codimension-`r` minimality gives a weaker density-increment threshold, growing linearly with `r`.

## Setup

Fix

```math
theta=1-delta<1.
```

The desired finite-field forcing statement is

```math
n >= C alpha^{-theta}
```

for density-`alpha` subsets of `F_p^n`.

Let `A subset F_p^n` be a minimal counterexample near the critical boundary,

```math
n ~= C alpha^{-theta}.
```

For an affine subspace `W` of codimension `r`, write

```math
alpha_W = |A cap W|/|W|.
```

Since `A cap W` is still 4AP-free in `W ~= F_p^{n-r}`, minimality implies that `A cap W` cannot itself be a counterexample.  Therefore

```math
n-r < C alpha_W^{-theta}.
```

Equivalently,

```math
alpha_W < (C/(n-r))^{1/theta}.
```

## Near-boundary expansion

Using `n ~= C alpha^{-theta}`, the preceding bound becomes

```math
alpha_W
< alpha (n/(n-r))^{1/theta}.
```

For `r << n`,

```math
(n/(n-r))^{1/theta}
= (1-r/n)^{-1/theta}
= 1 + r/(theta n) + O(r^2/n^2).
```

Thus raw codimension-`r` minimality only forbids relative density increments larger than about

```math
r/(theta n).
```

Equivalently, the absolute increment scale it controls is

```math
alpha r/n.
```

## No upgrade over hyperplanes

For `r=1`, this recovers the hyperplane scale

```math
alpha/n.
```

For larger `r`, the bound becomes

```math
alpha r/n,
```

which is weaker, not stronger.

Therefore simply passing from hyperplanes to codimension-`r` affine subspaces cannot improve the Fourier scale.

## Comparison with the trilinear scale

To rule out a trilinear obstruction of size

```math
|T_i| >= c alpha^3,
```

one needs to rule out a Fourier/density-increment scale about

```math
alpha^2.
```

Codimension-`r` minimality gives only

```math
alpha r/n.
```

At the critical scale `n ~= alpha^{-theta}`, this is

```math
r alpha^{1+theta}.
```

To make this at most `alpha^2`, one would need

```math
r <= alpha^{1-theta} = alpha^delta.
```

For small `alpha`, this is less than `1`.  Hence no positive codimension can reach the `alpha^2` trilinear scale by raw minimality alone.

## Consequence

The previous question

```math
Can minimality be iterated to codimension r to upgrade alpha/n to alpha^2?
```

has a negative answer in this naive form.

Codimension minimality alone cannot close the exponent gap.  Any successful argument must use additional structure beyond the fact that lower-dimensional affine sections are not themselves critical counterexamples.

## What remains possible

The failure of raw codimension minimality does not rule out stronger mechanisms, such as:

1. energy increment across many Fourier modes;
2. a density increment on a structured subspace not measured only by codimension minimality;
3. use of the negative quartic 4AP identity;
4. classification of pure four-balanced obstructions;
5. an arithmetic regularity or entropy argument that gains more than `r/n` per codimension.

## Updated next research question

Can the forced negative quartic identity produce an energy increment or structured density increment stronger than the codimension-minimality bound

```math
alpha r/n?
```

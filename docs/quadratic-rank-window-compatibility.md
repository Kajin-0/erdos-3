# Quadratic rank-window compatibility

## Status

Proof-audit bookkeeping lemma.  This note checks whether the proposed low-rank and high-rank quadratic branches can cover all quadratic ranks without leaving a fatal medium-rank window.

## Setup

In the pure four-balanced branch, assume a one-sided quadratic-structure theorem produces a density increment on a quadratic level set with absolute increment

```math
rho >= c alpha^{2-epsilon_F}
```

and quadratic rank `R`.

The target finite-field exponent is

```math
n ~ alpha^{-theta},
qquad theta=1-delta<1.
```

## Low-rank coverage

The low-rank minimality threshold says that an affine increment of size `rho >= alpha^{2-epsilon_F}` contradicts minimality provided the rank/codimension obeys

```math
R << alpha^{-(epsilon_F-delta)}.
```

Thus the low-rank branch covers all ranks up to a power of `alpha^{-1}`, assuming

```math
epsilon_F>delta.
```

## High-rank coverage

The high-rank relative recurrence target should apply once the rank is at least some threshold

```math
R >= R_high(n,beta),
```

where `beta` is the relative density on the quadratic level.  In the relevant regime,

```math
beta ~ alpha.
```

A plausible high-rank theorem should have threshold at most polylogarithmic or small-power in `1/beta`, for example

```math
R_high(n,beta) = O_p(log(1/beta))
```

or more generally

```math
R_high(n,beta) <= beta^{-sigma}
```

for some `sigma>0`.

## Compatibility condition

There is no fatal medium-rank window if

```math
R_high(n,alpha) << alpha^{-(epsilon_F-delta)}.
```

If

```math
R_high(n,alpha)=O_p(log(1/alpha)),
```

this holds for every fixed positive `epsilon_F-delta`.

If instead

```math
R_high(n,alpha) <= alpha^{-sigma},
```

then compatibility requires

```math
sigma < epsilon_F-delta.
```

## Consequence

A high-rank theorem with logarithmic rank threshold is highly compatible with the low-rank minimality branch.

The dangerous case is a high-rank recurrence theorem whose rank threshold is itself a large power of `alpha^{-1}`.  Then the medium-rank window

```math
alpha^{-(epsilon_F-delta)} \lesssim R \lesssim alpha^{-sigma}
```

would remain unresolved whenever

```math
sigma >= epsilon_F-delta.
```

## Updated theorem target

The one-sided quadratic rank split should aim for the following parameter profile:

1. low-rank branch: density increment at least `alpha^{2-epsilon_F}` for ranks

```math
R <= alpha^{-(epsilon_F-delta)};
```

2. high-rank branch: relative recurrence or structured escape once

```math
R >= C_p log(1/alpha)
```

or at worst `R >= alpha^{-sigma}` with `sigma < epsilon_F-delta`.

Under a logarithmic high-rank threshold and `epsilon_F>delta`, the rank split has overlap rather than a gap.

## Interpretation

The medium-rank issue is not an independent obstruction if the high-rank counting theorem begins at logarithmic rank.  It becomes a real obstruction only if high-rank equidistribution requires rank polynomially large in `1/alpha` with exponent comparable to or larger than the density-increment exponent gain.

## Next research question

Can high-rank quadratic-level relative counting be made effective at rank

```math
R >= C_p log(1/beta)
```

rather than at a polynomial rank threshold?  This is now the precise rank-threshold requirement for the pure `U^3` route.

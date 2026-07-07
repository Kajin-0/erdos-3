# Correlation threshold for a viable density increment

## Status

Proof-audit model following the density-increment cost calculation.  This note translates the forced `U^3` obstruction into the minimum correlation/increment strength needed for an iterative proof to remain below total codimension `alpha^{-1}`.

## Forced obstruction size

For a 4AP-free set `A subset F_p^n` of density `alpha`, the balanced function

```math
f = 1_A - alpha
```

satisfies

```math
||f||_{U^3} >= c alpha^4.
```

Let

```math
delta := ||f||_{U^3}.
```

Then the available obstruction size is only

```math
delta >= c alpha^4.
```

## Generic inverse/correlation route

A standard route has the schematic form

```math
large U^3 norm delta
-> correlation at least rho(delta)
-> density increment at least comparable to rho(delta)
```

on a structured object of some codimension cost.

Suppose the output correlation is a power law

```math
rho(delta) >= c delta^M.
```

With `delta >= c alpha^4`, this gives a density increment no larger than the scale

```math
Delta alpha ~ alpha^{4M}.
```

Thus, in the density-increment notation,

```math
t = 4M.
```

## Viability threshold

The previous cost model requires

```math
s + t < 2,
```

where `s` is the per-step codimension exponent and `t` is the density-increment exponent.

Substituting `t=4M` gives the necessary condition

```math
s + 4M < 2.
```

In particular, even if codimension per step were free (`s=0`), one would need

```math
M < 1/2.
```

So a usual inverse-theorem output with `M >= 1` cannot reach the reciprocal-sum threshold through a naive iterative density-increment route.

## Interpretation

A standard implication of the form

```math
||f||_{U^3} >= delta
=> correlation >= delta^M
```

is too weak if `M >= 1`, because the forced obstruction itself is only `alpha^4`.

To make an iterative route viable, one needs a consequence of the no-4AP hypothesis that is stronger than ordinary black-box inversion.  Roughly, the proof would have to upgrade an `alpha^4` 4AP-counting deficiency into a density increment closer to linear in `alpha`.

## Consequence for full inverse theorem strategy

The full quantitative `U^3` inverse theorem is not merely quantitatively inefficient.  In this cost model, any black-box inverse theorem whose useful correlation is at most on the order of `delta` already leads to `t>=4`, hence too many iterations.

Therefore a successful proof needs at least one nonstandard feature:

1. a direct contradiction rather than iterative density increments;
2. a density increment much larger than the raw `U^3` obstruction scale;
3. an iteration that reuses accumulated structure so the naive iteration count `alpha^{-(t-1)}` is false;
4. a recurrence/counting inequality that extracts more from the indicator/no-4AP hypotheses than generic `U^3` inversion.

## Next research question

Can 4AP-freeness force a density increment of size

```math
Delta alpha >= c alpha^{1+epsilon}
```

on a structured object of codimension at most

```math
alpha^{-1+o(1)-epsilon},
```

or is any increment derived from the `U^3` obstruction necessarily of size at most about `alpha^4`?

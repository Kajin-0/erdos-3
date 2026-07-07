# Density-increment cost model after forced U3 obstruction

## Status

Proof-audit model.  This note converts the forced `U^3` obstruction into a generic density-increment cost calculation.  It is not a theorem; it is a constraint on possible proof architectures.

## Starting point

For a 4AP-free set `A subset F_p^n` of density `alpha`, once `|G| >= 2 alpha^{-3}`, the balanced function

```math
f = 1_A - alpha
```

satisfies

```math
||f||_{U^3} >= c alpha^4.
```

Thus a direct proof must exploit a large `U^3` obstruction of size about `alpha^4`.

## Generic density-increment black box

Suppose one has a black box of the following form:

If `A` has density `alpha` and no nontrivial 4AP, then there is an affine subspace `W` of codimension at most

```math
C alpha^{-s}
```

on which the relative density of `A` increases by at least

```math
c alpha^{t}.
```

That is,

```math
alpha_W >= alpha + c alpha^t.
```

## Iteration count

The number of iterations needed to raise density from `alpha` to an absolute constant is controlled by

```math
int_alpha^1 x^{-t} dx.
```

For `t>1`, this is roughly

```math
alpha^{-(t-1)}.
```

For `t=1`, it is logarithmic in `1/alpha`.

## Total codimension cost

If each step costs at most `alpha^{-s}` codimension at the current density scale, and the density increment is `alpha^t`, then the total codimension cost is roughly

```math
alpha^{-s} alpha^{-(t-1)} = alpha^{-(s+t-1)}.
```

To beat the reciprocal-sum threshold in the finite-field sandbox, one needs total codimension

```math
<< alpha^{-1+delta}
```

for some `delta>0`.

Thus the black-box exponents must satisfy

```math
s + t - 1 < 1,
```

or

```math
s + t < 2.
```

## Consequence

This is a severe constraint.

A density increment of size only

```math
alpha^4
```

would have `t=4`.  Even if the codimension cost per step were constant (`s=0`), the total iteration count alone would be

```math
alpha^{-3},
```

far above the target `alpha^{-1+delta}`.

Therefore a successful proof cannot merely convert

```math
||1_A-alpha||_{U^3} >= c alpha^4
```

into a density increment of comparable size.  It needs either:

1. a much larger density increment, ideally `t<2`; or
2. a non-iterative contradiction/counting mechanism; or
3. an iteration with accelerating increments or reused structure so that the naive `alpha^{-(t-1)}` count is avoided.

## Updated target

A viable finite-field density-increment route should aim for something like:

```math
codim step cost: alpha^{-s},
 density increment: alpha^t,
 s+t<2.
```

The closer `t` is to `1`, the more codimension budget remains.  If `t=1+epsilon`, then one may tolerate `s<1-epsilon`.

## Next research question

Can the special no-4AP hypothesis upgrade the consequence of large `U^3` norm from a tiny increment of size `alpha^C` to an increment of size approximately linear in `alpha`, without paying codimension above `alpha^{1-o(1)}`?

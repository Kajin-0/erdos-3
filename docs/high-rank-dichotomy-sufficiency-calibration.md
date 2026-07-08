# High-rank dichotomy sufficiency calibration

## Status

Proof-audit implication check.  This note verifies when the sharpened high-rank quadratic-level dichotomy would actually imply a useful gain for the main `r_4` program.

## Candidate high-rank dichotomy

The sharpened high-rank target is:

> For fixed `p>4`, if `q` is high-rank and `B subset V_t={x:q(x)=t}` is internally 4AP-free with relative density `beta`, then either
>
> 1. `B` has a linear/low-rank density increment of codimension `O_p(log(1/beta))`; or
> 2. `beta <= C_p n^{-1-epsilon_h}`.

Here `epsilon_h>0` is the high-rank independence gain.

## Threshold comparison

In the main finite-field model, the desired forcing scale is

```math
n >= C alpha^{-theta},
qquad theta=1-delta<1.
```

In the high-rank branch, the relative density on the quadratic level is typically

```math
beta = alpha + rho.
```

In the small-increment regime, this is essentially

```math
beta ~ alpha.
```

The high-rank recurrence side applies when

```math
beta > C_p n^{-1-epsilon_h}.
```

Substituting `n ~ alpha^{-theta}` and `beta ~ alpha`, this requires

```math
alpha > C_p alpha^{theta(1+epsilon_h)}.
```

For small `alpha`, this holds exactly when

```math
theta(1+epsilon_h) > 1.
```

Equivalently,

```math
theta > 1/(1+epsilon_h).
```

Since `theta=1-delta`, this is

```math
1-delta > 1/(1+epsilon_h),
```

or

```math
delta < epsilon_h/(1+epsilon_h).
```

## Consequence

A high-rank independence gain `epsilon_h` would support a finite-field forcing exponent

```math
theta > 1/(1+epsilon_h),
```

hence a reciprocal-summability-type gain

```math
delta < epsilon_h/(1+epsilon_h).
```

Thus any positive `epsilon_h` is, in principle, enough to produce some positive exponent gap below `1` in the finite-field model.

For small `epsilon_h`, the usable `delta` is approximately

```math
delta < epsilon_h.
```

## Logarithmic-codimension increment cost

If the dichotomy returns a structured density increment rather than recurrence, the codimension cost is

```math
O_p(log(1/beta)).
```

At `beta ~ alpha`, this is

```math
O_p(log(1/alpha)).
```

This is negligible relative to the critical dimension scale

```math
n ~ alpha^{-theta}
```

for every fixed `theta>0`.

Therefore the low-rank escape branch is not too expensive at the level of dimension bookkeeping.

The real issue is the increment size: the returned density increment must be large enough to feed into the existing density-increment/minimality mechanism.  A constant-factor or `beta^{2-epsilon}`-type increment would be meaningful; a merely infinitesimal increment may not be.

## What the dichotomy would prove

If the high-rank branch gives the above dichotomy with `epsilon_h>0`, and if the structured-increment branch gives a usable density increment, then the high-rank pure-`U^3` branch can be closed for any target exponent

```math
theta > 1/(1+epsilon_h).
```

Equivalently, it contributes to proving a dyadically summable `r_4`-type estimate with a positive logarithmic gain.

## Remaining caveat

This only handles the high-rank quadratic-level branch.  The full proof still also needs to handle:

1. the borderline trilinear branch;
2. the low-rank quadratic branch;
3. medium-rank cases that are not high-rank enough for the relative counting lemma but too high-rank for cheap affine decomposition;
4. the transfer from finite-field model to integer `r_4(N)` estimates.

## Updated target statement

The useful high-rank theorem should be stated with explicit parameters:

> For fixed `p>4`, there exist `epsilon_h>0`, constants `C_p,c_p`, and a rank threshold `R_p(n,beta)` such that if `q` has rank at least `R_p(n,beta)` and `B subset {q=t}` is internally 4AP-free with density `beta`, then either
>
> ```math
> beta <= C_p n^{-1-epsilon_h},
> ```
>
> or `B` has a density increment of size at least `c_p F(beta)` on a linear/low-rank factor of codimension `O_p(log(1/beta))`.

The function `F(beta)` is the next quantity to determine.

## Next research question

Can the high-rank checkpoint be proved with `epsilon_h=0` and a quantitatively useful increment function `F(beta)`?  This is the minimal test before seeking the exponent-improving `epsilon_h>0` form.

# Prendiville threshold calibration

## Status

Proof-audit calibration.  This note compares Prendiville's relative `U^3` inverse theorem against the actual exponent threshold needed for the reciprocal-sum/4AP route.

The conclusion is mixed:

1. Prendiville's theorem has the right *structural* shape for the high-rank quadratic-level branch.
2. As a black-box density theorem it does not yet provide the needed exponent unless its hidden power exceeds `1`.
3. Its most useful role is likely not as a final bound, but as the high-rank inverse step after a sharper no-4AP `=>` relative `U^3` lower bound is proved.

## Required finite-field threshold

The finite-field surrogate target is:

```math
A\subset F_p^n,
\qquad |A|/p^n=\alpha,
```

and every density-`alpha` set contains a nontrivial 4AP once

```math
n\ge C\alpha^{-1+\delta}.
```

Equivalently, the largest 4AP-free density should satisfy

```math
\alpha\ll n^{-1/(1-\delta)}.
```

Since

```math
\frac{1}{1-\delta}=1+\frac{\delta}{1-\delta}>1,
```

this route needs an exponent strictly larger than `1`:

```math
\alpha\ll n^{-1-\epsilon}.
```

A generic positive-power bound

```math
\alpha\ll n^{-c_p}
```

is not enough unless

```math
c_p>1.
```

## What Prendiville provides at black-box level

Prendiville's Theorem 1.5 gives, for translation-invariant configurations of complexity two, a density bound of the form

```math
|A|/p^n\ll_p n^{-\Omega_p(1)}.
```

This includes the same general complexity-two universe as finite-field 4APs, but the exponent is only stated as a positive `p`-dependent constant.

Therefore, as a black box, it does not yet reach the reciprocal-sum threshold.  To close the dyadic route we would need to extract or improve the exponent to exceed `1`.

## What Prendiville provides structurally

Theorem 1.2 is much more valuable structurally.  It says that for a 1-bounded function supported on a quadratic level set

```math
Q^{-1}(0),
```

large relative `U^3` norm implies either:

1. correlation with a quadratic phase of strength

```math
\delta^{O_p(1)}|Q^{-1}(0)|;
```

or

2. a low-rank escape: some nontrivial linear combination of the homogeneous quadratic parts of the host tuple has rank

```math
O_p(d+\log(2/\delta)).
```

The second alternative is crucial: if `delta` is a power of the relative density `beta`, the low-rank threshold becomes

```math
O_p(d+\log(1/\beta)),
```

which matches the previously identified acceptable logarithmic rank-window escape.

## Implication for the high-rank branch

For the repo's high-rank branch, suppose

```math
B\subset V_t=\{x:q(x)=t\},
\qquad |B|/|V_t|=\beta,
```

and `B` is internally 4AP-free.

The needed chain is not merely Prendiville's theorem.  It is:

```math
\text{internal 4AP-free}
\Rightarrow
\text{relative }U^3\text{ mass }\delta(\beta)
\Rightarrow
\text{relative quadratic correlation}
\Rightarrow
\text{density increment or recurrence}.
```

The theorem supplies the middle implication only.

## Exponent audit

Assume the relative generalized von Neumann step gives

```math
\delta(\beta)\gtrsim \beta^s.
```

Prendiville then gives a relative quadratic correlation of size roughly

```math
\beta^{sC_p}
```

for some constant `C_p` hidden in `O_p(1)`.

If correlation converts directly to an increment of the same scale, the increment exponent is

```math
u=sC_p.
```

To be useful against the existing minimality/rank-window model, one wants an increment at least

```math
\beta^{2-\epsilon_F},
```

so one needs

```math
sC_p<2.
```

If `sC_p\ge2`, then Prendiville still gives structure, but not an increment strong enough for the current exponent-gap strategy without an additional non-iterative or high-rank recurrence gain.

## High-rank recurrence alternative

The other way to use Prendiville is not to demand a large affine increment.  Instead, use it to prove a relative recurrence theorem inside high-rank quadratic hosts:

```math
B\subset V_t,
\qquad B\text{ internally 4AP-free}
\Rightarrow
\beta\le C_p n^{-1-\epsilon_h}.
```

This would directly supply the needed high-rank independence gain.  But Prendiville's stated application gives only

```math
n^{-\Omega_p(1)}
```

at black-box level, so a stronger extraction is required.

## Updated bottleneck

The bottleneck is now precise:

> Can the specific internal 4AP system inside a high-rank quadratic level set produce either a relative `U^3` lower bound and correlation-to-increment exponent satisfying `sC_p<2`, or a direct high-rank recurrence exponent `1+epsilon_h`?

If yes, Prendiville likely closes the high-rank branch.

If no, Prendiville is still useful but not enough for the reciprocal-sum threshold.

## Immediate tasks

1. Extract the exact exponent hidden in Prendiville's `delta^{O_p(1)}`.
2. Extract the density-increment step in §§7--9 and determine the increment exponent.
3. Specialize the relative counting lemma to internal 4APs on a single high-rank quadratic level set.
4. Check whether the resulting density bound exponent exceeds `1`.
5. If the exponent is below or equal to `1`, return to the pair-fiber/shear-energy route to seek a stronger system-specific gain.

## Current verdict

Prendiville is a serious structural unlock, but not yet a solved bottleneck.

It validates the high-rank quadratic-level architecture and supplies the right logarithmic low-rank escape threshold.  The remaining question is quantitative: does the resulting exponent cross the `1` threshold required for dyadic summability?

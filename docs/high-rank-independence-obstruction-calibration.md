# High-rank independence obstruction calibration

## Status

Proof-audit stress test.  This note checks the plausibility of the high-rank relative independence target by calibrating obvious structured subsets of a quadratic level set.

## Setup

Let

```math
G=F_p^n,
qquad p>4,
```

and let `q:G -> F_p` be a high-rank quadratic polynomial.  Let

```math
V_t={x:q(x)=t}
```

and let `H_q` be the internal 4AP hypergraph on `V_t`.

The desired high-rank recurrence target is an independence bound

```math
alpha(H_q) <= C_p |V_t|/n^{1+epsilon}
```

unless the independent set has a linear or low-rank density increment.

The first checkpoint is the weaker estimate

```math
alpha(H_q) <= C_p |V_t|/n.
```

## Calibration: linear slices

A codimension-`R` affine slice of `V_t` has expected size

```math
|V_t| p^{-R}
```

when the slice is transverse to the quadratic level.

Thus the scale

```math
|V_t|/n
```

corresponds to

```math
p^{-R} ~ 1/n,
```

or

```math
R ~ log_p n.
```

Therefore the high-rank theorem cannot merely exclude constant-codimension linear concentration.  To prove an independence bound at the `|V_t|/n` scale, it must treat even logarithmic-codimension linear concentration as an escape branch.

This is still potentially acceptable for the main proof program: spending codimension `O(log n)` is negligible compared with the target dimension scale `n ~ alpha^{-1+delta}`.

## Totally isotropic affine subspaces

High-rank quadratic level sets contain affine subspaces coming from totally isotropic directions.  In a nondegenerate quadratic space of dimension `n`, maximal totally isotropic subspaces have dimension about `n/2`.

Such a subspace has size roughly

```math
p^{n/2}.
```

Meanwhile a high-rank quadratic level has size about

```math
|V_t| ~ p^{n-1}.
```

The relative size is therefore about

```math
p^{1-n/2},
```

which is exponentially smaller than `1/n`.

Thus totally isotropic affine subspaces do not obstruct a polynomial-scale bound such as `|V_t|/n` or `|V_t|/n^{1+epsilon}`.

## Hyperplane fibers

A single hyperplane slice of `V_t` has relative size about `1/p`, much larger than `1/n`.

Such a set may or may not contain internal 4APs, depending on the induced quadratic geometry on the hyperplane.  But in either case it is not a high-rank pseudorandom obstruction: it has an obvious linear density increment.

Therefore a valid high-rank theorem must be stated as a dichotomy:

1. return a linear or low-rank density increment; or
2. prove internal 4AP recurrence in the remaining pseudorandom part.

## Implication for theorem formulation

The desired high-rank theorem should not be written as a raw universal bound

```math
alpha(H_q) <= C_p |V_t|/n^{1+epsilon}
```

for all subsets, because large structured slices may violate it while belonging to the low-rank/linear branch.

A more accurate theorem is:

> If `B subset V_t` is internally 4AP-free and has relative density `beta >= C/n^{1+epsilon}`, then `B` has a density increment on a linear or low-rank factor of codimension at most `O_p(log(1/beta))`.

At the checkpoint `beta ~ 1/n`, this codimension is `O(log n)`.

## Why this is compatible with the main target

If the high-rank branch returns a codimension `O(log(1/beta))` density increment, this cost is small relative to the critical scale

```math
n ~ beta^{-theta},
qquad theta<1.
```

Therefore logarithmic-codimension escape routes are not fatal.  They may actually be the right regularity output: either count internal APs, or find a structured low-complexity factor on which density has increased.

## Updated target

The high-rank target should be sharpened to:

> For fixed `p>4`, if `q` has high rank and `B subset V_t` is internally 4AP-free with relative density `beta`, then either
>
> 1. `B` has a linear/low-rank density increment of codimension `O_p(log(1/beta))`, or
> 2. `beta <= C_p/n^{1+epsilon}`.

This formulation is stronger and cleaner than a raw independence-number bound because it separates genuine high-rank pseudorandom behavior from structured slices.

## Next research question

Can one prove the checkpoint dichotomy with `epsilon=0`:

```math
B \text{ internally 4AP-free},\quad beta >= C/n
```

implies a linear or low-rank density increment of codimension `O_p(log n)`?

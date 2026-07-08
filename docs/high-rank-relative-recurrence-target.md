# High-rank relative recurrence target

## Status

Proof-audit target formulation.  This note translates the high-rank quadratic branch into an explicit recurrence theorem that would be strong enough to matter for the main `r_4` summability problem.

## Setup

Let

```math
G=F_p^n,
qquad p>4,
```

and let `q:G -> F_p` be a quadratic polynomial whose homogeneous quadratic part has high rank.

For a level set

```math
V_t={x:q(x)=t},
```

consider the internal 4AP hypergraph on `V_t`: edges are quadruples

```math
x,\quad x+d,\quad x+2d,\quad x+3d
```

lying entirely in `V_t`.

Equivalently, the parameters `(x,d)` satisfy

```math
q(x)=t,
qquad
q_2(d)=0,
qquad
q(x+d)=q(x).
```

For high rank, this edge set has the expected algebraic scale about

```math
p^{2n-3}.
```

## Relative recurrence theorem needed

A high-rank quadratic density increment gives a set

```math
B=A cap V_t
```

with relative density

```math
beta=|B|/|V_t|.
```

To close the high-rank branch by direct recurrence, one would need a theorem of the following type:

> For fixed `p>4`, if `q` has sufficiently high rank and `B subset V_t` has relative density `beta`, then `B` contains a nontrivial internal 4AP whenever
>
> ```math
> n >= C beta^{-theta_q}
> ```
>
> for some exponent `theta_q<1`.

If such a theorem held with `theta_q<1`, then it would match the desired summability scale better than the ordinary logarithmic-barrier branch.

## Why the exponent matters

In the main proof track, a minimal critical obstruction has ambient scale

```math
n ~ alpha^{-theta},
qquad theta=1-delta<1.
```

A quadratic-level increment usually gives

```math
beta = alpha + rho.
```

In the relevant small-increment regime, `rho` may be much smaller than `alpha`, so

```math
beta ~ alpha.
```

Therefore the high-rank recurrence theorem must work at density roughly `alpha` and dimension roughly `alpha^{-theta}`.

If the best available theorem has `theta_q >= 1`, it does not beat the logarithmic barrier.  If it has `theta_q<1`, then the high-rank branch can potentially close the gap.

## Non-circularity requirement

The high-rank theorem must exploit special structure of the internal AP hypergraph on the quadratic level set.

A theorem that merely reduces the problem to ordinary 4AP recurrence in an affine space of comparable dimension is circular: it would require essentially the same `r_4` bound we are trying to prove.

Thus the desired theorem must use at least one of:

1. high-rank equidistribution of the quadratic form;
2. pseudorandomness of the isotropic-direction AP hypergraph;
3. the fact that the host is a fixed-codimension algebraic variety with constant edge density inside `G^2`;
4. hyperplane-flatness inherited from minimality;
5. the sign information `Q<0`, not merely density on `V_t`.

## Random-model heuristic

The full internal AP hypergraph has about

```math
p^{2n-3}
```

parameterized edges.  A random subset of `V_t` of relative density `beta` would contain about

```math
beta^4 p^{2n-3}
```

internal 4APs.

At the critical scale `n ~ beta^{-theta}` with `theta<1`, this expected count is enormous.

However, this random heuristic is not a proof for arbitrary `B subset V_t`.  The real question is whether the high-rank algebraic AP hypergraph has sufficiently strong quasirandomness or expansion to force edges in every dense subset at the required quantitative threshold.

## Possible obstruction

A subset `B subset V_t` may concentrate on lower-rank or linearly structured pieces of the variety.  Those pieces could avoid many internal APs while still having nontrivial relative density.

Therefore any high-rank recurrence theorem likely needs a regularity or decomposition statement:

1. if `B` has linear/low-rank concentration, return to the affine or low-rank density-increment branch;
2. otherwise, prove relative counting in the high-rank pseudorandom part.

## Updated high-rank target

The high-rank branch should aim for a dichotomy:

```math
B subset V_t,\quad |B|/|V_t|=beta
```

implies either

1. `B` has a linear or low-rank density increment compatible with the low-rank branch; or
2. `B` contains an internal 4AP once `n >= C beta^{-theta_q}` for some `theta_q<1`.

## Next research question

Can the internal 4AP hypergraph of a high-rank quadratic level set be shown to have a relative independence number at most

```math
|V_t| / n^{1+epsilon}
```

or any stronger bound implying dyadic summability along the finite-field model?

# Low-rank quadratic minimality threshold

## Status

Proof-audit scale lemma.  This note applies minimal criticality to the low-rank quadratic branch.  It quantifies when a quadratic-level density increment can actually contradict minimality.

## Setup

Let

```math
A subset F_p^n,
qquad
alpha=|A|/p^n,
```

be a minimal counterexample near the target scale

```math
n \sim C alpha^{-theta},
qquad
theta=1-delta<1.
```

Suppose the pure `U^3` branch yields correlation with a quadratic phase `q` of rank at most `R`, and hence a density increment of size `rho` on a quadratic level set

```math
V_t={x:q(x)=t}.
```

In the low-rank case, `V_t` decomposes into affine pieces of codimension at most `R`, so averaging gives an affine subspace `W` with

```math
codim(W) <= R
```

and

```math
alpha_W >= alpha + c_p rho.
```

## Minimality bound at codimension R

Minimality says that no codimension-`R` affine section can remain a counterexample.  Thus, near the critical boundary,

```math
alpha_W < alpha (n/(n-R))^{1/theta}.
```

For `R << n`, this gives

```math
alpha_W < alpha(1 + R/(theta n) + O(R^2/n^2)).
```

Therefore any affine-subspace density increment compatible with minimality must satisfy roughly

```math
rho <= C_{p,theta} alpha R/n.
```

At the critical scale `n ~ alpha^{-theta}`, this becomes

```math
rho <= C_{p,theta} R alpha^{1+theta}
     = C_{p,theta} R alpha^{2-delta}.
```

## Consequence for a desired improved increment

Suppose a one-sided quadratic theorem could produce

```math
rho >= c alpha^{2-epsilon}.
```

Then this contradicts minimality provided

```math
alpha^{2-epsilon} >> R alpha^{2-delta},
```

or equivalently

```math
R << alpha^{-(epsilon-delta)}.
```

Thus, for a fixed target `delta`, an exponent-improving increment `alpha^{2-epsilon}` is useful only when

```math
epsilon>delta
```

and the quadratic rank is below the threshold

```math
R < alpha^{-(epsilon-delta)}
```

up to constants.

## Interpretation

This is the precise low-rank target.

To prove the `r_4` summability target with some gain `delta>0`, a low-rank quadratic branch must provide:

1. a density increment stronger than the logarithmic-barrier scale, say `alpha^{2-epsilon}` with `epsilon>delta`;
2. rank/codimension cost below approximately `alpha^{-(epsilon-delta)}`.

If the rank is larger than this threshold, minimality no longer rules it out, and the branch effectively becomes a medium/high-rank recurrence problem rather than a clean density-increment step.

## Generic inverse theorem comparison

A generic inverse theorem starting only from

```math
||f||_{U^3} >= c alpha^4
```

usually gives correlation scale

```math
rho ~ alpha^{4M}
```

with `M>=1` in ordinary black-box uses.

This is far smaller than `alpha^{2-epsilon}` and therefore cannot beat the minimality threshold.

So the low-rank branch cannot be solved by a generic inverse theorem.  It requires a one-sided theorem using more of the assumptions:

```math
Q<0,
qquad
f=1_A-alpha,
qquad
4AP\text{-free},
qquad
minimal/flat.
```

## Updated next research question

Can the sign condition `Q<0` force either:

```math
rho >= alpha^{2-epsilon}
```

with rank

```math
R < alpha^{-(epsilon-delta)},
```

or else force a high-rank recurrence contradiction?

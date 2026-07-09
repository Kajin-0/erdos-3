# Load increment first dichotomy

## Status

Local lemma.  This note proves the first rigorous step in the pair-fiber load-variance model.

High second moment of the vertex-load function gives a concrete pair-neighborhood increment.  This is not yet a subspace or Bohr-set increment; it is the raw increment object that later must be structured.

## Setup

Let `G` be a finite abelian group of size `N`, and let

```math
A\subseteq G,
\qquad
|A|=\alpha N,
\qquad
b=1_A.
```

Let `D` be a direction set with `K=|D|`.  For each `d in D`, define

```math
P_d=\{x:x,x+d\in A\},
\qquad
1_{P_d}(x)=b(x)b(x+d).
```

The vertex-load function is

```math
L_D(x)=\sum_{d\in D}1_{P_d}(x)
=\sum_{d\in D}b(x)b(x+d).
```

It is supported on `A`.  Define the average load on `A` by

```math
\lambda=E_{x\in A}L_D(x)
=\frac{1}{|A|}\sum_xL_D(x)
=\frac{1}{\alpha}\sum_{d\in D}\rho_d,
```

where

```math
\rho_d=N^{-1}|P_d|.
```

In the popular-direction model, `rho_d approx alpha^2`, hence

```math
\lambda\approx \alpha K.
```

## Exact second-moment identity

The second moment satisfies

```math
\sum_xL_D(x)^2
=\sum_{d,e\in D}|P_d\cap P_e|.
```

Indeed,

```math
L_D(x)^2
=\sum_{d,e\in D}1_{P_d}(x)1_{P_e}(x),
```

and summing in `x` gives

```math
\sum_x1_{P_d}(x)1_{P_e}(x)=|P_d\cap P_e|.
```

Writing

```math
I(d,e)=|P_d\cap P_e|
=|\{x:x,x+d,x+e\in A\}|,
```

the identity is

```math
\sum_xL_D(x)^2=\sum_{d,e\in D}I(d,e).
```

## Minimal second moment

Since `L_D` is supported on `A`, Cauchy--Schwarz gives

```math
\sum_xL_D(x)^2
\ge
\frac{(\sum_xL_D(x))^2}{|A|}
=|A|\lambda^2.
```

Thus

```math
M_2(D):=\sum_xL_D(x)^2
```

is minimal exactly when `L_D` is constant on `A`.

The load-variance excess is

```math
\mathsf{Var}_A(L_D)
:=E_{x\in A}(L_D(x)-\lambda)^2
=
\frac{M_2(D)}{|A|}-\lambda^2.
```

So the high-variance condition

```math
M_2(D)\ge(1+\eta)|A|\lambda^2
```

is equivalent to

```math
\mathsf{Var}_A(L_D)\ge\eta\lambda^2.
```

## Pair-neighborhood increment

For each `x in A`, define the local density of `A` in the translated direction cloud `x+D`:

```math
\delta_D(x)=\frac{1}{K}\sum_{d\in D}b(x+d)=\frac{L_D(x)}{K}.
```

Since `x in A`, this is the density of forward neighbors of `x` lying in `A` along `D`.

The average over `A` is

```math
E_{x\in A}\delta_D(x)=\frac{\lambda}{K}.
```

In the popular model this is approximately `alpha`.

If `L_D(x)>(1+\theta)\lambda`, then

```math
\delta_D(x)>(1+\theta)\frac{\lambda}{K}.
```

Thus any high-load point gives a local pair-neighborhood density increment of relative size `theta` inside the translate `x+D`.

This is the first raw increment object.

## Quantitative high-load extraction

Assume

```math
E_{x\in A}(L_D(x)-\lambda)^2\ge\eta\lambda^2.
```

Let

```math
U=K/\lambda.
```

Since `0<=L_D(x)<=K`, the normalized variable

```math
Y(x)=L_D(x)/\lambda
```

satisfies

```math
E_{x\in A}Y=1,
\qquad
0\le Y\le U,
\qquad
E_{x\in A}(Y-1)^2\ge\eta.
```

Because `E(Y-1)=0`, the positive and negative parts have equal first moment.  In particular, high variance forces a nontrivial positive tail.  A crude but useful consequence is:

```math
\exists x\in A\quad L_D(x)\ge(1+\eta)\lambda.
```

Otherwise `L_D(x)<=(1+\eta)\lambda` for all `x`, and since the negative part is bounded below by `-\lambda`, the variance cannot reach `\eta\lambda^2` without some positive excess of size at least `\eta\lambda`.

More robustly, for any `0<\theta<\eta`, the set

```math
S_\theta=\{x\in A:L_D(x)\ge(1+\theta)\lambda\}
```

must carry positive load excess.  Its exact size depends on the upper bound `U=K/\lambda`, which is about `1/alpha` in the popular model.  Thus high variance alone may produce a small set, but that set has genuine pair-neighborhood increment.

## What this increment does and does not prove

The conclusion

```math
\exists x\in A:\quad |A\cap(x+D)|>(1+\theta)\frac{\lambda}{K}|D|
```

is not yet a density increment in the usual Roth/Szemeredi sense.  It is a density increment on a translate of the direction set `D`.

To become useful, one must show that `D` has structure, or replace `D` by a structured subset during sifting.  Therefore the high-load branch splits again:

1. if `D` is structured, transfer the pair-neighborhood increment to a structured ambient set;
2. if `D` is not structured, use the high-load set to define a new sifted direction/vertex system with improved regularity or stronger interaction constraints.

## Load-regular alternative

If the high-variance condition fails, then

```math
M_2(D)\le(1+\eta)|A|\lambda^2,
```

or equivalently

```math
E_{x\in A}(L_D(x)-\lambda)^2\le\eta\lambda^2.
```

By Chebyshev, for any `\theta>0`, all but at most an `eta/theta^2` fraction of points of `A` satisfy

```math
|L_D(x)-\lambda|\le\theta\lambda.
```

This gives the load-regular hypothesis needed for the shifted-interaction stage.

In this branch, pair starts are not concentrated enough to give an immediate increment.  The proof must use the exact missing diagonal

```math
J(d,d)=0
```

inside the shifted interaction matrix.

## First rigorous dichotomy

For every direction set `D` and parameter `eta>0`, exactly one of the following holds.

### Branch 1: load increment

```math
\sum_xL_D(x)^2>(1+\eta)|A|\lambda^2.
```

Then there exists `x in A` with

```math
|A\cap(x+D)|=L_D(x)>(1+\eta)\lambda,
```

and more generally the positive tail of `L_D` gives a pair-neighborhood increment.

### Branch 2: load regularity

```math
\sum_xL_D(x)^2\le(1+\eta)|A|\lambda^2.
```

Then for every `\theta>0`, outside an `eta/theta^2` fraction of `A`,

```math
L_D(x)=(1+O(\theta))\lambda.
```

This is the correct local regularity assumption for the next sifting stage.

## Immediate next task

Work in Branch 2.  Under load regularity, analyze the shifted interaction matrix

```math
J(d,e)=|P_d\cap(P_e-2e)|.
```

The forbidden diagonal `J(d,d)=0` is invisible in the full average when `|D|` is large, so the next step must either:

1. find concentration in the off-diagonal matrix `J(d,e)`, producing direction structure; or
2. sample/sift a subfamily `D'` where the missing diagonal becomes visible without destroying pair-fiber mass.

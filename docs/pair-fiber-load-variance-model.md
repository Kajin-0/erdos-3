# Pair-fiber load variance model

## Status

Simplified physical-space model.  This note turns the pair-fiber sifting target into explicit first- and second-moment quantities.

The aim is to test the hard case:

```math
\rho_d\approx \alpha^2
\quad\text{for many }d,
\qquad
P_d\cap(P_d-2d)=\varnothing
\quad\text{for all nonzero }d,
```

while the vertex-load statistics still look pseudorandom.

## Setup

Let `G` be a finite abelian group of size `N`, and let

```math
b=1_A,
\qquad |A|=\alpha N.
```

For a direction set `D`, define

```math
P_d=\{x:x,x+d\in A\},
\qquad
1_{P_d}(x)=b(x)b(x+d),
```

and

```math
\rho_d=N^{-1}|P_d|.
```

Assume `D` is a popular direction set, meaning roughly

```math
\rho_d\sim \alpha^2
\qquad(d\in D).
```

Set `K=|D|`.

## Vertex load

Define

```math
L_D(x)=\sum_{d\in D}1_{P_d}(x)
=\sum_{d\in D}b(x)b(x+d).
```

Then

```math
\sum_x L_D(x)=\sum_{d\in D}|P_d|=N\sum_{d\in D}\rho_d.
```

Since `L_D` is supported on `A`, the average load over `A` is

```math
\lambda_D
=\frac{1}{|A|}\sum_x L_D(x)
=\frac{1}{\alpha}\sum_{d\in D}\rho_d.
```

In the popular model `rho_d sim alpha^2`, this gives

```math
\lambda_D\sim \alpha K.
```

Thus a point of `A` starts about `alpha K` popular pairs in the pseudorandom model.

## Load variance and shared origins

The second moment is

```math
\sum_x L_D(x)^2
=\sum_{d,e\in D}|P_d\cap P_e|.
```

Define the shared-origin statistic

```math
I(d,e)=|P_d\cap P_e|
=|\{x:x,x+d,x+e\in A\}|.
```

Then

```math
\sum_x L_D(x)^2=\sum_{d,e\in D}I(d,e).
```

If `L_D` is nearly uniform on `A`, then

```math
\sum_x L_D(x)^2\approx |A|\lambda_D^2
\sim \alpha N(\alpha K)^2
=\alpha^3K^2N.
```

This matches the random heuristic

```math
I(d,e)\approx \alpha^3N
```

for generic distinct directions.

Thus excessive second moment is a density-increment signal, while near-minimal second moment is the true hard case.

## Shifted load and forbidden diagonal

Define the shifted load

```math
S_D(x)=\sum_{d\in D}1_{P_d}(x+2d)
=\sum_{d\in D}b(x+2d)b(x+3d).
```

The 4AP-free condition says that for every nonzero `d`,

```math
1_{P_d}(x)1_{P_d}(x+2d)=0
\qquad\text{for every }x.
```

Equivalently,

```math
\langle 1_{P_d},1_{P_d}(\cdot+2d)\rangle=0.
```

Summing over `d in D`, the diagonal contribution in

```math
\sum_x L_D(x)S_D(x)
```

is exactly missing.

Indeed,

```math
\sum_x L_D(x)S_D(x)
=\sum_{d,e\in D}J(d,e),
```

where

```math
J(d,e)=|P_d\cap(P_e-2e)|
=|\{x:x,x+d,x+2e,x+3e\in A\}|.
```

The forbidden 4AP condition is

```math
J(d,d)=0
\qquad(d\ne0).
```

In a random model one would expect

```math
J(d,d)\approx \alpha^4N.
```

So the total diagonal deficit over `D` is heuristically

```math
\alpha^4KN.
```

The question is whether this deficit can be hidden among the off-diagonal terms `J(d,e)` without creating structure.

## Why the diagonal deficit alone is too small

The off-diagonal mass has size about

```math
\sum_{d\ne e}J(d,e)\approx \alpha^4K^2N.
```

The missing diagonal has size about

```math
\alpha^4KN.
```

Thus if `K` is large, the diagonal deficit is only a `1/K` perturbation of the full shifted interaction mass.  A direct averaging argument over all pairs `(d,e)` will not see it.

Therefore the sifting lemma cannot merely compare diagonal and off-diagonal averages.  It must amplify the missing diagonal by selecting a smaller or more structured subfamily of directions where diagonal constraints become visible.

## Sifting principle

The useful operation is to replace `D` by a subfamily `D'` chosen from load or interaction information, so that:

1. pair-fiber mass is mostly preserved;
2. off-diagonal noise is reduced;
3. the forbidden diagonal constraints `J(d,d)=0` become a non-negligible obstruction.

This is the physical-space analogue of energy increment/sifting in modern 3AP arguments.

## First dichotomy: load increment or load regularity

For any popular direction set `D`, one has the dichotomy:

1. **Load increment.**  If

```math
\sum_x L_D(x)^2\gg \alpha N\lambda_D^2,
```

then many pair starts concentrate on a smaller subset of `A`; this should yield a density increment or a structured pair-neighborhood.

2. **Load regularity.**  If

```math
\sum_x L_D(x)^2\lesssim \alpha N\lambda_D^2,
```

then most points of `A` have load near `lambda_D` after discarding a small exceptional set.  The proof must then exploit shifted disjointness rather than load concentration.

This is the first sifting gate.

## Second dichotomy: interaction concentration or interaction regularity

Inside the load-regular branch, inspect

```math
J(d,e)=|P_d\cap(P_e-2e)|.
```

If a small subfamily of directions carries too much of the off-diagonal interaction, then `D` has additive/low-rank concentration and should feed the direction-structure branch.

If the off-diagonal interactions are spread, then one can try to sample a smaller `D'` for which the off-diagonal background drops while each forbidden diagonal `J(d,d)=0` remains exact.

This is the expected amplification step.

## Candidate load-variance sifting lemma

A sharper lemma would be:

> Let `D` be a popular direction set with `rho_d sim alpha^2`.  Suppose `A` is 4AP-free, so `J(d,d)=0` for all nonzero `d in D`.  Then either:
>
> 1. `L_D` has high variance on `A`, yielding a density/pair-neighborhood increment;
> 2. the matrix `J(d,e)` has concentrated off-diagonal mass, yielding direction structure;
> 3. there exists a subfamily `D' subset D` such that pair-fiber mass remains large but the missing diagonal in `J_{D'}` is visible enough to force a contradiction to pseudorandomness.

This lemma is still schematic, but it isolates the exact quantities that must be controlled.

## Relation to exponent gain

The desired finite-field bound is of density scale

```math
\alpha\ll n^{-1-\epsilon}.
```

A successful sifting lemma must therefore lose less than the critical power of `alpha` across iteration.  Any argument with only logarithmic or weak polynomial savings will likely not suffice.

The load-variance model is useful because it identifies where power losses enter:

1. discarding unpopular directions;
2. passing from high load variance to an actual structured increment;
3. sampling `D'` without destroying pair-fiber mass;
4. converting direction concentration into a low-rank/quadratic branch.

## Immediate proof task

Prove the first load dichotomy rigorously:

```math
\sum_x L_D(x)^2
=\sum_{d,e}I(d,e).
```

If this second moment is large, derive an explicit increment object.  If it is near minimal, record the load-regular hypotheses needed for the shifted-interaction stage.

This is a concrete, local step and does not yet require Fourier analysis.

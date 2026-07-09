# Pair-fiber sifting lemma

## Status

Physical-space extraction target.  This note formulates the sifting lemma suggested by the failure of the Fourier-only route.

The current Fourier branch is underdetermined: fixed-shift line autocorrelation gives derivative labels mixed with support effects.  A physical-space pair-fiber lemma attacks the support problem directly.

## Physical-space pair fibers

Let `A subset G` be 4AP-free, and write

```math
b=1_A,
\qquad |A|=\alpha |G|.
```

For a direction `d`, define the pair fiber

```math
P_d=\{x: x\in A,\ x+d\in A\}.
```

Equivalently,

```math
1_{P_d}(x)=b(x)b(x+d).
```

A 4-term arithmetic progression with common difference `d` is a point `x` such that

```math
x,x+d,x+2d,x+3d\in A.
```

In pair-fiber notation this is

```math
x\in P_d
\qquad\text{and}\qquad
x+2d\in P_d.
```

Thus 4AP-freeness gives the exact disjointness

```math
P_d\cap(P_d-2d)=\varnothing
```

for every nonzero `d`.

## Why this is stronger than Fourier line data

The Fourier shear identity detects autocorrelation of spectral pair functions.  It does not directly control whether line modes are caused by true phase structure or irregular support.

The physical-space condition

```math
P_d\cap(P_d-2d)=\varnothing
```

is exact and support-level.  It is the direct source of the obstruction.

A sifting lemma should exploit many such exact disjointness constraints simultaneously.

## Marginals

The pair-fiber density is

```math
\rho_d=E_x b(x)b(x+d).
```

Averaging over directions gives

```math
E_d\rho_d\approx \alpha^2
```

up to the usual zero-direction and ambient normalization issues.

In the hard branch one expects many popular directions with

```math
\rho_d\approx \alpha^2,
```

but each corresponding pair fiber is shift-disjoint:

```math
P_d\cap(P_d-2d)=\varnothing.
```

The sifting problem is to show that this cannot remain pseudorandom at density above the desired threshold.

## Vertex load function

Given a set of popular directions `D`, define the vertex load

```math
L_D(x)=\sum_{d\in D}1_{P_d}(x)
=
\sum_{d\in D}b(x)b(x+d).
```

This counts how many selected pairs start at `x`.

If `L_D` is uneven on `A`, then one obtains a density increment candidate: there is a subset or structured region where points of `A` participate in unusually many pairs.

If `L_D` is uniform, then the exact disjointness constraints for many `d` should force expansion: the shifted sets `P_d+2d` avoid `P_d`, but many of them still live inside the same high-density environment.  Uniformity should eventually contradict the number of pairs unless the directions or vertices are structured.

## Sifting operation

A sifting step should choose a direction subfamily

```math
D'\subseteq D
```

and retain vertices with high or stable load:

```math
S=\{x\in A: L_{D'}(x)\text{ is large/stable}\}.
```

The goal is to preserve many pair fibers while reducing noise.  Iterating this should produce one of two outcomes:

1. a density increment on a structured set;
2. a coherent subconfiguration where many pair-fiber disjointness constraints share common vertices/directions.

The second outcome is the physical-space analogue of producing many anchored triangle closures in the spectral pair graph.

## Candidate sifting lemma

A useful lemma would be:

> Let `A subset G` have density `alpha`, and let `D` be a set of directions such that for many `d in D`,
>
> ```math
> |P_d|\ge c\alpha^2 |G|.
> ```
>
> Suppose also
>
> ```math
> P_d\cap(P_d-2d)=\varnothing
> ```
>
> for all `d in D`.  Then at least one of the following holds:
>
> 1. **density increment:** `A` has increased density on a structured set, ideally a subspace, Bohr-type set, quadratic level set, or pair-neighborhood;
> 2. **direction structure:** `D` has low-rank/additive structure strong enough to enter the quadratic-level route;
> 3. **coherent pair-fiber subsystem:** there is `D' subset D` and a large vertex set `S` such that many fibers `P_d` restricted to `S` are simultaneously popular and their disjointness constraints are aligned.

The third conclusion is not final; it is the cleaned object needed for the spectral/chirp compatibility machinery.

## What aligned disjointness should mean

For two directions `d,e`, compare the pair fibers

```math
P_d=\{x:x,x+d\in A\},
\qquad
P_e=\{x:x,x+e\in A\}.
```

A useful interaction statistic is the shared-origin count

```math
I(d,e)=|P_d\cap P_e|
=|\{x:x,x+d,x+e\in A\}|.
```

Another is the shifted interaction

```math
J(d,e)=|P_d\cap(P_e-2e)|.
```

The forbidden condition says `J(d,d)=0`.  If many off-diagonal interactions are large while the diagonal shifted interactions vanish, this resembles a graph with many edges but missing many forced translates.  That is where expansion or structure should appear.

## Relation to previous Fourier branches

The physical-space sifting lemma is designed to supply the missing input in two places.

### For the affine coboundary branch

Sifting may produce a coherent subsystem of pair-lines whose spectral modes satisfy many anchored triangle closures.  This would provide the phase-comparison input that the Fourier shear energy alone did not force.

### For the non-isotropic chirp branch

Sifting may control support irregularity along pair-lines, separating genuine chirp derivatives from support artifacts.  Without this, fixed-shift autocorrelation cannot identify quadratic line coefficients.

Thus pair-fiber sifting is not an alternative aesthetic route.  It is the missing support-control mechanism for both Fourier branches.

## Toy finite-field target

In a finite-field group `G=F_p^n`, a strong target would be:

```math
\alpha\gg n^{-1-\epsilon}
\quad\Longrightarrow\quad
\exists d\ne0\text{ with }P_d\cap(P_d-2d)\ne\varnothing.
```

Equivalently, if all nonzero `d` satisfy the disjointness condition, then

```math
\alpha\ll n^{-1-\epsilon}.
```

This is exactly the exponent type needed for the dyadic harmonic-sum route.

## Immediate proof task

Start with a simplified model:

1. assume a set `D` of popular directions with `rho_d approx alpha^2`;
2. assume uniform vertex load `L_D(x) approx alpha |D|` on `A`;
3. use exact disjointness `P_d cap (P_d-2d)=empty`;
4. prove that either off-diagonal interactions force a structured increment, or the assumptions are mutually inconsistent above a threshold.

This is the next concrete route after the Fourier-only obstruction.

# Raw pair disjointness identity

## Status

Proof-audit identity.  This note records an exact physical-space consequence of 4AP-freeness using raw pair indicators rather than balanced pair products.

## Setup

Let

```math
G=F_p^n,
\qquad p>4,
```

and let

```math
A\subset G,
\qquad
\alpha=|A|/|G|.
```

For each direction `d`, define the raw adjacent-pair profile

```math
b_d(x)=1_A(x)1_A(x+d).
```

Let

```math
p_d=E_x b_d(x)=E_x 1_A(x)1_A(x+d).
```

This is the density of adjacent `A`-pairs with difference `d`.

## Exact disjointness from 4AP-freeness

If `A` is 4AP-free, then for every nonzero `d`,

```math
b_d(x)b_d(x+2d)=0
```

for every `x`.

Indeed, if both factors were `1`, then

```math
x,
\quad x+d,
\quad x+2d,
\quad x+3d
```

would all lie in `A`, giving a nontrivial 4AP.

Equivalently,

```math
\langle b_d,\tau_{2d}b_d\rangle=0
```

for all nonzero `d`.

## Centered autocorrelation identity

Since `E b_d=p_d`, we have

```math
\langle b_d-p_d,\tau_{2d}(b_d-p_d)\rangle
=\langle b_d,\tau_{2d}b_d\rangle-p_d^2.
```

For nonzero `d`, the first term vanishes by 4AP-freeness.  Hence

```math
\langle b_d-p_d,\tau_{2d}(b_d-p_d)\rangle=-p_d^2.
```

This is an exact identity, not an inequality.

## Averaged form

Averaging over nonzero directions gives

```math
E_{d\ne0}\langle b_d-p_d,\tau_{2d}(b_d-p_d)\rangle
=-E_{d\ne0}p_d^2.
```

Since

```math
E_d p_d=\alpha^2
```

including the zero direction up to negligible finite-field effects, Cauchy--Schwarz gives roughly

```math
E_d p_d^2\ge \alpha^4.
```

Thus raw pair profiles have unavoidable averaged negative centered autocorrelation at scale at least `alpha^4` in every 4AP-free set.

## Relation to the balanced Q obstruction

The balanced pair-product identity used

```math
g_d(x)=f(x)f(x+d),
\qquad f=1_A-\alpha,
```

and wrote

```math
Q=E_d\langle g_d,\tau_{2d}g_d\rangle.
```

The raw identity is stronger pointwise in `d`, but it contains large density terms.  The balanced identity removes those lower-order density contributions and isolates the pure `U^3` obstruction.

The useful physical-space question is whether the raw exact disjointness can be combined with minimality/hyperplane-flatness to avoid losing information during balancing.

## Sifting interpretation

The functions `b_d` are indicator functions of pair-fibers

```math
A\cap(A-d).
```

4AP-freeness says each pair-fiber is disjoint from its `2d` translate.  Therefore a popular difference `d`, for which

```math
p_d\gg \alpha^2,
```

creates a relatively large set `A\cap(A-d)` that avoids its own `2d` translate.

This suggests a sifting route:

1. either many pair densities `p_d` are abnormally large, producing structured popular differences;
2. or the pair densities are uniform near `alpha^2`, in which case the exact disjointness supplies many medium anti-correlations that may be aggregable by almost-periodicity.

## Limit of the immediate identity

The identity alone does not beat the logarithmic barrier.

A random-like 4AP-free obstruction would have

```math
p_d\approx \alpha^2
```

for most `d`, giving only the expected scale

```math
p_d^2\approx \alpha^4.
```

To get an exponent gain, one needs an additional mechanism turning the family of disjoint pair-fibers into either:

1. an affine density increment of size `alpha^{2-epsilon}`;
2. a structured difference set suitable for sifting;
3. or a high-rank relative-host counting contradiction.

## Next research question

Can a family of pair-fibers `B_d=A\cap(A-d)` with

```math
B_d\cap(B_d-2d)=\emptyset
```

for all popular `d` be sifted to produce a density increment stronger than the direct Fourier `alpha^2` increment?

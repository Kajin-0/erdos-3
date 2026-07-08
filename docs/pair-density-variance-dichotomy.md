# Pair-density variance dichotomy

## Status

Proof-audit lemma.  This note turns the raw pair-fiber viewpoint into a quantitative dichotomy: either pair-density variance already gives a large Fourier/hyperplane increment, or the proof must handle a uniform pair-fiber disjointness regime.

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
\alpha=|A|/|G|,
\qquad
a=1_A.
```

For each direction `d`, define

```math
p_d=E_x a(x)a(x+d).
```

Then

```math
E_d p_d=\alpha^2.
```

## Fourier formula for pair densities

With normalized Fourier transform,

```math
p_d=\sum_\xi |\widehat a(\xi)|^2 e_p(d\cdot \xi).
```

Since

```math
\widehat a(0)=\alpha,
```

we have

```math
p_d-\alpha^2=\sum_{\xi\ne0}|\widehat a(\xi)|^2 e_p(d\cdot \xi).
```

Therefore Parseval in the `d` variable gives

```math
E_d |p_d-\alpha^2|^2
=\sum_{\xi\ne0}|\widehat a(\xi)|^4.
```

## Variance implies Fourier increment

Let

```math
V=E_d |p_d-\alpha^2|^2.
```

Since

```math
\sum_{\xi\ne0}|\widehat a(\xi)|^2=\alpha(1-\alpha)\le \alpha,
```

we have

```math
V\le \|\widehat a\|_{\infty,\xi\ne0}^2\alpha.
```

Consequently, if

```math
V\ge c\alpha^{5-2\epsilon},
```

then

```math
\|\widehat a\|_{\infty,\xi\ne0}\ge c^{1/2}\alpha^{2-\epsilon}.
```

This is exactly the desired scale for a hyperplane density increment in the finite-field minimality framework.

## No-increment regime

Therefore, after excluding affine increments of size `alpha^{2-epsilon}`, one may assume

```math
E_d |p_d-\alpha^2|^2 \ll \alpha^{5-2\epsilon}.
```

Equivalently, the pair densities are almost flat in `L^2(d)` at the scale relevant to the desired exponent gain.

In a minimal critical counterexample with hyperplane-flatness

```math
\|\widehat a\|_{\infty,\xi\ne0}\lesssim \alpha^{2-\delta},
```

the same formula gives the automatic bound

```math
E_d |p_d-\alpha^2|^2
\lesssim \alpha^{5-2\delta}.
```

Thus hyperplane-flatness forces pair-density variance to be tiny unless the desired Fourier increment has already appeared.

## Interaction with raw disjointness

For a 4AP-free set, the raw pair-fiber identity gives for every nonzero `d`

```math
\langle b_d-p_d,\tau_{2d}(b_d-p_d)\rangle=-p_d^2,
```

where

```math
b_d(x)=a(x)a(x+d).
```

If pair densities are flat, then for most directions

```math
p_d\approx \alpha^2,
```

so the negative autocorrelation scale is approximately

```math
-p_d^2\approx -\alpha^4.
```

This is the uniform pair-fiber disjointness regime.

## Dichotomy

The pair-fiber attack now has a clean split:

1. **Pair-density variance branch.** If

```math
E_d |p_d-\alpha^2|^2\ge c\alpha^{5-2\epsilon},
```

then `A` has a nontrivial Fourier coefficient of size at least `alpha^{2-epsilon}`, hence a hyperplane increment at the desired scale.

2. **Uniform pair-fiber branch.** If not, then most adjacent-pair fibers

```math
B_d=A\cap(A-d)
```

have density near `alpha^2`, and 4AP-freeness gives

```math
B_d\cap(B_d-2d)=\emptyset.
```

The remaining task is to exploit many nearly-uniform pair-fibers, each disjoint from its own translate.

## Why this matters

This removes one possible source of hidden gain.  If pair densities are uneven, the desired increment is already present.  Therefore any genuinely hard obstruction must have:

1. hyperplane-flat `A`;
2. pair densities `p_d` nearly constant in `L^2`;
3. many pair-fibers of density about `alpha^2`;
4. exact translate-disjointness `B_d cap (B_d-2d)=emptyset`.

This is a more rigid object than an arbitrary pure `U^3` obstruction.

## Next research question

In the uniform pair-fiber branch, can the family

```math
\{B_d=A\cap(A-d): p_d\approx\alpha^2\}
```

with

```math
B_d\cap(B_d-2d)=\emptyset
```

be shown to create either an `alpha^{2-epsilon}` density increment or a high-rank relative-host obstruction?

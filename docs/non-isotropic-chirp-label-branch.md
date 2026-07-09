# Non-isotropic chirp-label branch

## Status

Extraction target.  This note formulates the second branch in the phase-sensitive shear route: active pair-lines whose phases are genuinely quadratic in the line parameter.

The motivation is the barrier recorded in `triangle-average-not-forced-by-shear.md`: affine line modes alone need not cohere into anchored triangle closures.  Moreover, a genuine quadratic spectral phase normally produces a quadratic chirp on each pair-line, not a pure affine mode.

## Pair-line phase model

For an oriented pair `a -> b`, set

```math
w=a+b
```

and

```math
H_{a,b}(t)=c_{a+t w}c_{b-t w}.
```

Suppose on a structured part of the spectral cloud

```math
c_x\approx A(x)e_p(q(x)),
```

where `q` is a quadratic phase with homogeneous quadratic part `Q_q` and polar form `B_q`.

Then

```math
q(a+t w)+q(b-t w)
```

is a quadratic polynomial in `t`:

```math
q(a+t w)+q(b-t w)
=
C(a,b)+A(w)t^2+M(a,b)t,
```

where

```math
A(w)=2Q_q(w),
```

and

```math
M(a,b)=B_q(w,a-b).
```

Thus the correct line label is not just the affine mode `mu(a,b)`.  It is the chirp label

```math
(A(w),M(a,b)).
```

The affine pair-lift branch is the special case

```math
A(w)=0.
```

## Why fixed-shift autocorrelation misses full chirps

If

```math
H(t)=e_p(A t^2+M t)
```

on a complete line with constant amplitude, then

```math
H(t)\overline{H(t+2)}
=e_p(-4A t-4A-2M).
```

Averaging over `t` gives zero unless

```math
A=0.
```

Therefore the original fixed-shift shear autocorrelation strongly detects affine/isotropic line modes but cancels for complete non-isotropic quadratic chirps.

Consequently, if a non-isotropic chirp branch contributes to the original shear sum, at least one additional feature must be present:

1. the line support is incomplete or structured, so the linear derivative does not cancel;
2. the relevant active directions satisfy `A(w)=0` on a large subfamily after all, returning to the affine branch;
3. amplitudes are nonconstant and correlate with the derivative phase;
4. the correct extraction must use multiple shifts or quadratic Fourier projections rather than only the fixed shift `2`.

## Quadratic Fourier projection on a line

For a one-dimensional line function `H:F_p -> C`, define the quadratic line spectrum

```math
\mathcal Q_H(A,M)=E_{t\in F_p}H(t)e_p(-A t^2-M t).
```

A genuine chirp

```math
H(t)\approx \rho(t)e_p(A t^2+M t)
```

has large `mathcal Q_H(A,M)` when the amplitude `rho` is not too oscillatory.

Thus a non-isotropic extraction should look for large quadratic Fourier coefficients of the line functions `H_{a,b}`, not just large ordinary Fourier coefficients.

## Chirp-label predictions from a global quadratic phase

If the line labels come from one global quadratic phase `q`, then they satisfy strong compatibility equations.

### Direction-only quadratic coefficient

The quadratic coefficient depends only on

```math
w=a+b:
```

```math
A(a,b)=A(w)=2Q_q(w).
```

Thus the first test is whether the extracted quadratic coefficient is constant along shear orbits

```math
(a,b)\mapsto(a+s(a+b),b-s(a+b)).
```

### Affine coefficient

The affine coefficient is

```math
M(a,b)=B_q(a+b,a-b).
```

It is antisymmetric:

```math
M(b,a)=-M(a,b),
```

while the quadratic coefficient is symmetric:

```math
A(b,a)=A(a,b).
```

### Relation between `A` and `M`

Since

```math
A(w)=2Q_q(w),
```

the polar form of `A/2` should recover `B_q`:

```math
B_q(x,y)=\frac{1}{2}(A(x+y)-A(x)-A(y)).
```

Therefore the affine coefficient should satisfy

```math
M(a,b)=\frac{1}{2}\left(A(2a)-A(2b)\right)
```

in a homogeneous quadratic normalization, equivalently

```math
M(a,b)=2Q_q(a)-2Q_q(b).
```

This recovers the affine coboundary formula even when `A(a+b)` is nonzero, but now the full line phase also contains the `A(a+b)t^2` term.

## Chirp cocycle target

The natural compatibility object is now a richer edge label

```math
\chi(a,b)=(A(a+b),M(a,b)).
```

A useful theorem would be:

> If many active pair-lines have large quadratic Fourier coefficients at labels `(A(w),M(a,b))`, and these labels satisfy shear-orbit invariance, reversal symmetry, and many local compatibility equations, then either:
>
> 1. there is a quadratic form `Q` such that
>
> ```math
> A(w)=2Q(w),\qquad M(a,b)=2Q(a)-2Q(b)
> ```
>
> on a large structured subcloud; or
> 2. failures of compatibility concentrate on low-rank/additive structure, giving an increment branch.

This is the non-isotropic analogue of the affine coboundary route.

## Relation to the original shear obstruction

A problem remains: the original shear energy sees fixed-shift autocorrelations, not quadratic Fourier coefficients directly.

For a line chirp with coefficient `A`, the fixed-shift derivative is the affine phase

```math
-4A t-4A-2M.
```

Thus a large fixed-shift autocorrelation can occur if the support/amplitude of the line function has ordinary Fourier mass at frequency

```math
4A.
```

Equivalently, the fixed-shift extraction sees the derivative of the chirp, not the chirp itself.

Therefore one possible route is:

```math
\text{fixed-shift line mode }m
\Rightarrow
\text{candidate derivative frequency }m=-4A
\Rightarrow
\text{recover }A\text{ if support effects are controlled}.
```

But this is unstable unless the support of `H_{a,b}` is sufficiently regular.  Otherwise the observed affine mode may be caused by amplitude/support oscillation rather than by a quadratic phase derivative.

## Updated trichotomy

The phase-sensitive branch should now be organized as:

1. **Affine/isotropic coherent branch.**  Many active directions have `A(w)=0`; line modes are edge labels `mu(a,b)` and can be tested by anchored triangles.
2. **Non-isotropic chirp branch.**  Active line functions have large quadratic Fourier coefficients with labels `(A(w),M(a,b))`; compatibility should reconstruct a global quadratic form.
3. **Support-derivative branch.**  Fixed-shift line modes come mainly from interaction between chirp derivatives and irregular line supports/amplitudes; this likely requires sifting or a physical-space pair-fiber argument.

## Immediate proof task

Formulate a line-level dichotomy:

> If `H:F_p -> C` has large fixed-shift autocorrelation, then either:
>
> 1. `H` has a large affine Fourier coefficient;
> 2. after demodulating by a quadratic chirp, `H` has structured support/amplitude producing the autocorrelation;
> 3. or no stable chirp interpretation is possible.

This line-level dichotomy should be tested before attempting global chirp-label compatibility.

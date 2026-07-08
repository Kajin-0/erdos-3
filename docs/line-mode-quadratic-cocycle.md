# Line-mode quadratic-chirp target

## Status

Proof-audit correction and target.  This note corrects a previous oversimplification: a quadratic spectral phase does not usually make the paired line function `H_{w,r}(t)` linear in `t`.  It makes it a quadratic chirp.  The shift autocorrelation of that chirp has linear phase.

This distinction matters for the proof search.  The line-mode data should not be forced prematurely into an affine slope map.  The correct object is a quadratic-chirp/cocycle structure on spectral lines.

## Setup

Let

```math
G=F_p^n,
\qquad p>4,
```

and let

```math
f=1_A-\alpha,
\qquad
c_\zeta=\widehat f(\zeta).
```

For `w\ne0`, define spectral pair-fibers

```math
h_w(u)=c_u c_{w-u}.
```

On a line parallel to `w`, choose a representative `r` and define

```math
H_{w,r}(t)=h_w(r+tw)
=c_{r+tw}c_{w-r-tw}.
```

The pure obstruction forces negative autocorrelation in these line functions after summing over `(w,r)`:

```math
\sum_{w\ne0,r}\sum_t H_{w,r}(t)\overline{H_{w,r}(t+2)}\le -c\alpha^4.
```

## Correct quadratic model

Suppose heuristically that on some spectral support the Fourier coefficients have phase modeled by

```math
c_\zeta \approx A(\zeta)e_p(q(\zeta)),
```

where

```math
q(\zeta)=Q(\zeta)+\ell(\zeta)+c_0
```

with `Q` homogeneous quadratic and associated symmetric bilinear form `B_Q`.

Then

```math
q(r+tw)+q(w-r-tw)
```

is a quadratic polynomial in `t`, not generally a linear polynomial.

More precisely,

```math
q(r+tw)+q(w-r-tw)
= C(w,r)+2Q(w)t^2+B_Q(w,2r-w)t.
```

The linear part `ell` contributes only to the constant term because the paired arguments sum to `w`.

Therefore a quadratic phase naturally makes

```math
H_{w,r}(t)
```

look like a quadratic chirp

```math
A_{w,r}(t)e_p(2Q(w)t^2+B_Q(w,2r-w)t+C(w,r)),
```

not a pure linear mode.

## Shift autocorrelation of a quadratic chirp

If

```math
\psi_{w,r}(t)=2Q(w)t^2+B_Q(w,2r-w)t+C(w,r),
```

then

```math
\psi_{w,r}(t)-\psi_{w,r}(t+2)
=-8Q(w)t-8Q(w)-2B_Q(w,2r-w).
```

Thus the *shift autocorrelation* of a quadratic chirp has linear phase in `t`.

This is the corrected bridge:

- line Fourier modes of `H_{w,r}` detect oscillation of the chirp itself;
- the autocorrelation `H_{w,r}(t)\overline{H_{w,r}(t+2)}` detects the derivative of the quadratic phase along the line.

## Consequence for the previous slope-map idea

The earlier target

```math
m(w,r)=B(w,2r-w)+\ell(w)
```

is too naive as a direct description of modes of `H_{w,r}`.

A correct extraction must allow a quadratic coefficient depending only on `w`:

```math
H_{w,r}(t)\approx A_{w,r}(t)e_p(a(w)t^2+b(w,r)t+C(w,r)),
```

with the quadratic model predicting

```math
a(w)=2Q(w),
\qquad
b(w,r)=B_Q(w,2r-w).
```

The affine-in-`r` condition applies to `b(w,r)` after the quadratic coefficient `a(w)` is accounted for.

## Isotropic special case

If

```math
Q(w)=0,
```

then the quadratic chirp degenerates to a linear mode along the `w`-line:

```math
H_{w,r}(t)\approx A_{w,r}(t)e_p(B_Q(w,2r-w)t+C(w,r)).
```

This is exactly the isotropic-direction condition that also appears in high-rank quadratic-level 4AP geometry.

Therefore the spectral line-mode obstruction and the high-rank quadratic-level branch are not separate accidents: both naturally single out directions `w` with special behavior under a quadratic form.

## Compatibility tests for a quadratic-chirp model

A coherent quadratic model should satisfy:

1. **Quadratic coefficient consistency.**  The `t^2` coefficient depends only on `w`, not on the line representative `r`:

```math
a(w)\approx 2Q(w).
```

2. **Affine slope consistency.**  After removing `a(w)t^2`, the linear coefficient in `t` is affine in `r`:

```math
b(w,r+s)-b(w,r)\approx 2B_Q(w,s).
```

3. **Symmetry.**  Swapping the paired variables `u` and `w-u` corresponds to an affine reparametrization of `t`; the extracted coefficients must transform compatibly.

Failure of these consistency conditions should yield additive spectral concentration or a density increment.  Success should produce a quadratic form/factor.

## Candidate corrected cocycle lemma

A useful theorem would be:

> Suppose the pure obstruction forces many line functions `H_{w,r}` to have substantial oscillatory autocorrelation, while no Fourier coefficient satisfies
>
> ```math
> |c_\zeta|\ge \alpha^{2-\epsilon}
> ```
>
> and the marginal fourth moment is small.  Then either:
>
> 1. the extracted line data fail quadratic-chirp compatibility, giving an affine density increment or additive spectral concentration; or
> 2. on a large substructure there exist functions `a(w)` and `b(w,r)` with
>
> ```math
> a(w)=2Q(w),
> \qquad
> b(w,r)=B_Q(w,2r-w),
> ```
>
> for some quadratic form `Q`, producing a quadratic factor.

## Low-rank / high-rank split

Once a quadratic form `Q` or bilinear form `B_Q` is extracted, the existing rank split applies:

1. low rank gives affine/quadratic-level structure and should lead to a density increment;
2. high rank sends the obstruction to the high-rank relative-host recurrence branch.

The correction does not weaken the quadratic route; it makes the target algebraically accurate.

## Next research question

Can the line autocorrelation data be converted into a robust quadratic-chirp model

```math
H_{w,r}(t)\approx A_{w,r}(t)e_p(a(w)t^2+b(w,r)t+C(w,r))
```

on a large substructure, or else force a large Fourier atom/density increment?

# Phase-sensitive flat-cloud lemma

## Status

Extraction target.  This note turns the low-coefficient shear-cloud branch into a phase-sensitive line-mode problem.

The key point is that support incidence is not enough.  A flat spectral cloud contributes to the signed shear sum only when the phases of the pair functions

```math
h_w(u)=c_uc_{w-u}
```

have large autocorrelation under the unipotent shift

```math
u_w:u\mapsto u+2w.
```

This is the precise bridge from flat shear clouds to quadratic-chirp/cocycle structure.

## Setup

Let

```math
Q_{\mathrm{shear}}
=\sum_{u,v}c_uc_v\overline{c_{3u+2v}c_{-2u-v}}.
```

Write

```math
w=u+v,
\qquad v=w-u.
```

Then

```math
3u+2v=u+2w,
\qquad
-2u-v=-u-w=w-(u+2w).
```

Define

```math
h_w(u)=c_uc_{w-u}.
```

The shear sum becomes

```math
Q_{\mathrm{shear}}
=\sum_w\sum_u h_w(u)\overline{h_w(u+2w)}.
```

Thus the obstruction is exactly a sum of line-fiber autocorrelations.

## Flat-cloud phase model

Suppose on a spectral cloud `Omega` one has

```math
c_\xi\approx \lambda e_p(\phi(\xi)).
```

For a fixed `w`, restrict to

```math
\Omega_w=\Omega\cap(w-\Omega).
```

Then

```math
h_w(u)\approx \lambda^2 e_p(\theta_w(u)),
\qquad
\theta_w(u)=\phi(u)+\phi(w-u).
```

The `w`-fiber contribution is

```math
\sum_u h_w(u)\overline{h_w(u+2w)}
\approx
\lambda^4\sum_{u\in\Omega_w\cap(\Omega_w-2w)}
e_p(\theta_w(u)-\theta_w(u+2w)).
```

Therefore a large contribution from the flat cloud requires two simultaneous facts:

1. many shear edges:

```math
|\Omega_w\cap(\Omega_w-2w)|\text{ large for many }w;
```

2. phase alignment:

```math
\theta_w(u)-\theta_w(u+2w)
```

is concentrated in phase on many of those edges.

## Autocorrelation-to-mode extraction

For a fixed `w`, decompose `h_w` on lines parallel to `w`.  For representatives `r mod <w>`, define

```math
H_{w,r}(t)=h_w(r+tw).
```

Then

```math
\sum_u h_w(u)\overline{h_w(u+2w)}
=\sum_r\sum_t H_{w,r}(t)\overline{H_{w,r}(t+2)}.
```

By one-dimensional Fourier expansion in `t`,

```math
\sum_t H_{w,r}(t)\overline{H_{w,r}(t+2)}
=\sum_m |\widehat H_{w,r}(m)|^2 e_p(2m)
```

up to normalization convention.

Thus a large signed contribution forces mass of `H_{w,r}` on line modes `m` for which `e_p(2m)` has the needed phase.  Negative real contribution forces mass on modes with

```math
\cos(4\pi m/p)<0.
```

This is an exact, elementary extraction: large autocorrelation gives line-mode concentration.

## From line modes to chirps

A pure line mode for `H_{w,r}` means

```math
H_{w,r}(t)\approx A_{w,r}(t)e_p(m(w,r)t),
```

where `A_{w,r}` is a slowly varying or nearly constant amplitude on the active support.

But recall

```math
H_{w,r}(t)=c_{r+tw}c_{w-r-tw}.
```

If the original coefficients have a quadratic phase

```math
c_\xi\approx A(\xi)e_p(q(\xi)),
```

then along this line

```math
q(r+tw)+q(w-r-tw)
```

is generally a quadratic polynomial in `t`, not merely linear.  Therefore the correct global model is a quadratic chirp whose shift-derivative produces line modes.

Concretely, if `q` has homogeneous quadratic part `Q_q` and bilinear form `B_q`, then

```math
q(r+tw)+q(w-r-tw)
=
C(w,r)+2Q_q(w)t^2+B_q(w,2r-w)t.
```

The shift derivative

```math
\psi(t)-\psi(t+2)
```

is linear in `t`.  Thus persistent line-mode extraction across many shifts should be interpreted as evidence for a quadratic chirp/cocycle, not just affine slope structure.

## Candidate phase-sensitive flat-cloud lemma

A useful lemma would be:

> Let `Omega` be a spectral cloud with nearly flat coefficient magnitude `lambda`, and suppose its contribution to the shear sum is at least `eta`.  Then either:
>
> 1. the support `Omega` has low-rank/additive structure strong enough to enter a BSG/Bogolyubov branch; or
> 2. for many `w` and many line representatives `r`, the functions
>
> ```math
> H_{w,r}(t)=c_{r+tw}c_{w-r-tw}
> ```
>
> have significant Fourier mass on coherent line modes; or
> 3. the phases of `c_xi` agree with a quadratic-chirp model on a large structured subset of the spectral cloud.

The intended progression is

```math
\text{flat cloud shear energy}
\Rightarrow
\text{line-mode concentration}
\Rightarrow
\text{quadratic chirp/cocycle}
\Rightarrow
\text{Prendiville/high-rank route or low-rank increment}.
```

## Exponent relevance

This lemma would avoid the cutoff loss.  Instead of discarding low coefficients, it treats their coherent contribution as direct evidence of structure.

The remaining exponent question is whether the extracted line-mode/chirp structure is strong enough to produce either:

```math
\alpha^{2-\epsilon}\text{ increment},
```

or a high-rank recurrence bound

```math
\beta\le C_p n^{-1-\epsilon_h}.
```

## Immediate proof task

Prove the fixed-`w` line-mode extraction rigorously with all normalizations, then determine what compatibility between the extracted modes `m(w,r)` is forced by the factorization

```math
H_{w,r}(t)=c_{r+tw}c_{w-r-tw}.
```

The compatibility of these modes across many `(w,r)` is the likely place where quadratic structure enters.

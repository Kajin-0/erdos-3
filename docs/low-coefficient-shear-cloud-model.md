# Low-coefficient shear cloud model

## Status

Proof-audit scale test.  This note examines the low-coefficient alternative exposed by the dyadic cutoff barrier.

The conclusion is that tiny Fourier coefficients cannot be dismissed by a simple interpolation inequality.  A flat cloud of small coefficients can carry shear energy at scale `alpha^4` if it has enough shear-fiber incidence and coherent phase.  Therefore the low-coefficient alternative must be treated as a structural object, not as an error term.

## Setup

Let

```math
c_\xi=\widehat f(\xi),
\qquad
\sum_\xi |c_\xi|^2\le \alpha.
```

The pure shear form is

```math
Q=\sum_{u,v}c_uc_v\overline{c_{3u+2v}c_{-2u-v}}.
```

Let `\Omega` be a spectral cloud on which

```math
|c_\xi|\approx \lambda
```

and suppose

```math
|\Omega|=M.
```

The energy constraint gives

```math
M\lambda^2\lesssim \alpha.
```

In a flat model, take

```math
\lambda^2\approx \alpha/M.
```

## Shear edge count in a flat cloud

A shear edge is a pair `(u,v)` such that

```math
u_1=u,
\qquad
u_2=v,
\qquad
u_3=3u+2v,
\qquad
u_4=-2u-v
```

all lie in `\Omega`.

Let

```math
E_T(\Omega)=|\{(u,v):u,v,3u+2v,-2u-v\in\Omega\}|.
```

If phases are coherent on these edges, the contribution from this cloud is roughly

```math
E_T(\Omega)\lambda^4.
```

Using `\lambda^2\approx\alpha/M`, this becomes

```math
E_T(\Omega)\frac{\alpha^2}{M^2}.
```

To contribute at the obstruction scale `alpha^4`, it is enough that

```math
E_T(\Omega)\gtrsim \alpha^2 M^2.
```

Thus the cloud need not be close to fully shear-closed.  It only needs shear-edge density about `alpha^2` inside `\Omega^2`.

## Consequence

This is a serious obstruction to crude truncation.  Even if

```math
\lambda\ll \alpha^{2-\epsilon},
```

so that every Fourier coefficient is individually too small to give the desired linear increment, a large enough cloud can still carry the full `alpha^4` shear obstruction.

The required shear-edge density is only `alpha^2`, which is small but not negligible at the finite-field threshold.

## Why interpolation does not remove it

Cauchy--Schwarz gives only

```math
|Q|\le \left(\sum_{u,v}|c_uc_v|^2\right)^{1/2}
       \left(\sum_{u,v}|c_{3u+2v}c_{-2u-v}|^2\right)^{1/2}
\le \alpha^2.
```

This misses the desired scale by a factor of `alpha^{-2}`.

Adding an `L^\infty` bound on `c` does not automatically give `alpha^4`, because the remaining trilinear convolution can be supported on many frequencies.  Tiny coefficients can still accumulate if the support has enough shear incidences.

## Fiber interpretation

Because the shear map preserves

```math
w=u+v,
```

the edge count can be written fiberwise.  For each `w`, define

```math
\Omega_w=\Omega\cap(w-\Omega).
```

Then the shear condition is

```math
u_1\in\Omega_w,
\qquad
u_1+2w\in\Omega_w.
```

Thus

```math
E_T(\Omega)=\sum_w |\Omega_w\cap(\Omega_w-2w)|.
```

The low-coefficient obstruction is therefore a cloud whose additive pair-fibers have nontrivial self-overlap under the unipotent shift.

This is exactly the support-level analogue of the spectral-pair autocorrelation identity.

## Phase requirement

Support incidence is not enough.  The actual shear sum is signed/complex:

```math
\sum_{u,v}c_uc_v\overline{c_{3u+2v}c_{-2u-v}}.
```

A flat cloud contributes only if phases align along many shear edges.  Writing

```math
c_\xi=\lambda e_p(\phi(\xi))
```

on the cloud, the phase relation is

```math
\phi(u)+\phi(v)-\phi(3u+2v)-\phi(-2u-v)\approx \text{constant}
```

on many shear edges.

In fiber variables `w=u+v`, this becomes a line-difference condition for

```math
h_w(u)=c_uc_{w-u}.
```

Thus the low-coefficient alternative is already a quadratic-chirp/cocycle candidate, provided the phase alignment is robust.

## Revised dichotomy

The dyadic cutoff barrier should be handled by the following dichotomy:

1. **Concentrated-scale branch.**  A bounded number of coefficient layers captures the shear sum.  Then run shear-BSG on those layers.
2. **Flat-cloud branch.**  Many tiny coefficients carry the shear sum.  Then the support must have shear-edge density at least `alpha^2` and the phases must satisfy a coherent shear-cocycle relation on many edges.

The flat-cloud branch is not an error.  It is another route into quadratic structure.

## Next research question

Can one prove a phase-sensitive BSG lemma for flat shear clouds?

A useful target is:

> If a flat spectral cloud `Omega` with coefficient size `lambda` contributes `alpha^4` to the shear sum, then either `Omega` has a large additive/low-rank structured component or the phase function on `Omega` agrees with a quadratic chirp on many shear fibers.

This is the right replacement for a nonexistent interpolation cutoff.

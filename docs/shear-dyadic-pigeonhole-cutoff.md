# Shear dyadic pigeonhole cutoff barrier

## Status

Proof-audit correction and partial lemma.  This note makes the dyadic pigeonholing step in the shear-BSG route precise enough to expose its first technical barrier.

The main point:

```math
\text{dyadic pigeonholing is easy only after a contribution-capturing truncation.}
```

There is no automatic coefficient-size cutoff from `L^2` energy alone.

## Setup

Let

```math
G=F_p^n,
\qquad f=1_A-\alpha,
\qquad c_\xi=\widehat f(\xi).
```

In the pure four-balanced branch,

```math
Q=\sum_{u,v}c_uc_v\overline{c_{3u+2v}c_{-2u-v}}
```

and

```math
|Q|\ge \kappa\alpha^4.
```

Let the four linear forms be

```math
L_1(u,v)=u,
\qquad
L_2(u,v)=v,
\qquad
L_3(u,v)=3u+2v,
\qquad
L_4(u,v)=-2u-v.
```

## Conditional dyadic pigeonhole lemma

For dyadic scales `lambda`, define

```math
\Omega_\lambda=\{\xi\ne0:\lambda<|c_\xi|\le 2\lambda\}.
```

Fix a finite dyadic scale family `D`.  Let `Q_D` denote the part of `Q` whose four frequencies all lie in layers from `D`.

If

```math
|Q_D|\ge \kappa_D\alpha^4,
```

and

```math
R=|D|,
```

then there exist four dyadic scales

```math
\lambda_1,\lambda_2,\lambda_3,\lambda_4\in D
```

such that the restricted shear sum

```math
Q_{\lambda_1,\lambda_2,\lambda_3,\lambda_4}
=
\sum_{\substack{u,v:\ L_i(u,v)\in\Omega_{\lambda_i}}}
 c_uc_v\overline{c_{3u+2v}c_{-2u-v}}
```

satisfies

```math
|Q_{\lambda_1,\lambda_2,\lambda_3,\lambda_4}|
\ge
\kappa_D\alpha^4/R^4.
```

This is just the triangle inequality and pigeonhole principle.

## Edge-count consequence

On this restricted layer, every nonzero term has magnitude at most

```math
16\lambda_1\lambda_2\lambda_3\lambda_4
```

and at least

```math
\lambda_1\lambda_2\lambda_3\lambda_4.
```

Thus the number of participating shear edges is at least

```math
N_{\mathrm{edge}}
\ge
\frac{\kappa_D\alpha^4}
{16R^4\lambda_1\lambda_2\lambda_3\lambda_4}.
```

Here a shear edge means a pair `(u,v)` such that

```math
u_i=L_i(u,v)\in\Omega_{\lambda_i}
```

for all `i=1,2,3,4`.

## The cutoff problem

The conditional lemma is not yet enough.  One must produce a finite scale family `D` with small enough `R` and with

```math
|Q_D|\gtrsim \alpha^4.
```

A naive choice is

```math
D=\{\lambda:\lambda_{\min}\le \lambda\le \lambda_{\max}\}.
```

The upper endpoint is harmless because

```math
|c_\xi|\le \alpha.
```

The lower endpoint is not harmless.

The `L^2` energy bound

```math
\sum_\xi |c_\xi|^2\le \alpha
```

alone does not imply that coefficients below a small threshold make negligible shear contribution.  A very large number of tiny coefficients can still contribute to a quartic form through coherent phase alignment.

Therefore one cannot simply discard all coefficients below, say, `alpha^C`, unless an additional estimate is supplied.

## Why this matters

If the number of active dyadic scales is allowed to be as large as

```math
\log |G|\sim n,
```

then the dyadic loss can be polynomial in `1/alpha` near the finite-field threshold

```math
n\sim \alpha^{-1+\delta}.
```

That loss may destroy the exponent gain.  The route needs only logarithmic losses in `1/alpha`, not uncontrolled losses in the ambient dimension.

## Possible ways to close the cutoff gap

One needs one of the following additional inputs.

### 1. Contribution-weighted truncation

Find a scale family `D` with small entropy under the contribution measure

```math
\mu(u,v)\propto
|c_uc_vc_{3u+2v}c_{-2u-v}|.
```

This would justify pigeonholing without requiring a hard coefficient cutoff.

### 2. Higher-moment control

If pair-density flatness or another hard-branch hypothesis gives strong enough control of

```math
\sum_\xi |c_\xi|^r
```

for some `r>2`, then very small coefficients may be made negligible in the shear form.

The existing pair-density variance gives only

```math
\sum_{\xi\ne0}|\widehat{1_A}(\xi)|^4,
```

which helps but does not automatically control the full phase-sensitive shear contribution.

### 3. Phase-sensitive cancellation

Tiny coefficients might contribute in absolute value, but not with coherent sign.  A phase-sensitive lemma could show that if tiny coefficients carry a large negative shear sum, then they already organize into a quadratic chirp/cocycle structure.

### 4. Physical-space sifting

Avoid dyadic spectral truncation entirely.  Work with pair-fiber disjointness in physical space and use a Kelley--Meka/Raghavan-style sifting mechanism to aggregate medium obstructions before passing to Fourier/quadratic structure.

## Revised toy lemma

The correct toy lemma should be stated with an explicit truncation alternative:

> If the nontrivial shear sum has size at least `kappa alpha^4`, then either:
>
> 1. a bounded number of dyadic coefficient layers captures a comparable share of the shear sum, giving a shear-BSG input; or
> 2. the shear sum is carried by many tiny/coherently phased coefficients, which itself should be treated as a quadratic-chirp/cocycle obstruction.

## Next research question

Can the low-coefficient alternative be converted directly into quadratic structure?  If yes, the dyadic cutoff problem becomes a feature rather than a bug.  If no, the shear-BSG route needs a new norm or moment estimate stronger than `L^2` but weaker than full generic `U^3` inversion.

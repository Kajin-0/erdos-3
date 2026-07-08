# Shear BSG toy lemma

## Status

Extraction target.  This note starts the requested pivot from broad architecture to a concrete shear-energy extraction problem.

The aim is not yet to prove the final theorem.  The aim is to isolate the first place where a Balog--Szemeredi--Gowers-style extraction could enter the pair-fiber/shear route.

## External motivation

Recent work around Roth/Kelley--Meka/Raghavan suggests that the relevant move is not to find one large Fourier coefficient immediately, but to sift many medium obstructions into one structured increment.

Milićević's `U^4(F_p^n)` inverse theorem is not directly a 4AP theorem, but its proof architecture -- abstract BSG, algebraic regularity, bilinear Bogolyubov, and algebraic dependent random choice -- is a useful model for turning large multilinear energy into algebraic structure.

The shear-energy problem has the right shape for this kind of extraction.

## Setup

Let

```math
G=F_p^n,
\qquad p>4,
```

and let

```math
f=1_A-\alpha,
\qquad c_\xi=\widehat f(\xi).
```

In the pure four-balanced branch,

```math
Q=\Lambda_4(f,f,f,f)\le -\kappa\alpha^4.
```

The shear form is

```math
Q=\sum_{u,v} c_u c_v\overline{c_{3u+2v}c_{-2u-v}}.
```

Define

```math
T(u,v)=(3u+2v,-2u-v).
```

Then

```math
Q=\sum_{u,v}F(u,v)\overline{F(T(u,v))},
\qquad
F(u,v)=c_uc_v.
```

The map `T` is unipotent and preserves

```math
w=u+v.
```

## No-large-atom regime

Assume the desired Fourier increment is absent:

```math
\|c\|_{\infty,\xi\ne0}<\alpha^{2-\epsilon}.
```

Then the negative shear energy cannot be attributed to one large Fourier atom.  It must be carried by many medium coefficients whose products align along `T`-orbits.

This is the setting for BSG-type extraction.

## Dyadic spectral pigeonholing

For dyadic scales `lambda`, define

```math
\Omega_\lambda=\{\xi\ne0: \lambda<|c_\xi|\le 2\lambda\}.
```

Decompose the shear sum according to the four coefficient scales:

```math
u_1=u,
\qquad
u_2=v,
\qquad
u_3=3u+2v,
\qquad
u_4=-2u-v.
```

If

```math
|Q|\ge \kappa\alpha^4,
```

then after losing only logarithmic factors there exist dyadic scales

```math
\lambda_1,\lambda_2,\lambda_3,\lambda_4
```

such that the restricted shear sum over

```math
u_i\in\Omega_{\lambda_i}
```

has magnitude at least

```math
\gg \kappa\alpha^4/\mathrm{polylog}(1/\alpha).
```

This is the first concrete extraction statement.

## From large weighted sum to many shear edges

On the restricted level, each term has magnitude about

```math
\lambda_1\lambda_2\lambda_3\lambda_4.
```

Therefore the number of participating shear edges must be at least

```math
N_{\mathrm{edge}}
\gg
\frac{\kappa\alpha^4}
{\lambda_1\lambda_2\lambda_3\lambda_4\,\mathrm{polylog}(1/\alpha)}.
```

Here a shear edge is a pair `(u,v)` such that

```math
u_1=u\in\Omega_{\lambda_1},
\quad
\nu_2=v\in\Omega_{\lambda_2},
\quad
\nu_3=3u+2v\in\Omega_{\lambda_3},
\quad
\nu_4=-2u-v\in\Omega_{\lambda_4}.
```

The relation automatically satisfies

```math
\nu_1+\nu_2=\nu_3+\nu_4.
```

Thus large shear energy gives many additive quadruples across dyadic spectral layers, but with the stronger constraint that the second pair is the unipotent image of the first.

## Why ordinary additive energy is not enough

The relation

```math
\nu_1+\nu_2=\nu_3+\nu_4
```

only gives additive energy.  The shear relation also imposes

```math
(\nu_3,\nu_4)=T(\nu_1,\nu_2).
```

Equivalently, within each fiber

```math
w=\nu_1+\nu_2,
```

the map is the translation

```math
\nu_1\mapsto \nu_1+2w.
```

A useful extraction must preserve this fiberwise unipotent structure.  Otherwise it collapses back to a generic `U^3` inverse theorem and loses the exponent.

## Toy BSG target

A first toy lemma to prove is:

> Suppose a set of weighted coefficients `c` has no atom above `alpha^{2-epsilon}`, has controlled fourth moment, and satisfies
>
> ```math
> \left|\sum_{u,v} c_uc_v\overline{c_{3u+2v}c_{-2u-v}}\right|
> \ge \kappa\alpha^4.
> ```
>
> Then there exist dyadic spectral layers and a subset of frequencies `\Omega` with high additive energy along shear fibers.  More precisely, there is a large set of sums `W` such that for many `w in W`, the fiber
>
> ```math
> \Omega\cap(w-\Omega)
> ```
>
> has large intersection with its translate by `2w`.

This is the shear-specific version of an additive-energy extraction lemma.

## Desired BSG conclusion

The hoped-for conclusion is not merely a small-doubling set.  It should be one of:

1. **Large Fourier atom.**  Contradicts the no-large-atom assumption and gives the desired increment.
2. **Low-rank additive/quadratic model.**  Leads to the low-rank quadratic increment branch.
3. **Quadratic chirp/cocycle model.**  Produces line functions

```math
H_{w,r}(t)=c_{r+tw}c_{w-r-tw}
```

with coherent quadratic-chirp behavior, suitable for Prendiville or the high-rank branch.

## Where this could fail

The pigeonholing step is straightforward.  The difficult step is upgrading many shear edges into a structured spectral object without losing the exponent.

A generic BSG extraction may only yield additive structure at a scale too weak for the `alpha^{2-epsilon}` increment target.  The extraction must use:

1. the unipotent shear map;
2. the phase alignment of the weighted sum, not just support size;
3. the endpoint factorization `F(u,v)=c_uc_v`;
4. the physical pair-fiber origin of the obstruction.

## Immediate next proof task

Prove the dyadic pigeonholing lemma rigorously, with explicit logarithmic losses, then test whether the resulting restricted shear graph has enough additive energy for a BSG extraction.

If the BSG step only gives ordinary additive energy, this route probably cannot beat the generic `U^3` barrier.  If it preserves the shear-fiber structure, it may be the first genuine path to an `alpha^{2-epsilon}` increment.

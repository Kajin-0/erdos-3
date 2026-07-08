# Unipotent shear orbit decomposition

## Status

Proof-audit identity and structural reduction.  This note decomposes the shear-energy obstruction into spectral fibers preserved by a unipotent map.  It gives a more precise object than a generic quartic Fourier sum.

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

Then

```math
c_0=0,
\qquad
\sum_\zeta |c_\zeta|^2=E|f|^2=\alpha(1-\alpha)\le \alpha.
```

The pure four-balanced obstruction is

```math
Q=\Lambda_4(f,f,f,f)
```

and in the pure branch

```math
Q\le -c\alpha^4.
```

## Shear-energy form

From the pair-product formulation, define

```math
G_f(x,d)=f(x)f(x+d).
```

Then

```math
Q=\langle G_f,G_f\circ S\rangle_{G\times G},
\qquad
S(x,d)=(x+2d,d).
```

Using Fourier variables `(xi,eta)`, the Fourier transform factors as

```math
\widehat {G_f}(\xi,\eta)=c_{\xi-\eta}c_\eta.
```

Thus

```math
Q=\sum_{\xi,\eta}
c_{\xi-\eta}c_\eta
\overline{c_{3\xi-\eta}c_{\eta-2\xi}}.
```

## Change of variables

Set

```math
u=\xi-\eta,
\qquad
v=\eta.
```

Then

```math
\xi=u+v.
```

The two transformed frequencies are

```math
3\xi-\eta=3u+2v,
\qquad
\eta-2\xi=-2u-v.
```

So define the linear map

```math
T(u,v)=(3u+2v,-2u-v).
```

Then

```math
Q=\sum_{u,v} c_u c_v\overline{c_{T_1(u,v)}c_{T_2(u,v)}}.
```

Equivalently, for

```math
F(u,v)=c_u c_v,
```

we have

```math
Q=\langle F,F\circ T\rangle.
```

## Unipotent structure

The map `T` is unipotent:

```math
T=I+N,
\qquad
N(u,v)=2(u+v)(1,-1),
\qquad
N^2=0.
```

It preserves the spectral sum

```math
w=u+v.
```

On the fiber

```math
L_w=\{(u,v):u+v=w\},
```

write `v=w-u`.  Then

```math
T(u,w-u)=(u+2w,w-u-2w).
```

Thus, on each spectral fiber `L_w`, the shear acts as the translation

```math
u\mapsto u+2w.
```

For `w=0`, the translation is trivial; for `w\ne0`, it is a nonzero translation of the affine line `L_w`.

## Fiber autocorrelation formula

Define the spectral pair-fiber function

```math
h_w(u)=c_u c_{w-u}.
```

Then the pure obstruction decomposes as

```math
Q=\sum_w \sum_u h_w(u)\overline{h_w(u+2w)}.
```

Equivalently,

```math
Q=\sum_w \langle h_w,\tau_{2w}h_w\rangle.
```

This is the spectral dual of the physical pair-fiber identity.

## Consequences

The fiber `w=0` contributes

```math
\sum_u |c_u c_{-u}|^2\ge0.
```

Therefore the negative pure obstruction must come from nonzero spectral-sum fibers `w\ne0`:

```math
\sum_{w\ne0}\langle h_w,\tau_{2w}h_w\rangle\le -c\alpha^4
```

up to the nonnegative `w=0` term.

Thus the obstruction is not an undifferentiated quartic Fourier sum.  It is an average of negative autocorrelations of spectral pair-fibers under their natural translations.

## Spectral pair mass

Let

```math
m_w=\sum_u |h_w(u)|^2
=\sum_u |c_u|^2|c_{w-u}|^2.
```

Then

```math
\sum_w m_w=\left(\sum_u |c_u|^2\right)^2\le \alpha^2.
```

Also

```math
|\langle h_w,\tau_{2w}h_w\rangle|\le m_w.
```

Therefore any negative contribution of size `alpha^4` must be carried by spectral fibers whose total mass is at least `alpha^4`.  This is not enough by itself, because the total spectral pair mass may be as large as `alpha^2`; additional structure is needed.

## Relation to marginal flatness

The pair-density flatness condition controls

```math
\sum_{u\ne0}|c_u|^4.
```

This is only the diagonal piece of the spectral pair mass.  The obstruction may live in off-diagonal fibers

```math
h_w(u)=c_uc_{w-u},
\qquad w\ne0,
```

with many small coefficients coherently phased along the translation `u -> u+2w`.

## New classification target

A sharpened classification theorem would say:

> If
> ```math
> \sum_{w\ne0}\langle h_w,\tau_{2w}h_w\rangle\le -c\alpha^4,
> ```
> while no coefficient satisfies
> ```math
> |c_u|\ge \alpha^{2-\epsilon},
> ```
> and the marginal fourth moment is small, then either the spectral pair-fibers `h_w` have low-rank additive/quadratic organization, or the obstruction is supported on high-rank quadratic structure suitable for the relative-host branch.

## Why this is useful

The map `T` preserving `w=u+v` prevents the shear sum from being a black-box global quartic.  It reduces the problem to many one-dimensional autocorrelation problems in frequency space, with a translation length determined by the same fiber parameter `w`.

This mirrors the physical-space statement:

```math
B_d=A\cap(A-d),
\qquad
B_d\cap(B_d-2d)=\emptyset.
```

The proof may need to compare physical pair-fiber disjointness with spectral pair-fiber anti-correlation.  A density increment should emerge when these two dual fiber systems cannot both remain flat.

## Next research question

Can one prove a dual-fiber lemma: if both the physical pair-fibers and spectral pair-fibers are flat, then the average negative autocorrelation at scale `alpha^4` is impossible?  If not, classify the common extremizers; they should be quadratic rather than linear.

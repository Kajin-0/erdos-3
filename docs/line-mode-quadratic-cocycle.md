# Line-mode quadratic cocycle target

## Status

Proof-audit target.  This note explains why the spectral line modes forced by the pure four-balanced obstruction have the right algebraic shape to assemble into a quadratic phase/factor.

The goal is to convert line-mode data

```math
(w,r,m)
```

into a quadratic-cocycle condition rather than treating it as unstructured Fourier oscillation.

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

Negative pure obstruction forces substantial nonzero one-dimensional Fourier modes of these functions.

## Quadratic phases produce linear line modes

Suppose, heuristically, that on some spectral support the Fourier coefficients have phase modeled by

```math
c_\zeta \approx A(\zeta)e_p(q(\zeta)),
```

where `q` is a quadratic form and `A(\zeta)` is a slowly varying amplitude.

Then along a paired line,

```math
q(r+tw)+q(w-r-tw)
```

is a polynomial in `t` of degree at most two.  The quadratic terms cancel because the two arguments move in opposite directions.

Indeed, if `B_q` is the symmetric bilinear form associated to `q`, then

```math
q(r+tw)+q(w-r-tw)
=\text{constant}+t\,B_q(w,2r-w)
```

up to the convention-dependent linear part.

Thus a quadratic phase naturally gives a linear mode in `t` for `H_{w,r}`.

This explains why the line-mode obstruction is a quadratic signature.

## Cocycle interpretation

If `H_{w,r}` has a large Fourier mode `m`, then morally

```math
c_{r+tw}c_{w-r-tw}
```

has phase close to

```math
e_p(mt+\theta_{w,r})
```

on a significant portion of the line.

Equivalently, writing `\phi(\zeta)` for the phase of `c_\zeta`, the relation is

```math
\phi(r+tw)+\phi(w-r-tw)\approx mt+\theta_{w,r}.
```

For a genuine quadratic phase, the slope `m` should be controlled by a bilinear form:

```math
m=m(w,r)\approx B(w,2r-w)+\ell(w)
```

for some symmetric bilinear form `B` and possible linear correction `\ell`.

Therefore the data `(w,r,m)` should satisfy compatibility relations as `(w,r)` varies.

## First compatibility test

For fixed `w`, if `r` is replaced by

```math
r'=r+sw,
```

then the same spectral line is being reparametrized.  The corresponding mode should transform only by the reparametrization of `t`, not define a new independent slope.

Thus line-mode data must first be quotient-consistent on

```math
G/\langle w\rangle.
```

This is already built into the choice of representatives, but any extraction theorem must avoid counting the same line multiple times.

## Second compatibility test: parallelogram consistency

A bilinear model predicts that the slope function in `r` has linear increments:

```math
m(w,r+s)-m(w,r)\approx 2B(w,s).
```

Thus for fixed `w`, the map

```math
r\mapsto m(w,r)
```

should be approximately affine on the quotient `G/<w>`.

If it is not, then the line-mode mass is not organized by one quadratic factor and may instead yield additive-energy structure or a density increment.

## Third compatibility test: symmetry in the paired variables

The pair

```math
u=r+tw,
\qquad
w-\nu=w-r-tw
```

is symmetric under swapping `u` and `w-u`, which corresponds to `t` being replaced by an affine function of `t` depending on `r,w`.

A coherent quadratic model should give compatible modes under this involution.  Failure of this compatibility is another possible source of structured increment.

## Candidate quadratic-cocycle lemma

A useful theorem would be:

> Suppose the pure obstruction forces many large line modes
>
> ```math
> |\widehat H_{w,r}(m)|
> ```
>
> while `|c_\zeta|<alpha^{2-epsilon}` for all nonzero `\zeta` and the marginal fourth moment is small.
>
> Then either:
>
> 1. the extracted slopes `m(w,r)` fail affine/parallelogram consistency, yielding a density increment or additive spectral concentration; or
> 2. they agree on a large substructure with
>
> ```math
> m(w,r)=B(w,2r-w)+\ell(w)
> ```
>
> for a bilinear form `B`, producing a quadratic factor.

## Low-rank / high-rank split

Once a bilinear form `B` is extracted, the existing rank split applies:

1. if `B` has low rank, quadratic-level sets decompose into affine structure and should give a density increment;
2. if `B` has high rank, the obstruction belongs in the high-rank relative-host recurrence branch.

Thus the line-mode cocycle is a bridge from spectral shear cancellation to the quadratic rank program.

## Why this is progress

The previous formulation said only that there is nonzero line-mode mass.  This note identifies the consistency relations that must hold if the line modes really come from a quadratic obstruction.

The proof search can now try to show:

```math
\text{large inconsistent line-mode mass} \Rightarrow \text{density increment},
```

while

```math
\text{large consistent line-mode mass} \Rightarrow \text{quadratic factor}.
```

## Next research question

Can a Balog--Szemeredi--Gowers-type extraction on the set of large line modes produce an approximately affine slope map

```math
(w,r)\mapsto m(w,r),
```

or else force a large Fourier atom/density increment?

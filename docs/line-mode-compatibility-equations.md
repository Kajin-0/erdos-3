# Line-mode compatibility equations

## Status

Extraction target.  This note starts the second implication in the phase-sensitive flat-cloud route:

```math
\text{many biased line modes }m(w,r)
\Rightarrow
\text{compatibility of }m(w,r)
\Rightarrow
\text{quadratic/low-rank structure or increment}.
```

The point is to distinguish true modes coming from one common coefficient field `c_xi` from arbitrary line-by-line choices.

## Setup

For each nonzero `w in G`, define

```math
h_w(u)=c_uc_{w-u}.
```

For a representative `r in G/<w>`, set

```math
H_{w,r}(t)=h_w(r+tw)=c_{r+tw}c_{w-r-tw}.
```

Suppose that for many `(w,r)`, the one-dimensional function `H_{w,r}` has substantial Fourier mass near a mode

```math
m=m(w,r).
```

The compatibility question is: what algebraic restrictions must the mode field `m(w,r)` satisfy because all `H_{w,r}` are built out of one common coefficient function `c`?

## Gauge invariance under representative shift

The representative `r` is only defined modulo the line `<w>`.  If

```math
r'=r+sw,
```

then

```math
H_{w,r'}(t)=H_{w,r}(t+s).
```

A translation in `t` changes Fourier phases but not Fourier frequencies.  Therefore the extracted mode must satisfy

```math
m(w,r+sw)=m(w,r)
```

whenever the same line is being described.

Thus `m(w,r)` is a function on the quotient variable

```math
r\in G/<w>.
```

## Reversal symmetry

The pair defining `h_w` is unordered:

```math
c_uc_{w-u}=c_{w-u}c_u.
```

Replacing `r` by `w-r` gives

```math
H_{w,w-r}(t)
=c_{w-r+tw}c_{r-tw}
=H_{w,r}(-t).
```

Therefore a line mode must reverse sign:

```math
m(w,w-r)=-m(w,r).
```

This is a nontrivial compatibility constraint.  Arbitrary line-mode selections need not satisfy it.

## Quadratic model prediction

Suppose on a structured spectral cloud the coefficients have phase

```math
c_\xi\approx A(\xi)e_p(q(\xi)),
```

where `q` is quadratic with homogeneous quadratic part `Q_q` and polar bilinear form `B_q`.

Then

```math
q(r+tw)+q(w-r-tw)
=
C(w,r)+2Q_q(w)t^2+B_q(w,2r-w)t.
```

Thus the affine line-mode prediction is valid only when the quadratic `t^2` term is absent or suppressed, for example when

```math
Q_q(w)=0
```

on the active directions.

In that degenerate/isotropic case,

```math
m(w,r)=B_q(w,2r-w)=2B_q(w,r)-B_q(w,w).
```

If `Q_q(w)=0`, then `B_q(w,w)=2Q_q(w)=0`, so

```math
m(w,r)=2B_q(w,r).
```

This automatically satisfies the representative-shift invariance:

```math
m(w,r+sw)=2B_q(w,r)+2sB_q(w,w)=m(w,r).
```

It also satisfies reversal:

```math
m(w,w-r)=2B_q(w,w-r)=-2B_q(w,r)=-m(w,r).
```

## Affinity in the base variable

In the quadratic isotropic model, for fixed `w`, the map

```math
r\mapsto m(w,r)
```

is a linear functional on the quotient `G/<w>`:

```math
m(w,r_1+r_2)=m(w,r_1)+m(w,r_2)
```

whenever the expressions are interpreted modulo the representative gauge and the relevant lines remain active.

Therefore the next extraction test is:

> Do the line modes obtained from autocorrelation behave like linear functionals in `r` for many fixed `w`?

Failure of this test means the mode field is not yet a quadratic phase; it may be support-truncation noise or require a different structured branch.

## Bilinearity in direction and basepoint

A true quadratic model also predicts bilinearity:

```math
m(w,r)=2B_q(w,r).
```

Hence, on compatible active directions,

```math
m(w_1+w_2,r)=m(w_1,r)+m(w_2,r)
```

and

```math
m(w,r_1+r_2)=m(w,r_1)+m(w,r_2),
```

again modulo the quotient gauges and active-support restrictions.

This is a much stronger target than fixed-line mode extraction.  It turns the problem into a cocycle-stability problem for the empirical mode field `m(w,r)`.

## Three-point compatibility test

A concrete local test is obtained by comparing three pairings among points `a,b,c`.

Let

```math
w_{ab}=a+b,
\qquad
w_{ac}=a+c,
\qquad
w_{bc}=b+c.
```

If modes come from a bilinear form, then the values associated to the pairs should satisfy additive identities after rewriting each pair in its own line coordinate.

For example, in the isotropic quadratic model,

```math
m(w_{ab},a)=2B_q(a+b,a),
```

and similarly for the other pairs.  Linear combinations of such quantities eliminate quadratic diagonal terms when the active directions are isotropic.  Any systematic failure of these local cocycle identities indicates that the extracted line modes do not come from a global quadratic phase.

This suggests a BSG-style route:

```math
\text{many compatible local mode identities}
\Rightarrow
\text{large subset where }m(w,r)\text{ is bilinear}
\Rightarrow
\text{quadratic model or low-rank structure}.
```

## Why this matters for exponent gain

The fixed-line extraction alone has no exponent power.  It only says that autocorrelation creates line-mode bias.

Exponent gain can enter only if many such biased modes are forced to agree with a low-complexity algebraic object.  The simplest candidate object is a bilinear form `B_q`, hence a quadratic phase `q`.

If the compatibility extraction succeeds, then the route becomes:

```math
\text{large shear contribution}
\Rightarrow
\text{many line modes}
\Rightarrow
\text{bilinear mode field}
\Rightarrow
\text{quadratic phase/cocycle}
\Rightarrow
\text{Prendiville or low-rank increment}.
```

## Immediate proof task

Prove a robust version of the following statement:

> Suppose line-mode extraction gives modes `m(w,r)` for a positive-weight family of pairs `(w,r)`, and suppose these modes arise from functions
>
> ```math
> H_{w,r}(t)=c_{r+tw}c_{w-r-tw}.
> ```
>
> If the modes satisfy representative invariance, reversal symmetry, and many local additive identities, then on a large subfamily there exists a bilinear form `B` such that
>
> ```math
> m(w,r)\approx 2B(w,r).
> ```

This is the line-mode compatibility lemma needed after the fixed-`w` extraction.

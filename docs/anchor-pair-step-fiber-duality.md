# Anchor-pair step-fiber duality

## Status

Exact state-independent transpose identity for root-level weighted three-AP
multiplicity in a four-AP-free dyadic block.

The theorem resolves reuse of one anchor pair across several numerical steps:
it is not an uncontrolled second multiplicity. It is one lower-scale
four-AP-free step-fiber child whose harmonic mass equals the assigned debt.

---

## 1. Fixed-step anchor stars

Let

```math
B\subseteq[N,2N)
```

be four-AP-free. For each step `d>0`, define

```math
P_d
=
\{p:p,p+d,p+2d\in B\}.
```

If `P_d` is nonempty, choose the canonical base anchor

```math
a_d=\min P_d.
```

Every remaining anchor `p in P_d\setminus\{a_d\}` gives one collision
incidence

```math
(d,\{a_d,p\}).
```

The fixed-step excess is

```math
R_{\rm step}(B)
=
\sum_d\frac{|P_d|-1}{d}.
```

---

## 2. Anchor-pair step fibers

For an unordered parent anchor pair

```math
f=\{a,p\},
\qquad a<p,
```

define its canonical step fiber

```math
S_f
=
\{d:a_d=a,\ p\in P_d\}.
```

Equivalently, `d in S_f` means

```text
a,a+d,a+2d are in B;
p,p+d,p+2d are in B;
a is the minimum start of every step-d three-AP in B.
```

The canonical minimum condition assigns every nonbase fixed-step occurrence to
exactly one anchor pair.

---

## 3. Exact transpose identity

The set of collision incidences can be summed first by step or first by anchor
pair:

```math
\sum_d
\sum_{p\in P_d\setminus\{a_d\}}
\frac1d
=
\sum_f
\sum_{d\in S_f}
\frac1d.
```

Therefore

```math
\boxed{
R_{\rm step}(B)
=
\sum_f H(S_f).
}
```

This is an exact identity. No overlap constant, aspect coefficient, or fitted
potential is used.

---

## 4. Every step fiber is four-AP-free

Fix `f={a,p}`. Since

```math
a+S_f\subseteq B,
```

translation and subsetting imply

```math
\boxed{S_f\text{ is four-AP-free}.}
```

The second anchor gives the additional inclusions

```math
p+S_f\subseteq B,
```

```math
a+2S_f\subseteq B,
```

and

```math
p+2S_f\subseteq B.
```

Thus every fiber forces the four affine layers

```math
(a+S_f)
\cup
(a+2S_f)
\cup
(p+S_f)
\cup
(p+2S_f)
\subseteq B.
```

The fiber is a lower-dimensional rectangle state inside the parent.

---

## 5. Strict scale descent

Every step of a three-AP in `[N,2N)` satisfies

```math
0<d<N/2.
```

Resolve each `S_f` into standard dyadic shells

```math
S_{f,M}=S_f\cap[M,2M).
```

Because `N` and `M` are powers of two and no step reaches `N/2`, every
nonempty shell satisfies

```math
\boxed{M\le N/4.}
```

Hence the exact transpose identity resolves into strictly lower-scale
four-AP-free children:

```math
\boxed{
R_{\rm step}(B)
=
\sum_f\sum_{M\le N/4}H(S_{f,M}).
}
```

---

## 6. Role-star rigidity inherited by the fibers

Every `S_f` is a subset of the first-point role star at `a` and at `p`.
Consequently it inherits the side-role exclusions

```math
S_f\cap3S_f=\varnothing
```

and

```math
2S_f\cap3S_f=\varnothing.
```

Only doubling-chain overlap can remain among

```math
S_f,
\qquad
2S_f,
\qquad
3S_f.
```

A parity split of each fiber therefore gives two valid side-oriented
subfibers with pairwise-disjoint first three dilates and no harmonic loss
across the two colors.

This makes every collision fiber compatible with the full-edge recursive
interface.

---

## 7. First appearance plus fiber recursion

The weighted parent three-AP load has the exact decomposition

```math
\boxed{
\mathcal L_3(B)
=
U(B)
+
\sum_f H(S_f),
}
```

where

```math
U(B)
=
\sum_{d:P_d\ne\varnothing}\frac1d
```

is distinct numerical-step first appearance.

Thus the entering AP-load problem separates into:

```text
one copy of every numerical step;
strictly lower-scale anchor-pair step fibers carrying all repeated copies.
```

The base-six obstruction is now interpreted correctly. Its enormous unit-step
multiplicity creates many anchor-pair incidences; after transposition, those
incidences become lower-scale step fibers rather than an entering scalar debt.

---

## 8. Relation to rectangle-aspect tokens

For `d in S_f`, write

```math
f=\{a,p\},
\qquad
\delta=p-a.
```

The incidence has exact aspect factorization

```math
\frac1d
=
\frac\delta d\frac1\delta.
```

The step-fiber identity retains the left representation `1/d`; the
rectangle-aspect ledger retains the right representation `(delta/d)(1/delta)`.
They are two views of the same incidence.

This provides a choice in a global potential:

1. recurse on the lower-scale step fiber `S_f`;
2. charge a near-aspect incidence to the anchor pair `f`;
3. transport a far-aspect incidence by its dyadic rectangle ratio.

---

## 9. Remaining overlap layer

Different anchor pairs may produce step fibers sharing the same numerical
steps. That overlap is not hidden: for a fixed step `d`, its fiber multiplicity
is exactly `|P_d|-1`, the original collision count.

The transpose theorem therefore does not contract raw occurrence mass by
itself. Its gain is structural:

```text
all repeated root AP load is represented by genuine lower-scale four-AP-free
children with exact provenance and side-role rigidity.
```

The next theorem must combine first appearance of the pair-step incidence
`(f,d)` with scale-critical full-edge transport. No further anonymous
multiplicity layer remains.

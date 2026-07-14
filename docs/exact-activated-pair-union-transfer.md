# Exact activated-pair union transfer

## Status

State-independent one-generation transfer theorem for any selected family of
distinct three-AP occurrences in a four-AP-free dyadic block.

The theorem merges base-step edges and translated near-collision pairs before
payment. Every activated physical pair is spent at most once. All unpaid
occurrence mass is exported as strictly lower-scale four-AP-free fibers.

---

## 1. Selected occurrence family

Let

```math
B\subseteq[N,2N)
```

be four-AP-free, and let

```math
\mathcal A
\subseteq
\{(p,d):p,p+d,p+2d\in B\}
```

be any set of distinct three-AP occurrences.

For each used step `d`, choose the minimum selected start `a_d`. The base
occurrence is paid by the adjacent physical pair

```math
e_d=\{a_d,a_d+d\},
\qquad
w(e_d)=\frac1d.
```

Let

```math
E_{\rm step}=\{e_d\}.
```

Distinct steps produce distinct pairs.

---

## 2. Near translated-pair targets

For every nonbase occurrence with start `p>a_d`, put

```math
\delta=p-a_d.
```

If `delta<=d`, define the translated middle-row pair

```math
g=\{a_d+d,p+d\}.
```

For one target pair `g={x,y}`, let

```math
D_g
=
\{d:g=\{a_d+d,p+d\}\text{ for a near selected occurrence}\}.
```

Then:

1. the incidence-to-`(g,d)` map is injective;
2. `D_g` is four-AP-free because `x-D_g subseteq B`;
3. every `d in D_g` satisfies `d>=y-x`;
4. the total near occurrence mass at `g` is exactly `H(D_g)`.

Let

```math
G_{\rm near}=\{g:D_g\ne\varnothing\}.
```

---

## 3. Merge pair capacity before payment

Define the activated physical-pair union

```math
E_{\rm act}
=
E_{\rm step}\cup G_{\rm near}.
```

There are two cases for one near target `g`.

### New translated pair

If

```math
g\notin E_{\rm step},
```

choose `d_0(g)=min D_g`. Since `d_0(g)>=|g|`,

```math
\frac1{d_0(g)}
\le
w(g).
```

The new pair pays one preimage. The residual recursive set is

```math
D_g^+=D_g\setminus\{d_0(g)\}.
```

Thus

```math
H(D_g)
\le
w(g)+H(D_g^+).
```

### Pair already spent as a base edge

If

```math
g\in E_{\rm step},
```

its physical-pair capacity has already paid the base occurrence associated
with that step edge. It is not spent again. The entire preimage set `D_g`
remains recursive.

This is exact first-appearance semantics: pair overlap is merged, not bounded
by a multiplicity coefficient.

---

## 4. Far fibers

If `d<delta`, assign the occurrence to its canonical anchor-pair far fiber

```math
S_f^{\rm far},
\qquad
f=\{a_d,p\}.
```

The far mass is exactly

```math
R_{\rm far}
=
\sum_fH(S_f^{\rm far}).
```

Every far fiber is four-AP-free.

---

## 5. Complete exact-union row

Let

```math
\mathcal D_{\rm new}
=
\{D_g^+:g\in G_{\rm near}\setminus E_{\rm step}\},
```

and

```math
\mathcal D_{\rm reused}
=
\{D_g:g\in G_{\rm near}\cap E_{\rm step}\}.
```

Then

```math
\boxed{
\begin{aligned}
L(\mathcal A)
\le{}&
J(E_{\rm act})\\
&+
\sum_{D\in\mathcal D_{\rm new}}H(D)\\
&+
\sum_{D\in\mathcal D_{\rm reused}}H(D)\\
&+
\sum_fH(S_f^{\rm far}).
\end{aligned}
}
```

Every pair in `E_act` is distinct and paid once. Every selected three-AP
occurrence contributes to exactly one term on the right, except for the one
inequality `1/d_0(g)<=w(g)` used by each new translated pair.

No pair-energy prepayment, pair-overlap coefficient, or fitted scalar is used.

---

## 6. Strict scale descent of recursive terms

Every step in `D_g`, `D_g^+`, or `S_f^far` is a three-AP step inside
`[N,2N)`, hence is strictly less than `N/2`.

After standard dyadic resolution, every recursive fiber shell has base at most

```math
\boxed{N/4.}
```

All recursive fibers are four-AP-free and inherit side-role ratio exclusions.
They are valid inputs to the same full-edge construction.

Thus the row has exactly two outputs:

```text
distinct activated physical pairs at the current parent;
recursive four-AP-free fibers at least two dyadic levels lower.
```

---

## 7. Pair-provenance compatibility

The activated pair token is the actual unordered parent pair `e={u,v}` with
weight `1/|u-v|`. If the parent is represented in affine root coordinates,
this is exactly the existing root-pair resource.

Repeated appearances of the same pair across step-edge and translated-pair
roles are true reuse of one capacity and are merged in `E_act`.

The row therefore composes with:

1. affine pair first-appearance accounting;
2. sponsor-pair forward transport;
3. residual/backward/direct terminal classification;
4. completion and rectangle obstruction export.

---

## 8. Application to recursive collision preimages

For one fixed full-edge type, remove parent-target first appearances and view
the excess child preimages in one oriented shell as a selected AP occurrence
family `A`.

The exact-union row gives:

```text
one distinct activated child-root pair union;
strictly lower-scale collision fibers.
```

Completion transport embeds every activated child-root pair into the parent
pair universe. Thus the recursive collision term is no longer an anonymous
scalar `Y(P)`; it has exact pair-union and lower-scale-fiber semantics.

---

## 9. Strategic consequence

The complete local architecture is now:

```text
selected child AP occurrences
-> distinct activated physical pair union
   + lower-scale four-AP-free fibers.
```

The remaining global theorem is not a local packing statement. It must show
that activated pair first appearances, sponsor-pair terminal targets, and the
strictly descending recursive fibers telescope across the whole tree.

This row is the conceptual transfer law required before any further corrected
frontier propagation. Generation six remains unnecessary.

# Coordinated-deletion latent degree-two theorem

## Status

State-independent one-generation theorem for the coordinated deletion architecture used by the retained quotient.

Every parent root pair has at most two recursive latent owners among the complete raw backbone and middle-fiber shell outputs. If two latent owners exist, one is a backbone shell and the other is a middle-fiber shell. Higher latent multiplicity and middle-middle latent reuse are impossible.

Each backbone-middle duplicate also has two canonical translated parent-pair reserves of the same physical gap.

---

## 1. Completed coordinated deletion schedule

Let `P` be one finite parent state. A completed coordinated deletion schedule selects three-AP actions

```math
(s,c,o;d),
```

where:

```text
s is the sponsor;
c is the center;
o is the opposite endpoint;
d is the progression step.
```

After selecting an action, the sponsor `s` is removed from the current working set. Consequently:

```math
\boxed{
\text{each parent root is selected as sponsor at most once.}
}
```

The orientation for one step `d` is fixed by the parity rule. Write it as

```math
c=s+\varepsilon(d)d,
\qquad
o=s+2\varepsilon(d)d,
\qquad
\varepsilon(d)\in\{-1,+1\}.
```

---

## 2. Backbone root ownership

Let

```math
m=\min P.
```

The backbone labels are

```math
p-m,
\qquad
p\in P\setminus\{m\}.
```

Standard dyadic shelling partitions these labels. Every parent root `p` therefore belongs to exactly one backbone shell output.

Hence every parent pair

```math
f=\{p,q\}
```

belongs latently to at most one recursive backbone child.

---

## 3. Middle-fiber root ownership

Fix one selected step `d`. Order its selected centers:

```math
c_0<c_1<\cdots<c_t
```

with sponsors

```math
s_i=c_i-\varepsilon(d)d.
```

The middle fiber has labels

```math
c_i-c_0
=
s_i-s_0,
\qquad
1\le i\le t,
```

and affine reference `s_0`. Its provenance roots are the sponsors

```math
s_1,\ldots,s_t.
```

Each selected sponsor occurs in only one schedule action and therefore in the provenance set of only one step fiber. Standard shelling then places it in at most one middle-fiber shell output.

Thus every parent root belongs to at most one middle child, and every parent pair belongs latently to at most one recursive middle child.

---

## 4. Latent degree bound

A parent pair can have:

```text
at most one recursive backbone owner;
at most one recursive middle-fiber owner.
```

Therefore its recursive latent owner count satisfies

```math
\boxed{\ell_f\le2.}
```

If

```math
\ell_f=2,
```

then the owner profile is exactly

```text
one backbone child;
one middle-fiber child.
```

In particular:

```math
\boxed{
\text{middle-middle and backbone-backbone latent reuse are impossible.}
}
```

The theorem holds before exact-state quotienting and point-disjoint retention. Passing to a subfamily preserves it.

---

## 5. Exact residual form

After current-latent reclassification, the genuine latent activation residual is

```math
R_{\rm latent-latent}
=
\sum_f\frac{(\ell_f-1)_+}{D(f)}.
```

Since `ell_f<=2`, every nonzero summand is exactly one copy:

```math
\boxed{
R_{\rm latent-latent}
=
\sum_{f\in\mathcal D_{BM}}
\frac1{D(f)},
}
```

where `D_BM` is the set of parent pairs occurring latently in one retained backbone child and one retained middle child.

There is no higher-multiplicity coefficient.

---

## 6. Translated center and opposite reserves

Fix one middle-fiber child of selected step `d`, orientation `epsilon`, and sponsor-root set `Q`.

For every root

```math
p\in Q,
```

the parent contains the complete selected progression

```math
p,
\qquad
p+\varepsilon d,
\qquad
p+2\varepsilon d.
```

For one duplicated latent pair

```math
f=\{p,q\}\in\binom Q2,
```

define the center-copy pair

```math
C_d(f)
=
\{p+\varepsilon d,q+\varepsilon d\}
```

and opposite-copy pair

```math
O_d(f)
=
\{p+2\varepsilon d,q+2\varepsilon d\}.
```

Both are physical parent pairs and preserve the exact gap:

```math
D(C_d(f))
=
D(O_d(f))
=
D(f).
```

Therefore

```math
\boxed{
w(C_d(f))=w(O_d(f))=w(f).}
```

For one fixed middle fiber, both maps

```math
f\mapsto C_d(f),
\qquad
f\mapsto O_d(f)
```

are injective.

---

## 7. Local duplicate payment

Let

```math
\mathcal D_M
```

be the set of pairs duplicated between one fixed middle child and the backbone family. Then

```math
\sum_{f\in\mathcal D_M}\frac1{D(f)}
=
J(C_d(\mathcal D_M))
=
J(O_d(\mathcal D_M)).
```

Thus each middle-fiber duplicate family has two independently sufficient local parent-pair reserve copies.

These are alternative copies, not two simultaneously spendable payments.

---

## 8. Remaining global collision

Reserve pairs from different middle fibers may coincide physically. A center-copy reserve may also already be assigned to another parent-pair obligation.

Hence the local translated-copy theorem does not by itself close the whole-tree ledger. The remaining problem is substantially narrower:

```text
pack one copy of every backbone-middle duplicated pair
into the union of its center-copy or opposite-copy reserve,
while retaining production ownership and scale.
```

The input latent multiplicity is already bounded by two; only reserve projection collisions remain.

---

## 9. Exact examples

### Recorded retained chain through `F5`

Every recorded repeated parent resource has `ell_f=1`, so the genuine latent residual vanishes.

### Policy-compatible no-go

The parent in

```text
docs/lexicographic-retained-latent-reuse-no-go.md
```

has three duplicated pairs between one recursive middle child and one recursive backbone child. Each has `ell_f=2`, attaining the theorem's bound.

---

## 10. Strategic consequence

The coordinated deletion architecture eliminates the unbounded latent multiplicity present in unrestricted full-edge branching.

The active pair-activation obstruction is now a degree-two alternative-reserve packing problem, not an arbitrary multiplicity problem.
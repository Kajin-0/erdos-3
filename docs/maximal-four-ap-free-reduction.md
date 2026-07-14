# Maximal four-AP-free reduction

## Status

Standard maximality reduction for the fixed four-term case.

For completion terms arising inside a retained parent root set `P`, one must distinguish:

1. a completion root lying in the ambient counterexample but outside `P`;
2. a completion integer genuinely absent from the ambient counterexample.

Maximality applies only to the second class.

---

## 1. Reduction

Let `A\subseteq\mathbb N` be four-AP-free. Consider the partially ordered family

```math
\mathcal F
=
\{B\subseteq\mathbb N:A\subseteq B,\ B\text{ is four-AP-free}\},
```

ordered by inclusion.

If `\mathcal C\subseteq\mathcal F` is a chain, then

```math
U=\bigcup_{B\in\mathcal C}B
```

is four-AP-free. Indeed, any four-term arithmetic progression is finite, so if it were contained in `U`, all four of its points would lie in one sufficiently large member of the chain.

Therefore every chain has an upper bound in `\mathcal F`. By Zorn's lemma, `A` is contained in an inclusion-maximal four-AP-free set `A^{\max}`.

If

```math
\sum_{n\in A}\frac1n=\infty,
```

then automatically

```math
\sum_{n\in A^{\max}}\frac1n=\infty.
```

Hence, for the fixed four-term problem, it is sufficient to rule out divergent reciprocal sums for inclusion-maximal four-AP-free sets.

---

## 2. Saturation certificate

Let `B` be inclusion-maximal four-AP-free and let `x\notin B`. Then

```math
B\cup\{x\}
```

contains a four-term arithmetic progression. Since `B` itself is four-AP-free, that progression must contain `x`.

Thus every integer absent from `B` has a witness

```math
p,\ p+h,\ p+2h,\ p+3h,
\qquad h>0,
```

for which exactly one of the four displayed entries is `x` and the other three belong to `B`.

Fixing any deterministic ordering of witnesses gives a well-defined completion map

```math
x\longmapsto W(x).
```

---

## 3. Parent absence versus ambient absence

Let `P\subseteq B` be the root set of one retained affine parent. A completion calculation may produce

```math
c\notin P.
```

This has two distinct meanings.

### External ambient completion

```math
c\in B\setminus P.
```

Then `c` is a genuine ambient-set point that is absent only from the current parent lineage. It must be exported to an external-root, completion-support, or rectangle-transport ledger. Maximality supplies no new four-AP witness because `c` is not missing from `B`.

### Genuine ambient hole

```math
c\notin B.
```

Only in this case does maximality supply a four-AP witness with three points of `B`.

Therefore every parent-level missing-completion term must retain the trichotomy

```text
completion in P;
completion in B \ P;
completion outside B.
```

Collapsing the last two cases is invalid.

---

## 4. Application to residual-minimum star debt

In the residual-minimum star completion theorem, an unpaid backward star has

```math
c=2s-a\notin P
```

and contributes

```math
\frac1{s-a}
=
\frac2{c-a}.
```

For fixed `a`, the map

```math
s\longmapsto c=2s-a
```

is injective. Split its image as

```math
C_a^{\rm ext}
=
\{c:c\in B\setminus P\},
```

and

```math
C_a^{\rm hole}
=
\{c:c\notin B\}.
```

Then

```math
M_a(P)
=
M_a^{\rm ext}(P)
+
M_a^{\rm hole}(P),
```

where

```math
M_a^{\rm ext}(P)
=
\sum_{c\in C_a^{\rm ext}}\frac2{c-a},
```

and

```math
M_a^{\rm hole}(P)
=
\sum_{c\in C_a^{\rm hole}}\frac2{c-a}.
```

The external term is a lineage/export problem. The hole term is a maximality/completion-witness problem.

---

## 5. Witness-position decomposition for genuine holes

For each `c\in C_a^{\rm hole}`, the deterministic four-AP witness places `c` in one of four roles:

```text
role 0: c, c+h, c+2h, c+3h;
role 1: c-h, c, c+h, c+2h;
role 2: c-2h, c-h, c, c+h;
role 3: c-3h, c-2h, c-h, c.
```

The weighted hole ledger may be partitioned by:

1. witness role;
2. witness step `h`;
3. dyadic ratio between `h` and `c-a`;
4. whether `a` is one of the three witness points;
5. whether the witness lies in the same dyadic block as the parent or crosses a block boundary.

If `a` belongs to the witness, then

```math
c-a\in\{h,2h,3h\},
```

so

```math
\frac2{c-a}
\le
\frac2h.
```

Those terms are directly comparable with weighted four-AP witness incidence. The remaining terms are cross-anchor rectangle cases.

---

## 6. Remaining theorem

The correct completion-export target is

```math
M_a^{\rm ext}(P)
+
M_a^{\rm hole}(P).
```

The two terms require different mechanisms:

```math
M_a^{\rm ext}(P)
```

must be charged to ambient roots omitted from the current lineage, while

```math
M_a^{\rm hole}(P)
```

must be charged to maximality witnesses.

A complete inequality should have the form

```math
M_a(P)
\le
C\,\Phi_{\rm external}(P)
+
C\,\Phi_{\rm completion}(P)
+
C\,\Phi_{\rm rectangle}(P)
+
\text{summable boundary error},
```

with bounded reuse across the recursive tree.

The exact significance of maximality is therefore:

```text
genuine ambient holes always carry four-AP obstruction witnesses;
parent-external ambient roots require a separate provenance export.
```

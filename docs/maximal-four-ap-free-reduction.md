# Maximal four-AP-free reduction

## Status

Standard maximality reduction for the fixed four-term case, recorded here because it converts the missing-completion term in the sponsor-star inequality into genuine four-AP witness data.

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

Thus every missing integer has a witness

```math
p,\ p+h,\ p+2h,\ p+3h,
\qquad h>0,
```

for which exactly one of the four displayed entries is `x` and the other three belong to `B`.

Fixing any deterministic ordering of witnesses gives a well-defined completion map

```math
x\longmapsto W(x).
```

No missing integer lacks a completion witness.

---

## 3. Application to residual-minimum star debt

In the residual-minimum star completion theorem, an unpaid backward star has

```math
c=2s-a\notin P,
```

and contributes weight

```math
\frac1{s-a}
=
\frac2{c-a}.
```

When the ambient counterexample is taken inclusion-maximal, `c` has a four-AP completion witness with three ambient-set points.

The map

```math
s\longmapsto c=2s-a
```

is injective for fixed `a`. Therefore the missing-completion star mass becomes a weighted family of **distinct missing integers**, each carrying a genuine four-AP witness:

```math
M_a(P)
=
\sum_{c\in C_a}\frac2{c-a},
```

where

```math
C_a
=
\{2s-a:s\text{ is an unpaid close backward sponsor}\}.
```

This is precisely the type of object that can be exported to completion support or rectangle transport.

---

## 4. Witness-position decomposition

For each `c\in C_a`, the deterministic witness places `c` in one of four roles:

```text
role 0: c, c+h, c+2h, c+3h;
role 1: c-h, c, c+h, c+2h;
role 2: c-2h, c-h, c, c+h;
role 3: c-3h, c-2h, c-h, c.
```

The weighted missing-completion ledger can therefore be partitioned by:

1. witness role;
2. witness step `h`;
3. dyadic ratio between `h` and `c-a`;
4. whether `a` is one of the three witness points;
5. whether the witness lies in the same dyadic block as the parent or crosses a block boundary.

If `a` belongs to the witness, then

```math
c-a\in\{h,2h,3h\},
```

and consequently

```math
\frac2{c-a}
\le
\frac2h.
```

Those terms are directly comparable with weighted four-AP witness incidence. The remaining terms are the cross-anchor rectangle case.

---

## 5. Remaining theorem

Maximality does not by itself bound the total witness multiplicity: many missing integers may be completed by overlapping triples of ambient points.

The required next inequality is a weighted completion-export bound of the form

```math
\sum_{c\in C_a}\frac1{c-a}
\le
C\,\Phi_{\rm completion}(P)
+
C\,\Phi_{\rm rectangle}(P)
+
\text{summable boundary error},
```

with bounded reuse of each witness resource across the recursive tree.

The significance of the maximality reduction is narrower and exact:

```text
missing sponsor-star completions are never unsupported holes;
they always carry four-AP obstruction witnesses.
```

Thus the cross residual-sponsor star problem has been reduced to the already identified completion/rectangle transport frontier.

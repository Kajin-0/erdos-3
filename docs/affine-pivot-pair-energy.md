# Affine pivot forests and root-pair energy

## Status

Symbolic theorem for affine minimum-translation states. No arithmetic-progression hypothesis is required for the algebraic packing lemma.

The theorem does not bound the initial pair energy of a four-AP-free block. It identifies an exact treewise potential for any retained subtree whose states admit affine root coordinates and whose child root sets are pairwise disjoint.

---

## 1. Affine root coordinates

Let `P` be a finite set of integer root labels and let

```math
r<\min P.
```

Define the affine state

```math
S_r(P)
=
\{p-r:p\in P\}.
```

Let

```math
a=\min P.
```

The minimum current label is `a-r`. The minimum-translation backbone is

```math
\begin{aligned}
\mathcal B(S_r(P))
&=
\{(p-r)-(a-r):p\in P,\ p>a\}\\
&=
\{p-a:p\in P\setminus\{a\}\}\\
&=
S_a(P\setminus\{a\}).
\end{aligned}
```

Thus a pure backbone step is exactly the root-reference pivot

```math
\boxed{r\longrightarrow a.}
```

A surviving root `p` moves from current label

```math
p-r
```

to

```math
p-a.
```

Its harmonic gain is

```math
\boxed{
\frac1{p-a}-\frac1{p-r}
=
\frac{a-r}{(p-a)(p-r)}.
}
```

The associated harmonic interval is

```math
(p-a,p-r].
```

---

## 2. Exact retained-subset identity

Let `Q` be any retained subset of `P\setminus\{a\}`. Then

```math
H(S_a(Q))-H(S_r(P))
=
\sum_{p\in Q}
\left(
\frac1{p-a}-\frac1{p-r}
\right)
-
\sum_{p\in P\setminus Q}
\frac1{p-r}.
```

This is the root-coordinate form of survivor gain minus exiting parent release.

For multiple pairwise root-disjoint retained children

```math
Q_1,\ldots,Q_k
\subseteq
P\setminus\{a\},
```

the same identity holds after replacing `Q` by the disjoint union of the `Q_i`.

---

## 3. Root-pair energy

Define the reciprocal-difference pair energy

```math
\boxed{
J(P)
=
\sum_{x,y\in P:\ x<y}
\frac1{y-x}.
}
```

This potential depends only on original root labels. It is independent of the current affine reference.

Separating pairs incident to the minimum root `a` gives

```math
J(P)
=
\sum_{p\in P\setminus\{a\}}
\frac1{p-a}
+
J(P\setminus\{a\}).
```

The first term is exactly the harmonic mass of the full minimum-translation backbone.

---

## 4. Pair-energy Bellman inequality

Let

```math
Q_1,\ldots,Q_k
```

be pairwise disjoint subsets of `P\setminus\{a\}`. Then

```math
\boxed{
\sum_{i=1}^k
\left(
H(S_a(Q_i))+J(Q_i)
\right)
\le
J(P).
}
```

### Proof

For each child,

```math
H(S_a(Q_i))
=
\sum_{p\in Q_i}\frac1{p-a}.
```

These terms correspond to the root pairs

```math
(a,p),
\qquad p\in Q_i.
```

Because the `Q_i` are disjoint, no such pair is counted twice.

The terms in `J(Q_i)` correspond to unordered pairs with both endpoints in the same child root set. Again, pairwise disjointness of the `Q_i` prevents duplication. Every pair counted on the left is therefore a distinct pair from `P`, and all have weight `1/(y-x)`. Hence the left side is a sub-sum of `J(P)`.

---

## 5. Iterated affine pivot forest

Consider a rooted retained tree in which every node has affine state

```math
S_r(P),
```

uses the minimum root `a=min(P)` as its pivot, and emits children

```math
S_a(Q_1),\ldots,S_a(Q_k)
```

with pairwise disjoint root sets.

Applying the pair-energy Bellman inequality at every internal node gives a telescoping treewise bound:

```math
\boxed{
\text{total terminal harmonic mass}
+
\text{pair energy remaining at the frontier}
\le
J(P_{\rm root}).
}
```

Equivalently, every harmonic child term is charged to one root pair `(a,p)`, and every pair can be used at most once in the affine pivot forest.

This resolves cross-generation reuse **inside the affine root-pivot model**. It does not bound the root potential `J(P_root)` itself.

---

## 6. Relation to the minimum-translation reserve

For `a=min(P)` and current reference `r`, the one-step full translation reserve is

```math
A_r(P)
=
\sum_{p>a}
\left(
\frac1{p-a}-\frac1{p-r}
\right).
```

This is only the currently exposed minimum-star increment. The pair energy `J(P)` contains:

1. the complete current minimum star `1/(p-a)`;
2. every possible future pivot star among the remaining roots.

Therefore regeneration of `A` after a pivot is not mysterious. A new minimum exposes a different set of root pairs already stored in `J(P)`.

This explains why a current-state potential such as

```math
H+\kappa A
```

may fail even though the cumulative pair potential telescopes exactly.

---

## 7. What remains open

The affine pivot theorem transfers the whole-tree problem to a sharper initial-capacity question.

A complete proof still needs one of the following:

1. a summable bound for the pair energy entering affine recursive components;
2. a theorem charging large pair energy to terminal first appearance, completion, rectangle support, or cheap-extension exclusion;
3. a stronger restricted pair-energy bound for root sets produced by coordinated deletion;
4. a proof that non-affine recursive components terminate or export sufficient arithmetic obstruction before entering the affine regime.

The unrestricted estimate

```math
J(P)
\ll
H(S_r(P))
```

is false in general. Closely spaced root pairs can make `J(P)` much larger than current harmonic mass.

The active question is therefore not whether affine pivot reuse can be controlled. It can. The active question is:

```math
\boxed{
\text{how is the initial root-pair energy paid for?}
}
```

---

## 8. Application protocol

Before applying this theorem to a recorded retained frontier, verify exactly:

1. one common affine reference `r` for every point in each parent state;
2. the pivot root is the provenance root of the minimum current label;
3. every retained backbone child point satisfies `u'=p-a`;
4. child root sets are pairwise disjoint;
5. terminal and dropped roots are not silently reused elsewhere;
6. any non-affine child is separated and charged independently.

The finite `R_4 -> R_5` affine-root probe is designed to certify these hypotheses for the current adversarial frontier.

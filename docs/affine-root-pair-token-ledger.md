# Affine root-pair tokens and first-appearance capacity

## Status

Symbolic theorem for affine root-coordinate forests.

This note distinguishes two questions that were previously conflated:

1. whether two occurrences have the same detailed genealogy;
2. whether they consume the same harmonic pair resource.

Immediate provenance may be needed for the first question. It does not create a second copy of the resource in the second question.

---

## 1. Affine point identity

Let `P_0` be a fixed finite root universe. An affine state has the form

```math
S_r(P)=\{p-r:p\in P\},
\qquad
P\subseteq P_0,
\qquad
r\in P_0,
\qquad
r<\min P.
```

A current point carries:

```text
current label u = p-r
root provenance p.
```

Therefore

```math
\boxed{r=p-u.}
```

The coarse token

```math
\tau(u,p)=(u,p)
```

is equivalent to the ordered root-pair token

```math
\widehat\tau(u,p)=(p-u,p)=(r,p).
```

The correspondence is bijective on affine points. Its harmonic weight is

```math
\frac1u
=
\frac1{p-r}.
```

---

## 2. Global first-appearance bound

Let an arbitrary finite or locally finite affine forest be built from the same root universe `P_0`. States may overlap and the same affine point token may occur in multiple branches or generations.

Choose any deterministic total order on point occurrences and charge each coarse token only at its first appearance.

Because every first-appearance token corresponds to one distinct pair

```math
(r,p)\in\binom{P_0}{2},
```

we have

```math
\boxed{
\sum_{\text{first-appearance }(u,p)}\frac1u
\le
J(P_0),
}
```

where

```math
J(P_0)
=
\sum_{r<p,\ r,p\in P_0}\frac1{p-r}.
```

The same statement holds separately for terminal points, recursive points, or any selected point class.

### Proof

Map each first-appearance token `(u,p)` to `(p-u,p)`. Distinct coarse tokens give distinct ordered root pairs. The token weight equals the corresponding pair weight. Hence the first-appearance sum is a sub-sum of `J(P_0)`.

---

## 3. Meaning of a repeated coarse token

Suppose two occurrences share

```math
(u,p).
```

Then both have the same inferred affine reference

```math
r=p-u
```

and therefore correspond to the same root pair `(r,p)`.

For pair-capacity accounting, this is genuine resource reuse. The second occurrence cannot be assigned another weight `1/u` from root-pair energy.

The refined token

```math
(u,p,i)
```

may separate the two occurrence histories through different immediate provenances `i`. That distinction is genealogically real, but it does not produce a second root pair.

Thus:

```text
(u,p)       = capacity identity
(u,p,i)     = occurrence-history identity
```

They serve different purposes.

---

## 4. Pivot monotonicity along one lineage

In a minimum-pivot step

```math
S_r(P)\longrightarrow S_a(Q),
\qquad
r<a<\min Q,
```

a surviving root `p` changes token from

```math
(r,p)
```

to

```math
(a,p).
```

Since references strictly increase along a surviving affine lineage, the same pair token cannot recur on one lineage.

Any repeated coarse token must therefore arise from branch duplication, branch recombination, or regeneration of the same affine embedding elsewhere in the retained tree.

This isolates pair-token collisions as a direct measurement of non-treewise overlap.

---

## 5. Consequence for terminal accounting

The general first-appearance lemma in `docs/terminal-sink-first-appearance-ledger.md` remains correct for every fixed token map.

In the affine regime, the pair interpretation supplies the missing global union bound:

```math
\operatorname{TermSink}_{\rm first}
\le
J(P_0).
```

No global injectivity theorem for `(u,p,i)` is required to obtain this pair-capacity bound. A finer token may still be retained as metadata, but pair payment is attached to `(u,p)` only once.

---

## 6. Consequence for recursive accounting

The same first-appearance quotient can be applied to recursively continuing points. It gives

```math
\sum_{\text{first recursive pair appearances}}\frac1u
\le
J(P_0).
```

This does not immediately bound raw recursive occurrence mass, because repeated pair tokens may be emitted again. Define the pair-reuse mass as

```math
R_{\rm pair}
=
\sum_{\text{non-first pair occurrences}}\frac1u.
```

Then

```text
raw recursive mass
=
first-appearance pair mass
+
pair-reuse mass.
```

The next structural problem is to control `R_pair` by branch separation, pair multiplicity, terminalization, or arithmetic obstruction.

---

## 7. Relation to earlier token collisions

The recorded recurrence of a terminal token such as

```text
(60, 1354490)
```

has a direct pair interpretation:

```math
r=1354490-60=1354430,
```

so both occurrences use the same root pair

```math
(1354430,1354490).
```

Different immediate provenance separates their histories but does not separate their pair capacity.

This changes the interpretation of coarse-token collisions:

```text
not merely a failed signature
but an exact certificate of pair-resource reuse.
```

---

## 8. Open hypotheses

Application to the full retained program requires exact verification that:

1. every point being charged has an affine reference `r=p-u` in the designated root universe;
2. non-affine points are separated and charged through another mechanism;
3. the entering pair energy `J(P_0)` is itself paid by a parent potential or amortized production theorem;
4. pair-reuse mass is controlled without refining pair capacity into history-specific copies;
5. root-universe changes across non-affine transitions are explicit and provenance preserving.

The theorem does not claim that all recorded retained generations are affine. That is the purpose of the finite affine-frontier probes.

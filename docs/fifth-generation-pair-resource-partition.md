# Exact pair-resource partition at the fifth retained frontier

## Status

Exact finite theorem strengthening the numerical pair-energy row in `docs/fifth-generation-pair-energy-bellman-row.md`.

The result proves that the complete fifth retained output is not merely smaller in total pair-energy mass. Every fifth current-point resource and every fifth latent recursive pair is a distinct member of the fourth-generation affine pair-resource universe.

No sixth generation is constructed.

Primary files:

- `src/probe_pair_resource_ownership.py`;
- `src/verify_pair_resource_ownership.py`;
- `data/pair_resource_ownership_certificate_2026-07-14.txt`.

---

## 1. Parent resource universe

For an affine fourth-generation parent state

```math
S_r(P)=\{p-r:p\in P\},
```

define two resource classes.

### Current pairs

Each current point `p-r` uses the pair

```math
(r,p)
```

of weight

```math
\frac1{p-r}.
```

The twelve fourth recursive parents have

```text
1,717 current pairs.
```

Their total weight is exactly

```math
H(R_4)=1.536133538213\ldots.
```

### Latent pairs

Every unordered pair

```math
(x,y),
\qquad x<y,
\qquad x,y\in P
```

is a latent pivot resource of weight `1/(y-x)`.

The fourth recursive family has

```text
370,505 latent pairs.
```

Their total weight is

```math
J(R_4)=2743.858245303490\ldots.
```

### Complete parent universe

The complete fourth resource universe therefore contains

```text
372,222 pair tokens
```

with exact mass

```math
H(R_4)+J(R_4)
=2745.394378841703\ldots.
```

Every parent resource token has multiplicity one.

---

## 2. Fifth resource usage

The complete fifth retained family uses:

```text
1,032 current-point pairs
106,381 recursive latent pairs
107,413 total pair resources.
```

The current-point resources split as:

```text
17 terminal current pairs
1,015 recursive current pairs.
```

Every fifth resource token has multiplicity one.

The exact total used mass is

```math
H(F_5)+J(R_5^{\rm rec})
=1586.466623468978\ldots.
```

---

## 3. Exact containment theorem

Every fifth current pair and every fifth recursive latent pair belongs to the fourth parent resource universe.

More strongly, all fifth resources come from fourth **latent** pairs:

| fifth resource class | from fourth current | from fourth latent |
|---|---:|---:|
| terminal current | `0` | `17` |
| recursive current | `0` | `1,015` |
| recursive latent | `0` | `106,381` |

Thus:

```math
\boxed{
\mathcal R(F_5)
\subseteq
\mathcal J(R_4),
}
```

where `R(F_5)` is the complete current-plus-future fifth resource set and `J(R_4)` is the fourth latent pair set.

The fifth family does not consume any fourth current pair.

---

## 4. Exact disjointness theorem

No fifth pair resource is used twice:

```text
maximum fifth pair multiplicity = 1
repeated fifth pair-resource mass = 0.
```

Consequently, occurrence-valued and union-valued resource mass agree exactly.

This proves that numerical overlap, provenance overlap, and terminal-recursive interaction have all been resolved at the pair-resource level on this transition.

---

## 5. Exact partition

The fourth resource universe splits into:

```text
107,413 used fifth resources
264,809 unused fourth resources.
```

Their masses are:

```text
used   = 1586.466623468978...
unused = 1158.927755372724...
total  = 2745.394378841703...
```

and satisfy the exact identity

```math
\boxed{
\operatorname{Used}(F_5)
+
\operatorname{Unused}(R_4\to F_5)
=
H(R_4)+J(R_4).
}
```

The used fraction is

```math
\frac{1586.466623468978\ldots}
     {2745.394378841703\ldots}
=0.577864745297\ldots.
```

---

## 6. Strengthened Bellman statement

The semantic resource theorem gives

```math
\boxed{
H(F_5)+J(R_5^{\rm rec})
+
U_{4\to5}
=
H(R_4)+J(R_4),
}
```

where

```math
U_{4\to5}
=1158.927755372724\ldots
```

is the exact unused pair-resource mass.

Since all fifth resources come from fourth latent pairs, one also has the stronger inequality

```math
H(F_5)+J(R_5^{\rm rec})
\le
J(R_4),
```

proved numerically and by explicit pair containment.

---

## 7. Consequences

This theorem establishes all of the following on the recorded transition:

1. a concrete pair-resource universe;
2. exact child-to-parent token ownership;
3. no repeated payment;
4. exact terminal and recursive coexistence;
5. exact unused-capacity export;
6. a legitimate set-valued Bellman identity.

The pair-energy row is therefore structurally valid, not merely a successful scalar comparison.

---

## 8. Remaining frontier

The same ownership test must now be moved backward to earlier retained transitions.

The relevant failure modes are:

- non-affine child states;
- repeated root pairs across state occurrences;
- current pair tokens recurring from earlier generations;
- a child resource absent from its parent resource universe;
- one pair token used simultaneously by multiple children;
- pair-universe changes under middle-fiber output.

The next exact targets are:

```text
R1 -> F2
R2 -> F3
R3 -> F4.
```

The goal is to locate the earliest transition where exact pair-resource containment and disjointness become valid, and to isolate the finite non-affine/reuse prefix that precedes it.

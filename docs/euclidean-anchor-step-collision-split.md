# Euclidean anchor-step collision split

## Status

Exact aspect-weighted refinement of anchor-pair step-fiber duality.

Every repeated fixed-step incidence has two positive gaps:

```text
progression step d;
anchor separation delta.
```

The incidence transfers to the smaller gap with coefficient at most one. The
larger gap strictly decreases. This gives a Euclidean path coordinate for root
three-AP multiplicity.

---

## 1. Collision incidence matrix

Let `B subseteq [N,2N)` be four-AP-free. For each step `d`, put

```math
P_d=\{p:p,p+d,p+2d\in B\},
\qquad
a_d=\min P_d.
```

The nonbase collision incidences are

```math
\mathcal I(B)
=
\{(d,p):p\in P_d\setminus\{a_d\}\}.
```

For one incidence define

```math
\delta=p-a_d.
```

Its collision weight is `1/d`.

The total fixed-step excess is

```math
R_{\rm step}(B)
=
\sum_{(d,p)\in\mathcal I(B)}\frac1d.
```

---

## 2. Near and far rectangles

Partition the incidence set into

```math
\mathcal I_{\rm near}
=
\{(d,p):\delta\le d\}
```

and

```math
\mathcal I_{\rm far}
=
\{(d,p):d<\delta\}.
```

### Near incidence

If `delta<=d`, then

```math
\boxed{
\frac1d
=
\frac\delta d\frac1\delta,
\qquad
0<\frac\delta d\le1.
}
```

The incidence transfers to the smaller anchor gap `delta` with aspect
coefficient `delta/d`.

### Far incidence

If `d<delta`, retain the smaller step gap itself:

```math
\boxed{
\frac1d
=1\cdot\frac1d.
}
```

In both cases the target gap is

```math
\boxed{g'=\min(d,\delta)}
```

and the coefficient is at most one.

The rectangle diameter

```math
g=\max(d,\delta)
```

strictly decreases:

```math
g'<g.
```

---

## 3. Four-AP-free output sets

For each fixed step `d`, define the near anchor-difference set

```math
A_d^{\rm near}
=
\{p-a_d:(d,p)\in\mathcal I_{\rm near}\}.
```

It is a subset of the translated anchor set `P_d-a_d`, hence is
four-AP-free.

For each canonical anchor pair

```math
f=\{a,p\},
```

define the far step fiber

```math
S_f^{\rm far}
=
\{d:a_d=a,\ p\in P_d,\ d<p-a\}.
```

It is a subset of the four-AP-free step fiber `S_f`, hence is four-AP-free.

Both families lie strictly below the original block scale. After standard
dyadic resolution, every shell has base at most `N/4`.

---

## 4. Exact aspect-weighted identity

The collision excess decomposes exactly as

```math
\boxed{
R_{\rm step}(B)
=
\sum_d
\sum_{\delta\in A_d^{\rm near}}
\frac\delta d\frac1\delta
+
\sum_fH(S_f^{\rm far}).
}
```

Dropping the near coefficients gives the unweighted upper bound

```math
\boxed{
R_{\rm step}(B)
\le
\sum_dH(A_d^{\rm near})
+
\sum_fH(S_f^{\rm far}).
}
```

The exact form is stronger: no collision occurrence creates more than one unit
of harmonic target weight before numerical deduplication.

---

## 5. Integer-gap termination

Iterate only the collision transfer, ignoring new arithmetic branching. Every
incidence carries an ordered pair of positive integer gaps `(d,delta)` and
moves to the smaller one.

Since

```math
\min(d,\delta)<\max(d,\delta),
```

no collision-transfer lineage can cycle. Every lineage terminates after fewer
than

```math
\log_2 g_0+O(1)
```

dyadic aspect changes if each step is grouped by its dyadic maximum gap, and
after at most `g_0-1` literal integer decreases without grouping.

The product of aspect coefficients along a near-transfer lineage is at most
one.

This is a pathwise nonamplification theorem for collision transfer. It does
not by itself control the number of arithmetic branches that may later emerge
from the transferred four-AP-free sets.

---

## 6. Bipartite transpose interpretation

Let the left vertices be numerical steps `d` and the right vertices be
canonical anchor pairs `f`. Each collision incidence is one weighted edge.

The near/far rule orients the edge toward the endpoint carrying the smaller
numerical gap:

```text
anchor separation delta <= d: orient to f;
step d < delta:               orient to d inside S_f.
```

The oriented edge weight is the original `1/d`, represented either as

```math
(\delta/d)\cdot(1/\delta)
```

or as `1/d`.

Thus the collision matrix admits an exact Euclidean orientation into
lower-scale four-AP-free row and column fibers.

---

## 7. Unified recursive interface

Every output set in the split:

1. is four-AP-free;
2. lies at strictly lower dyadic scale;
3. inherits exact provenance from one collision incidence;
4. can be parity-resolved into valid side-oriented full-edge inputs;
5. carries an aspect coefficient at most one.

The active whole-tree problem is now isolated to numerical overlap between
these output fibers after different collision incidences are merged. There is
no pathwise amplification and no unidentified source of occurrence
multiplicity.

A complete theorem needs a first-appearance ledger for the oriented gap token

```math
(g',\text{source rectangle},\text{aspect band}),
```

showing that numerical reuse across different Euclidean fibers either merges
into one physical pair capacity or creates another strictly descending
rectangle token.

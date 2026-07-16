# Row-star branching as state-pair overlap energy

## Status

State-independent reduction for the remaining branching term after point-disjoint affine retention.

Repeated use of one parent pair by several retained children can be assigned to ordered pairs of child states. For recursive affine children, the complete parent-resource overlap of two states is exactly the pair energy of their common augmented-root set.

---

## 1. Augmented root set

Let one affine child state be

```math
S_i=\{\sigma_i(p-r_i):p\in Q_i\}.
```

Define its augmented root set

```math
A_i=\{r_i\}\cup Q_i.
```

If the child is recursive, its complete parent resource universe consists of:

```text
current pairs {r_i,p}, p in Q_i;
latent pairs binom(Q_i,2).
```

Therefore

```math
\boxed{
\mathcal U_i=\binom{A_i}{2}.
}
```

For a terminal child whose latent pair energy is not propagated, retain only the current star

```math
\mathcal U_i^{\rm term}
=\{\{r_i,p\}:p\in Q_i\}.
```

---

## 2. Exact overlap of two recursive children

For two recursive children,

```math
\mathcal U_i\cap\mathcal U_j
=
\binom{A_i}{2}\cap\binom{A_j}{2}.
```

A pair belongs to both complete graphs exactly when both endpoints belong to both augmented root sets. Hence

```math
\boxed{
\mathcal U_i\cap\mathcal U_j
=
\binom{A_i\cap A_j}{2}.
}
```

Its complete reciprocal-gap mass is

```math
\boxed{
J(\mathcal U_i\cap\mathcal U_j)
=
J(A_i\cap A_j).
}
```

The common augmented-root set is a subset of the four-AP-free parent root universe and is therefore four-AP-free.

---

## 3. Terminal mixed overlaps

If one child is terminal, its resource universe is a star. Thus

```math
\mathcal U_i^{\rm term}\cap\mathcal U_j
\subseteq
\binom{A_i\cap A_j}{2}.
```

The same upper bound holds for two terminal children. Consequently, for arbitrary retained affine children,

```math
\boxed{
J(\mathcal U_i\cap\mathcal U_j)
\le
J(A_i\cap A_j),
}
```

with equality for a recursive-recursive pair.

---

## 4. Assigning row-star branching excess

Assume the numerical child resource families are point-disjoint, so the owner graph is a row-star forest.

For every repeated parent resource `f`, let

```math
I(f)=\{i:f\in\mathcal U_i\}
```

be its child-owner set. Choose one deterministic base owner

```math
i_0(f)=\min I(f).
```

For every other owner `j in I(f)\setminus {i_0(f)}`, create the state-pair overlap token

```math
\Theta(f,j)
=
(f,i_0(f),j).
```

The map from nonbase row-star leaves to these tokens is injective. Therefore the complete branching excess is exactly

```math
\boxed{
R_{\rm branch}
=
\sum_f\sum_{j\in I(f)\setminus\{i_0(f)\}}
\frac1{D(f)}.
}
```

---

## 5. Pairwise overlap envelope

For one unordered state pair `{i,j}`, collect all resources assigned between them:

```math
\mathcal O_{ij}
=
\{f:\Theta(f,j)\text{ or }\Theta(f,i)\text{ uses }\{i,j\}\}.
```

Then

```math
\mathcal O_{ij}
\subseteq
\mathcal U_i\cap\mathcal U_j.
```

Hence

```math
\sum_{f\in\mathcal O_{ij}}\frac1{D(f)}
\le
J(A_i\cap A_j).
```

Summing over state pairs gives the universal envelope

```math
\boxed{
R_{\rm branch}
\le
\sum_{i<j}J(A_i\cap A_j).
}
```

This inequality is generally not exact because a resource with `m` owners contributes only `m-1` branching tokens but appears in `binom(m,2)` pairwise intersections.

---

## 6. Reference-pair interpretation

The state pair `{i,j}` has reference pair

```math
\{r_i,r_j\}
```

and reference separation

```math
\delta_{ij}=|r_i-r_j|.
```

Every assigned common resource `f` of gap `D(f)` gives the exact rectangle identity

```math
\frac1{D(f)}
=
\frac{\delta_{ij}}{D(f)}
\frac1{\delta_{ij}}.
```

Therefore the complete branching mass assigned to one state pair is

```math
\boxed{
\sum_{f\in\mathcal O_{ij}}\frac1{D(f)}
=
\left(
\sum_{f\in\mathcal O_{ij}}
\frac{\delta_{ij}}{D(f)}
\right)
\frac1{\delta_{ij}}.
}
```

The coefficient is the total rectangle-aspect exposure of the common resource set.

For a recursive-recursive state pair, the largest possible assigned resource set is exactly

```math
\binom{A_i\cap A_j}{2}.
```

Thus reuse of one reference-pair token is pair energy of a common augmented-root intersection, not anonymous multiplicity.

---

## 7. State-overlap graph

Define a graph on retained affine child states by joining `i` and `j` when

```math
|A_i\cap A_j|\ge2.
```

Weight the edge by

```math
\Omega_{ij}=J(A_i\cap A_j).
```

The preceding theorem places the entire row-star branching excess under this weighted state-overlap graph:

```math
R_{\rm branch}
\le
\sum_{ij}\Omega_{ij}.
```

The exact assigned version replaces `Omega_ij` by the smaller mass of `O_ij`.

---

## 8. Exact `S7` interface

`src/probe_s7_affine_owner_incidence_graph.py` records every row-star rectangle occurrence. The next exact refinement should group those rows by state pair and compare:

```text
assigned branching mass;
complete overlap mass J(A_i intersection A_j);
reference-pair occurrence and union mass;
maximum overlap-set size;
state-overlap graph cycle rank.
```

This will determine whether the certified frontier is controlled by sparse pairwise overlap or requires higher-order common-root incidence.

---

## 9. Remaining theorem

The global problem after point-disjoint retention is reduced from pair multiplicity to weighted intersections of augmented root sets.

A closing theorem may take one of the following forms:

1. a packing bound for `sum J(A_i intersection A_j)`;
2. a scale-weighted bound using the reference separation `delta_ij`;
3. a higher-order inclusion-exclusion potential for resources shared by three or more states;
4. a terminal-release theorem for overlap edges whose child states stop.

The important reduction is exact: row-star branching is common-root pair energy.
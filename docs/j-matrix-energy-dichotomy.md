# J-matrix energy dichotomy

## Status

Local matrix lemma.  This note continues the load-regular pair-fiber branch by making the shifted-interaction energy test precise.

The goal is not yet to extract a density increment.  The goal is to decide whether the shifted-interaction matrix

```math
J(d,e)=|P_d\cap(P_e-2e)|
```

contains usable concentration.  If it does, the next object is a dense direction graph.  If it does not, the literal missing diagonal `J(d,d)=0` is provably invisible to this level of analysis.

## Setup

Let `D` be a popular direction set with

```math
K=|D|.
```

For `d,e in D`, define

```math
J(d,e)=|P_d\cap(P_e-2e)|
=|\{x:x,x+d,x+2e,x+3e\in A\}|.
```

The 4AP-free condition gives

```math
J(d,d)=0
\qquad(d\ne0).
```

Let

```math
T_J=\sum_{d,e\in D}J(d,e),
\qquad
\mathcal E_J=\sum_{d,e\in D}J(d,e)^2.
```

In the random heuristic,

```math
T_J\approx \alpha^4K^2N,
\qquad
\mathcal E_J\approx K^2\alpha^8N^2.
```

## Universal lower bound

By Cauchy--Schwarz,

```math
\mathcal E_J
=\sum_{d,e}J(d,e)^2
\ge
\frac{T_J^2}{K^2}.
```

Equality corresponds to `J(d,e)` being essentially constant over `D x D`.

Thus the normalized concentration parameter is

```math
\kappa_J=
\frac{K^2\mathcal E_J}{T_J^2}.
```

Always

```math
\kappa_J\ge1.
```

The pseudorandom matrix branch is `kappa_J=O(1)`.  The concentrated branch is `kappa_J>>1`.

## High-energy consequence

Assume

```math
\kappa_J\ge M
```

for some `M>1`.  Then the mass of `J` is not uniformly distributed.

A crude but useful form is:

```math
\max_{d,e}J(d,e)
\ge
\frac{\mathcal E_J}{T_J}
=
\kappa_J\frac{T_J}{K^2}.
```

Thus high energy gives at least one direction pair with shifted interaction larger than the average by a factor `kappa_J`.

This single-pair conclusion is too weak for iteration, but it is the first concentration certificate.

## Dyadic concentration graph

A more useful statement is obtained by dyadic pigeonholing.

Let

```math
\mu_J=\frac{T_J}{K^2}
```

be the average matrix entry.  Decompose entries according to dyadic levels

```math
2^r\mu_J\le J(d,e)<2^{r+1}\mu_J.
```

Since

```math
\sum_{d,e}J(d,e)^2=\mathcal E_J,
```

there exists a level `r` such that the edge set

```math
\mathcal G_r=\{(d,e):2^r\mu_J\le J(d,e)<2^{r+1}\mu_J\}
```

satisfies

```math
|\mathcal G_r|(2^r\mu_J)^2
\gtrsim
\frac{\mathcal E_J}{\log N_*},
```

where `N_*` is the relevant dynamic range of possible nonzero `J(d,e)` values.

Equivalently,

```math
|\mathcal G_r|
\gtrsim
\frac{\kappa_J K^2}{2^{2r}\log N_*}.
```

The `J`-mass carried by this graph is at least

```math
\sum_{(d,e)\in\mathcal G_r}J(d,e)
\gtrsim
\frac{\kappa_J}{2^r\log N_*}T_J.
```

Thus high matrix energy yields a direction graph whose edges carry above-average shifted interactions.

## Interpretation of an edge

An edge `(d,e)` in `G_r` means there are many `x` with

```math
x,\quad x+d,\quad x+2e,\quad x+3e
\in A.
```

This is a four-point corner-like configuration with two directions `d` and `e`.

When `d=e`, it is exactly a 4AP and is forbidden.  Large off-diagonal `J(d,e)` means many approximate or skew 4AP shadows survive.

Therefore a dense graph of large `J(d,e)` edges should be treated as structured information, not noise.

## Near-minimal energy branch

If

```math
\kappa_J=O(1),
```

then `J` has near-minimal second moment.  In that branch, the matrix is spread out at the level seen by first and second moments.

The missing diagonal has scale about

```math
K\mu_J
```

while the full mass is

```math
K^2\mu_J.
```

So the relative deficit remains only

```math
1/K.
```

No contradiction follows from the diagonal deletion unless additional structure creates many more depleted entries.

This formally records the pseudorandom `J` obstruction.

## Relation to direction structure

The graph `G_r` has vertex set `D` and directed edges `(d,e)` with many configurations

```math
x,x+d,x+2e,x+3e\in A.
```

If this graph has high edge density and high codegrees, a dependent-random-choice step may produce a subset `D_0 subset D` such that many pairs in `D_0` have many common `J`-neighbors.

Such common-neighbor structure is a possible route to additive structure in directions.  Schematically,

```math
\mathcal E_J\text{ large}
\Rightarrow
\text{dense weighted direction graph}
\Rightarrow
\text{DRC/BSG candidate}
\Rightarrow
\text{direction structure or coherent subsystem}.
```

This is not yet proved, but it identifies the next combinatorial object.

## Physical-space expansion of the energy

The energy has an exact point-count interpretation:

```math
\mathcal E_J
=
|\{x,y,d,e:
 x,x+d,x+2e,x+3e\in A,
 y,y+d,y+2e,y+3e\in A\}|.
```

Writing `h=y-x`, this becomes a count of two translated copies of the same skew 4-point pattern:

```math
x,x+d,x+2e,x+3e,
\qquad
x+h,x+h+d,x+h+2e,x+h+3e
\in A.
```

Thus high `J`-energy is a repeated-pattern statistic.  It should be convertible into either direction structure or a density increment after another Cauchy--Schwarz / DRC step.

## Matrix dichotomy

The local dichotomy is:

### Branch 1: J-energy concentration

If

```math
\mathcal E_J\ge M\frac{T_J^2}{K^2}
```

with `M>>1`, then there exists a dyadic direction graph `G_r` carrying above-average shifted interactions.  This graph is the next object for graph-BSG or DRC.

### Branch 2: J-energy regularity

If

```math
\mathcal E_J\le C\frac{T_J^2}{K^2},
```

then the shifted-interaction matrix is second-moment regular.  At this level, the forbidden diagonal `J(d,d)=0` is invisible unless one can generate a larger depleted relation

```math
\mathcal R\subseteq D\times D
```

with

```math
|\mathcal R|\gg K.
```

## Immediate next task

Work in Branch 1 and try to extract structure from the dense weighted direction graph `G_r`.

If that fails, the remaining path is a stronger sifting mechanism that creates many depleted near-diagonal relations, not merely the literal diagonal.

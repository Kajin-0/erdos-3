# Primitive weighted extension incidence

## Status

Exact one-generation compatibility theorem for harmonic primitive extraction.

Let a dyadic block

```math
B=A\cap[N,2N)
```

lie inside a 4-AP-free set `A`.  Every three-term progression in `B` has a forbidden predecessor `p`, and the corresponding step fiber

```math
D_p=\{d\ge1:p+d,p+2d,p+3d\in B\}
```

belongs to the hereditary three-dilate class.  Applying multiplicative-chain primitive extraction independently in every row `D_p` preserves at least one third of the step-weighted extension load.

The retained incidences also have a dual column structure: for every retained step `s`, its predecessor set `Q_s` is 4-AP-free and its three translates by `s,2s,3s` are pairwise disjoint subsets of `B`.

This produces an exact bipartite primitive-incidence system carrying total weight linear in the dyadic block density.

## Dyadic setup

Let

```math
B=A\cap[N,2N),
\qquad
|B|=\alpha N,
```

where `A subseteq N` has no nontrivial four-term arithmetic progression.

For an integer `p`, define

```math
D_p
=
\{d\ge1:p+d,p+2d,p+3d\in B\}.
```

Every `d in D_p` satisfies

```math
1\le d\le N/2,
```

and every relevant predecessor lies in

```math
N/2\le p<2N.
```

The three affine copies

```math
p+D_p,
\qquad
p+2D_p,
\qquad
p+3D_p
```

are subsets of `B`.  Hence

```math
D_p\cup2D_p\cup3D_p
```

is 4-AP-free.

## Step-weighted extension load

Define

```math
\mathcal L(B)
=
\sum_p\sum_{d\in D_p}\frac1d.
```

The map

```math
(p,d)
\longmapsto
(p+d,p+2d,p+3d)
```

is a bijection between the incidences counted by `mathcal L(B)` and nontrivial three-term arithmetic progressions in `B`, with weight equal to the reciprocal of the common difference.

Let

```math
T_3(B)
=
|\{(y,d):d\ge1,\ y,y+d,y+2d\in B\}|.
```

Since every such common difference satisfies `d<=N/2`,

```math
\frac1d\ge\frac2N.
```

Therefore

```math
\boxed{
\mathcal L(B)
\ge
\frac{2}{N}T_3(B).
}
```

The deletion bound

```math
T_3(B)\ge |B|-r_3(N)
```

gives

```math
\boxed{
\mathcal L(B)
\ge
2\left(
\alpha-\frac{r_3(N)}N
\right).
}
```

Thus the step-weighted extension load is linear in the block density, up to the Roth error.

## Primitive extraction in every predecessor row

For each `p`, apply the multiplicative-chain map inside `D_p`:

```math
d\longmapsto
\begin{cases}
3d,&3d\in D_p,\\[2pt]
3d/2,&3d\in2D_p.
\end{cases}
```

Let

```math
S_p\subseteq D_p
```

be the set of initial vertices of its chain components.

The harmonic primitive extraction theorem gives

```math
\sum_{d\in D_p}\frac1d
\le
3\sum_{s\in S_p}\frac1s.
```

Define the retained primitive load

```math
\mathcal P(B)
=
\sum_p\sum_{s\in S_p}\frac1s.
```

Summing over `p` yields

```math
\boxed{
\mathcal P(B)
\ge
\frac13\mathcal L(B)
\ge
\frac23\left(
\alpha-\frac{r_3(N)}N
\right).
}
```

For each row `p`, primitive extraction also gives

```math
S_p,
\qquad
2S_p,
\qquad
3S_p
```

pairwise disjoint, while

```math
p+S_p,
\qquad
p+2S_p,
\qquad
p+3S_p
```

remain subsets of `B`.

Hence a fixed positive fraction of the harmonic step load survives in rows with exact three-branch disjointness.

## Primitive incidence relation

Define the retained bipartite incidence set

```math
\mathcal R(B)
=
\{(p,s):s\in S_p\}.
```

Then

```math
\mathcal P(B)
=
\sum_{(p,s)\in\mathcal R(B)}\frac1s.
```

For a fixed retained step `s`, define its predecessor column

```math
Q_s
=
\{p:(p,s)\in\mathcal R(B)\}.
```

Double counting gives the dual identity

```math
\boxed{
\mathcal P(B)
=
\sum_s\frac{|Q_s|}{s}.
}
```

## Column 4-AP-freeness

Every `Q_s` is 4-AP-free.

Indeed, if

```math
p,\ p+r,\ p+2r,\ p+3r\in Q_s
```

with `r ne 0`, then the first affine branch gives

```math
p+s,\ p+s+r,\ p+s+2r,\ p+s+3r\in B,
```

a nontrivial four-term arithmetic progression.

Therefore

```math
\boxed{Q_s\text{ is 4-AP-free for every retained step }s.}
```

## Pairwise-disjoint translated columns

For every retained step `s`, the three translates

```math
Q_s+s,
\qquad
Q_s+2s,
\qquad
Q_s+3s
```

are pairwise disjoint subsets of `B`.

They are subsets of `B` by the definition of `Q_s`.  Suppose two translated points coincide:

```math
p_1+is=p_2+js,
\qquad
i,j\in\{1,2,3\}.
```

If `p_1 ne p_2`, then

```math
|p_1-p_2|\in\{s,2s\}.
```

If `p_2=p_1+s`, the two triples with predecessors `p_1,p_2` contain

```math
p_1+s,\ p_1+2s,\ p_1+3s,\ p_1+4s,
```

which is a 4-AP in `B`.

If `p_2=p_1+2s`, their union contains

```math
p_1+2s,\ p_1+3s,\ p_1+4s,\ p_1+5s,
```

again a 4-AP.

Both cases are impossible.  Hence

```math
\boxed{
Q_s+s,\ Q_s+2s,\ Q_s+3s
\text{ are pairwise disjoint subsets of }B.
}
```

In particular,

```math
\boxed{3|Q_s|\le |B|.}
```

Since `Q_s` lies in an interval of length at most `3N/2`, one also has

```math
|Q_s|\le r_4(3N/2).
```

Thus

```math
\boxed{
|Q_s|
\le
\min\left\{
\frac{|B|}{3},
\ r_4(3N/2)
\right\}.
}
```

## Row-column symmetry

The retained incidence relation has two complementary forms of rigidity.

### Fixed predecessor row

For each `p`,

```math
S_p,\ 2S_p,\ 3S_p
```

are pairwise disjoint and their common translate by `p` lies in `B`.

### Fixed step column

For each `s`,

```math
Q_s+s,\ Q_s+2s,\ Q_s+3s
```

are pairwise disjoint subsets of `B`, and `Q_s` itself is 4-AP-free.

Hence the primitive incidence system is rigid in both coordinates.  It is not an arbitrary collection of three-term progressions.

## Cross-scale divergence consequence

For dyadic blocks

```math
B_j=A\cap[2^j,2^{j+1}),
\qquad
|B_j|=\alpha_j2^j,
```

let `mathcal P_j` be the primitive load constructed above.  Then

```math
\boxed{
\mathcal P_j
\ge
\frac23\left(
\alpha_j-
\frac{r_3(2^j)}{2^j}
\right).
}
```

Using a quantitative Roth bound for which

```math
\sum_j\frac{r_3(2^j)}{2^j}<\infty,
```

one obtains

```math
\sum_j\alpha_j=\infty
\quad\Longrightarrow\quad
\boxed{\sum_j\mathcal P_j=\infty.}
```

Equivalently, a hypothetical 4-AP-free set with divergent reciprocal sum must generate infinite primitive incidence weight

```math
\sum_j\sum_s\frac{|Q_{j,s}|}{s}=\infty,
```

where every row has pairwise-disjoint dilates and every column has pairwise-disjoint translates.

## Remaining bottleneck

The primitive extraction is now compatible with all predecessor fibers at one generation and retains the required linear harmonic scale.

What remains is a global packing theorem for the incidence relation:

> Bound the total weighted size of a family `mathcal R(B)` for which every predecessor row has primitive three-dilate structure and every step column has three pairwise-disjoint translates inside one 4-AP-free block.

A bound that is summable across dyadic scales would close the cross-scale branch.  A weaker structure theorem separating high row overlap from high column overlap would still provide a concrete next dichotomy.
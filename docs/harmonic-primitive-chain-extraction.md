# Harmonic primitive chain extraction

## Status

Infinite-set consequence of the multiplicative-chain decomposition.

The logarithmic third-dilate expansion bound can be nearly saturated by long increasing multiplicative chains.  Such chains do not threaten the reciprocal-sum problem: each chain has finite reciprocal mass dominated by its first vertex.

The exact conclusion is:

> For any positive-integer set `D` with `D cap 2D = emptyset`, there is a subset `S subseteq D` containing the initial vertex of every `(3,3/2)` chain such that
> ```math
> \sum_{d\in D}\frac1d
> \le
> 3\sum_{s\in S}\frac1s.
> ```
> Hence reciprocal divergence passes to a subset with no internal ratios `3` or `3/2`.

When `D union 2D union 3D` is 4-AP-free, the extracted subset remains in the same three-dilate class.

## Infinite chain graph

Let

```math
D\subseteq\mathbb N
```

satisfy

```math
D\cap2D=\varnothing.
```

Define

```math
C=\{d\in D:3d\in D\cup2D\}
```

and, for `d in C`,

```math
\phi(d)=
\begin{cases}
3d,&3d\in D,\\[3pt]
3d/2,&3d\in2D.
\end{cases}
```

As before, `phi` is well-defined, injective, and satisfies

```math
\phi(d)\ge\frac32d>d.
```

Thus every connected component of the directed graph

```math
d\longrightarrow\phi(d)
```

is either a finite directed path or a one-sided infinite directed ray.

There are no cycles because values strictly increase.

## Every component has an initial vertex

Suppose a component had no initial vertex.  Starting from any `d_0` in that component, one could construct predecessors

```math
\cdots\longrightarrow d_{-2}\longrightarrow d_{-1}\longrightarrow d_0.
```

Every forward edge increases by at least `3/2`, so

```math
d_{-k}
\le
\left(\frac23\right)^k d_0.
```

For sufficiently large `k`, the right side is smaller than `1`, impossible for a positive integer.

Therefore every component has a unique initial vertex.

Let

```math
\mathcal S(D)
```

denote the set of these initial vertices.

## Reciprocal mass of a finite or infinite component

Let one component be

```math
d_0\longrightarrow d_1\longrightarrow d_2\longrightarrow\cdots,
```

where the path may terminate or continue indefinitely.

Since

```math
d_j\ge\left(\frac32\right)^j d_0,
```

we have

```math
\sum_j\frac1{d_j}
\le
\frac1{d_0}
\sum_{j\ge0}\left(\frac23\right)^j
=
\frac3{d_0}.
```

Summing over components gives

```math
\boxed{
\sum_{d\in D}\frac1d
\le
3\sum_{s\in\mathcal S(D)}\frac1s.
}
```

The statement is valid with either side infinite, by monotone convergence over finite truncations.

## Divergence survives primitive extraction

If

```math
\sum_{d\in D}\frac1d=\infty,
```

then necessarily

```math
\boxed{
\sum_{s\in\mathcal S(D)}\frac1s=\infty.
}
```

Thus long multiplicative chains can be removed without destroying reciprocal divergence: it is enough to keep one initial vertex from every chain.

## Ratio exclusions among initial vertices

The initial set has no two distinct elements in ratio `3` or `3/2`.

Indeed, if

```math
s_2=3s_1
```

with `s_1,s_2 in S(D)`, then `phi(s_1)=s_2`, so `s_2` has an incoming edge and is not initial.

Likewise, if

```math
s_2=\frac32s_1,
```

then

```math
3s_1=2s_2\in2D,
```

so again `phi(s_1)=s_2`.

Therefore

```math
\boxed{
\mathcal S(D)\cap3\mathcal S(D)=\varnothing
}
```

and

```math
\boxed{
2\mathcal S(D)\cap3\mathcal S(D)=\varnothing.
}
```

Together with `D cap 2D = emptyset`, this gives

```math
\boxed{
\mathcal S(D),\quad2\mathcal S(D),\quad3\mathcal S(D)
\text{ are pairwise disjoint}.
}
```

Hence

```math
\boxed{
|\mathcal S(D)\cup2\mathcal S(D)\cup3\mathcal S(D)|
=3|\mathcal S(D)|
}
```

for finite initial sets.

This is maximal third-dilate expansion, not merely the logarithmic lower bound.

## Preservation of the three-dilate 4-AP-free class

Assume additionally that

```math
D\cup2D\cup3D
```

is 4-AP-free.

Since

```math
\mathcal S(D)\subseteq D,
```

we have

```math
\mathcal S(D)
\cup2\mathcal S(D)
\cup3\mathcal S(D)
\subseteq
D\cup2D\cup3D.
```

Therefore

```math
\boxed{
\mathcal S(D)
\cup2\mathcal S(D)
\cup3\mathcal S(D)
\text{ is 4-AP-free}.
}
```

So primitive extraction remains inside the hereditary three-dilate class while upgrading the three dilates to pairwise disjointness.

## Primitive divergent reduction

Any divergent set in the three-dilate class admits a divergent subset `S` satisfying all of:

```math
S\cup2S\cup3S
\text{ is 4-AP-free},
```

```math
S,\ 2S,\ 3S
\text{ are pairwise disjoint},
```

and

```math
\sum_{s\in S}\frac1s=\infty.
```

This removes the near-minimal-expansion chain obstruction entirely at the cost of a factor at most `3` in reciprocal mass.

Equivalently, in the harmonic setting one may pass from a set whose third dilation is heavily absorbed to a divergent primitive subsystem where every third-dilate point is genuinely new.

## Relation to `(2,3)`-cores

Every multiplicative chain lies in one orbit

```math
\mathcal O_c
=
\{c2^a3^b:a,b\ge0\},
\qquad(c,6)=1.
```

The reciprocal mass of the entire orbit is

```math
\sum_{n\in\mathcal O_c}\frac1n=\frac3c.
```

The initial-set theorem gives a more local statement: even when one orbit contains many disconnected finite chain segments, all reciprocal mass is charged to their initial vertices.

Thus a divergent three-dilate set must continually create new multiplicative components whose initial vertices themselves have divergent reciprocal mass.

## Why this changes the recursion target

The previous stopping-time plan treated the logarithmic third-dilate slack as the only available gain.

For reciprocal divergence, that is unnecessarily pessimistic.  Long chains are summable and can be compressed to their starts.  After compression, the retained subsystem has exact expansion factor `3`:

```math
|S\cup2S\cup3S|=3|S|.
```

The next recursion should therefore distinguish:

1. **chain continuation:** harmonically chargeable to an earlier initial vertex;
2. **new chain start:** retained in the primitive subsystem and producing a genuinely disjoint third branch.

If primitive extraction can be made compatible with the predecessor-fiber tree, the formal branching factor may increase from the balanced binary value `2` to a genuinely supercritical value approaching `3` on the retained harmonic mass.

## Immediate next task

Prove a fiber-tree-compatible primitive extraction lemma:

> Select initial vertices in the child fibers so that a fixed positive fraction of the total reciprocal extension mass survives, while the selected first, second, and third affine branches are globally disjoint or have controlled overlap.

Such a lemma would replace the polylogarithmic third-branch gain by a constant-factor gain on the harmonically relevant part of the recursion.
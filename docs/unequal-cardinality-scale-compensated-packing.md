# Unequal-cardinality scale-compensated packing

## Status

Exact extension of the full componentwise scale-export theorem to arbitrary side and middle cardinalities.

The equal-cardinality assumption was not used in the component classification.  The full side-middle intersection graph is a forest on

```math
m+n
```

vertices, where

```math
m=|S|,
\qquad
n=|T|.
```

The same component credits therefore give the homogeneous estimate

```math
\boxed{
|A(S)\cup M_q(T)|
+
|T\cap[1,R)|
\ge
2+
\frac43(m+n)
-
\eta.
}
```

Here `0<=eta<=2` records possible coincidences of the two anchors with the opposite branch set.

If the middle set is itself restricted to the same shell

```math
T\subseteq[R,2R),
```

then the credit term vanishes and one obtains the direct shell-packing theorem

```math
\boxed{
|A(S)\cup M_q(T)|
\ge
2+
\frac43(|S|+|T|)
-
\eta.
}
```

No matching of the two cardinalities is needed.

## Setup

Let

```math
S\subseteq[R,2R)
```

be a coordinated side shell.  Let `T` be any finite subset of the paired selected middle child.  Put

```math
m=|S|,
\qquad
n=|T|.
```

Define

```math
A(S)=\{0\}\cup S\cup2S
```

and

```math
M_q(T)=\{q\}\cup(q-T)\cup(q+T).
```

The coordinated side construction gives

```math
S\cap2S=\varnothing.
```

Positivity gives

```math
(q-T)\cap(q+T)=\varnothing.
```

Consequently

```math
|S\cup2S|=2m,
\qquad
|(q-T)\cup(q+T)|=2n.
```

## Full intersection graph

Form the bipartite graph

```math
G=G_q(S,T)
```

with left vertex set `S`, right vertex set `T`, and an edge whenever

```math
cs=q\pm t,
\qquad
c\in\{1,2\}.
```

As in the full componentwise scale-export theorem:

1. each edge corresponds bijectively to one point of
   ```math
   (S\cup2S)\cap((q-T)\cup(q+T));
   ```
2. every vertex has degree at most two;
3. the graph is a forest of paths.

Let

```math
c(G)
```

be the number of connected components, including isolated vertices.  Since `G` is a forest on `m+n` vertices,

```math
\boxed{
|E(G)|=m+n-c(G).
}
```

Therefore the branch union has exact size

```math
\begin{aligned}
|(S\cup2S)\cup((q-T)\cup(q+T))|
&=2m+2n-|E(G)|\\
&=m+n+c(G).
\end{aligned}
```

Let

```math
0\le\eta\le2
```

count the anchors `0,q` that already lie in the opposite branch set.  Then

```math
\boxed{
|A(S)\cup M_q(T)|
=
2+m+n+c(G)-\eta.
}
```

## Component credit

For a connected component `K`, write

```math
v(K)=|V(K)|
```

and define

```math
\kappa(K)
=
\max\left\{
0,
\left\lceil\frac{v(K)}3\right\rceil-1
\right\}.
```

The full componentwise scale-export theorem gives at least `kappa(K)` distinct right vertices of `K` below `R`.

Different components have disjoint right-vertex sets, so

```math
\boxed{
\sum_K\kappa(K)
\le
|T\cap[1,R)|.
}
```

For every component,

```math
1+\kappa(K)
\ge
\frac{v(K)}3.
```

Summing over all components gives

```math
c(G)+\sum_K\kappa(K)
\ge
\frac13\sum_Kv(K)
=
\frac{m+n}{3}.
```

Substituting into the exact union identity yields

```math
\begin{aligned}
|A(S)\cup M_q(T)|
+
|T\cap[1,R)|
&\ge
2+m+n+c(G)-\eta
+
\sum_K\kappa(K)\\
&\ge
2+
\frac43(m+n)
-
\eta.
\end{aligned}
```

Hence

```math
\boxed{
|A(S)\cup M_q(T)|
+
|T\cap[1,R)|
\ge
2+
\frac43(|S|+|T|)
-
\eta.
}
```

This is the unequal-cardinality scale-compensated theorem.

## Harmonic form

Every exported witness `t<R` satisfies

```math
\frac Rt>1.
```

Therefore

```math
|T\cap[1,R)|
\le
R H(T\cap[1,R)),
```

where

```math
H(U)=\sum_{u\in U}\frac1u.
```

Thus

```math
\boxed{
|A(S)\cup M_q(T)|
+
R H(T\cap[1,R))
\ge
2+
\frac43(|S|+|T|)
-
\eta.
}
```

If `T` is also contained in `[R,2R)`, then

```math
T\cap[1,R)=\varnothing,
```

so

```math
\boxed{
|A(S)\cup M_q(T)|
\ge
2+
\frac43(|S|+|T|)
-
\eta.
}
```

Since, for a shell `U subseteq [R,2R)`,

```math
R H(U)\le |U|,
```

one obtains the direct same-shell harmonic estimate

```math
\boxed{
|A(S)\cup M_q(T)|
\ge
2+
\frac43R\bigl(H(S)+H(T)\bigr)
-
\eta.
}
```

## Interpretation

The correct homogeneous quantity is

```math
\frac43(|S|+|T|),
```

not an asymmetric expression such as

```math
2|S|+\frac23|T|.
```

The reason is that the physical branch union is governed by the total number of vertices in the side-middle intersection forest.  A component contributes one unit of forest capacity, and each exported lower-scale witness supplies the integer correction needed to reach one third of that component's vertex count.

The equal-cardinality result was only the specialization

```math
m=n,
```

for which

```math
\frac43(m+n)=\frac83m.
```

## Consequence for dyadic resolution

When both descendants are resolved into the same dyadic shell, no lower-scale correction is needed.  Every connected component demanding a positive credit would itself contain a right vertex below that shell and therefore could not occur in the restricted same-shell graph.

Hence same-shell side-middle interactions satisfy unconditional `4/3` expansion of their combined cardinality.  Cross-shell interactions are precisely where the missing capacity is transferred downward through the harmonic credit term.

## Next task

Insert the unequal-cardinality theorem into a multiscale potential.

For a fixed side shell `S subseteq [R,2R)`, decompose the paired middle child into

```math
T_{<R},
\qquad
T_R=T\cap[R,2R),
\qquad
T_{>2R}.
```

The same-shell part `T_R` is controlled directly.  The lower part `T_{<R}` is the telescoping credit.  The remaining task is to combine this theorem with the existing far-scale packing estimate for `T_{>2R}` and formulate one transition inequality whose lower-scale harmonic terms cancel across recursive generations.
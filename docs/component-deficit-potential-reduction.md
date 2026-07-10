# Component-deficit potential reduction

## Status

Exact graph-theoretic reduction of the coordinated side-middle shell-packing problem.

The local `8/3` packing inequality is false without a lower-scale correction.  The correct bookkeeping object is the full side-middle intersection graph.  Every intersection edge saves one parent point; every connected component contributes one unit of forest capacity.  Components larger than three vertices create the only possible deficit relative to the `8/3` target.

For an equal-cardinality side and middle shell, the following reduction is exact up to at most two anchor coincidences:

```math
\boxed{
\text{parent union}
+
\text{lower-scale component credits}
\ge
\frac83\times\text{shell cardinality}
}
```

provided each component `K` receives at least

```math
\boxed{
\kappa(K)
\ge
\max\left\{0,\left\lceil\frac{|V(K)|}{3}\right\rceil-1\right\}
}
```

distinct exported lower-scale witnesses.

This converts the remaining argument into a finite classification of path components of sizes four through seven.

## Shell setup

Let

```math
S\subseteq[R,2R)
```

be a coordinated side shell and let `T` be one shell of the paired selected middle child.  Assume

```math
|S|=|T|=m.
```

Define the branch parts of the two physical lifts by

```math
A^\circ(S)=S\cup2S
```

and

```math
M_q^\circ(T)=(q-T)\cup(q+T).
```

The coordinated construction gives

```math
S\cap2S=\varnothing.
```

Positivity gives

```math
(q-T)\cap(q+T)=\varnothing.
```

Hence

```math
|A^\circ(S)|=2m,
\qquad
|M_q^\circ(T)|=2m.
```

The full lifts are

```math
A(S)=\{0\}\cup A^\circ(S)
```

and

```math
M_q(T)=\{q\}\cup M_q^\circ(T).
```

## Full intersection graph

Define a bipartite graph

```math
G=G_q(S,T)
```

with left vertex set `S` and right vertex set `T`.  Join `s in S` to `t in T` for every relation

```math
cs=q\pm t,
\qquad c\in\{1,2\}.
```

An edge records one point of

```math
A^\circ(S)\cap M_q^\circ(T).
```

Because `S cap 2S` is empty, one parent point cannot arise from both branch coefficients `1` and `2`.  Because `q-T` and `q+T` are disjoint, one parent point cannot arise from both middle signs.  Therefore edge-point correspondence is bijective:

```math
\boxed{
|E(G)|
=
|A^\circ(S)\cap M_q^\circ(T)|.
}
```

## Degree bounds and acyclicity

Every left vertex has degree at most two, one possible edge for branch coefficient `1` and one for coefficient `2`.

Every right vertex also has degree at most two.  Its possible left preimages are

```math
q-t,
\quad
q+t,
\quad
\frac{q-t}{2},
\quad
\frac{q+t}{2},
```

which form two doubling pairs.  Since `S cap 2S` is empty, at most one member of each pair lies in `S`.

Thus

```math
\deg_G(v)\le2
```

on both sides.

A cycle would have every left vertex of degree two, so all of its left sources would be completely absorbed.  The coordinated absorption-forest theorem excludes such cycles.  Hence

```math
\boxed{G\text{ is a forest of paths}.}
```

Isolated vertices are included as one-vertex components.

## Exact forest count

Let

```math
c(G)
```

be the number of connected components, including isolated vertices.  The graph has

```math
|V(G)|=2m.
```

Since it is a forest,

```math
\boxed{
|E(G)|=2m-c(G).
}
```

Ignoring the two anchors for the moment,

```math
|A^\circ(S)\cup M_q^\circ(T)|
=
4m-|E(G)|
=
2m+c(G).
```

Therefore

```math
\boxed{
|A^\circ(S)\cup M_q^\circ(T)|
=
2m+c(G).
}
```

The anchors `0` and `q` contribute two additional points unless one or both already occur in the opposite branch set.  Let

```math
0\le\eta\le2
```

be the number of such anchor coincidences.  Then

```math
\boxed{
|A(S)\cup M_q(T)|
=
2+2m+c(G)-\eta.
}
```

Thus all nonconstant packing loss is encoded by the component count.

## Component deficit relative to triples

For a component `K`, put

```math
v(K)=|V(K)|.
```

The target inequality

```math
c(G)+\text{credits}
\ge
\frac{2m}{3}
```

can be checked componentwise because

```math
\sum_K v(K)=2m.
```

A component by itself contributes one unit to `c(G)`.  Its deficit relative to the `v(K)/3` target is

```math
\frac{v(K)}3-1.
```

Since credits are supplied by distinct exported witnesses, the natural integer credit requirement is

```math
\boxed{
\kappa(K)
=
\max\left\{0,\left\lceil\frac{v(K)}3\right\rceil-1\right\}.
}
```

Indeed,

```math
1+\kappa(K)
\ge
\frac{v(K)}3.
```

Summing gives

```math
c(G)+\sum_K\kappa(K)
\ge
\frac13\sum_Kv(K)
=
\frac{2m}{3}.
```

Combining with the forest identity yields

```math
\boxed{
|A(S)\cup M_q(T)|
+
\sum_K\kappa(K)
\ge
2+\frac83m-\eta.
}
```

This is the exact scale-compensated `8/3` target at the cardinality level.

If every credited component exports distinct witnesses below `R`, then

```math
\sum_K\kappa(K)
\le
|T\cap[1,R)|
\le
R\sum_{t\in T\cap[1,R)}\frac1t.
```

Hence

```math
\boxed{
|A(S)\cup M_q(T)|
+
R H(T_{<R})
\ge
2+\frac83m-\eta.
}
```

## Finite component types

The dyadic-shell complete-absorption theorem says that a connected block of degree-two left vertices contains at most two such sources.

Because every component of `G` is a path, this bounds all possible component sizes.

### Right-right endpoints

If both endpoints are right vertices, every left vertex is completely absorbed.  Therefore there are at most two left vertices:

```math
(l,r)\in\{(1,2),(2,3)\}.
```

### One left and one right endpoint

If the endpoints lie on opposite sides, exactly one left vertex is partial and the remaining `l-1` left vertices are completely absorbed.  Hence

```math
l-1\le2,
```

so

```math
(l,r)\in\{(1,1),(2,2),(3,3)\}.
```

### Left-left endpoints

If both endpoints are left vertices, exactly two left vertices are partial and the remaining `l-2` are completely absorbed.  Hence

```math
l-2\le2,
```

so

```math
(l,r)\in\{(2,1),(3,2),(4,3)\}.
```

Thus every component has at most seven vertices.  The only types requiring credits are:

```math
\begin{array}{c|c|c}
(l,r)&v=l+r&\kappa\\
\hline
(2,2)&4&1\\
(2,3),(3,2)&5&1\\
(3,3)&6&1\\
(4,3)&7&2.
\end{array}
```

All components with at most three vertices require no lower-scale credit.

## Progress already available

The three-by-three scale-export theorem proves the required one-unit credit for the extremal type

```math
(l,r)=(3,3).
```

Every such component contains a distinct middle witness below `R`.

The explicit near-`7/3` counterexample consists entirely of `(3,3)` components.  It therefore saturates the uncorrected local packing count while simultaneously supplying exactly the lower-scale credits required by the potential inequality.

This explains why the counterexample does not obstruct the harmonic recursion.

## Remaining finite classification

The entire equal-shell componentwise problem is reduced to four cases:

1. prove one lower-scale witness for every `(2,2)` component;
2. prove one lower-scale witness for every `(2,3)` component;
3. prove one lower-scale witness for every `(3,2)` component;
4. either exclude `(4,3)` components or prove that each exports two distinct lower-scale witnesses.

No unbounded component, logarithmic chain, or arbitrary overlap remains.

## Immediate next task

Classify the coefficient words and endpoint orientations for the four remaining path types.  The desired output is the exact componentwise export rule

```math
\boxed{
\#\{\text{distinct witnesses below }R\text{ in }K\}
\ge
\kappa(K).
}
```

Once established, the scale-compensated `8/3` inequality follows by summing over components and can be inserted directly into a telescoping multiscale harmonic potential.
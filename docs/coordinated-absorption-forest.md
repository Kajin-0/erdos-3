# Coordinated absorption forest

## Status

Exact structural theorem for side points absorbed by a paired middle child.

Fix a duplicated side-middle pair in the coordinated valuation recursion.  A side source `s` is completely absorbed when both of its non-anchor parent points are already supplied by the middle lift.  The two middle steps responsible for that absorption define a bipartite incidence graph.

Under the primitive dilation conditions of the coordinated children, this graph is a forest of paths.  In particular, absorption cannot recycle through cycles.

## Setup

Let `C` be a coordinated side child and let `q in C` be the step of the base three-term progression pairing it with a selected middle child `T`.

Assume

```math
C,\qquad2C,\qquad3C
```

are pairwise disjoint.  In particular,

```math
C\cap2C=\varnothing
```

and

```math
2C\cap3C=\varnothing.
```

Let `T` be a finite positive-integer set.  In translated coordinates, its middle lift is

```math
M_q(T)=\{q\}\cup(q-T)\cup(q+T).
```

Define the nonbase completely absorbed sources

```math
E
=
\{s\in C\setminus\{q\}:s\in M_q(T),\ 2s\in M_q(T)\}.
```

## Absorption graph

Construct a bipartite graph `G_q(C,T)` with:

- left vertex set `E`;
- right vertex set `T`;
- an edge from `s in E` to `t in T` whenever
  ```math
  s=q\pm t
  ```
  or
  ```math
  2s=q\pm t.
  ```

Thus the right neighbors of `s` are the middle steps whose reflected point pairs contain the side points `s` and `2s`.

## Every left vertex has degree two

Because `s` is completely absorbed, each of `s` and `2s` has a representation in the middle lift.  Therefore `s` has at least one neighbor for each branch coefficient `1` and `2`.

These two neighbors are distinct.  If the same `t` represented both branch points, then

```math
|q-s|=|q-2s|.
```

For positive `s`, the only nonzero solution is

```math
3s=2q.
```

But `s,q in C`, so this would put the same integer in

```math
3C
```

and

```math
2C,
```

contrary to `2C cap 3C = emptyset`.

Hence

```math
\boxed{\deg_G(s)=2\qquad(s\in E).}
```

## Every right vertex has degree at most two

Fix `t in T`.  A neighboring source must belong to the four-element candidate set

```math
q-t,
\qquad
q+t,
\qquad
\frac{q-t}{2},
\qquad
\frac{q+t}{2},
```

whenever the displayed quantities are positive integers.

These candidates form two doubling pairs:

```math
\left\{q-t,\frac{q-t}{2}\right\}
```

and

```math
\left\{q+t,\frac{q+t}{2}\right\}.
```

Since `C cap 2C` is empty, at most one member of each pair can lie in `C`.  Therefore

```math
\boxed{\deg_G(t)\le2\qquad(t\in T).}
```

Consequently every connected component of `G` is either a path or a cycle.

## Shared right vertices and coefficient labels

Label an edge at its left endpoint by `c in {1,2}` according to whether it represents the branch point `cs`.

Suppose a right vertex `t` is shared by two distinct left sources `s,s'`, with branch labels `c,d in {1,2}`.  Then

```math
q-cs=\sigma t,
\qquad
q-ds'=\tau t
```

for signs `sigma,tau in {−1,+1}`.

If `sigma=tau`, then

```math
cs=ds'.
```

For distinct sources and coefficients in `{1,2}`, this forces one source to be twice the other, contradicting `C cap 2C = emptyset`.

Therefore the signs are opposite, and every shared right vertex gives

```math
\boxed{cs+ds'=2q.}
```

## Cycle exclusion

Assume for contradiction that `G` contains a cycle.  Collapse each right vertex of the bipartite cycle to an edge between its two neighboring left sources.

Let the cycle contain `k` left sources.  Every left source uses exactly one branch-`1` edge and one branch-`2` edge, because its two right neighbors represent `s` and `2s` respectively.

Choose the largest left source `s_max` on the cycle.  Its branch-`2` edge has the form

```math
2s_{\max}+d s'=2q
```

with `d in {1,2}` and `s'>0`.  Hence

```math
s_{\max}<q.
```

All left sources on the cycle are therefore strictly smaller than `q`.

An edge of coefficient type `(1,1)` would satisfy

```math
s+s'=2q,
```

which is impossible because both endpoints are smaller than `q`.

Across the collapsed `k`-edge cycle there are exactly `k` coefficient-`1` incidences, one from each left source.

- an edge of type `(1,2)` uses one coefficient-`1` incidence;
- an edge of type `(2,2)` uses none;
- type `(1,1)` has already been excluded.

Therefore every edge must be of type `(1,2)`.

Orient each edge from its coefficient-`1` endpoint `s` to its coefficient-`2` endpoint `s'`.  The edge equation becomes

```math
s+2s'=2q,
```

so

```math
s'=F(s),
\qquad
F(s)=q-\frac{s}{2}.
```

Every vertex has one outgoing and one incoming edge, so the alleged cycle is a periodic orbit of `F`.

The unique fixed point of `F` is

```math
\frac{2q}{3},
```

and

```math
F^k(s)-\frac{2q}{3}
=
\left(-\frac12\right)^k
\left(s-\frac{2q}{3}\right).
```

If `F^k(s)=s`, then

```math
\left(1-\left(-\frac12\right)^k\right)
\left(s-\frac{2q}{3}\right)=0.
```

The first factor is nonzero, so every point of the orbit would equal `2q/3`.  This is not a nontrivial cycle; moreover `3s=2q` is already forbidden by `2C cap 3C = emptyset`.

Contradiction.

Hence

```math
\boxed{G_q(C,T)\text{ is a forest}.}
```

Since all left degrees equal `2` and all right degrees are at most `2`, every nonempty component is a path whose two endpoints lie on the right side.

## Exact right-vertex count

Let

```math
e=|E|
```

and let

```math
c
```

be the number of nonempty connected components of the absorption graph.

The graph has `2e` edges.  Since it is a forest,

```math
2e
=
(e+|N(E)|)-c,
```

where `N(E) subseteq T` is the set of right vertices used by absorption.

Therefore

```math
\boxed{|N(E)|=e+c.}
```

In particular, whenever `E` is nonempty,

```math
\boxed{|N(E)|\ge e+1.}
```

Thus complete absorption of `e` nonbase side sources requires at least `e+1` distinct middle steps.

The base step `q` is not a right neighbor of a nonbase absorbed source: a relation `|q-cs|=q` would force `s=2q` or `s=q`, both excluded by the primitive conditions and the definition of `E`.  Hence the middle child also contains its separate base element `q`.

## Interpretation

The general unmatched-overlap problem allows one middle lift to absorb many side branch points.  The forest theorem shows that this absorption is not arbitrary:

- every absorbed side source has two distinct middle witnesses;
- every witness is shared by at most two sources;
- the sharing pattern contains no cycle;
- each absorption component has two unshared terminal witnesses.

This is an affine analogue of the earlier multiplicative-chain decomposition, but now for overlap between two different role children.

## Relation to far-scale packing

In the far-scale regimes, every absorbed source also creates two reflected parent points outside the side lift.  The absorption forest gives additional information about the middle-step witnesses responsible for those points.

In the comparable-scale regime, where reflected points may return to the side-lift range, the forest remains valid and supplies the main available structure.  The remaining task is to attach a harmonic or scale-sensitive charge to the endpoints of these absorption paths.

## Immediate next target

For each path component of `G_q(C,T)`, prove a reciprocal-mass inequality of the form

```math
\sum_{s\text{ on the left path}}\frac1s
\le
C
\sum_{t\text{ at selected right endpoints}}\frac1t
```

or a scale-weighted variant with a summable loss.

Such an endpoint charge would convert the forest decomposition into a weighted packing theorem for the unmatched comparable-scale descendants.
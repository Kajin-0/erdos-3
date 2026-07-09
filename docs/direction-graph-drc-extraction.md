# Direction graph DRC extraction

## Status

Branch-1 continuation.  This note starts from the dyadic direction graph obtained in the `J`-energy concentration branch and records exactly what graph-level DRC gives.

The conclusion is deliberately limited: DRC gives many directions with many common shifted-interaction neighbors.  It does not, by itself, give additive structure in the direction set.  To reach additive structure, the graph must be coupled to its physical-space labels.

## Input from J-energy concentration

From the `J`-matrix energy dichotomy, assume there is a dyadic graph

```math
\mathcal G\subseteq D\times D
```

and a level `\tau` such that each edge `(d,e) in mathcal G` satisfies

```math
J(d,e)=|P_d\cap(P_e-2e)|\sim \tau.
```

Equivalently, for each edge `(d,e)` there are about `tau` points `x` with

```math
x,\quad x+d,\quad x+2e,\quad x+3e\in A.
```

Write

```math
K=|D|,
\qquad
m=|\mathcal G|,
\qquad
\delta=m/K^2.
```

The graph may be directed.  For this note, treat `d` as the left direction and `e` as the right direction.

## First DRC/codegree identity

For `d in D`, define the out-neighborhood

```math
N^+(d)=\{e:(d,e)\in\mathcal G\}.
```

The total number of directed two-stars with common right endpoint is

```math
\sum_{e\in D}\deg^-(e)^2
=
\sum_{d_1,d_2\in D}|N^+(d_1)\cap N^+(d_2)|.
```

By Cauchy--Schwarz,

```math
\sum_{e\in D}\deg^-(e)^2
\ge
\frac{m^2}{K}
=
\delta^2K^3.
```

Therefore the average common out-neighborhood size over ordered pairs `(d_1,d_2)` is at least

```math
\delta^2K.
```

So a dense direction graph necessarily contains many pairs of left directions with many common right-neighbors.

## A concrete extraction

Define the common-neighbor relation

```math
\mathcal C_\sigma
=
\{(d_1,d_2): |N^+(d_1)\cap N^+(d_2)|\ge \sigma\delta^2K\}.
```

For an absolute choice such as `sigma=1/2`, either:

1. `mathcal C_sigma` contains a positive fraction of the common-neighbor mass; or
2. the common-neighbor mass is concentrated on a smaller exceptional set of direction pairs.

In the first case, many ordered pairs `(d_1,d_2)` share many `e` such that both

```math
J(d_1,e)\sim\tau,
\qquad
J(d_2,e)\sim\tau.
```

This is the basic graph-DRC output.

## Physical meaning of a common neighbor

If `e` is a common neighbor of `d_1` and `d_2`, then there are many `x_1,x_2` such that

```math
x_1,\ x_1+d_1,\ x_1+2e,\ x_1+3e\in A,
```

and

```math
x_2,\ x_2+d_2,\ x_2+2e,\ x_2+3e\in A.
```

Thus common-neighbor structure gives many pairs of skew 4-point shadows sharing the same right direction `e`.

At this stage, however, `x_1` and `x_2` are unrelated.  Without relating the basepoints, this does not yet impose an additive relation among `d_1`, `d_2`, and `e`.

## Why graph DRC alone is insufficient

A dense abstract graph on `D x D` can have large common neighborhoods without `D` having small doubling, low rank, or any useful additive structure.  Therefore the implication

```math
\text{dense direction graph}
\Rightarrow
\text{additive structure in }D
```

is false without additional information.

The missing information is the edge label set

```math
X_{d,e}=P_d\cap(P_e-2e)
=
\{x:x,x+d,x+2e,x+3e\in A\}.
```

The graph edge `(d,e)` is not just present; it carries a large fiber `X_{d,e}`.  Any route to additive structure must use overlaps, translations, or correlations among these fibers.

## Labelled DRC target

A useful strengthened extraction would be:

> From a dense dyadic graph with `|X_{d,e}|\sim\tau` on each edge, either extract direction structure or find a subgraph in which many common-neighbor fibers overlap after translation.

For example, for common neighbor `e` of `d_1,d_2`, compare

```math
X_{d_1,e}
\qquad\text{and}\qquad
X_{d_2,e}+h.
```

If many such fibers overlap for many `h`, then one obtains repeated labelled skew patterns:

```math
x,x+d_1,x+2e,x+3e,
```

and

```math
x+h,x+h+d_2,x+h+2e,x+h+3e
```

inside `A`.

This is exactly the physical-space expansion of `J`-energy, now localized to a graph.

## Possible additive leverage

Suppose for many triples `(d_1,d_2,e)` there are many basepoint pairs with

```math
x_2=x_1+h
```

for a restricted set of shifts `h`.  Then the eight-point pattern depends on the direction data

```math
d_1,\quad d_2,\quad e,\quad h.
```

If the same `h` recurs often, then differences such as

```math
d_1-d_2
```

appear as repeated differences between points of `A` in aligned copies.  This may create additive energy in `D` or a density increment in a pair-neighborhood.

But this is an additional labelled-overlap statement, not a consequence of graph density alone.

## Refined Branch-1 dichotomy

The `J`-energy concentration branch should therefore be split again:

1. **Abstract graph concentration only.**  DRC gives common-neighbor structure, but no labelled fiber alignment.  This is insufficient.
2. **Labelled fiber overlap.**  Many edge fibers `X_{d,e}` overlap after controlled translations; this may yield additive structure or a density increment.
3. **Labelled incoherence.**  The direction graph is dense, but the physical fibers behave independently; then another sifting step is needed to create aligned labels or to expose cancellation/concentration elsewhere.

## Immediate proof task

Define a labelled energy for the dyadic graph:

```math
\mathcal E_X
=
\sum_{e\in D}\sum_{d_1,d_2\in N^-(e)}
|X_{d_1,e}|\,|X_{d_2,e}|.
```

This unlabelled version is just the common-neighbor count weighted by fiber sizes.  The useful refinement is the translated-overlap energy

```math
\mathcal E_X^{\mathrm{align}}
=
\sum_{e}\sum_{d_1,d_2\in N^-(e)}\sum_h
|X_{d_1,e}\cap(X_{d_2,e}-h)|^2.
```

The next step is to determine whether high `J`-energy forces nontrivial aligned fiber energy, or whether an additional sifting hypothesis is required.

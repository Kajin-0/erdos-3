# Multiplicative-chain decomposition and reciprocal core charge

## Status

Exact structural refinement of the third-dilate expansion lemma.

For a positive-integer set `D` with

```math
D\cap 2D=\varnothing,
```

the overlap of `3D` with `D\cup 2D` is governed by an injective increasing map.  Its components are geometric paths whose edge ratios are `3` or `3/2`.

This gives more than the cardinality estimate used previously:

1. the third-dilate expansion defect is exactly the number of multiplicative chains;
2. the reciprocal mass of every chain is controlled by its first element;
3. all vertices of a chain lie in one `(2,3)`-multiplicative orbit;
4. a divergent reciprocal sum cannot be generated inside finitely many such orbits.

The result identifies the correct alternative to uniform expansion: near-minimal third-dilate expansion forces low multiplicative-orbit complexity.

## Covered sources and the chain map

Let

```math
D\subseteq\mathbb N
```

be finite and satisfy

```math
D\cap2D=\varnothing.
```

Define

```math
C=\{d\in D:3d\in D\cup2D\}.
```

For `d in C`, define

```math
\phi(d)=
\begin{cases}
3d, & 3d\in D,\\[3pt]
3d/2, & 3d\in2D.
\end{cases}
```

The two cases cannot occur simultaneously, because that would put `3d` in `D cap 2D`.

As proved in the third-dilate expansion note, `phi` is injective and

```math
\phi(d)\ge\frac32d>d.
```

Therefore the directed graph

```math
d\longrightarrow\phi(d)
```

has indegree at most one, outdegree at most one, and no directed cycle.

## Exact chain decomposition

Every connected component is a directed path

```math
d_0\longrightarrow d_1\longrightarrow\cdots\longrightarrow d_\ell,
```

where each ratio satisfies

```math
\frac{d_{j+1}}{d_j}\in\left\{\frac32,3\right\}.
```

Let

```math
\mathcal S(D)
```

be the set of initial vertices and

```math
\mathcal T(D)=D\setminus C
```

be the set of terminal vertices.

Every component has exactly one initial vertex and one terminal vertex.  Hence

```math
\boxed{
|\mathcal S(D)|=|\mathcal T(D)|.
}
```

Multiplication by `3` is a bijection from `D` to `3D`, and a source `d` contributes a new point of `3D` precisely when `d notin C`.  Therefore

```math
\boxed{
|\mathcal T(D)|
=
|3D\setminus(D\cup2D)|.
}
```

Consequently the exact expansion identity is

```math
\boxed{
|D\cup2D\cup3D|
=
2|D|+|\mathcal T(D)|.
}
```

Thus the excess beyond the binary factor `2` is exactly the number of multiplicative chains.

## Cardinality bound from the number of chains

If `D subseteq [1,M]`, then every edge increases by at least `3/2`.  A chain therefore has at most

```math
1+\lfloor\log_{3/2}M\rfloor
```

vertices.

Writing

```math
t(D)=|\mathcal T(D)|=|\mathcal S(D)|,
```

we obtain

```math
\boxed{
|D|
\le
t(D)\bigl(1+\lfloor\log_{3/2}M\rfloor\bigr).
}
```

Equivalently,

```math
\boxed{
t(D)
\ge
\frac{|D|}{1+\lfloor\log_{3/2}M\rfloor}.}
```

This recovers the previous logarithmic third-dilate expansion lemma, now as a consequence of an exact path decomposition.

## Reciprocal mass of one chain

Let

```math
d_0\longrightarrow d_1\longrightarrow\cdots\longrightarrow d_\ell
```

be one component.  Since

```math
d_j\ge\left(\frac32\right)^j d_0,
```

we have

```math
\sum_{j=0}^{\ell}\frac1{d_j}
\le
\frac1{d_0}
\sum_{j\ge0}\left(\frac23\right)^j
=
\frac3{d_0}.
```

Therefore

```math
\boxed{
\sum_{d\in D}\frac1d
\le
3\sum_{s\in\mathcal S(D)}\frac1s.
}
```

This is the reciprocal analogue of the cardinality chain bound.  A long chain is harmonically inexpensive: its entire reciprocal mass is at most three times that of its first vertex.

Since the starts are distinct positive integers, if `t=t(D)` then

```math
\sum_{s\in\mathcal S(D)}\frac1s
\le H_t,
```

where `H_t` is the `t`-th harmonic number.  Hence

```math
\boxed{
\sum_{d\in D}\frac1d
\le
3H_{t(D)}
\le
3(1+\log t(D)).
}
```

Equivalently, large reciprocal mass forces many multiplicative chains:

```math
\boxed{
t(D)
\ge
\exp\left(\frac13\sum_{d\in D}\frac1d-1\right).}
```

The last inequality is weak for small reciprocal mass, but it is an exact structural direction: harmonic mass cannot hide indefinitely in a bounded number of near-minimal-expansion chains.

## `(2,3)`-multiplicative cores

For a positive integer `n`, define its `6`-free core by

```math
\mathrm{core}_{2,3}(n)
=
\frac{n}{2^{v_2(n)}3^{v_3(n)}}.
```

This integer is coprime to `6`.

Every edge of a chain multiplies by either `3` or `3/2`.  Therefore

```math
\boxed{
\mathrm{core}_{2,3}(\phi(d))
=
\mathrm{core}_{2,3}(d).
}
```

So every multiplicative chain lies inside one orbit

```math
\mathcal O_c
=
\{c2^a3^b:a,b\ge0\},
\qquad (c,6)=1.
```

The full orbit has finite reciprocal mass:

```math
\sum_{n\in\mathcal O_c}\frac1n
=
\frac1c
\sum_{a\ge0}2^{-a}
\sum_{b\ge0}3^{-b}
=
\boxed{\frac3c}.
```

Consequently, for any set `X subseteq N`,

```math
\boxed{
\sum_{n\in X}\frac1n
\le
3\sum_{c\in\mathrm{Core}(X)}\frac1c,
}
```

where `Core(X)` is the set of distinct `(2,3)`-cores represented in `X`.

In particular,

```math
\sum_{n\in X}\frac1n=\infty
```

implies

```math
\boxed{
\sum_{c\in\mathrm{Core}(X)}\frac1c=\infty.
}
```

Thus a divergent candidate cannot obtain its divergence by repeatedly occupying only finitely many `(2,3)`-multiplicative orbits.  It must continually introduce new cores with divergent reciprocal mass.

## Expansion-or-orbit-complexity interpretation

For an affine extension fiber, the three-dilate union is 4-AP-free, hence `D cap 2D` is empty and all preceding conclusions apply.

There are now two quantitatively distinct possibilities.

### Many chains

If

```math
t(D)=|3D\setminus(D\cup2D)|
```

is large, then the third dilation creates many genuinely new points.  This is the expansion branch.

### Few chains

If `t(D)` is small, then `D` is covered by few increasing paths, each contained in one `(2,3)`-orbit and each having reciprocal mass controlled by its initial vertex.

This is a multiplicative-complexity branch rather than an additive-density branch.

The previous worst-case contraction estimate used only

```math
t(D)\ge |D|/(1+\log_{3/2}M).
```

The exact identity

```math
|D\cup2D\cup3D|=2|D|+t(D)
```

suggests retaining `t(D)` as a local parameter instead of replacing it immediately by its logarithmic lower bound.

Along a recursive affine-fiber tree, one should track both:

```math
\text{normalized child mass}
```

and

```math
\text{new multiplicative-chain starts / new }(2,3)\text{-cores}.
```

A successful stopping-time argument could then charge:

- large `t(D)` to strict physical expansion;
- small `t(D)` to a small collection of harmonically summable multiplicative orbits.

## Sharpness warning

The path-length estimate is optimal for the chain-map argument alone: a path whose every edge has ratio `3/2` has length comparable to `log M`.

This does **not** by itself prove that the full three-dilate 4-AP-free condition admits every such extremal chain.  Any improvement from logarithmic to constant expansion would have to use additional additive information beyond `D cap 2D=emptyset`.

## Immediate next task

Develop a recursive potential combining

```math
\sum_{d\in D}\frac1d
```

with the exact chain count

```math
t(D)=|3D\setminus(D\cup2D)|.
```

The target is an inequality in which every recursive node either pays a definite amount of third-dilate expansion or transfers its reciprocal mass to a controlled set of new `(2,3)`-cores.  This would convert the present local decomposition into a cross-scale summability mechanism.
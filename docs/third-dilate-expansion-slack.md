# Third-dilate expansion slack

## Status

Exact multiplicative-expansion lemma for the concentrated affine-fiber branch.

The binary part of the recursion is exactly balanced: a depth-`h` descendant has `2^h` disjoint affine copies in the root, while the total normalized child mass can grow by nearly a factor `2` per generation.  Therefore the binary argument alone has no quantitative slack.

The first genuine slack comes from the third dilation.  If

```math
D\cup2D\cup3D
```

is 4-AP-free, then `D cap 2D` is empty.  The set `3D` cannot be almost completely absorbed by `D union 2D` without creating long increasing multiplicative chains inside `D`.  Since `D subseteq [1,M]`, those chains have logarithmically bounded length.

This yields:

1. a strict expansion bound
   ```math
   |D\cup2D\cup3D|
   \ge
   \left(2+\frac{1}{1+\lfloor\log_{3/2}M\rfloor}\right)|D|;
   ```
2. a strict density contraction along every recursive predecessor edge;
3. an accumulated polylogarithmic loss along a deep concentration path.

The result does not yet prove the Erdős conjecture, but it breaks the exact factor-`2` balance that blocked the previous multiplicity argument.

## Setup

Let

```math
D\subseteq[1,M]
```

be a finite set satisfying

```math
D\cap2D=\varnothing.
```

Every concentrated extension fiber satisfies this condition because

```math
D\cup2D\cup3D
```

is 4-AP-free.

Define the covered-source set

```math
C
=
\{d\in D:3d\in D\cup2D\}.
```

For `d in C`, define a target `phi(d) in D` by

```math
\phi(d)
=
\begin{cases}
3d, & 3d\in D,\\[3pt]
3d/2, & 3d\in2D.
\end{cases}
```

The definition is unambiguous.  If both alternatives held, then

```math
3d\in D\cap2D,
```

contrary to `D cap 2D=emptyset`.

## Multiplicative-chain lemma

The map

```math
\phi:C\to D
```

is injective and satisfies

```math
\phi(d)\ge\frac32d>d.
```

### Proof of injectivity

Within either branch of the definition, injectivity is immediate.

For a cross-branch collision, suppose

```math
3d_1=\frac32d_2.
```

Then

```math
d_2=2d_1,
```

which is impossible because `d_1,d_2 in D` and `D cap 2D=emptyset`.

Thus the directed graph

```math
d\longmapsto\phi(d)
```

has indegree at most one, outdegree at most one, and every edge strictly increases its value by a factor at least `3/2`.

Consequently its connected components are directed paths.

Put

```math
L(M)=\left\lfloor\log_{3/2}M\right\rfloor.
```

A directed path has at most `L(M)` edges and at most `L(M)+1` vertices, because after `ell` edges its value has grown by at least `(3/2)^ell` while remaining at most `M`.

Every directed component has one terminal vertex, and terminal vertices are precisely elements of `D setminus C`.  Hence

```math
|D\setminus C|
\ge
\frac{|D|}{L(M)+1}.
```

Therefore

```math
\boxed{
|\{d\in D:3d\notin D\cup2D\}|
\ge
\frac{|D|}{1+\lfloor\log_{3/2}M\rfloor}.
}
```

## Strict three-dilate expansion

Multiplication by `3` is a bijection from `D` to `3D`.  Therefore

```math
|3D\setminus(D\cup2D)|
=
|D\setminus C|.
```

Since `D` and `2D` are disjoint,

```math
|D\cup2D|=2|D|.
```

Combining these identities with the chain lemma gives

```math
\boxed{
|D\cup2D\cup3D|
\ge
\left(
2+
\frac{1}{1+\lfloor\log_{3/2}M\rfloor}
\right)|D|.
}
```

This is a strict improvement over the earlier bound

```math
|D\cup2D\cup3D|\ge2|D|.
```

The gain is only logarithmic, but it accumulates along recursive concentration paths.

## Improved extremal comparison

Recall

```math
s_4^{(3)}(M)
=
\max\{|D|:D\subseteq[1,M],\ D\cup2D\cup3D\text{ is 4-AP-free}\}.
```

Since the three-dilate union lies in `[1,3M]`, the strict expansion lemma gives

```math
\boxed{
s_4^{(3)}(M)
\le
\frac{r_4(3M)}{
2+\bigl(1+\lfloor\log_{3/2}M\rfloor\bigr)^{-1}
}.
}
```

This is still only a logarithmic improvement over the factor-`1/2` comparison, so its main value is recursive rather than one-shot.

## Density contraction along one predecessor edge

Let a parent fiber satisfy

```math
D_{t-1}\subseteq[1,M_{t-1}],
```

and let

```math
D_t=E_{q_t}(D_{t-1})
```

be a child predecessor fiber.  Its natural ambient scale is

```math
M_t=\frac{M_{t-1}}2.
```

The three translated copies

```math
q_t+D_t,
\qquad
q_t+2D_t,
\qquad
q_t+3D_t
```

lie inside `D_{t-1}`.  Applying the strict expansion lemma to `D_t subseteq [1,M_t]` yields

```math
|D_{t-1}|
\ge
\left(
2+
\frac{1}{1+\lfloor\log_{3/2}M_t\rfloor}
\right)|D_t|.
```

Define natural-scale densities

```math
\beta_t=\frac{|D_t|}{M_t}.
```

Then

```math
\boxed{
\beta_t
\le
c(M_t)\beta_{t-1},
}
```

where

```math
c(m)
=
\frac{2}{
2+\bigl(1+\lfloor\log_{3/2}m\rfloor\bigr)^{-1}
}
<1.
```

Thus every nonempty recursive edge causes a strict density loss.  This improves the earlier non-increase statement `beta_t<=beta_{t-1}`.

## Accumulated path contraction

Along a depth-`h` path beginning at scale `M`, put

```math
M_t=\frac{M}{2^t}.
```

Iterating the edge inequality gives

```math
\boxed{
\beta_h
\le
\beta_0
\prod_{t=1}^h c(M_t).
}
```

A convenient explicit estimate follows.  Put

```math
a=\frac32,
\qquad
\gamma=\frac{\log a}{3\log2}.
```

For

```math
\delta(m)
=
\frac{1}{1+\lfloor\log_a m\rfloor},
```

one has

```math
c(m)=\frac{1}{1+\delta(m)/2}.
```

Since `0<delta(m)<=1`,

```math
\log c(m)
=-\log(1+\delta(m)/2)
\le
-\frac{\delta(m)}3.
```

Also

```math
\delta(m)
\ge
\frac{\log a}{\log m+\log a}.
```

Summing over the dyadically decreasing scales and comparing with an integral gives

```math
\boxed{
\prod_{t=1}^h c(M_t)
\le
\left(
\frac{\log M_h+\log(3/2)}
{\log M+\log(3/2)}
\right)^\gamma.
}
```

Therefore

```math
\boxed{
\beta_h
\le
\beta_0
\left(
\frac{\log M_h+\log(3/2)}
{\log M+\log(3/2)}
\right)^\gamma.
}
```

The exponent

```math
\gamma
=
\frac{\log(3/2)}{3\log2}
```

is an absolute positive constant.

## Maximum possible concentration depth

If `D_h` is nonempty, then

```math
\beta_h
\ge
\frac1{M_h}
=
\frac{2^h}{M}.
```

Combining this with the path-contraction estimate gives

```math
\boxed{
2^h
\le
|D_0|
\left(
\frac{\log M_h+\log(3/2)}
{\log M+\log(3/2)}
\right)^\gamma.
}
```

Equivalently,

```math
\boxed{
M_h
\ge
\frac1{\beta_0}
\left(
\frac{\log M+\log(3/2)}
{\log M_h+\log(3/2)}
\right)^\gamma.
}
```

Thus a concentration path cannot descend all the way to the naive binary limit `M_h approximately 1/beta_0`.  It must stop earlier by a polylogarithmic factor.

## Why this is genuine but not yet sufficient

The previous lower-bound mechanism gives total normalized child mass close to a factor `2` per generation.  The binary disjoint-copy lemma also gives a factor `2` capacity per generation, so those two statements exactly balance.

The third-dilate lemma introduces the first strict loss:

```math
\text{single-path capacity}
\le
2^h\times\text{polylogarithmic contraction}.
```

However, the recursive tree can respond by splitting its mass among many children that terminate near the Roth-error scale.  The path-contraction theorem alone therefore does not prove reciprocal convergence.

## Immediate next task

Develop a stopping-time inequality that combines:

1. near-doubling of total normalized child mass above the Roth-error scale;
2. strict polylogarithmic contraction along every surviving path;
3. charging of terminated branches to the summable Roth-error sequence.

A successful inequality would bound the total root mass by the accumulated stopping errors.  This is the clearest remaining route for turning the linear three-AP extension load into a summability theorem.
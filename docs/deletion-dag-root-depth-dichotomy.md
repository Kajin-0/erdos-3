# Deletion-DAG root-depth dichotomy

## Status

Exact dichotomy supplementing the merge-difference recursion.

For the side-anchor deletion DAG on a four-term-progression-free block, the number of indegree-zero vertices controls two complementary phenomena:

1. many roots give a strict harmonic gain in the merge-difference children;
2. few roots force a long directed affine path.

Thus a recursion which remains close to the critical factor `1` cannot also have shallow deletion DAGs.

## Setup

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free.  Run side-anchor deletion until a three-term-progression-free residual set remains.

Write

```math
K=|D|-s
```

for the number of deleted vertices, where

```math
s\le r_3(N).
```

The affine deletion DAG has:

- vertex set `D`;
- outdegree exactly two at each deleted vertex;
- outdegree zero at each residual vertex;
- `2K` directed edges;
- no directed cycle.

Let

```math
\rho
```

be the number of indegree-zero vertices.

The merge-difference construction gives four-term-progression-free children `Delta_v subseteq[1,N)` with total harmonic mass

```math
\boxed{
\sum_vH(\Delta_v)
\ge
\frac{|D|-2s+\rho}{N}.
}
```

## Many roots give strict harmonic gain

Since

```math
H(D)\le\frac{|D|}{N},
```

if

```math
\rho\ge\delta|D|
```

for some `delta>0`, then

```math
\begin{aligned}
\sum_vH(\Delta_v)
&\ge
\frac{(1+\delta)|D|-2s}{N}\\
&\ge
(1+\delta)H(D)-2\frac{r_3(N)}N.
\end{aligned}
```

Therefore

```math
\boxed{
\rho\ge\delta|D|
\quad\Longrightarrow\quad
\sum_vH(\Delta_v)
\ge
(1+\delta)H(D)-2\frac{r_3(N)}N.
}
```

A positive root proportion makes the merge recursion genuinely supercritical by itself.

## Every vertex descends from a root

Because the graph is a finite DAG, repeatedly following incoming edges backwards from any vertex must terminate at an indegree-zero vertex.  Hence every vertex is reachable from at least one root.

If every directed path had length at most `h`, then a fixed root could reach at most

```math
1+2+2^2+\cdots+2^h
=
2^{h+1}-1
```

vertices, because every vertex has outdegree at most two.

With `rho` roots this would imply

```math
|D|
\le
\rho(2^{h+1}-1).
```

Consequently the maximum directed path length `L` satisfies

```math
\boxed{
L
\ge
\left\lceil
\log_2\left(\frac{|D|}{\rho}+1\right)
\right\rceil-1.
}
```

In particular, if

```math
\rho<\delta|D|,
```

then

```math
\boxed{
L
\ge
\left\lceil
\log_2\left(\frac1\delta+1\right)
\right\rceil-1.
}
```

Thus a near-critical merge recursion with very few roots necessarily contains a long affine dependency chain.

## Affine form of a directed path

Consider a directed path

```math
x_0\longrightarrow x_1\longrightarrow\cdots\longrightarrow x_L.
```

At the vertex `x_j`, let `q_j` be the common difference of the selected progression sponsored by `x_j`.  The next vertex is either its center or its opposite endpoint, so

```math
x_{j+1}
=
x_j+\sigma_j c_jq_j,
```

where

```math
c_j\in\{1,2\}.
```

The coordinated side-anchor rule determines the sign:

```math
\sigma_j
=
\begin{cases}
+1,&v_2(q_j)\equiv0\pmod2,\\
-1,&v_2(q_j)\equiv1\pmod2.
\end{cases}
```

Therefore every long path satisfies

```math
\boxed{
x_{j+1}-x_j
=\sigma(q_j)c_jq_j,}
```

with the direction of motion fixed by the parity of the two-adic valuation of its step.

Since every path vertex remains in `[N,2N)`, one also has

```math
\boxed{
\left|
\sum_{j=u}^{v-1}\sigma_jc_jq_j
\right|<N
}
```

for every subpath `[u,v]`.

Thus long paths require substantial affine cancellation among step labels whose signs are prescribed by `v_2(q) mod 2`.

## Quantitative dichotomy

For every `delta in (0,1)`, at least one of the following holds.

### Root-rich case

```math
\boxed{
\sum_vH(\Delta_v)
\ge
(1+\delta)H(D)-2\frac{r_3(N)}N.
}
```

### Long-path case

The deletion DAG contains a path of length at least

```math
\boxed{
\left\lceil
\log_2\left(\frac1\delta+1\right)
\right\rceil-1.
}
```

whose increments have the valuation-controlled affine form

```math
\sigma(q_j)c_jq_j,
\qquad
c_j\in\{1,2\}.
```

## Interpretation

The merge-difference recursion can fail to gain a fixed multiplicative factor only when roots are sparse.  Sparse roots force long dependency paths.  Hence a hypothetical mass-regular counterexample must repeatedly choose between:

1. strict lower-scale harmonic expansion;
2. increasingly long affine paths with two-adically prescribed direction.

This isolates a new finite-dimensional target:

> Bound the length or scale distribution of a directed path in a four-term-progression-free side-anchor deletion DAG, using the rule that the sign of each increment is determined by `v_2(q) mod 2`.

A path theorem of logarithmic strength would combine with the root-rich alternative to give a genuine stopping-time mechanism for the merge recursion.
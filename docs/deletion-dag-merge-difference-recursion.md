# Deletion-DAG merge-difference recursion

## Status

Exact lower-scale recursion extracted from indegree merging in the side-anchor deletion DAG.

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free.  Run the side-anchor deletion process until the residual set is three-term-progression-free.  If `K` points are deleted and `s` points remain, then

```math
K=|D|-s,
\qquad
s\le r_3(N).
```

The resulting affine deletion DAG has `2K` directed edges.  Indegree excess in this DAG produces a family of translated sponsor-difference sets which:

1. are four-term-progression-free;
2. lie strictly below the parent scale;
3. contain exactly one element for every unit of indegree excess.

Combining these merge-difference children with the selected coordinated middle children gives a harmonic branching lower bound with factor `5/3`.  A binary thinning retains factor `7/6` while ensuring that every parent sponsor creates at most two child occurrences.

## Deletion DAG

Write the selected progressions as

```math
(a_i,b_i,c_i),
\qquad
 a_i+c_i=2b_i,
```

where `a_i` is the deleted coordinated side anchor.  Add directed edges

```math
a_i\longrightarrow b_i,
\qquad
a_i\longrightarrow c_i.
```

Every edge points to a vertex deleted later, or to a residual vertex, so the graph is acyclic.  Every deleted vertex has outdegree exactly two and every residual vertex has outdegree zero.

Let

```math
d^-(v)
```

be the indegree of `v`, and let

```math
\rho
```

be the number of indegree-zero vertices of the DAG.

Since the graph has `2K` edges and `K+s` vertices,

```math
\sum_v d^-(v)=2K.
```

The exact indegree-excess count is

```math
\begin{aligned}
M
&=
\sum_v\max\{d^-(v)-1,0\}\\
&=2K-|\{v:d^-(v)>0\}|\\
&=2K-(K+s-\rho).
\end{aligned}
```

Therefore

```math
\boxed{
M=K-s+\rho.
}
```

In particular,

```math
\boxed{
M\ge K-s=|D|-2s.
}
```

Thus a deletion process with a small Roth residual necessarily creates almost one unit of indegree merging per deleted element.

## Incoming-sponsor sets

For a vertex `v`, define its incoming-sponsor set

```math
I_v
=
\{a_i:a_i\to v\}.
```

This is a subset of `D`.  If `I_v` is nonempty, let

```math
p_v=\min I_v
```

and define the merge-difference child

```math
\Delta_v
=
\{a-p_v:a\in I_v,\ a>p_v\}.
```

Then

```math
|\Delta_v|=d^-(v)-1.
```

Since all incoming sponsors lie in `[N,2N)`, every element of `Delta_v` satisfies

```math
1\le a-p_v<N.
```

Hence

```math
\boxed{
\Delta_v\subseteq[1,N).
}
```

Every merge-difference child lies strictly below the parent dyadic scale.

## Four-term-progression-freeness

Each `Delta_v` is four-term-progression-free.

Indeed, if

```math
d,\ d+r,\ d+2r,\ d+3r\in\Delta_v,
```

then adding `p_v` gives

```math
p_v+d,\ p_v+d+r,\ p_v+d+2r,\ p_v+d+3r\in I_v\subseteq D,
```

which is a nontrivial four-term progression in `D`.

Therefore

```math
\boxed{
\Delta_v\text{ is four-term-progression-free for every }v.
}
```

## Exact total cardinality

Summing over all vertices gives

```math
\boxed{
\sum_v|\Delta_v|
=
\sum_v\max\{d^-(v)-1,0\}
=
M
=
K-s+\rho.
}
```

The merge-difference family records the full indegree excess without loss.

## Harmonic lower bound

Because every `delta in Delta_v` is smaller than `N`,

```math
\frac1\delta>\frac1N.
```

Consequently,

```math
\sum_vH(\Delta_v)
\ge
\frac{M}{N}.
```

Using the exact excess formula,

```math
\boxed{
\sum_vH(\Delta_v)
\ge
\frac{K-s+\rho}{N}.
}
```

Since `K=|D|-s`,

```math
\boxed{
\sum_vH(\Delta_v)
\ge
\frac{|D|-2s+\rho}{N}
\ge
\frac{|D|}{N}-2\frac{r_3(N)}N.
}
```

As

```math
H(D)\le\frac{|D|}{N},
```

we also obtain

```math
\boxed{
\sum_vH(\Delta_v)
\ge
H(D)-2\frac{r_3(N)}N.
}
```

Thus the merge-difference children alone preserve the parent harmonic mass up to the summable Roth error.

## Combination with selected middle children

For the same side-anchor deletion family, let

```math
\mathcal L_*(D)
=
\sum_{i=1}^K\frac1{q_i}
```

be the selected weighted three-term-progression load.  Since every selected step satisfies `q_i<=N/2`,

```math
\mathcal L_*(D)\ge\frac{2K}{N}.
```

Choose a `chi=v_2-v_3 mod 3` color carrying maximal selected load, and form the associated sparse middle children `M_x^*`.  Then

```math
\sum_xH(M_x^*)
\ge
\frac13\mathcal L_*(D)
\ge
\frac{2K}{3N}.
```

Adding the merge-difference and middle-child lower bounds gives

```math
\begin{aligned}
\sum_vH(\Delta_v)
+
\sum_xH(M_x^*)
&\ge
\frac{K-s+\rho}{N}
+
\frac{2K}{3N}\\
&=
\frac{5K/3-s+\rho}{N}.
\end{aligned}
```

Since `K=|D|-s`,

```math
\boxed{
\sum_vH(\Delta_v)
+
\sum_xH(M_x^*)
\ge
\frac53\frac{|D|}{N}
-
\frac83\frac{s}{N}
+
\frac{\rho}{N}.
}
```

Therefore

```math
\boxed{
\sum_vH(\Delta_v)
+
\sum_xH(M_x^*)
\ge
\frac53H(D)
-
\frac83\frac{r_3(N)}N.
}
```

This is an exact lower-scale harmonic branching theorem with factor `5/3`.

All children involved are four-term-progression-free and lie below the parent scale:

- each middle step is at most `N/2`;
- each merge difference is smaller than `N` and becomes strictly lower after dyadic resolution.

## Occurrence genealogy

Every merge-difference occurrence

```math
a-p_v\in\Delta_v
```

is associated with the nonminimal incoming sponsor `a` and the target vertex `v`.

A deleted sponsor has exactly two outgoing DAG edges, so it can be nonminimal in at most two incoming-sponsor sets.  Hence

```math
\boxed{
\text{each parent sponsor creates at most two merge-difference occurrences.}
}
```

It creates at most one selected middle occurrence.  Consequently the unthinned combined recursion has at most three child occurrences per sponsor.

## Binary thinning

For every sponsor which creates one or two merge-difference occurrences, retain exactly one of them.  Let the resulting subsets be

```math
\Delta_v'.
```

If `U` is the number of sponsors which create at least one merge occurrence, then

```math
M\le2U,
```

so

```math
U\ge\frac M2.
```

The retained children remain four-term-progression-free because

```math
\Delta_v'\subseteq\Delta_v.
```

Their harmonic mass satisfies

```math
\sum_vH(\Delta_v')
\ge
\frac{U}{N}
\ge
\frac{M}{2N}.
```

Combining with the selected middle children,

```math
\begin{aligned}
\sum_vH(\Delta_v')
+
\sum_xH(M_x^*)
&\ge
\frac{K-s+\rho}{2N}
+
\frac{2K}{3N}\\
&=
\frac{7K/6-s/2+\rho/2}{N}.
\end{aligned}
```

Using `K=|D|-s`,

```math
\boxed{
\sum_vH(\Delta_v')
+
\sum_xH(M_x^*)
\ge
\frac76\frac{|D|}{N}
-
\frac53\frac{s}{N}
+
\frac{\rho}{2N}.
}
```

Thus

```math
\boxed{
\sum_vH(\Delta_v')
+
\sum_xH(M_x^*)
\ge
\frac76H(D)
-
\frac53\frac{r_3(N)}N.
}
```

After thinning, every parent sponsor creates at most:

1. one merge-difference occurrence;
2. one selected middle occurrence.

Therefore

```math
\boxed{
\text{the thinned recursion is binary and still has harmonic growth factor }7/6.
}
```

## What this resolves

The side-anchor deletion DAG contains a large canonical lower-scale subsystem that was not visible in the original role recursion.

- Sparse residual sets force large indegree excess.
- Every unit of excess becomes a lower-scale difference occurrence.
- Those occurrences organize into genuine four-term-progression-free child sets.
- The full merge-plus-middle recursion has factor `5/3`.
- A binary version retains factor `7/6`.

This is a global construction: it does not pair whole child states and does not rely on a local overlap inequality.

## Remaining limitation

The new branching theorem is still counted with multiplicity across child states.  The binary thinning gives a canonical genealogy, but abstract binary scale descent can support reciprocal-mass growth because labels may contract rapidly.

The next target is to exploit the special form of the merge labels

```math
\delta=a-p_v,
```

where `a` and `p_v` are two sponsors whose selected affine forks share the same later vertex `v`.

A closing theorem should show that repeated merge descent cannot remain arbitrary.  Plausible forms are:

1. a scale-compensated potential in which small merge differences pay for rapid contraction;
2. a rigidity theorem for repeated shared-target sponsor differences;
3. an energy inequality controlling how often one sponsor can participate in mass-regular merge chains across generations.

The precise new bottleneck is therefore the multigeneration geometry of translated incoming-sponsor sets, not the existence of enough lower-scale children.
# Second-generation affine-fiber obstruction

## Status

Exact inherited structure for concentrated three-AP extension fibers.

The cross-scale extension-load construction produces fibers

```math
D_{j,p}
=
\{d\ge1:p+d,p+2d,p+3d\in A\cap[N,2N)\}.
```

Such a fiber is more constrained than an arbitrary 4-AP-free subset of `[1,N/2]`:

1. the union of its first three dilates is itself 4-AP-free;
2. in particular, the fiber is disjoint from its double;
3. a three-AP inside the fiber is forbidden for several explicit predecessor-to-step ratios;
4. the resulting three-dilate class is hereditary under further predecessor-fiber extraction.

The final point corrects an initially tempting but false interpretation: recursion does not automatically create a strictly decreasing hierarchy of new extremal classes.  It keeps producing members of the same hereditary class.  The quantity that grows under recursion is affine-tree multiplicity.

## First-generation affine union

Let `A subset Z` be 4-AP-free.  Suppose

```math
p+D,
\qquad
p+2D,
\qquad
p+3D
\subseteq A
```

for a finite set of positive integers `D`.

Define

```math
\mathcal U_3(D)=D\cup2D\cup3D.
```

Then

```math
p+\mathcal U_3(D)\subseteq A.
```

Translation preserves arithmetic progressions, so

```math
\boxed{\mathcal U_3(D)\text{ is 4-AP-free}.}
```

This contains the earlier fact that `D` itself is 4-AP-free, but is strictly stronger.

## No-doubling lemma

One has

```math
\boxed{D\cap2D=\varnothing.}
```

### Proof

Suppose `d in D` and `2d in D`.  Since `d in D`,

```math
p+d,
\quad
p+2d,
\quad
p+3d
\in A.
```

Since `2d in D`,

```math
p+4d\in A.
```

Therefore

```math
p+d,
\quad
p+2d,
\quad
p+3d,
\quad
p+4d
```

is a nontrivial four-term arithmetic progression in `A`, contradiction.

Equivalently, the two dilates `D` and `2D` are disjoint subsets of the 4-AP-free set `mathcal U_3(D)`.

## Immediate extremal bound

For `M>=1`, define

```math
s_4^{(3)}(M)
=
\max\left\{
|D|:
D\subseteq[1,M],
\ D\cup2D\cup3D\text{ is 4-AP-free}
\right\}.
```

Because `D cap 2D` is empty,

```math
|D\cup2D\cup3D|
\ge
|D\cup2D|
=
2|D|.
```

Also

```math
D\cup2D\cup3D\subseteq[1,3M].
```

Hence

```math
2|D|
\le
r_4(3M),
```

and therefore

```math
\boxed{
s_4^{(3)}(M)
\le
\frac12 r_4(3M).
}
```

This only improves the ordinary `r_4` bound by a constant factor, but it identifies the correct inherited class for concentrated extension fibers.

## Second-generation grid

Assume now that the fiber `D` itself contains a three-term progression

```math
q+d,
\qquad
q+2d,
\qquad
q+3d
\in D,
\qquad d>0.
```

Since each of these three directions belongs to `D`, the original set `A` contains the nine-point affine grid

```math
\boxed{
p+i(q+jd)\in A
\qquad
(i,j\in\{1,2,3\}).
}
```

After subtracting `p` and dividing by `d`, the grid is

```math
\{i(t+j):i,j\in\{1,2,3\}\},
\qquad
t=\frac qd.
```

Whenever this normalized grid contains a four-term arithmetic progression, the assumed three-AP in `D` is impossible.

## Seven explicit forbidden integer ratios

For every integer

```math
c\in\{0,1,2,3,4,5,6\},
```

the fiber `D` cannot contain

```math
(c+1)d,
\qquad
(c+2)d,
\qquad
(c+3)d.
```

Equivalently, `D` contains no three consecutive multiples of a common step beginning at any of the first seven positions.

### Ratio `c=0`

The normalized grid contains

```math
1,\ 2,\ 3,\ 4,
```

using cells

```math
(1,1),\ (1,2),\ (1,3),\ (2,2).
```

### Ratio `c=1`

The normalized grid contains

```math
2,\ 4,\ 6,\ 8,
```

using cells

```math
(1,1),\ (1,3),\ (2,2),\ (2,3).
```

### Ratio `c=2`

The normalized grid contains

```math
3,\ 4,\ 5,\ 6,
```

using cells

```math
(1,1),\ (1,2),\ (1,3),\ (2,1).
```

### Ratio `c=3`

The normalized grid contains

```math
4,\ 6,\ 8,\ 10,
```

using cells

```math
(1,1),\ (1,3),\ (2,1),\ (2,2).
```

### Ratio `c=4`

The normalized grid contains

```math
6,\ 10,\ 14,\ 18,
```

using cells

```math
(1,2),\ (2,1),\ (2,3),\ (3,2).
```

### Ratio `c=5`

The normalized grid contains

```math
6,\ 12,\ 18,\ 24,
```

using cells

```math
(1,1),\ (2,1),\ (3,1),\ (3,3).
```

### Ratio `c=6`

The normalized grid contains

```math
18,\ 21,\ 24,\ 27,
```

using cells

```math
(2,3),\ (3,1),\ (3,2),\ (3,3).
```

In every case, multiplying by `d` and adding `p` produces a nontrivial four-term progression in `A`.  Thus

```math
\boxed{
\{(c+1)d,(c+2)d,(c+3)d\}
\not\subseteq D
\quad
(c=0,1,\dots,6).
}
```

These exclusions are consequences of the single condition that `mathcal U_3(D)` is 4-AP-free.  They are not evidence of a new depth-two extremal class.

## Application to extension fibers

For the dyadic block

```math
B=A\cap[N,2N),
```

define

```math
F_j(p)
=
|D_{j,p}|,
```

where

```math
D_{j,p}
=
\{d:p+d,p+2d,p+3d\in B\}.
```

Since `D_{j,p} subseteq [1,N/2]` and its first three dilates have a common translate inside `A`,

```math
\boxed{
F_j(p)
\le
s_4^{(3)}(N/2)
\le
\frac12 r_4(3N/2).
}
```

This replaces the earlier generic bound

```math
F_j(p)\le r_4(N/2)
```

by a bound in the correct inherited class.

## Forced-predecessor support bound

Let

```math
S_j=\{p:F_j(p)>0\}.
```

The extension-load identity and deletion bound give

```math
\sum_pF_j(p)
=
T_3(B)
\ge
|B|-r_3(N).
```

Since every nonzero fiber is bounded by `s_4^{(3)}(N/2)`,

```math
|S_j|s_4^{(3)}(N/2)
\ge
|B|-r_3(N).
```

Therefore

```math
\boxed{
|S_j|
\ge
\frac{|B|-r_3(N)}{s_4^{(3)}(N/2)}.
}
```

Using the crude comparison with `r_4`,

```math
\boxed{
|S_j|
\ge
\frac{2\bigl(|B|-r_3(N)\bigr)}{r_4(3N/2)}.
}
```

Thus every dense block either creates many distinct forbidden predecessors or produces a fiber near the extremal size of the three-dilate class.

## Hereditary closure under predecessor fibers

Let `D subseteq [1,M]` satisfy

```math
D\cup2D\cup3D
\text{ is 4-AP-free}.
```

For an integer `q`, define the predecessor fiber inside `D` by

```math
E_q(D)
=
\{d:q+d,q+2d,q+3d\in D\}.
```

Then

```math
q+E_q(D),
\qquad
q+2E_q(D),
\qquad
q+3E_q(D)
\subseteq D.
```

Hence

```math
q+\bigl(E_q(D)\cup2E_q(D)\cup3E_q(D)\bigr)
\subseteq D.
```

Since `D` is itself a subset of the 4-AP-free set `D union 2D union 3D`, it is 4-AP-free.  Translation therefore gives

```math
\boxed{
E_q(D)\cup2E_q(D)\cup3E_q(D)
\text{ is 4-AP-free}.
}
```

Thus the three-dilate class is closed under recursive predecessor-fiber extraction.

## Recursive normalized-mass identity

Let

```math
T_3(D)
=
\sum_q|E_q(D)|.
```

The same deletion argument gives

```math
T_3(D)
\ge
|D|-r_3(M).
```

Every child fiber lies in an interval of length at most `M/2`.  Therefore the sum of the child densities relative to their natural ambient scale satisfies

```math
\sum_q\frac{|E_q(D)|}{M/2}
=
\frac{2T_3(D)}M
\ge
2\left(
\frac{|D|}M-rac{r_3(M)}M
\right).
```

Equivalently,

```math
\boxed{
\sum_q \operatorname{dens}(E_q(D))
\ge
2\bigl(\operatorname{dens}(D)-r_3(M)/M\bigr).
}
```

Once `D` is above the Roth error scale, the total normalized mass of all recursive children is nearly twice the normalized mass of the parent.

## The actual recursion obstruction

The preceding inequality counts children with multiplicity.  Different predecessor fibers can overlap heavily, and the same direction can appear along many affine-tree paths.

Therefore the nearly doubling recursive mass does not yet contradict finite ambient size.  The central unresolved quantity is the overlap multiplicity of the affine-fiber tree.

The recursion does **not** automatically produce a chain

```math
s_4^{(3)}
\supsetneq
s_4^{(3,2)}
\supsetneq\cdots.
```

Instead, every generation remains inside the same hereditary three-dilate class while the number of affine representations grows.

## Immediate next task

Prove one of the following multiplicity statements:

1. **bounded-overlap extraction:** from the recursive children, select a large subfamily whose direction sets have controlled overlap, so the near-doubling of normalized mass becomes physical rather than formal;
2. **high-multiplicity contradiction:** show that a direction appearing in too many depth-`h` affine-fiber paths forces a four-term progression in the original set;
3. **tree-energy inequality:** bound the total depth-`h` path multiplicity by a quantity that grows more slowly than the lower bound produced by repeated linear extension mass.

This multiplicity problem, not a new extremal hierarchy, is the precise bottleneck in the concentrated extension branch.

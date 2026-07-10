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
3. a second-generation three-AP inside the fiber is forbidden for several explicit predecessor-to-step ratios;
4. this defines a stricter extremal function that controls concentration and the number of distinct forbidden predecessors.

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

This only improves the ordinary `r_4` bound by a constant factor, but it identifies the correct stricter extremal class for recursive concentration.

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

Whenever this normalized grid contains a four-term arithmetic progression, the assumed second-generation three-AP in `D` is impossible.

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

The first case includes the no-doubling obstruction in a stronger three-point form.

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

Thus every dense block either creates many distinct forbidden predecessors or produces a fiber near the extremal size of the stricter three-dilate class.

## Why the new extremal function matters

The full conjecture will not follow merely from the constant-factor estimate

```math
s_4^{(3)}(M)\le\frac12r_4(3M).
```

The possible gain is recursive:

- arbitrary 4-AP-free sets are controlled by `r_4`;
- first-generation concentrated fibers are controlled by `s_4^{(3)}`;
- second-generation concentrated fibers must also avoid the explicit affine-grid ratios above;
- deeper generations inherit increasingly many affine-grid exclusions.

This suggests a hierarchy

```math
r_4(M)
\supseteq
s_4^{(3)}(M)
\supseteq
s_4^{(3,2)}(M)
\supseteq\cdots
```

of progressively more rigid recursive fiber classes.

A useful theorem would show that the extremal density decays uniformly with generation depth.  Such a decay could convert repeated concentration into a contradiction while the spread branch accounts for the linear extension mass.

## Immediate next task

Define the depth-`h` affine-fiber class precisely and prove either:

1. a uniform density loss at each generation; or
2. a finite depth `h` for which every sufficiently large depth-`h` fiber necessarily contains a four-term progression.

The second-generation grid calculation above is the first nontrivial inherited obstruction in that hierarchy.

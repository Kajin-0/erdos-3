# Second-generation affine-fiber obstruction

## Status

Exact inherited structure for concentrated three-AP extension fibers.

The cross-scale extension-load construction produces

```math
D_{j,p}
=
\{d\ge1:p+d,p+2d,p+3d\in A\cap[N,2N)\}.
```

Such a fiber is more rigid than an arbitrary 4-AP-free subset of `[1,N/2]`:

1. its first three dilates have a 4-AP-free union;
2. it is disjoint from its double;
3. several explicit second-generation affine grids are forbidden;
4. the three-dilate class is hereditary under further predecessor-fiber extraction.

The final point corrects a tempting but false interpretation: recursion does not automatically create a strictly decreasing hierarchy of extremal classes.  It stays inside one hereditary class.  What grows is affine-tree multiplicity.

## Three-dilate inheritance

Let `A subset Z` be 4-AP-free and suppose

```math
p+D,
\qquad
p+2D,
\qquad
p+3D
\subseteq A
```

for a finite positive-integer set `D`.

Define

```math
\mathcal U_3(D)=D\cup2D\cup3D.
```

Then

```math
p+\mathcal U_3(D)\subseteq A,
```

so translation invariance gives

```math
\boxed{\mathcal U_3(D)\text{ is 4-AP-free}.}
```

In particular, `D` itself is 4-AP-free.

## No-doubling lemma

One has

```math
\boxed{D\cap2D=\varnothing.}
```

Indeed, if `d,2d in D`, then `d in D` gives

```math
p+d,\ p+2d,\ p+3d\in A,
```

while `2d in D` gives `p+4d in A`.  These four points form a 4-AP.

## The three-dilate extremal function

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

Since `D` and `2D` are disjoint,

```math
|D\cup2D\cup3D|\ge2|D|.
```

The union lies in `[1,3M]`, hence

```math
2|D|\le r_4(3M).
```

Therefore

```math
\boxed{
s_4^{(3)}(M)
\le
\frac12 r_4(3M).
}
```

This is only a constant-factor improvement over a generic `r_4` estimate, but it identifies the correct inherited class for concentrated fibers.

## Second-generation affine grid

Suppose the fiber `D` contains

```math
q+d,
\qquad
q+2d,
\qquad
q+3d
\in D,
\qquad d>0.
```

Then the original set contains the nine-point grid

```math
\boxed{
p+i(q+jd)\in A
\qquad(i,j\in\{1,2,3\}).
}
```

After subtracting `p` and dividing by `d`, this becomes

```math
\{i(t+j):i,j\in\{1,2,3\}\},
\qquad t=q/d.
```

Whenever this normalized grid contains a 4-AP, the assumed three-AP in `D` is impossible.

## Seven explicit forbidden integer ratios

For every

```math
c\in\{0,1,2,3,4,5,6\},
```

the set `D` cannot contain

```math
(c+1)d,
\qquad
(c+2)d,
\qquad
(c+3)d.
```

The corresponding 4-APs in the normalized grid are:

| `c` | forbidden 4-AP in `U_3(D)` |
|---:|---|
| 0 | `1,2,3,4` |
| 1 | `2,4,6,8` |
| 2 | `3,4,5,6` |
| 3 | `4,6,8,10` |
| 4 | `6,10,14,18` |
| 5 | `6,12,18,24` |
| 6 | `18,21,24,27` |

For example, when `c=0`, the cells

```math
(1,1),\ (1,2),\ (1,3),\ (2,2)
```

give `1,2,3,4`.  When `c=6`, the cells

```math
(2,3),\ (3,1),\ (3,2),\ (3,3)
```

give `18,21,24,27`.  The other rows follow by the same direct substitution.

Thus

```math
\boxed{
\{(c+1)d,(c+2)d,(c+3)d\}
\not\subseteq D
\quad(c=0,1,\dots,6).
}
```

These are consequences of the single condition that `U_3(D)` is 4-AP-free.  They do not define a new depth-two class.

## Application to dyadic extension fibers

Let

```math
B=A\cap[N,2N)
```

and

```math
F_j(p)=|D_{j,p}|.
```

Since `D_{j,p} subseteq [1,N/2]` and its first three dilates have a common translate inside `A`,

```math
\boxed{
F_j(p)
\le
s_4^{(3)}(N/2)
\le
\frac12r_4(3N/2).
}
```

Let

```math
S_j=\{p:F_j(p)>0\}.
```

The extension-load identity and deletion bound give

```math
\sum_pF_j(p)
=T_3(B)
\ge
|B|-r_3(N).
```

Consequently,

```math
\boxed{
|S_j|
\ge
\frac{|B|-r_3(N)}{s_4^{(3)}(N/2)}
\ge
\frac{2\bigl(|B|-r_3(N)\bigr)}{r_4(3N/2)}.
}
```

Thus a block with substantial linear extension mass either creates many distinct forbidden predecessors or contains a fiber close to the extremal size of the three-dilate class.

## Hereditary closure

Let `D subseteq [1,M]` satisfy

```math
D\cup2D\cup3D
\text{ is 4-AP-free}.
```

For an integer `q`, define

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

Therefore

```math
q+\bigl(E_q(D)\cup2E_q(D)\cup3E_q(D)\bigr)
\subseteq D.
```

Since `D` is 4-AP-free, translation gives

```math
\boxed{
E_q(D)\cup2E_q(D)\cup3E_q(D)
\text{ is 4-AP-free}.
}
```

Hence the three-dilate class is closed under recursive predecessor-fiber extraction.

## Recursive normalized-mass identity

Let

```math
T_3(D)=\sum_q|E_q(D)|.
```

The deletion argument gives

```math
T_3(D)\ge|D|-r_3(M).
```

Every child fiber lies in an interval of length at most `M/2`.  Thus the sum of child densities at their natural scale satisfies

```math
\sum_q\frac{|E_q(D)|}{M/2}
=
\frac{2T_3(D)}M
\ge
2\left(
\frac{|D|}M-
\frac{r_3(M)}M
\right).
```

Equivalently,

```math
\boxed{
\sum_q\operatorname{dens}(E_q(D))
\ge
2\bigl(\operatorname{dens}(D)-r_3(M)/M\bigr).
}
```

Above the Roth error scale, the total normalized mass of all children is nearly twice that of the parent.

## The actual recursion obstruction

The preceding inequality counts fibers with multiplicity.  Different children can overlap heavily, and the same direction can occur along many affine-tree paths.

Therefore the formal near-doubling of recursive mass does not contradict finite ambient size.  Recursion remains inside the same hereditary class; it does not automatically produce a chain of strictly smaller extremal classes.

The unresolved object is the overlap multiplicity of the affine-fiber tree.

## Immediate next task

Prove one of the following:

1. **bounded-overlap extraction:** select a large family of children with controlled overlap, converting formal mass growth into physical mass growth;
2. **high-multiplicity contradiction:** show that a direction represented by too many depth-`h` affine paths forces a 4-AP;
3. **tree-energy inequality:** upper-bound total depth-`h` path multiplicity by a quantity growing more slowly than the repeated lower bound from linear extension mass.

This multiplicity problem, not a new extremal hierarchy, is the precise bottleneck in the concentrated extension branch.

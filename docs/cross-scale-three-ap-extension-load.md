# Cross-scale three-AP extension load

## Status

Exact cross-scale mechanism with linear block-density mass.

The single-scale high-`J` route produces quantities of order `alpha^3` at the natural threshold.  This note identifies a different object whose total mass is linear in the dyadic block density:

> Every three-term progression inside a dyadic block has a unique predecessor.  In a 4-AP-free set that predecessor must be absent.  A deletion argument shows that the total predecessor load is at least the block size minus `r_3` of the block length.

The load has a useful concentration alternative: if many three-APs share one predecessor, their common differences form a large 4-AP-free set with three affine copies inside the original block.

## Dyadic block setup

Let

```math
I_j=[N,2N),
\qquad
N=2^j,
```

and put

```math
B=A\cap I_j,
\qquad
|B|=\alpha_jN.
```

Assume `A` contains no nontrivial four-term arithmetic progression.

## Backward extension load

For an integer `p`, define

```math
F_j(p)
=
|\{d\ge1:
p+d,p+2d,p+3d\in B\}|.
```

Thus `F_j(p)` counts three-term progressions in `B` whose unique predecessor is `p`.

If

```math
p+d,p+2d,p+3d\in[N,2N),
```

then

```math
\frac N2\le p<2N.
```

Therefore

```math
\operatorname{supp}F_j
\subseteq
[N/2,2N),
```

which meets only the current and immediately preceding dyadic scale.

## Exact forbidden-predecessor identity

For every `p in A`,

```math
\boxed{F_j(p)=0.}
```

Indeed, if `F_j(p)>0`, then for some `d>=1`,

```math
p,p+d,p+2d,p+3d\in A,
```

which is a nontrivial four-term arithmetic progression.

Let

```math
T_3(B)
=
|\{(y,d):d\ge1,\ y,y+d,y+2d\in B\}|.
```

The map

```math
(y,d)\mapsto p=y-d
```

is a bijection from three-term progressions in `B` to the objects counted by `F_j`.  Hence

```math
\boxed{
\sum_pF_j(p)=T_3(B).
}
```

All of this extension load is supported on the complement of `A`.

## Linear supersaturation by deletion

Let `r_3(N)` denote the largest size of a three-AP-free subset of an interval of length `N`.

Then

```math
\boxed{
T_3(B)\ge |B|-r_3(N).
}
```

### Proof

Starting from `B`, repeatedly remove one element from a remaining nontrivial three-term progression.  Each removal destroys at least one progression that was present at that stage.  The process therefore uses at most the original number `T_3(B)` of progressions.

The final set is three-AP-free, so it has size at most `r_3(N)`.  Consequently,

```math
|B|-T_3(B)\le r_3(N),
```

which proves the claim.

Combining the identities gives

```math
\boxed{
\sum_pF_j(p)
\ge
\alpha_jN-r_3(N).
}
```

After normalizing by the block length,

```math
\boxed{
\frac1N\sum_pF_j(p)
\ge
\alpha_j-\frac{r_3(N)}N.
}
```

Unlike the natural skew-interaction statistic, this quantity is linear in `alpha_j`.

## Summation across logarithmic scales

Define

```math
W_j(p)=\frac{F_j(p)}{2^j}.
```

Then

```math
\sum_pW_j(p)
\ge
\alpha_j-\frac{r_3(2^j)}{2^j}.
```

A point `p` lies in the support range `[2^{j-1},2^{j+1})` for at most two values of `j`.  Thus the loads are local across adjacent logarithmic scales rather than being spread over the entire past.

If one uses any quantitative Roth bound satisfying

```math
\sum_j\frac{r_3(2^j)}{2^j}<\infty,
```

then reciprocal divergence

```math
\sum_j\alpha_j=\infty
```

forces

```math
\boxed{
\sum_j\sum_pW_j(p)=\infty.
}
```

Hence a 4-AP-free divergent candidate must generate an infinite amount of normalized backward-extension load, all supported outside `A` and localized to neighboring scales.

## Concentration fibers

For fixed `j,p`, define the difference fiber

```math
D_{j,p}
=
\{d\ge1:p+d,p+2d,p+3d\in B\}.
```

Then

```math
|D_{j,p}|=F_j(p),
```

and

```math
p+D_{j,p},
\qquad
p+2D_{j,p},
\qquad
p+3D_{j,p}
```

are all subsets of `B`.

Moreover,

```math
D_{j,p}\subseteq[1,N/2].
```

## Fiber inheritance lemma

Every `D_{j,p}` is 4-AP-free.

### Proof

If

```math
d,d+q,d+2q,d+3q\in D_{j,p},
```

then already the first affine copy gives

```math
p+d,\ p+d+q,\ p+d+2q,\ p+d+3q\in B\subseteq A,
```

contradicting 4-AP-freeness.

Therefore

```math
\boxed{D_{j,p}\text{ is 4-AP-free}.}
```

In particular,

```math
F_j(p)=|D_{j,p}|\le r_4(N/2).
```

## Spread-or-recursive-structure dichotomy

Let

```math
S_j=\{p:F_j(p)>0\}.
```

For any parameter `M>=1`, either

```math
|S_j|\ge M,
```

so the block generates at least `M` distinct forbidden predecessors, or there exists `p` such that

```math
F_j(p)
\ge
\frac{T_3(B)}{M}
\ge
\frac{\alpha_jN-r_3(N)}{M}.
```

In the second branch, `A` contains three affine copies of a 4-AP-free set

```math
D_{j,p}\subseteq[1,N/2]
```

of that size:

```math
p+D_{j,p},
\quad
p+2D_{j,p},
\quad
p+3D_{j,p}
\subseteq A.
```

The harmonic mass of the fiber has the crude lower bound

```math
\sum_{d\in D_{j,p}}\frac1d
\ge
\frac{2|D_{j,p}|}{N}.
```

Thus a concentrated extension load transfers a linear fraction of the block-density mass into a smaller-scale 4-AP-free difference set, together with a rigid three-copy embedding into `A`.

## Why this is different from the high-J route

The high-`J` route begins with a four-point skew count at natural scale `alpha_j^4N` and obtains normalized popularity of order `alpha_j^3`.

The extension-load identity instead starts from three-term progressions and uses the exact inequality

```math
T_3(B)\ge |B|-r_3(N).
```

Once the `r_3` error is negligible, its normalized mass is order

```math
\alpha_j.
```

This is the correct scale for reciprocal divergence.

## Remaining obstruction

Divergence of total extension load does not itself contradict 4-AP-freeness, because the complement of `A` can absorb arbitrarily much load over infinitely many scales.

The next step must exploit one of the two branches:

1. **spread:** show that sufficiently many forbidden predecessors force a quantitative loss of harmonic mass in adjacent blocks;
2. **concentration:** iterate or classify the large fibers `D_{j,p}` and their three affine copies.

The concentration branch is particularly structured.  Repeated concentration produces a nested affine tree resembling a variable-base digit construction.  Fixed finite-state versions of such constructions are already known to have convergent reciprocal sum, suggesting that an infinite divergent example would require unbounded state/complexity across scales.

## Immediate next task

Prove a quantitative iteration lemma for concentrated extension fibers:

> If a positive fraction of the linear extension mass repeatedly concentrates into fibers `D_{j,p}`, then either the affine-copy tree creates a four-term progression, or its branching complexity grows quickly enough to force reciprocal convergence.

This is now the most promising cross-scale target because it preserves the linear block-density quantity required by harmonic divergence.

# Harmonic star recursion

## Status

Exact recursive reformulation of the primitive weighted extension system.

For a 4-AP-free dyadic block `B`, primitive extraction produces a weighted incidence relation between forbidden predecessors `p` and retained steps `s`.  Reorganizing the same incidences by the three actual block points

```math
p+s,
\qquad
p+2s,
\qquad
p+3s
```

gives a family of smaller 4-AP-free step sets.

The total harmonic mass of these step-set children is at least twice the parent block's harmonic mass, up to the summable Roth error.

This is a genuine supercritical harmonic branching identity.  The remaining issue is overlap: the same step may occur in many star children.

## Primitive incidence setup

Let

```math
B=A\cap[N,2N),
\qquad
|B|=\alpha N,
```

where `A` is 4-AP-free.

For each predecessor `p`, let

```math
S_p\subseteq
\{s:p+s,p+2s,p+3s\in B\}
```

be the primitive initial-vertex subset from the multiplicative-chain extraction.

Define

```math
\mathcal R(B)
=
\{(p,s):s\in S_p\}.
```

Its retained harmonic step load is

```math
\mathcal P(B)
=
\sum_{(p,s)\in\mathcal R(B)}\frac1s.
```

The primitive weighted extension theorem gives

```math
\boxed{
\mathcal P(B)
\ge
\frac23\left(
\alpha-\frac{r_3(N)}N
\right).
}
```

Every retained step satisfies

```math
1\le s\le N/2.
```

## Star children at a block point

For `x in B` and a role

```math
i\in\{1,2,3\},
```

define

```math
T_i(x)
=
\{s:
 (x-is,s)\in\mathcal R(B)
\}.
```

Equivalently, `s in T_i(x)` precisely when a retained three-term progression

```math
p+s,p+2s,p+3s
```

has `x` as its `i`-th point.

Thus:

- `T_1(x)` consists of retained steps for progressions beginning at `x`;
- `T_2(x)` consists of retained steps for progressions centered at `x`;
- `T_3(x)` consists of retained steps for progressions ending at `x`.

Every star child lies in

```math
[1,N/2].
```

## Each star child is 4-AP-free

Fix `x` and `i`.  Suppose

```math
s,\ s+r,\ s+2r,\ s+3r\in T_i(x)
```

with `r ne 0`.

Choose a branch index

```math
k\in\{1,2,3\},
\qquad
k\ne i.
```

For every `t in T_i(x)`, the corresponding progression contains

```math
x+(k-i)t.
```

Therefore `B` contains

```math
x+(k-i)s,
```

```math
x+(k-i)(s+r),
```

```math
x+(k-i)(s+2r),
```

```math
x+(k-i)(s+3r).
```

These form a nontrivial four-term arithmetic progression with common difference `(k-i)r`, contradiction.

Hence

```math
\boxed{
T_i(x)\text{ is 4-AP-free for every }x\in B,\ i\in\{1,2,3\}.
}
```

## The three children at one point are disjoint

For fixed `x`, the sets

```math
T_1(x),
\qquad
T_2(x),
\qquad
T_3(x)
```

are pairwise disjoint.

Indeed, suppose the same step `s` belonged to two roles `i<j`.  Then there would be two retained progressions of common difference `s`, one placing `x` in role `i` and one placing `x` in role `j`.

Their predecessors differ by

```math
(j-i)s\in\{s,2s\}.
```

Two common-difference-`s` triples whose predecessors differ by `s` or `2s` combine to contain four consecutive points of an `s`-progression, creating a 4-AP in `B`.

Therefore

```math
\boxed{
T_1(x),T_2(x),T_3(x)
\text{ are pairwise disjoint.}
}
```

This is a local three-way split of the retained step set at each root point.

## Exact harmonic mass identity

Define the harmonic mass of a finite step set by

```math
H(T)=\sum_{s\in T}\frac1s.
```

Every incidence `(p,s) in mathcal R(B)` contributes the same weight `1/s` to exactly three star children:

```math
s\in T_1(p+s),
```

```math
s\in T_2(p+2s),
```

```math
s\in T_3(p+3s).
```

Conversely, every star-child membership arises from one retained incidence.

Therefore

```math
\boxed{
\sum_{x\in B}
\sum_{i=1}^3
H(T_i(x))
=
3\mathcal P(B).
}
```

Combining with the primitive lower bound gives

```math
\boxed{
\sum_{x\in B}
\sum_{i=1}^3
H(T_i(x))
\ge
2\left(
\alpha-\frac{r_3(N)}N
\right).
}
```

## Comparison with parent harmonic mass

Let

```math
H(B)=\sum_{b\in B}\frac1b.
```

Since `B subseteq [N,2N)`,

```math
\frac{\alpha}{2}
\le
H(B)
\le
\alpha.
```

Hence

```math
\boxed{
\sum_{x\in B}
\sum_{i=1}^3
H(T_i(x))
\ge
2H(B)-2\frac{r_3(N)}N.
}
```

Thus, up to the Roth error, the total harmonic mass of the smaller 4-AP-free star children is at least twice the harmonic mass of the parent block.

The children live at integer scale at most `N/2`, so this is a scale-descending harmonic branching statement.

## Dyadic decomposition of the children

A child `T_i(x) subseteq [1,N/2]` need not lie in one dyadic shell.  Decompose it as

```math
T_i(x)
=
\bigcup_{k<j}
T_i(x)\cap[2^k,2^{k+1}),
\qquad N=2^j.
```

The harmonic masses add exactly:

```math
H(T_i(x))
=
\sum_{k<j}
H\bigl(T_i(x)\cap[2^k,2^{k+1})\bigr).
```

Every shell remains 4-AP-free.  Therefore the star recursion can be iterated after dyadically resolving each child.

No harmonic mass is lost in this shell decomposition.

## Cross-scale branching consequence

For a collection of dyadic parent blocks, the total Roth error

```math
\sum_j\frac{r_3(2^j)}{2^j}
```

is finite.

Consequently, if the root harmonic mass diverges, then repeated application of the star identity formally generates a scale-descending family of 4-AP-free descendants whose total harmonic mass grows by a factor asymptotically at least `2` per generation, until branches reach the Roth-error scale.

Schematically,

```math
\text{parent harmonic mass}
\longmapsto
\text{total child harmonic mass}
\gtrsim
2\times\text{parent mass}.
```

This is stronger and cleaner than the earlier normalized-cardinality recursion because the conserved quantity is exactly the reciprocal weight relevant to the original conjecture.

## Overlap multiplicity

The identity counts children with multiplicity.  A step `s` can belong to many star children.

For a fixed step `s`, let

```math
Q_s
=
\{p:(p,s)\in\mathcal R(B)\}.
```

The corresponding triples are pairwise disjoint, so `s` occurs in exactly

```math
3|Q_s|
```

star children, at the distinct points

```math
Q_s+s,
\qquad
Q_s+2s,
\qquad
Q_s+3s.
```

Thus the total child mass identity may be rewritten as

```math
\sum_s\frac{3|Q_s|}{s}
=
3\mathcal P(B).
```

The column bound

```math
3|Q_s|\le |B|
```

controls one generation, but does not prevent large multiplicity over a deep recursive tree.

## Why the depth-two counterexample does not invalidate the identity

Sparse finite-avoidance constructions can create arbitrarily many depth-two lifts sharing a terminal direction and root points.  Therefore maximum overlap is not uniformly bounded.

The star recursion supplies additional quantitative hypotheses absent from those examples:

1. total harmonic child mass is forced to be supercritical;
2. this lower bound must persist over many scales;
3. all children arise simultaneously from primitive row-column incidence systems;
4. the summable Roth errors limit how much mass can terminate cheaply.

The unresolved problem is therefore weighted mass-regular overlap, not arbitrary pointwise overlap.

## Revised main target

Prove a stopping-time or energy theorem for the star recursion:

> A 4-AP-free dyadic block cannot generate, over many generations, total harmonic descendant mass growing like `2^h` unless a summable amount of mass terminates at the Roth-error scale.

Equivalently, one needs an upper bound on the **weighted multiplicity** with which the same small step can recur among mass-regular star descendants.

This is now the clearest recursion compatible with the original reciprocal-sum quantity.
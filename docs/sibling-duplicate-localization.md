# Localization of duplicated sibling terminal progressions

## Status

Exact refinement of the sibling two-layer multiplicity theorem.

In the multiplicity-resolved deletion-DAG recursion, every recursive child lifts to a translated subset of the same parent four-term-progression-free set `D`. After structural thinning, each parent point belongs to at most one structural lifted child and at most one middle-fiber lifted child.

This note proves that a three-term progression duplicated across two sibling child states can occur only in one specific overlap type:

```math
\boxed{
\text{middle multiplicity fiber}
\cap
\text{spanning-forest component child}.
}
```

It cannot occur between two structural children, between two middle-fiber children, or between a middle fiber and a merge-difference child.

---

# 1. The lifted recursive families

Let the selected parent progressions be

```math
(a_i,b_i,c_i),
\qquad
q_i=|b_i-a_i|.
```

The recursive middle-fiber child for a repeated step `r` lifts to the sponsor subset

```math
A_r^+
=
\{a_i:q_i=r\}\setminus\{\min\{a_i:q_i=r\}\}.
```

The structural children lift to subsets of two types.

## Spanning-forest type

For a chosen spanning-forest component `C`, the component-translation child lifts to

```math
C^+=C\setminus\{\min C\}.
```

## Merge-difference type

For a target vertex `v`, let

```math
I_v=\{a_i:a_i\to v\}.
```

The merge-difference child lifts to

```math
I_v^+=I_v\setminus\{\min I_v\}.
```

Structural thinning retains at most one structural occurrence per parent point. Consequently the retained structural lifted subsets are pairwise disjoint.

The sets `A_r^+` are also pairwise disjoint, because every deleted sponsor belongs to exactly one selected progression and therefore has exactly one selected step `r`.

Hence a parent point can occur in two recursive sibling lifts only when it belongs to one middle-fiber set `A_r^+` and one structural set.

---

# 2. Merge-difference intersections have size at most two

Fix a repeated middle step `r`. The coordinated side-anchor rule depends only on `r`, so there is a sign

```math
\sigma(r)\in\{-1,+1\}
```

such that a sponsor `a in A_r^+` has outgoing deletion-DAG targets

```math
a+\sigma(r)r,
\qquad
a+2\sigma(r)r.
```

Suppose also that

```math
a\in I_v.
```

Then `v` is one of those two targets. Therefore

```math
a=v-\sigma(r)r
```

or

```math
a=v-2\sigma(r)r.
```

There are at most two possibilities for `a`. Thus

```math
\boxed{
|A_r^+\cap I_v^+|\le2.
}
```

In particular, `A_r^+ cap I_v^+` cannot contain a nontrivial three-term arithmetic progression.

Therefore a terminal progression cannot be duplicated between a middle-fiber child and a merge-difference child.

---

# 3. Only middle-fiber/component overlap remains

Suppose a terminal step `q` is duplicated across two sibling recursive states. Lifting the two selected `q`-progressions to the parent set gives the same parent progression

```math
x-q,
\qquad
x,
\qquad
x+q
```

inside the intersection of the two lifted child subsets.

The two lifted subsets cannot both be structural, because retained structural subsets are pairwise disjoint.

They cannot both be middle fibers, because the repeated-step sponsor sets `A_r^+` are pairwise disjoint.

They cannot be a middle fiber and a merge-difference child, because such an intersection has size at most two.

Hence

```math
\boxed{
\text{every duplicated sibling terminal progression lies in }
A_r^+\cap C^+
}
```

for some repeated parent step `r` and some spanning-forest component `C`.

This is the unique remaining sibling-duplication mechanism.

---

# 4. The duplicated terminal step differs from the fiber step

Suppose `A_r^+` contained a three-term progression of step `r`:

```math
a,
\qquad
a+r,
\qquad
a+2r.
```

All three points are sponsors of selected progressions with common difference `r` and the same coordinated orientation.

If the orientation is positive, the selected progression sponsored by `a` contains

```math
a,\ a+r,\ a+2r,
```

while the selected progression sponsored by `a+r` contains

```math
a+r,\ a+2r,\ a+3r.
```

Thus

```math
a,\ a+r,\ a+2r,\ a+3r
```

is a four-term progression in `D`, a contradiction.

The negative orientation gives the reflected four-term progression.

Therefore

```math
\boxed{
A_r^+\text{ contains no three-term progression of step }r.
}
```

Consequently, if a sibling terminal step `q` is duplicated through `A_r^+ cap C^+`, then

```math
\boxed{q\ne r.}
```

---

# 5. Additional forbidden low ratios

The same grid argument rules out several nearby ratios.

If

```math
q=kr
```

for `k in {1,2,3}`, the three sponsor progressions of step `r` based at

```math
a,\quad a+q,\quad a+2q
```

contain four consecutive points on the `r`-lattice. Hence `D` contains a four-term progression.

Interchanging `q` and `r` gives the reciprocal exclusions. Thus a duplicated progression in `A_r^+` must satisfy

```math
\boxed{
\frac qr\notin
\left\{
1,2,3,\frac12,\frac13
\right\}.
}
```

The ratio statement is only a first local exclusion; it is not claimed to be a complete classification.

---

# 6. Interpretation

The sibling two-layer theorem reduced arbitrary sibling multiplicity to at most two center layers. The present localization shows that the second layer is not generic. It can arise only when:

1. three sponsors of one repeated parent step `r` lie in a common spanning-forest component child;
2. those sponsors themselves form a three-term progression of a different step `q`;
3. the ratio `q/r` avoids the immediately forbidden values above.

Thus the remaining sibling problem is no longer arbitrary cross-state overlap. It is a specific interaction between repeated-step sponsor fibers and spanning-forest connectivity.

The next finite target is to classify or bound three-term progressions inside

```math
A_r^+\cap C^+.
```

A proof that this intersection is always three-term-progression-free would collapse the sibling two-layer theorem to a one-layer theorem and resolve all terminal multiplicity among siblings exactly.

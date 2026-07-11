# Sponsored three-AP binary recursion

## Status

Exact sparse reformulation of the coordinated harmonic branching construction.

The deletion proof of three-term-progression supersaturation can be strengthened by retaining a family of progressions with distinct sponsor elements.  Restricting the child construction to this sparse family preserves the full `8/3` harmonic lower bound, while every parent element sponsors at most two child memberships.

This removes the need to solve a global matching problem between all side and middle child states.

## Sponsored deletion family

Let

```math
D\subseteq[N,2N)
```

be finite and four-term-progression-free.  Starting with `D`, repeatedly:

1. choose a nontrivial three-term progression in the current set;
2. choose one of its three points as a sponsor;
3. record the progression and sponsor;
4. delete the sponsor.

Stop when the remaining set is three-term-progression-free.

If the recorded family is `mathcal F`, then the sponsors are distinct and

```math
\boxed{
|\mathcal F|
\ge
|D|-r_3(N).
}
```

Indeed, the process terminates with at most `r_3(N)` elements, and every iteration deletes exactly one new sponsor.

Write every recorded progression as

```math
y,
\qquad
y+q,
\qquad
y+2q,
```

with `q>0`.  Since all three points lie in an interval of length `N`,

```math
\boxed{q\le N/2.}
```

## Selected weighted load

Define

```math
\mathcal L_*(D)
=
\sum_{P\in\mathcal F}\frac1{q(P)}.
```

Because `q(P)<=N/2`,

```math
\mathcal L_*(D)
\ge
\frac2N|\mathcal F|.
```

Hence

```math
\boxed{
\mathcal L_*(D)
\ge
2\left(
\frac{|D|}{N}
-
\frac{r_3(N)}N
\right).
}
```

Thus the sparse sponsored family retains the same linear lower bound previously obtained from all three-term progressions.

## Coordinated side children

For a recorded progression of step `q`, use the global side color

```math
\epsilon(q)=v_2(q)\pmod2.
```

- If `epsilon(q)=0`, place `q` in the first-point side child anchored at `y`.
- If `epsilon(q)=1`, place `q` in the last-point side child anchored at `y+2q`.

Let the resulting sparse side children be denoted by

```math
C_u^*.
```

Every recorded progression contributes to exactly one side membership, so

```math
\boxed{
\sum_u H(C_u^*)
=
\mathcal L_*(D).
}
```

Each `C_u^*` is a subset of the corresponding full coordinated side child.  Therefore:

1. `C_u^*` is four-term-progression-free;
2. `C_u^*,2C_u^*,3C_u^*` are pairwise disjoint.

## Coordinated middle children

Define

```math
\chi(q)=v_2(q)-v_3(q)\pmod3.
```

Partition the sponsored load into the three `chi`-colors and choose a color `c_*` carrying maximum load.  Then

```math
\sum_{P\in\mathcal F:
\chi(q(P))=c_*}
\frac1{q(P)}
\ge
\frac13\mathcal L_*(D).
```

For every selected progression, place `q` in the middle child anchored at `y+q`.  Denote the sparse middle children by

```math
M_v^*.
```

Then

```math
\boxed{
\sum_vH(M_v^*)
\ge
\frac13\mathcal L_*(D).
}
```

Again each sparse middle child is a subset of a full coordinated middle child, so it is four-term-progression-free and its first three dilates are pairwise disjoint.

## Sparse eight-thirds branching

Combining the side and middle masses,

```math
\sum_uH(C_u^*)
+
\sum_vH(M_v^*)
\ge
\frac43\mathcal L_*(D).
```

Therefore

```math
\boxed{
\sum_uH(C_u^*)
+
\sum_vH(M_v^*)
\ge
\frac83
\left(
\frac{|D|}{N}
-
\frac{r_3(N)}N
\right).
}
```

Since

```math
H(D)\le\frac{|D|}{N},
```

one also has

```math
\boxed{
\sum_uH(C_u^*)
+
\sum_vH(M_v^*)
\ge
\frac83H(D)
-
\frac83\frac{r_3(N)}N.
}
```

Thus the full harmonic branching factor survives after sparsification.

## Canonical sponsor map

Every recorded progression has one distinct sponsor

```math
a(P)\in D.
```

It creates:

1. exactly one side membership of value `q(P)`;
2. either zero or one middle membership of the same value `q(P)`.

Consequently there is a canonical map from child membership occurrences to parent sponsors whose fibers have size at most two.

```math
\boxed{
\text{Every parent element sponsors at most two child occurrences.}
}
```

When two occurrences are created, they are precisely the coordinated side-middle pair belonging to the same base progression.

After dyadic shell resolution, each child occurrence remains attached to the same sponsor.  Hence the entire sparse recursive construction becomes a rooted binary mass-flow forest on element occurrences.

## Linear label potential

Let a sponsor `a` belong to the parent shell `[N,2N)`, and let its recorded progression have step `q`.  The sponsored child occurrences both have numerical label `q`, and

```math
q\le\frac N2\le\frac a2.
```

If there is one child,

```math
q\le a.
```

If there are two children,

```math
2q\le N\le a.
```

Thus, in all cases,

```math
\boxed{
\sum_{z\text{ sponsored by }a}z
\le a.
}
```

Summing over sponsors gives

```math
\boxed{
\sum_{\text{child occurrences }z}z
\le
\sum_{a\in D}a.
}
```

Iterating down the sponsor forest shows that the total sum of numerical labels at every depth is bounded by the corresponding root-label sum.

Equivalently, along each root sponsor `a_0`, the edge ratios satisfy a Kraft-type estimate

```math
\sum_{\text{depth-}h\text{ descendants }z}
\frac{z}{a_0}
\le1.
```

## Cardinality consequence

Because every sponsor has at most two children, the total number of depth-`h` element occurrences is at most

```math
\boxed{
2^h|D_0|.
}
```

Every numerical label also falls by at least a factor two along a sponsor edge.  Therefore a path beginning at a root value `a_0` has length at most

```math
\lfloor\log_2a_0\rfloor.
```

These facts give a canonical binary encoding of the sparse recursive tree.

## What this resolves

The full child-state graph may contain dense bipartite patterns, and selecting a matching can lose most middle-node mass.  Sponsored sparsification bypasses that problem:

- no middle child must be matched as an indivisible node;
- every retained harmonic atom comes from one selected progression;
- each progression has a distinct physical sponsor;
- the side-middle duplication is intrinsically binary.

Thus the global pairing ambiguity is removed at the level of element occurrences.

## Remaining limitation

The binary sponsor forest alone does not yet contradict harmonic growth.  Labels may fall rapidly, so reciprocal weights may increase much faster than the number of occurrences.

The current exact information is:

```math
\text{harmonic mass growth}
\gtrsim
\left(\frac83\right)^h,
```

while

```math
\text{occurrence count}
\le
2^h|D_0|
```

and

```math
\text{label sum}
\le
\sum_{a\in D_0}a.
```

A closing argument needs a multiscale potential interpolating between reciprocal mass and the conserved linear label sum.  The scale-compensated side-middle theorem is a candidate local ingredient: whenever the duplicated branch packs too efficiently, it exports harmonic credit to a lower scale.

## Next target

Construct a potential `Phi` on a multiset of labeled occurrences satisfying both:

1. the sparse sponsored recursion forces
   ```math
   \Phi(\text{children})
   \ge
   (1+\delta)\Phi(\text{parent})
   ```
   above the Roth-error scale;
2. the linear sponsor inequality and scale-export credits give a uniform upper bound for `Phi` in terms of the root set.

The sponsor forest provides the required canonical genealogy; the unresolved problem is the correct scale weight.
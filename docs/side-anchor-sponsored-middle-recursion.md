# Side-anchor-sponsored middle recursion

## Status

Exact specialization of the sponsored sparse three-AP recursion.

By always deleting the coordinated side anchor of a selected three-term progression, every sparse side child becomes a singleton.  Consequently every nonterminal recursive path is forced through middle-role children only.

This removes all persistent role ambiguity.  The price is that the large side harmonic load becomes terminal rather than contradictory; controlling that terminal load is a new explicit bottleneck.

## Side-anchor deletion process

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free.

While the current set contains a nontrivial progression

```math
y,
\qquad y+q,
\qquad y+2q,
```

choose one and delete its coordinated side anchor:

- delete `y` when
  ```math
  v_2(q)\equiv0\pmod2;
  ```
- delete `y+2q` when
  ```math
  v_2(q)\equiv1\pmod2.
  ```

Record the progression and continue until the remaining set is three-term-progression-free.

Let `mathcal F` be the recorded family.  Exactly one element is deleted at each step, so

```math
\boxed{
|\mathcal F|
\ge
|D|-r_3(N).
}
```

## Distinct side anchors

Every recorded progression is assigned the side anchor deleted at its selection step.

Once deleted, that point cannot occur in any later selected progression.  In particular it cannot be used again as a side anchor.  Therefore all recorded side anchors are distinct.

Let

```math
C_u^*
```

be the sparse coordinated side child at anchor `u`.  Since at most one selected progression has side anchor `u`,

```math
\boxed{|C_u^*|\le1.}
```

Every nonempty side child is therefore a singleton

```math
C_u^*=\{q\}.
```

A singleton contains no nontrivial three-term progression and produces no descendants under the recursive construction.

Hence:

```math
\boxed{
\text{all side branches terminate immediately.}
}
```

## Weighted selected load

As before, every selected step satisfies

```math
q\le N/2.
```

Define

```math
\mathcal L_*(D)
=
\sum_{P\in\mathcal F}\frac1{q(P)}.
```

Then

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

Because every selected progression creates exactly one singleton side child,

```math
\boxed{
\sum_uH(C_u^*)
=
\mathcal L_*(D).
}
```

Thus the terminal singleton side mass already satisfies

```math
\boxed{
\sum_uH(C_u^*)
\ge
2H(D)
-
2\frac{r_3(N)}N.
}
```

This is a large terminal mass, not a persistent one.

## Selected middle children

Partition the selected progressions by

```math
\chi(q)=v_2(q)-v_3(q)\pmod3
```

and choose a color `c_*` carrying maximum selected load.

For every selected progression with `chi(q)=c_*`, place `q` in the middle child anchored at `y+q`.  Denote these children by

```math
M_v^*.
```

Then

```math
\boxed{
\sum_vH(M_v^*)
\ge
\frac13\mathcal L_*(D)
\ge
\frac23\left(
\frac{|D|}{N}
-
\frac{r_3(N)}N
\right).
}
```

Every nonterminal child is one of these middle children.

## Persistent paths use only the middle role

Apply the same side-anchor deletion process independently inside every nontrivial middle child shell.

At every node:

1. all side children are singletons and terminate;
2. only selected middle children can continue.

Therefore every recursive path of length at least two has role word

```math
222\cdots2.
```

In the affine-lift notation, the branch coefficient set is always

```math
A_2=\{-1,+1\}.
```

A depth-`h` persistent path with anchors

```math
x_1,x_2,\ldots,x_h
```

and terminal direction `d` therefore generates the symmetric affine cube

```math
x_1
+\varepsilon_1x_2
+\varepsilon_1\varepsilon_2x_3
+\cdots
+\left(\prod_{j=1}^{h-1}\varepsilon_j\right)x_h
+\left(\prod_{j=1}^h\varepsilon_j\right)d,
```

where

```math
\varepsilon_j\in\{-1,+1\}.
```

The exact binary-tree lift theorem gives

```math
\boxed{
2^h|D_h|+(2^h-1)
\le
|D_0|.
}
```

Thus persistent paths have a simpler geometry than in the unrestricted role recursion.

## Canonical pairing at each sponsor

Each selected progression has one deleted side anchor as sponsor.

- Its singleton side child contains the base step `q`.
- If `chi(q)=c_*`, its middle child also contains `q`.

Hence every duplicated occurrence is canonically paired with a unique terminal side singleton.  There is no child-state matching problem and no possibility of three-role duplication.

## What the reduction gains

The persistent recursion now has:

1. one role only;
2. symmetric branch coefficients `{-1,+1}`;
3. a distinct deleted side-anchor sponsor for every selected progression;
4. immediate termination of every side branch;
5. a canonical terminal witness attached to every middle duplication.

Any overlap theorem for persistent paths may therefore assume a pure middle-role affine tree.

## Why this is not yet a proof

The persistent middle mass has only the guaranteed lower bound

```math
\sum_vH(M_v^*)
\ge
\frac23H(D)
-
\frac23\frac{r_3(N)}N,
```

which is not supercritical.

Most of the selected harmonic mass may terminate in the singleton side children.  Those terminal weights can be large because a selected progression may have a very small common difference `q`.

Thus the unresolved question becomes:

> Can the total harmonic mass of the terminal singleton differences created by side-anchor deletion be bounded or recursively charged to a smaller-scale four-term-progression-free structure?

A direct bound by the parent harmonic mass is false at one scale: many disjoint short three-term progressions may contribute large reciprocal step weight.

## Revised dichotomy

The side-anchor-sponsored construction yields a clean dichotomy at every node:

1. **persistent middle mass:** continues through a pure symmetric middle-role tree;
2. **terminal side mass:** consists of singleton common differences attached injectively to deleted parent anchors.

A successful proof may combine:

- a contraction or overlap theorem for the pure middle tree;
- a cross-scale charging theorem for the terminal singleton step load.

The latter is now the more concrete missing statement.
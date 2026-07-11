# Minimum-backbone aligned diamond counterexample

## Status

Explicit shell-compatible counterexample to a universal one-copy-per-anchor claim for the minimum-translation backbone recursion.

The same local three-term progression can occur simultaneously in

1. the minimum-translation backbone child;
2. a middle multiplicity-fiber child;

with the same inherited root translation anchor.

Thus the anchor-aligned branching diamond identified in

```text
docs/minimum-translation-backbone-recursion.md
```

is genuine.

---

## 1. Parent block

Fix an integer `N>=32` and let

```math
D_N
=
N+
\{0,1,2,16,17,18,21,22,23,26,27,28\}.
```

For example, taking `N=64` gives a subset of

```math
[64,128).
```

The unshifted pattern is

```math
G
=
\{0,1,2,16,17,18,21,22,23,26,27,28\}.
```

A direct check shows that `G`, and therefore every translate `D_N`, is four-term-progression-free.

---

## 2. Four selected progressions of step one

The coordinated orientation for step

```math
r=1
```

is positive because

```math
v_2(1)=0.
```

Select the four progressions

```math
N,N+1,N+2,
```

```math
N+16,N+17,N+18,
```

```math
N+21,N+22,N+23,
```

and

```math
N+26,N+27,N+28.
```

Delete the four sponsors in descending order

```math
N+26,
\quad N+21,
\quad N+16,
\quad N.
```

At every step the center and opposite endpoint remain present. Hence these are valid side-anchor deletions.

The selected step `r=1` occurs four times. Its centers are

```math
N+1,
\quad N+17,
\quad N+22,
\quad N+27.
```

The minimum center is `N+1`, whose sponsor is the parent minimum `N`.

---

## 3. Middle multiplicity-fiber child

Resolve the repeated middle label `r=1` by translating the nonrepresentative centers by the minimum center `N+1`.

The resulting fiber child is

```math
\Xi_1
=
\{16,21,26\}.
```

This is a three-term progression of terminal step

```math
q=5.
```

All three points lie in the standard dyadic shell

```math
[16,32).
```

---

## 4. Minimum-translation backbone child

The parent minimum is

```math
m=N.
```

The minimum-translation backbone is

```math
\mathcal B(D_N)
=
\{1,2,16,17,18,21,22,23,26,27,28\}.
```

Its dyadic shell `[16,32)` contains

```math
16,17,18,21,22,23,26,27,28.
```

In particular it contains the same local progression

```math
16,21,26
```

of step `q=5`.

---

## 5. Same anchor

Both children use the same root translation anchor.

- The middle multiplicity-fiber child is anchored at the representative sponsor `N`.
- The backbone child is anchored at the parent minimum `N`.

Thus the local progression

```math
16,21,26
```

occurs in two sibling states with identical root anchor `N`.

Equivalently, the same exact local progression is duplicated by one aligned middle-backbone branching event.

---

## 6. Sharp local statement

For the minimum-translation backbone recursion, one parent element creates at most

1. one middle multiplicity-resolved child occurrence;
2. one backbone child occurrence.

Therefore one parent state can produce at most two sibling copies of an exact local progression with one anchor.

The present example attains two. Hence

```math
\boxed{
\text{the one-parent same-anchor multiplicity bound }2
\text{ is sharp}.
}
```

---

## 7. What the example does not show

The aligned diamond does not self-replicate inside this gadget.

After translation by `N`, the duplicated progression is

```math
16,21,26.
```

Its minimum point is `16`, whereas the representative anchor `N` has already been removed from both child lifted subsets. Any descendant state must choose a new root anchor from its current lifted subset, so it cannot reuse anchor `N`.

Thus the example proves one aligned duplication event, not exponential persistence.

The remaining question is whether many distinct parent states can converge to the same anchor and independently create aligned diamonds. That is a predecessor-anchor convergence problem rather than a one-parent sibling problem.

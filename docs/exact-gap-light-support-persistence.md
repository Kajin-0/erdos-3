# Exact-gap light-support persistence

## Status

State-independent finite-persistence theorem for the only light-support case that can preserve the exact physical pair gap.

Under the canonical adjacent support rule, local-root-first completion semantics, capacity-aware reservation, and first appearance of pair identities, a chain of exact-gap multiplicity-one light transitions contains at most nine nonterminal pair identities. A final locally terminal support may add at most one last identity.

The finite constant is certified by an exhaustive two-syndetic four-AP-free lattice computation.

---

## 1. Equality in the light-support gap bound

Let one light role fiber use a canonical support pair `f` of gap `q`, with support multiplicity `m`. For every source target pair `e` of physical gap `D(e)`, the light condition gives

```math
q\le\frac{D(e)}m.
```

Suppose one source lineage preserves its exact gap:

```math
q=D(e)=D.
```

Then necessarily

```math
m=1.
```

Moreover the fiber is a singleton. Indeed its load contains `1/D`, while the complete light allowance is at most `1/q=1/D`. Any second positive source weight would exceed the allowance.

Thus every exact-gap light transition has:

```text
one source target pair;
one selected completion c;
one canonical support pair;
source gap = support gap = D;
support pair distinct from the reserved source pair.
```

---

## 2. Canonical witness geometry

Let the selected absent completion be `c`. Its canonical four-AP witness has step `D`, because the support pair has gap `D`.

Write the four witness positions as

```math
a,
\quad a+D,
\quad a+2D,
\quad a+3D,
```

and let `c` occupy the missing position.

The canonical support rule chooses the first adjacent root pair not incident to the missing position.

### Missing endpoint

If `c` is at witness position `0` or `3`, the canonical support pair has the third witness root as an actual adjacent three-AP completion. On its next processing it belongs to the local completed-edge class and terminates.

Endpoint-missing witnesses therefore cannot support two consecutive nonterminal exact-gap light transitions.

### Missing interior point

Only missing positions `1` and `2` can continue without an automatic local root.

---

## 3. Possible nonterminal shifts

Represent a physical gap-`D` pair by its left endpoint.

### Adjacent source completion

If `c` is an adjacent completion of the source pair, the distinct interior-witness support lies on the opposite side of `c`. The support left endpoint differs from the source left endpoint by

```math
\boxed{\pm3D.}
```

### Midpoint source completion

If `c` is the midpoint completion, then `D` is even. The distinct interior-witness support left endpoint differs by

```math
\boxed{\pm\frac{3D}{2}.}
```

No other nonterminal exact-gap shifts occur.

Put

```math
h=\frac{3D}{2}
```

when midpoint transitions are integral. In the adjacent-only odd-gap case one may instead use lattice unit `3D`.

After normalization, every consecutive nonterminal first-appearance pair changes its lattice index by

```text
1 or 2 in absolute value.
```

---

## 4. The left-endpoint lattice is four-AP-free

Every pair left endpoint is an ambient root. If four normalized left-endpoint indices formed an arithmetic progression, the corresponding four roots would form a four-term progression after affine rescaling.

Therefore the normalized first-appearance index set is four-AP-free.

Because each transition changes the index by at most two and the transition path is connected, the sorted index set has consecutive gaps at most two.

Thus exact-gap persistence reduces to the finite combinatorial question:

```text
How large can a four-AP-free integer set be if its successive gaps are at most 2?
```

---

## 5. Two-syndetic finite bound

Exact exhaustion of binary strings with:

```text
first symbol 1;
no substring 00;
no four occupied positions in arithmetic progression
```

has the profile

```text
length : valid strings
 1 : 1
 2 : 2
 3 : 3
 4 : 4
 5 : 6
 6 : 9
 7 : 8
 8 : 8
 9 : 12
10 : 11
11 : 9
12 : 6
13 : 3
14 : 4
15 : 3
16 : 1
17 : 0
```

The unique length-16 class has at most nine occupied positions, and no valid length-17 string exists.

Consequently every finite four-AP-free integer set with successive gaps at most two has

```math
\boxed{|S|\le9}
```

and diameter at most `15` after normalization.

---

## 6. Persistence theorem

A first-appearance chain of consecutive nonterminal exact-gap multiplicity-one light supports has at most nine distinct pair identities.

An endpoint-missing witness may emit one final equal-gap support, but that support has an actual local completion and terminates at the next processing. Therefore the complete exact-gap light episode has at most ten distinct pair identities, including a possible final local sink.

```math
\boxed{
\text{exact-gap light first appearances per episode}\le10.
}
```

This is a uniform state-independent bound.

---

## 7. Complete scale-preserving residue

The direct dyadic pair-gap theorem left two scale-preserving mechanisms:

```text
adjacent cross-shell actual-root swaps;
multiplicity-one light supports.
```

They now have finite first-appearance bounds:

```text
cross-shell swap episode     : at most 2 pair identities;
exact-gap light episode      : at most 10 pair identities.
```

If a multiplicity-one light transition has `q<D`, its integer physical gap strictly decreases. Within one dyadic gap shell there can be only finitely many such decreases before either a lower shell is reached or exact equality begins.

Thus no infinite first-appearance path can remain at one exact physical pair gap.

---

## 8. Remaining quantitative issue

The theorem bounds exact-gap episode length but does not yet give a scale-uniform bound on the number of strict integer decreases `q<D` that may occur inside one dyadic shell. That number can be as large as the shell width if treated only by order.

The remaining scale-preserving theorem must therefore weight strict within-shell gap decrease quantitatively, for example by:

```math
\log\frac{D_{\rm in}}{D_{\rm out}},
```

or by a discrete gap-defect potential, and combine it with the exact episode bounds above.

**Verifier:** `src/verify_exact_gap_light_persistence.py`.

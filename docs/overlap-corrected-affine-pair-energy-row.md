# Overlap-corrected affine pair-energy row

## Status

State-independent one-generation Bellman inequality for a point-disjoint retained affine child family produced by coordinated deletion.

It generalizes the pairwise root-disjoint affine pivot theorem. Root overlap is permitted. All latent-latent activation is handled by capacity-aware reserve matching with recursive export.

---

## 1. Retained affine children

Let `P` be the parent root universe. Let the retained affine children be

```math
S_{r_i}(Q_i)
=
\{q-r_i:q\in Q_i\},
\qquad i\in I.
```

Assume their numerical supports are pairwise disjoint.

For a terminal child, define only its current resource star

```math
\mathcal E_i^{\rm cur}
=
\{\{r_i,q\}:q\in Q_i\}.
```

For a recursive child, define its complete current-plus-latent resource family

```math
\mathcal E_i
=
\mathcal E_i^{\rm cur}
\cup
\binom{Q_i}{2}.
```

Every resource is a physical pair inside `P` and its pair weight equals the corresponding current or latent child weight.

Hence

```math
W(\mathcal E_i)
=
H(S_{r_i}(Q_i))
+
\mathbf 1_{i\text{ recursive}}J(Q_i).
```

---

## 2. Complete occurrence mass

Let

```math
\mathcal E_{\rm occ}
```

be the occurrence-tagged disjoint union of all child resource families, and let

```math
\mathcal F
=
\bigcup_i\mathcal E_i
```

be the physical first-appearance union.

Then

```math
\sum_i
\left(
H(S_{r_i}(Q_i))
+
\mathbf 1_{i\text{ recursive}}J(Q_i)
\right)
=
W(\mathcal E_{\rm occ}).
```

The exact owner-incidence decomposition gives

```math
W(\mathcal E_{\rm occ})
=
J(\mathcal F)
+
R_{\rm branch}.
```

Point-disjointness removes child-side recreation and owner cycle rank. Only parent-resource row-star branching remains.

---

## 3. Activation decomposition

Apply the exact activation row from

```text
docs/pair-activation-reserve-export-row.md.
```

This supplies:

```text
C_current: injective current-overlap occurrences;
D: duplicated latent demands;
R_used: matched center/opposite physical reserves;
X_middle: unmatched original middle-owner occurrences.
```

The exact branching identity is

```math
R_{\rm branch}
=
W(C_{\rm current})
+
J(R_{\rm used})
+
W(X_{\rm middle}).
```

Before matching, reserve the complete first-appearance union `F`. Thus the available reserve set is chosen outside `F`, and

```math
\mathcal F\cap R_{\rm used}=\varnothing.
```

Both sets lie inside the parent pair universe, so

```math
J(\mathcal F)+J(R_{\rm used})
=
J(\mathcal F\cup R_{\rm used})
\le
J(P).
```

---

## 4. Bellman row

Combining the preceding identities gives

```math
\begin{aligned}
&\sum_i
\left(
H(S_{r_i}(Q_i))
+
\mathbf 1_{i\text{ recursive}}J(Q_i)
\right)\\
&\qquad=
J(\mathcal F)
+
W(C_{\rm current})
+
J(R_{\rm used})
+
W(X_{\rm middle})\\
&\qquad\le
J(P)
+
W(C_{\rm current})
+
W(X_{\rm middle}).
\end{aligned}
```

Therefore

```math
\boxed{
\sum_i
\left(
H(S_{r_i}(Q_i))
+
\mathbf 1_{i\text{ recursive}}J(Q_i)
\right)
\le
J(P)
+
W(C_{\rm current})
+
W(X_{\rm middle}).
}
```

Equivalently,

```math
\boxed{
\sum_i
\left(
H(S_{r_i}(Q_i))
+
\mathbf 1_{i\text{ recursive}}J(Q_i)
\right)
-
W(C_{\rm current})
\le
J(P)+W(X_{\rm middle}).
}
```

This is the overlap-corrected affine pair-energy row.

---

## 5. Recovery of the root-disjoint theorem

If the child root sets are pairwise disjoint, then no parent resource can have two owners. Consequently

```math
C_{\rm current}=\varnothing,
\qquad
X_{\rm middle}=\varnothing,
```

and the row reduces to

```math
\sum_i
\left(
H(S_{r_i}(Q_i))+J(Q_i)
\right)
\le
J(P),
```

which is the affine pivot pair-energy theorem.

The new row therefore isolates exactly the correction required by root overlap.

---

## 6. Nature of the two residual occurrence families

### Current-overlap family

Every occurrence in `C_current` is one actual current/harmonic child term. It may be:

```text
terminal, in which case it enters the terminal sink ledger;
recursive, in which case it enters the direct activated-pair lineage ledger.
```

It is not anonymous pair-energy collision and must not be counted again as latent activation.

### Middle-export family

Every occurrence in `X_middle` is an original sponsor-owned pair occurrence in a retained middle shell of base

```math
L\le N/4.
```

Thus for the owner-scale moment

```math
\Theta_p(f;S)=\frac{S^p}{\operatorname{gap}(f)},
```

we have

```math
\Theta_p(X_{\rm middle})
\le
4^{-p}N^pW(D_{\rm export}).
```

In particular, at `p=1` the recursive activation residue contracts by a factor at most `1/4` and releases at least `3/4` of its parent critical mass.

---

## 7. Treewise interpretation

The parent pair energy now has four exact roles:

```text
first appearance of one child resource;
matched center/opposite reserve for one duplicated latent demand;
unspent pair capacity remaining for later pivots;
capacity excluded because it was already consumed by an earlier ledger.
```

The only outputs not absorbed into the parent physical pair union are named occurrences:

```text
current-overlap occurrences;
strictly lower-scale middle exports.
```

This eliminates anonymous root-overlap pair debt at one generation.

---

## 8. Remaining global theorem

A whole-tree proof must now control only:

1. recursive current-overlap occurrences through direct pair-lineage termination;
2. repeated middle exports through their `1/4` critical contraction and two-level depth release;
3. terminal-sink recreation;
4. first entry into the parent pair-energy potential `J(P)`;
5. the final comparison of entering pair energy with original reciprocal mass.

The local failure of root-disjointness no longer blocks the affine pair-energy Bellman architecture.

# Production-compatible overlap-corrected Bellman row

## Status

State-independent one-generation composition of:

```text
the overlap-corrected affine pair-energy row;
terminal-current stopping;
production-compatible direct discharge of recursive current-overlap occurrences;
recursive export of unmatched middle latent demands.
```

The theorem preserves exact ownership of parent pair capacity and parent three-AP edge occurrences. It does not discharge the entire parent pair potential a second time.

---

## 1. Affine child row

Let

```math
P\subseteq[N,2N)
```

be the parent root universe, and let the point-disjoint retained affine child family satisfy

```math
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
```

Here:

```text
J(P) pays child first appearances and matched center/opposite reserves;
C_current is the injective current-latent overlap occurrence family;
X_middle is the unmatched duplicated-latent middle occurrence family.
```

The physical pair identities underlying `C_current` already occur in the first-appearance union paid by `J(P)`. The term `W(C_current)` is an additional occurrence debt, not a second copy of physical pair capacity.

---

## 2. Terminal and recursive current overlap

Partition

```math
C_{\rm current}
=
C_{\rm term}
\sqcup
C_{\rm rec}
```

according to whether the unique current owner is terminal or recursive.

Then

```math
W(C_{\rm current})
=
W(C_{\rm term})+J(C_{\rm rec}),
```

because point-disjointness makes the recursive current physical identities distinct.

The terminal family leaves the recursive ledger. The recursive family is an activated occurrence-owned physical pair set and is sent through direct maximal-ambient discharge.

---

## 3. Occurrence-token partition for recursive current overlap

Let

```math
\mathscr E(P)
```

be the complete parent full-edge occurrence-token family, of mass

```math
W(\mathscr E(P))
=
\frac52\mathcal L_3(P).
```

Apply production-compatible direct discharge to the activated set

```math
A=C_{\rm rec}.
```

For every local completed pair, consume one deterministic parent edge occurrence. Let

```math
\mathscr E_{\rm free}
```

be the remaining edge-token family.

The production-compatible row gives

```math
\boxed{
J(C_{\rm rec})
+
W(\mathscr E_{\rm free})
\le
\frac52\mathcal L_3(P)
+
J(E_{\rm new})
+
W(H_{\rm rec})
+
W(H_{\rm term}).
}
```

Here:

```text
E_new is a genuinely new physical pair union;
H_rec is the occurrence-owned recursive heavy output;
H_term is the terminal heavy or obstruction sink output.
```

Capacity-aware light supports are included in `E_new`, and every physical output remains subject to the global exclusion ledger.

---

## 4. Combined Bellman inequality

Insert the direct-discharge estimate for `J(C_rec)` into the affine child row. This gives

```math
\begin{aligned}
&\sum_i
\left(
H(S_{r_i}(Q_i))
+
\mathbf 1_{i\text{ recursive}}J(Q_i)
\right)
+
W(\mathscr E_{\rm free})\\
&\qquad\le
J(P)
+
W(C_{\rm term})
+
\frac52\mathcal L_3(P)
+
J(E_{\rm new})
+
W(H_{\rm rec})
+
W(H_{\rm term})
+
W(X_{\rm middle}).
\end{aligned}
```

Therefore

```math
\boxed{
\begin{aligned}
\operatorname{Child}(P)
+
W(\mathscr E_{\rm free})
\le{}&
J(P)
+
\frac52\mathcal L_3(P)\\
&+
W(C_{\rm term})
+
J(E_{\rm new})\\
&+
W(H_{\rm rec})
+
W(H_{\rm term})
+
W(X_{\rm middle}),
\end{aligned}
}
```

where

```math
\operatorname{Child}(P)
=
\sum_i
\left(
H(S_{r_i}(Q_i))
+
\mathbf 1_{i\text{ recursive}}J(Q_i)
\right).
```

Dropping the nonnegative free-token term gives the weaker but simpler row

```math
\operatorname{Child}(P)
\le
J(P)
+
\frac52\mathcal L_3(P)
+
W(C_{\rm term})
+
J(E_{\rm new})
+
W(H_{\rm rec})
+
W(H_{\rm term})
+
W(X_{\rm middle}).
```

---

## 5. Ownership audit

Every resource has one role.

### Parent physical pair capacity

```text
child first appearance;
matched center/opposite latent reserve;
unspent future affine-pivot capacity.
```

These roles are disjoint subsets of `J(P)`.

### Parent full-edge occurrence capacity

```text
pay one local recursive current-overlap occurrence;
or remain in E_free.
```

One edge occurrence cannot do both.

### Additional occurrence outputs

```text
C_term: terminal current sink;
E_new: one new physical pair lineage;
H_rec: strictly lower-gap recursive heavy lineage;
H_term: terminal heavy/obstruction sink;
X_middle: strictly lower-owner-scale middle occurrence.
```

No parent physical pair is reused as both first-appearance capacity and a center/opposite reserve, because the complete first-appearance union is excluded before reserve matching.

---

## 6. Triangular coordinates

The recursive outputs have independent monotone coordinates.

### New direct pair lineages

`E_new` follows the direct-discharge pair-lineage theorem:

```text
physical dyadic gap never increases;
every first-appearance lineage terminates or recreates in finite time.
```

### Recursive heavy output

`H_rec` contracts physical dyadic gap by at least one level, or two levels in the outer role.

### Middle export

`X_middle` lies at owner scale at most `N/4`. At the critical owner-scale moment it contracts by a factor at most `1/4`.

### Terminal output

`C_term` and `H_term` leave the recursive ledger.

Thus every correction to the affine pair-energy row is either terminal, pathwise finite, lower-gap, or lower-owner-scale.

---

## 7. Why the parent pair potential remains

The term `J(P)` is not discharged in this composition because it has already been assigned to:

```text
child first appearances;
matched latent reserves;
future affine pivot capacity.
```

Applying direct discharge to all of `J(P)` simultaneously would spend the same physical pair capacity twice.

The remaining entry problem is therefore unchanged but sharper:

```math
\boxed{
\text{pay the first entry into }J(P)
\text{ once, then telescope it through the corrected affine tree.}
}
```

---

## 8. Remaining global theorem

The local current/latent overlap obstruction is closed. A complete proof must still:

1. pay the initial or newly entered parent pair potential `J(P)`;
2. pack the globally new pair union `E_new` across production owners;
3. control terminal-sink recreation;
4. sum direct finite lineages without losing their ownership labels;
5. combine the `7/4` first-appearance depth release with the `1/2` current and `1/4` middle owner-scale drops;
6. deduce dyadic reciprocal-density summability.

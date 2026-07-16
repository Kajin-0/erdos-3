# Production-compatible overlap-corrected Bellman row

## Status

State-independent one-generation composition of:

```text
the overlap-corrected affine pair-energy row;
production-compatible direct discharge of the complete parent pair potential;
terminal/current classification;
capacity-aware middle reserve export.
```

The parent pair energy is an intermediate Bellman potential and is eliminated completely. The free full-edge occurrence-token term prevents local three-AP production from being spent twice.

---

## 1. Overlap-corrected affine row

Let

```math
P\subseteq[N,2N)
```

be the parent root universe. For a point-disjoint retained affine child family, define

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

The overlap-corrected affine theorem gives

```math
\boxed{
\operatorname{Child}(P)
\le
J(P)
+
W(C_{\rm current})
+
W(X_{\rm middle}).
}
```

Here:

```text
J(P) is the complete intermediate parent pair potential;
C_current is the injective current-latent overlap occurrence family;
X_middle is the unmatched duplicated-latent middle occurrence family.
```

The internal proof partitions `J(P)` among child first appearances, matched center/opposite reserves, and unused pair capacity. That internal partition is used only to establish the displayed inequality.

---

## 2. Complete parent-pair discharge

Let

```math
\mathscr E(P)
```

be the complete full-edge occurrence-token family of the parent, with

```math
W(\mathscr E(P))
=
\frac52\mathcal L_3(P).
```

Activate the complete physical parent pair set

```math
A=\binom P2.
```

For every pair completed locally by a parent three-AP, consume one deterministic edge occurrence. Let

```math
\mathscr E_{\rm free}
```

be the remaining parent edge-token family.

Apply direct maximal-ambient discharge, capacity-aware light/heavy allocation, and terminal stopping to every pair in `A`. The production-compatible row gives

```math
\boxed{
J(P)
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

The output families are:

```text
E_new: one globally disjoint physical pair union outside the entering pair set;
H_rec: occurrence-owned recursive heavy output;
H_term: terminal heavy, maximality, or arithmetic-obstruction output.
```

Light support pairs are included in `E_new`. Every local edge occurrence used to discharge `J(P)` is removed from `E_free`.

---

## 3. Complete Bellman inequality

Add the nonnegative free-token family to the affine child row:

```math
\operatorname{Child}(P)
+
W(\mathscr E_{\rm free})
\le
J(P)
+
W(\mathscr E_{\rm free})
+
W(C_{\rm current})
+
W(X_{\rm middle}).
```

Substitute the complete parent-pair discharge inequality. This yields

```math
\boxed{
\begin{aligned}
\operatorname{Child}(P)
+
W(\mathscr E_{\rm free})
\le{}&
\frac52\mathcal L_3(P)
+
J(E_{\rm new})\\
&+
W(H_{\rm rec})
+
W(H_{\rm term})\\
&+
W(C_{\rm current})
+
W(X_{\rm middle}).
\end{aligned}
}
```

The intermediate parent pair potential `J(P)` has disappeared.

Dropping the nonnegative free-token term gives the weaker production-only row

```math
\boxed{
\operatorname{Child}(P)
\le
\frac52\mathcal L_3(P)
+
J(E_{\rm new})
+
W(H_{\rm rec})
+
W(H_{\rm term})
+
W(C_{\rm current})
+
W(X_{\rm middle}).
}
```

---

## 4. Why this does not double spend pair capacity

The two input inequalities use `J(P)` differently but compatibly.

### Affine inequality

`J(P)` is an intermediate numerical majorant for:

```text
one first occurrence of every child resource;
matched center/opposite reserve pairs;
unused affine pivot capacity.
```

### Direct-discharge inequality

The same intermediate scalar `J(P)` is paid by exactly one partition of parent resources:

```text
one parent edge occurrence for every local completed pair;
new physical pair output for cross-shell or light transfer;
recursive or terminal heavy output for the remaining holes.
```

The free-token term records every parent edge occurrence not consumed by local pair payment.

Combining

```math
\operatorname{Child}(P)\le J(P)+\text{corrections}
```

with

```math
J(P)+W(\mathscr E_{\rm free})\le\text{production outputs}
```

is ordinary Bellman elimination of an intermediate potential. `J(P)` is present once, then removed. No physical pair or edge occurrence appears twice in the final row.

---

## 5. Current-overlap classification

Partition

```math
C_{\rm current}
=
C_{\rm term}
\sqcup
C_{\rm rec}.
```

### Terminal current overlap

`C_term` enters the terminal sink ledger and does not recurse.

### Recursive current overlap

Every occurrence in `C_rec` lies in a retained child shell of base

```math
L\le\frac N2,
```

because every positive difference of two roots in `[N,2N)` is less than `N`.

Thus at the critical owner-scale moment

```math
\Theta_1(f;S)=\frac S{\operatorname{gap}(f)},
```

recursive current overlap contracts by a factor at most `1/2` before it enters its next direct pair-lineage step.

---

## 6. Middle-export classification

Every occurrence in `X_middle` lies in a retained middle shell of base

```math
L\le\frac N4.
```

Hence

```math
\Theta_1(X_{\rm middle})
\le
\frac14N\,W(D_{\rm export}).
```

At raw pair weight, every such export conserves its demand mass but releases at least two dyadic owner levels.

For one physical parent resource, at most one recursive current-overlap occurrence and at most one unmatched middle occurrence survive. Therefore its complete overlap residue satisfies

```math
\boxed{
\Theta_1(\text{overlap residue of }f)
\le
\left(\frac12+\frac14\right)
\frac N{\operatorname{gap}(f)}
=
\frac34\Theta_1(f;N).
}
```

---

## 7. Other output coordinates

### New pair union

`E_new` enters the occurrence-owned direct pair-lineage ledger. Physical dyadic gap never increases, and every first-appearance lineage terminates or recreates in finite time.

### Recursive heavy output

`H_rec` contracts physical dyadic gap by at least one level, or by at least two levels in the outer role.

### Terminal output

`H_term` and `C_term` leave the recursive ledger.

### Free edge tokens

`E_free` remains on the left of the strong row. It is unused production capacity and can supply later first-appearance branching without being regenerated.

---

## 8. Exact resource roles

Every parent object has one role.

### Parent edge occurrence

```text
pay one local parent pair;
or remain in E_free.
```

### Parent pair potential unit

```text
serve as an intermediate affine first-appearance/reserve majorant;
then be eliminated through direct discharge.
```

### Child overlap occurrence

```text
terminal current sink;
recursive current continuation at scale at most N/2;
recursive middle export at scale at most N/4.
```

### Direct-discharge output

```text
new pair lineage;
recursive lower-gap heavy lineage;
terminal obstruction output.
```

The final inequality contains no anonymous collision or unpaid entering pair-energy term.

---

## 9. Remaining global theorem

The local pair-energy entry problem is closed at one generation. The surviving whole-tree tasks are now:

1. pack `E_new` across production owners and merge physical recreations;
2. sum finite direct pair lineages globally rather than pathwise;
3. control recreation of terminal current and heavy sinks;
4. combine the exact `7/4` first-appearance depth release with the `1/2` current and `1/4` middle owner-scale contractions;
5. preserve the free-edge occurrence ledger across generations;
6. deduce dyadic reciprocal-density summability.

The active obstruction is global first-appearance and recreation packing, not local pair-energy entry or latent activation.

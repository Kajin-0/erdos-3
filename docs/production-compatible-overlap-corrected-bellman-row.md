# Production-compatible economical activation Bellman row

## Status

State-independent one-generation composition of:

```text
exact affine child resource accounting;
current-latent separation;
capacity-aware latent reserve matching and recursive export;
production-compatible direct discharge of only the physical pair resources actually used.
```

The parent pair potential is eliminated without activating the unused quadratic pair universe. The free full-edge occurrence-token term prevents local three-AP production from being spent twice.

---

## 1. Exact economical pair set

Let

```math
P\subseteq[N,2N)
```

be the parent root universe and let the point-disjoint retained affine child family have complete current-plus-recursive-latent occurrence family

```math
\mathcal E_{\rm occ}.
```

Let

```math
\mathcal F
```

be the physical first-appearance union of child resources.

Before latent reserve matching, mark every pair in `F` unavailable. Let

```math
R_{\rm used}
```

be the matched center/opposite physical reserve union. Then

```math
\mathcal F\cap R_{\rm used}=\varnothing.
```

Define the economical activated pair set

```math
\boxed{
U=\mathcal F\sqcup R_{\rm used}.
}
```

Only pairs in `U` are required to majorize the retained child family. Unused pairs in `binom(P,2)` are never activated.

---

## 2. Exact affine occurrence identity

Define

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

The current/latent activation theorem supplies two occurrence-tagged correction families:

```text
C_current: one current occurrence for every current-latent overlap;
X_middle: one original middle-owner occurrence for every unmatched latent duplicate.
```

The complete occurrence mass has the exact partition

```math
\boxed{
\operatorname{Child}(P)
=
J(U)
+
W(C_{\rm current})
+
W(X_{\rm middle}).
}
```

This identity is stronger than the coarse inequality using `J(P)`. It records only the physical pair capacity actually exposed.

---

## 3. Economical direct discharge

Let

```math
\mathscr E(P)
```

be the complete parent full-edge occurrence-token family, with

```math
W(\mathscr E(P))
=
\frac52\mathcal L_3(P).
```

Apply direct maximal-ambient discharge only to

```math
A=U.
```

For every pair in `U` completed locally by a parent three-AP, consume one deterministic edge occurrence. Let

```math
\mathscr E_{\rm free}
```

be the remaining edge-token family.

The production-compatible direct-discharge theorem gives

```math
\boxed{
J(U)
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
E_new is one genuinely new physical pair union disjoint from U;
H_rec is occurrence-owned recursive heavy output;
H_term is terminal heavy, maximality, or arithmetic-obstruction output.
```

No pair outside the economical activated set enters this discharge row.

---

## 4. Complete Bellman inequality

Add the free-token family to the exact affine identity and substitute the economical direct-discharge estimate:

```math
\begin{aligned}
\operatorname{Child}(P)
+
W(\mathscr E_{\rm free})
&=
J(U)
+
W(\mathscr E_{\rm free})\\
&\quad+
W(C_{\rm current})
+
W(X_{\rm middle})\\
&\le
\frac52\mathcal L_3(P)
+
J(E_{\rm new})\\
&\quad+
W(H_{\rm rec})
+
W(H_{\rm term})\\
&\quad+
W(C_{\rm current})
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

The intermediate pair energy has disappeared, and no unused parent pair has been converted into a new lineage.

Dropping the nonnegative free-token term gives

```math
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
```

---

## 5. Why the row is ownership-safe

### Physical pair first appearance

Every pair in `F` pays exactly one child resource occurrence.

### Matched latent reserve

Every pair in `R_used` pays exactly one duplicated latent occurrence and is disjoint from `F`.

### Economical activation

The union `U=F disjoint-union R_used` is discharged once. No pair outside `U` is activated.

### Parent edge occurrence

One full-edge token either:

```text
pays one locally completed pair in U;
or remains in E_free.
```

### Unmatched latent duplicate

The original sponsor-owned middle occurrence remains in `X_middle`; no new occurrence is created.

Thus every physical pair and every production occurrence has one role.

---

## 6. Recursive correction coordinates

Partition

```math
C_{\rm current}=C_{\rm term}\sqcup C_{\rm rec}.
```

### Current overlap

`C_term` stops. Every occurrence in `C_rec` lies in a retained child shell of base

```math
L\le\frac N2.
```

At the critical owner-scale moment

```math
\Theta_1(f;S)=\frac S{\operatorname{gap}(f)},
```

recursive current overlap contracts by a factor at most `1/2`.

### Middle export

Every occurrence in `X_middle` lies at owner scale

```math
L\le\frac N4,
```

so it contracts by a factor at most `1/4`.

For one physical parent resource, at most one recursive current occurrence and at most one unmatched middle occurrence survive. Hence

```math
\boxed{
\Theta_1(\text{complete overlap residue of }f)
\le
\frac34\Theta_1(f;N).
}
```

At raw weight, the current occurrence releases at least one dyadic owner level and the middle occurrence releases at least two.

---

## 7. Other output coordinates

### New pair union

`E_new` enters the occurrence-owned direct pair-lineage ledger. Physical dyadic gap never increases, and every first-appearance lineage terminates or recreates in finite time.

### Recursive heavy output

`H_rec` contracts physical dyadic gap by at least one level, or by at least two levels in the outer role.

### Terminal output

`H_term` and `C_term` leave the recursive ledger.

### Free edge tokens

`E_free` remains on the left of the strong row. It is production capacity not consumed by economical local pair payment.

---

## 8. Significance

The earlier pair-energy program faced two distinct problems:

```text
prepaying the complete quadratic pair universe;
reusing parent three-AP edge production for both local payment and branching.
```

The economical row removes both:

```text
only U is activated;
used local edge occurrences are removed from E_free;
root overlap is handled by current terms, matched reserves, or lower-scale exports.
```

This is the local economical pair-activation theorem required by the affine Bellman architecture.

---

## 9. Remaining global theorem

The local pair-energy entry and latent-activation problems are closed. The surviving whole-tree tasks are:

1. pack `E_new` across production owners and merge physical recreations;
2. sum finite direct pair lineages globally rather than pathwise;
3. control recreation of terminal current and heavy sinks;
4. combine the exact `7/4` first-appearance depth release with the `1/2` current and `1/4` middle contractions;
5. preserve the free-edge occurrence ledger across generations;
6. deduce dyadic reciprocal-density summability.

The active obstruction is global first-appearance/recreation packing, not local pair activation.

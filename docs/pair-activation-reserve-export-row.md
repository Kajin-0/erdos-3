# Pair-activation reserve-export row

## Status

State-independent exact raw-weight identity for a point-disjoint retained affine child family produced by one completed coordinated deletion schedule.

The row separates:

```text
physical first appearance;
current-latent occurrence overlap;
latent owner degree at most two;
center/opposite reserve matching;
recursive continuation of unmatched middle occurrences.
```

The raw identity remains valid. The corrected universal middle-owner scale is `L <= N/2`, not `N/4`.

---

## 1. Parent resource owners

Let `F` be the set of distinct parent root-pair resources exposed by the child family. For one resource `f`, let

```math
c_f\in\{0,1\}
```

be its current-owner count and

```math
\ell_f\in\{0,1,2\}
```

its recursive latent-owner count.

Coordinated deletion gives the stronger total bound

```math
\boxed{c_f+\ell_f\le2.}
```

One physical first-appearance token pays one owner whenever `c_f+ell_f>0`. The raw occurrence excess is

```math
R_{\rm branch}
=
\sum_f
\frac{(c_f+\ell_f-1)_+}{\operatorname{gap}(f)}.
```

---

## 2. Current-latent occurrence term

Because `c_f` is zero or one,

```math
(c_f+\ell_f-1)_+
=
c_f\mathbf 1_{\ell_f>0}
+
(\ell_f-1)_+.
```

Let `C_current` contain the unique current occurrence for each repeated current-latent resource. Then

```math
W(C_{\rm current})
=
\sum_f
c_f\mathbf 1_{\ell_f>0}
\frac1{\operatorname{gap}(f)}.
```

This occurrence belongs to the ordinary current/harmonic ledger. It is not a second copy of physical pair capacity.

---

## 3. Duplicated latent demands

Since `ell_f<=2`, the genuine duplicated latent set is

```math
D=\{f:\ell_f=2\}.
```

Every `f in D` has exactly one backbone latent owner and one middle latent owner.

If the middle owner is generated at step `d`, it supplies two equal-gap physical reserves

```math
C_d(f),
\qquad
O_d(f),
```

and one original sponsor-owned middle occurrence `tilde f`.

All have raw weight

```math
\frac1{\operatorname{gap}(f)}.
```

---

## 4. Capacity-aware reserve matching

Let `R_0` be the physical pair set already owned by earlier accounting. Delete those vertices from the center/opposite reserve graph and choose a maximum demand-to-reserve matching.

Define:

```text
D_match  = matched duplicated demands;
D_export = unmatched duplicated demands;
R_used   = matched physical reserve union;
X_middle = {tilde f : f in D_export}.
```

Then

```math
R_{\rm used}\cap R_0=\varnothing,
```

and every physical pair in `R_used` is used once.

---

## 5. Exact activation identity

The duplicated latent mass satisfies

```math
\boxed{
W(D)
=
J(R_{\rm used})
+
W(X_{\rm middle}).
}
```

Combining first appearance, current overlap, and duplicated latent allocation gives

```math
\boxed{
W_{\rm occ}
=
J(\mathcal F)
+
W(C_{\rm current})
+
J(R_{\rm used})
+
W(X_{\rm middle}).
}
```

Equivalently,

```math
\boxed{
R_{\rm branch}
=
W(C_{\rm current})
+
J(R_{\rm used})
+
W(X_{\rm middle}).
}
```

This is a raw reciprocal-weight identity. Every occurrence has one named role.

---

## 6. Corrected recursive scale release

Every exported occurrence in `X_middle` lies in a retained middle shell of base `L`. Because every middle label is a positive difference of two parent roots in `[N,2N)`,

```math
\boxed{L\le\frac N2.}
```

For

```math
\Theta_p(f;S)
=
\frac{S^p}{\operatorname{gap}(f)},
```

we have

```math
\boxed{
\Theta_p(X_{\rm middle})
\le
2^{-p}N^pW(D_{\rm export}).
}
```

In dyadic-depth form, each exported occurrence releases at least one owner level:

```math
\Lambda(D_{\rm export};N)
-
\Lambda(X_{\rm middle})
\ge
W(D_{\rm export}).
```

The former factor `4^{-p}` and two-level release are withdrawn.

---

## 7. Full-availability cycle form

If all center/opposite reserves are available, a connected reserve component `K` exports exactly

```math
\max(0,\beta(K)-1)
```

middle occurrences, where `beta(K)` is the component cycle rank.

For component gap `g`, the recursive raw mass is

```math
\frac{\max(0,\beta(K)-1)}g.
```

The rank-two raw no-go has three exported occurrences of total mass

```math
\frac1{50}+\frac1{100}+\frac1{50}=\frac1{20}.
```

---

## 8. Owner-exponent warning

The raw matching identity does not imply a small critical overlap coefficient.

A coordinated middle child can occur at shell base `N/2`. At owner exponent one:

```text
one latent occurrence may cost one full parent pair unit;
two latent owners may cost two parent units;
latent-latent residual may equal one full parent unit.
```

This is attained by the shell-valid witness in

```text
docs/coordinated-middle-half-scale-critical-no-go.md.
```

At exponent two, every current or latent owner family fits inside the original parent pair capacity, so reserve matching is unnecessary for owner-multiplicity control.

---

## 9. Production compatibility

The raw row uses no occurrence twice:

```text
one physical first-appearance token pays the first owner;
one current occurrence carries current-latent overlap;
one unused reserve pays each matched duplicate;
one original middle occurrence carries each unmatched duplicate.
```

The reserve matching is performed after earlier physical ownership decisions, so it is compatible with direct discharge and global exclusion.

---

## 10. Remaining global problem

The raw anonymous activation collision is classified, but treewise obligations remain:

1. telescope current and unmatched middle occurrence flow at their actual owner scales;
2. preserve global first use of physical reserves;
3. coordinate direct edge/support capacity;
4. retain source-indexed terminal and recreation value;
5. choose between the collision-free exponent-two row and a genuinely critical exponent-one occurrence/depth mechanism;
6. recover summability of the original raw reciprocal coordinate.

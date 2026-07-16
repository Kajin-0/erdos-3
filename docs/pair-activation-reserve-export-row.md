# Pair-activation reserve-export row

## Status

State-independent exact one-generation activation identity for a point-disjoint retained affine child family produced by one completed coordinated deletion schedule.

The row combines:

```text
owner-incidence first appearance;
current-latent separation;
latent owner degree at most two;
capacity-aware center/opposite reserve matching;
recursive export of every unmatched middle occurrence.
```

It closes the local repeated pair-activation accounting. It does not by itself prove global reciprocal summability.

---

## 1. Parent resource owners

Let

```math
\mathcal F
```

be the set of distinct parent root-pair resources exposed by a point-disjoint retained child family.

For

```math
f\in\mathcal F
```

write

```math
c_f\in\{0,1\}
```

for the number of current owners and

```math
\ell_f\in\{0,1,2\}
```

for the number of recursive latent owners.

The bounds follow from:

```text
point-disjointness for current owners;
coordinated-deletion sponsor uniqueness for latent owners.
```

The raw occurrence multiplicity is

```math
m_f=c_f+\ell_f.
```

One parent first-appearance pair token pays one occurrence whenever `m_f>0`. The remaining row-star branching excess is

```math
R_{\rm branch}
=
\sum_{f\in\mathcal F}
\frac{(c_f+\ell_f-1)_+}{\operatorname{gap}(f)}.
```

---

## 2. Current-latent term

Because `c_f` is zero or one,

```math
(c_f+\ell_f-1)_+
=
c_f\mathbf 1_{\ell_f>0}
+
(\ell_f-1)_+.
```

Let

```math
C_{\rm current}
```

be the occurrence-tagged current pair family consisting of the unique current occurrence for every resource with

```math
c_f=1,
\qquad
\ell_f>0.
```

Point-disjointness makes these current occurrences injective. Hence

```math
W(C_{\rm current})
=
\sum_f
c_f\mathbf 1_{\ell_f>0}
\frac1{\operatorname{gap}(f)}.
```

The current owner may be terminal or recursive. Its weight belongs to the ordinary current/harmonic ledger and is not a second latent activation charge.

---

## 3. Genuine duplicated latent demands

Since

```math
\ell_f\le2,
```

we have

```math
(\ell_f-1)_+
=
\mathbf 1_{\ell_f=2}.
```

Define the duplicated latent demand set

```math
D
=
\{f\in\mathcal F:\ell_f=2\}.
```

Every `f in D` has exactly:

```text
one recursive backbone owner;
one recursive middle-fiber owner.
```

Therefore

```math
W(D)
=
\sum_f
\frac{(\ell_f-1)_+}{\operatorname{gap}(f)}.
```

Let the middle owner of `f` arise from selected step `d`. It supplies two equal-gap physical parent reserves

```math
C_d(f),
\qquad
O_d(f),
```

and one original sponsor-owned middle occurrence

```math
\widetilde f.
```

All three have weight `w(f)`.

---

## 4. Capacity-aware reserve allocation

Let

```math
R_0
```

be the physical parent-pair set already owned by earlier accounting operations. The available reserves are the center/opposite pairs outside `R_0`.

For each gap, form the demand-to-available-reserve incidence graph and choose a maximum matching as in

```text
docs/reserve-pseudoforest-recursive-export.md.
```

Let

```text
D_match  = matched duplicated demands;
D_export = unmatched duplicated demands;
R_used   = matched physical reserve-pair union;
X_middle = {tilde f : f in D_export}.
```

Then

```math
W(D)
=
J(R_{\rm used})
+
W(X_{\rm middle}).
```

Moreover,

```math
R_{\rm used}\cap R_0=\varnothing,
```

and every physical pair in `R_used` is used once.

---

## 5. Exact activation row

Combining the preceding partitions gives

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

Equivalently, if

```math
W_{\rm occ}
=
\sum_f
\frac{c_f+\ell_f}{\operatorname{gap}(f)}
```

is the complete current-plus-latent occurrence mass and

```math
J(\mathcal F)
=
\sum_{f:m_f>0}
\frac1{\operatorname{gap}(f)}
```

is parent-resource first appearance, then

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

This is an identity. Every unit of occurrence mass has exactly one named role.

---

## 6. Recursive scale release

Every occurrence in `X_middle` lies in a retained middle shell

```math
M\subseteq[L,2L)
```

with

```math
L\le\frac N4.
```

For

```math
\Theta_p(f;S)
=
\frac{S^p}{\operatorname{gap}(f)},
\qquad p>0,
```

we obtain

```math
\boxed{
\Theta_p(X_{\rm middle})
\le
4^{-p}
N^pW(D_{\rm export}).
}
```

In dyadic-depth form, define

```math
\Lambda(f;S)
=
\frac{\log_2S}{\operatorname{gap}(f)}.
```

Then

```math
\begin{aligned}
\Lambda(D_{\rm export};N)
-
\Lambda(X_{\rm middle})
&=
\sum_{f\in D_{\rm export}}
\frac{\log_2(N/L_f)}{\operatorname{gap}(f)}\\
&\ge
2W(D_{\rm export}).
\end{aligned}
```

Thus

```math
\boxed{
\text{every recursively exported activation unit releases at least two dyadic levels.}
}
```

---

## 7. Full-availability cycle form

If no center/opposite reserve has been pre-consumed, one full reserve component `K` of gap `g` exports exactly

```math
\max(0,\beta(K)-1)
```

middle occurrences. Hence its recursive mass is

```math
\frac{\max(0,\beta(K)-1)}g.
```

The rank-two no-go example therefore has three exported occurrences of total mass

```math
\frac1{50}+\frac1{100}+\frac1{50}
=
\frac1{20}.
```

The pair-activation row remains exact despite failure of the pseudoforest conjecture.

---

## 8. Production compatibility

The row uses no occurrence twice:

```text
one parent first-appearance token pays the first owner;
one current occurrence carries the current-latent term;
one unused physical reserve pays each matched latent duplicate;
one original middle occurrence carries each unmatched latent duplicate.
```

The available-reserve set is formed only after all earlier physical-pair ownership decisions. Therefore direct discharge, cross-shell swaps, light supports, and reserve allocation can share one global exclusion ledger.

---

## 9. Remaining global problem

The local anonymous activation collision has been eliminated. The surviving treewise obligations are now explicit:

```text
ordinary current/harmonic continuation;
first-appearance physical pair resources;
uniquely consumed physical reserves;
strictly lower-scale exported middle occurrences;
terminal sink occurrences.
```

The next Bellman theorem must combine:

1. the exact first-appearance coefficient and its `7/4` critical depth release;
2. the two-level release of `X_middle`;
3. direct pair-lineage termination;
4. global first use of physical reserves;
5. terminal-sink recreation control;
6. the final comparison with original reciprocal mass.

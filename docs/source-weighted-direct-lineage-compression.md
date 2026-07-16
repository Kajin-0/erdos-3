# Source-weighted direct-lineage compression

## Status

State-independent macrostep theorem for occurrence-owned source-weighted direct pair lineages.

Every source occurrence is followed through deterministic direct discharge until it is locally paid, reaches a terminal sink, or repeats a physical pair identity already seen on that same lineage. The complete finite path is then replaced by one terminal or recreation token without increasing source mass or physical-gap moment.

---

## 1. Source-owned direct lineage

Let one activated source occurrence be

```math
\omega_0=(o,e_0,m),
```

where:

```text
o is the immutable production owner;
e_0 is the entering physical pair;
0<m<=1/gap(e_0) is the inherited source mass.
```

At every direct-discharge step, deterministic completion priority selects exactly one outcome:

```text
local parent-edge payment;
cross-shell adjacent-root swap;
light support transfer;
recursive heavy transfer;
terminal heavy or obstruction sink.
```

For a light or heavy fiber, the source mass assigned to the outgoing occurrence is the exact inherited role load. It is never replaced by full target-pair capacity.

---

## 2. First-appearance path

Maintain the ordered list of physical pair identities

```math
e_0,e_1,\ldots.
```

If an outgoing pair identity already occurred earlier on the same lineage, stop before treating it as a new first appearance.

The direct pair-lineage theorem proves that this stopping procedure is finite. Indeed:

```text
physical gap never increases;
strict gap decreases cannot continue indefinitely;
cross-shell equal-gap swaps form an involution;
equal-gap light episodes have uniformly bounded first-appearance length;
terminal output stops immediately.
```

Thus every source occurrence has a finite deterministic macro-outcome.

---

## 3. Macro-output classes

Partition the source occurrence family into three classes.

### Local payment

The lineage reaches a locally completed pair and consumes one parent three-AP edge occurrence. No outgoing pair token remains.

### Terminal output

The lineage reaches a terminal heavy, maximality, or arithmetic-obstruction sink. Retain one occurrence-tagged terminal token carrying the inherited source mass.

### Recreation output

The lineage first attempts to enter a physical pair

```math
e_j=e_i
```

with `i<j`. Retain one recreation token

```math
(o,e_i,m,\mathcal C),
```

where `C` records the finite cycle segment

```math
e_i,e_{i+1},\ldots,e_{j-1}.
```

The repeated target is not counted as a new physical pair capacity.

---

## 4. Source-mass conservation

Let

```math
\mu_{\rm in}
```

be a finite source occurrence measure. Let

```math
\mu_{\rm term}
```

and

```math
\mu_{\rm recreate}
```

be the terminal and recreation macro-output measures.

Every entering occurrence has one macro-outcome. Local payment removes its pair-lineage mass; terminal and recreation outcomes retain the inherited mass. Therefore

```math
\boxed{
W(\mu_{\rm term})
+
W(\mu_{\rm recreate})
\le
W(\mu_{\rm in}).
}
```

Equality holds after including the mass locally consumed by edge occurrences.

Different production owners may generate the same terminal or recreation identity. Their occurrence labels remain separate, or their masses may be aggregated without changing the total source measure.

---

## 5. Gap-moment monotonicity

For

```math
\Phi_p(\mu)
=
\sum_e\mu(e)G(e)^p,
\qquad p\ge0,
```

every individual direct step is nonexpanding. Consequently the macrostep is nonexpanding:

```math
\boxed{
\Phi_p(\mu_{\rm term})
+
\Phi_p(\mu_{\rm recreate})
\le
\Phi_p(\mu_{\rm in}).
}
```

If a lineage contains a midpoint transfer, a multiplicity-at-least-two light transfer, or a recursive heavy transfer, its macro-output has strictly smaller dyadic gap moment for every `p>0`.

Only a lineage composed entirely of adjacent-root swaps and multiplicity-one light transfers can preserve dyadic gap scale.

---

## 6. Bounded equal-gap cycle geometry

An equal-gap recreation cycle has only two possible local mechanisms.

### Adjacent-root cycle

The cross-shell involution returns to the entering pair after at most one new physical identity. Its simple cycle has length two.

### Light-support cycle

The exact-gap persistence theorem bounds a nonterminal first-appearance episode by at most nine identities, or ten including a final local support. Therefore the first repeated-pair cycle has uniformly bounded simple support.

Mixed equal-gap episodes remain bounded because encountering an actual-root completion invokes the involution after at most one further new identity.

Thus every scale-preserving recreation token carries a finite bounded local certificate rather than an unbounded path history.

---

## 7. Production-compatible macro row

Apply source-weighted direct discharge to an economical pair set `U`, and then compress every recursive direct occurrence to its macro-outcome.

Let

```text
E_free: unused parent full-edge occurrences;
T_dir: terminal macro-output measure;
C_dir: recreation macro-output measure.
```

Then

```math
\boxed{
J(U)+W(E_{\rm free})
=
\frac52\mathcal L_3(P)
+
W(T_{\rm dir})
+
W(C_{\rm dir}),
}
```

with the convention that local payments have already been removed through the edge-token partition.

At parent owner scale `N`,

```math
\boxed{
NJ(U)+NW(E_{\rm free})
=
\frac52N\mathcal L_3(P)
+
NW(T_{\rm dir})
+
NW(C_{\rm dir}).
}
```

No open-ended direct recursive queue remains after the macrostep.

---

## 8. Critical Bellman interface

Substituting the macro row into the critical economical activation theorem gives

```math
\boxed{
\begin{aligned}
\sum_i\mathcal V_i
+
NW(E_{\rm free})
\le{}&
\mathcal B(P)\\
&+
NW(T_{\rm dir})\\
&+
NW(C_{\rm dir})\\
&+
\mathcal R_{\rm crit}.
\end{aligned}
}
```

The only direct-discharge outputs are now named terminal and recreation tokens. Every long finite transport history has been eliminated.

---

## 9. Remaining global obstruction

The direct transport problem is no longer a recurrence problem. The remaining global questions are:

```text
how many production owners can create the same recreation certificate;
how terminal sink occurrences are first-appearance packed;
how recreation and terminal tokens consume depth release;
how free edge occurrences telescope through child production.
```

Source-weighted path length and target collisions create no additional mass. The unresolved term is cross-owner sink multiplicity, not transport along one lineage.

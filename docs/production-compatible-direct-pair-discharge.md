# Production-compatible direct pair discharge

## Status

State-independent refinement of the direct maximal-ambient activated-pair theorem.

The theorem shows that local three-AP edge payment and full-edge branching use one exact occurrence-token partition. Paying an activated local pair removes one physical edge occurrence from the branching output; every unconsumed edge token remains available. The local edge capacity is therefore not double counted.

---

## 1. Full-edge occurrence tokens

Let

```math
P\subseteq[N,2N)
```

be four-AP-free. For every three-AP

```math
Q=\{a,a+d,a+2d\}\subseteq P
```

introduce its three tagged physical edge tokens

```math
(Q,\{a,a+d\}),
\qquad
(Q,\{a+d,a+2d\}),
\qquad
(Q,\{a,a+2d\}).
```

Give a token the physical pair weight of its edge. The total occurrence-token mass is

```math
\boxed{
W(\mathscr E(P))
=
\frac52\mathcal L_3(P).
}
```

This is the exact full-edge branching identity.

---

## 2. First edge occurrence for local activated pairs

Let

```math
A_{\rm local}
\subseteq
\binom P2
```

be a physical pair set such that every pair is an edge of at least one three-AP in `P`.

For each

```math
e\in A_{\rm local},
```

choose one deterministic first witness `Q(e)` containing `e` as an edge and assign the occurrence token

```math
\eta(e)=(Q(e),e).
```

The map `eta` is injective because its second coordinate is the physical pair `e`. Therefore the used token family

```math
\mathscr E_{\rm used}
=
\eta(A_{\rm local})
```

has exact mass

```math
\boxed{
W(\mathscr E_{\rm used})
=
J(A_{\rm local}).
}
```

Let

```math
\mathscr E_{\rm free}
=
\mathscr E(P)\setminus\mathscr E_{\rm used}.
```

Then

```math
\boxed{
W(\mathscr E_{\rm free})
=
\frac52\mathcal L_3(P)-J(A_{\rm local}).
}
```

No assumption is required about how many three-APs contain one physical pair. Only one occurrence is removed.

---

## 3. Combination with direct maximal discharge

Let `B` be inclusion-maximal four-AP-free and `P=B intersect [N,2N)`. For an arbitrary activated pair set

```math
A\subseteq\binom P2,
```

apply the direct completion partition

```math
A
=
A_{\rm local}
\sqcup
A_{\rm cross}
\sqcup
A_{\rm hole}.
```

The direct theorem gives

```math
J(A_{\rm cross})+J(A_{\rm hole})
\le
J(E_{\rm new})
+
\sum_{S\in\mathcal H}\alpha(S)H(S),
```

where `E_new` is a genuinely new physical pair union disjoint from `A`.

Add `J(A_local)` and then use the exact token partition. This gives

```math
\boxed{
J(A)
+
W(\mathscr E_{\rm free})
\le
\frac52\mathcal L_3(P)
+
J(E_{\rm new})
+
\sum_{S\in\mathcal H}\alpha(S)H(S).
}
```

This is the production-compatible direct-discharge row.

---

## 4. Interpretation

The left side contains both obligations that must survive the local accounting step:

```text
entering activated physical pair debt;
all full-edge branching tokens not consumed by local pair payment.
```

The right side contains exactly one copy of the parent full-edge production, plus:

```text
genuinely new pair capacity;
strictly lower-scale heavy fibers.
```

Thus one local parent three-AP edge token has exactly one role:

```text
pay one local activated pair;
or remain as a branching output token.
```

It cannot do both.

---

## 5. Simultaneous shell version

For a finite family of standard dyadic shells `P_j`, choose first witness tokens independently inside each shell. Shell occurrence-token families are disjoint, so

```math
\boxed{
\sum_jJ(A_j)
+
\sum_jW(\mathscr E_{j,\rm free})
\le
\frac52\sum_j\mathcal L_3(P_j)
+
J(E_{\rm new})
+
\sum_{S\in\mathcal H}\alpha(S)H(S).
}
```

The global shell-batched theorem guarantees that `E_new` is one disjoint physical pair union across all shells.

---

## 6. Consequence for the Bellman architecture

The previous notation could make local edge payment appear to consume the entire branching budget while the complete child family was also retained. The occurrence-token partition removes that ambiguity.

The correct local operation is:

```text
full parent edge-token family
  -> used tokens paying local activated pairs
  + free tokens continuing as branching output.
```

Cross-shell roots and maximality holes are handled by the direct discharge theorem and do not consume a second copy of local edge production.

The remaining proof problem is therefore not local double counting. It is the treewise packing of the new pair union, free branching tokens, terminal heavy fibers, and recursive heavy fibers.
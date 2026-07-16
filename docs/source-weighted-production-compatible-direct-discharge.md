# Source-weighted production-compatible direct discharge

## Status

Occurrence-measure refinement of direct maximal-ambient pair discharge.

The theorem transports exact source mass rather than replacing every outgoing pair by its complete reciprocal-gap capacity. It is compatible with the full-edge occurrence-token partition and with the dyadic physical-gap moment.

---

## 1. Economical activated pair measure

Let

```math
P\subseteq[N,2N)
```

be a parent shell and let

```math
U\subseteq\binom P2
```

be an economical activated physical pair set.

Initially give every pair its full source mass

```math
\mu_{\rm in}(e)=\frac1{\operatorname{gap}(e)}.
```

The same proof works for occurrence-tagged submasses

```math
0\le\mu_{\rm in}(e)\le\frac1{\operatorname{gap}(e)},
```

provided local edge-token consumption is fractional. The full-mass form is sufficient for economical first appearances.

Partition

```math
U=U_{\rm local}\sqcup U_{\rm cross}\sqcup U_{\rm hole}
```

by deterministic maximal-ambient completion priority.

---

## 2. Local edge occurrences

For every pair

```math
e\in U_{\rm local},
```

choose one deterministic parent three-AP edge occurrence `(Q,e)`.

Consume exactly the source mass

```math
\mu_{\rm in}(e)=w(e)
```

from that edge occurrence. Let

```math
\mathscr E_{\rm free}
```

be the unused part of the complete parent full-edge occurrence family.

Then

```math
W(\mathscr E_{\rm free})
=
\frac52\mathcal L_3(P)
-
J(U_{\rm local}).
```

---

## 3. Cross-shell source measure

For every cross-shell adjacent-root swap

```math
e\longmapsto\rho(e),
```

the physical gap is preserved and the map is injective. Define

```math
\mu_{\rm cross}(\rho(e))
=
\mu_{\rm in}(e).
```

Then

```math
W(\mu_{\rm cross})
=
J(U_{\rm cross}),
```

and every target pair carries no more than its physical capacity.

---

## 4. Light-support source measure

For one canonical physical support pair `f`, let the selected light role fibers have exact weighted source loads

```math
L_1,\ldots,L_t.
```

Capacity-aware allocation guarantees

```math
\sum_{i=1}^tL_i\le w(f).
```

Define the aggregated support occurrence measure

```math
\boxed{
\mu_{\rm light}(f)=\sum_{i=1}^tL_i.
}
```

This is generally smaller than the complete physical support capacity `w(f)`. It records exactly the source debt transported to `f`.

Summing over supports gives

```math
W(\mu_{\rm light})
=
\text{total light source load}.
```

No target-gap amplification occurs.

---

## 5. Heavy source measure

Every heavy role fiber retains its exact source load:

```text
adjacent role: H(S);
outer role:    (1/2)H(S).
```

Resolve heavy fibers into terminal and recursive shells. Let

```math
\mu_{\rm heavy}^{\rm rec}
```

be the occurrence-owned horizontal-chain output measure and let

```math
\mu_{\rm heavy}^{\rm term}
```

be the terminal heavy sink measure.

The horizontal-chain theorem preserves the assigned source load before terminal removal and contracts physical dyadic gap for recursive output.

---

## 6. Exact raw-mass identity

Let

```math
\mu_{\rm dir}^{\rm rec}
=
\mu_{\rm cross}
+
\mu_{\rm light}
+
\mu_{\rm heavy}^{\rm rec}
```

and

```math
\mu_{\rm dir}^{\rm term}
=
\mu_{\rm heavy}^{\rm term}.
```

Every nonlocal source pair belongs to exactly one cross, light, or heavy output class. Therefore

```math
J(U_{\rm cross})+J(U_{\rm hole})
=
W(\mu_{\rm dir}^{\rm rec})
+
W(\mu_{\rm dir}^{\rm term}).
```

Adding the local edge-token partition gives

```math
\boxed{
J(U)
+
W(\mathscr E_{\rm free})
=
\frac52\mathcal L_3(P)
+
W(\mu_{\rm dir}^{\rm rec})
+
W(\mu_{\rm dir}^{\rm term}).
}
```

If a terminal convention discards sink mass immediately, the equality becomes the corresponding inequality with the terminal term removed.

---

## 7. Gap-moment monotonicity

Retain the production owner on every outgoing occurrence. For

```math
\Phi_p(\mu)
=
\sum_e\mu(e)G(e)^p,
\qquad p\ge0,
```

we have:

```text
cross-shell adjacent swap:       factor 1;
light multiplicity one:          factor at most 1;
light multiplicity at least two: factor at most 2^{-p};
recursive adjacent heavy:        factor at most 2^{-p};
recursive outer heavy:           factor at most 4^{-p};
terminal output:                 factor 0 in the recursive ledger.
```

Hence

```math
\boxed{
\Phi_p(\mu_{\rm dir}^{\rm rec})
\le
\Phi_p(\mu_{\rm in}|_{U_{\rm cross}\cup U_{\rm hole}}).
}
```

The outgoing occurrence measure never has more source-weighted gap moment than the entering nonlocal pair measure.

---

## 8. Collision handling

Different production owners may reach the same physical target pair. Do not replace their occurrence measures by several copies of full target capacity.

Instead either:

```text
retain the occurrence labels separately;
or
aggregate their masses up to the one physical target capacity and keep any excess source-labeled.
```

In both representations the total source-weighted mass is unchanged. Physical recreation does not create pair mass.

---

## 9. Critical owner-scale form

All direct-discharge operations in one parent row initially have common owner scale `N`. Multiplying the raw identity by `N` gives

```math
\boxed{
NJ(U)
+
N W(\mathscr E_{\rm free})
=
\frac52N\mathcal L_3(P)
+
N W(\mu_{\rm dir}^{\rm rec})
+
N W(\mu_{\rm dir}^{\rm term}).
}
```

When recursive outputs are installed in lower owner shells, their actual critical mass can only decrease.

Thus the term previously written as full target union energy `NJ(E_new)` may be replaced by the exact source-weighted occurrence mass.

---

## 10. Strategic consequence

The global direct-pair problem no longer includes target-capacity amplification. Every outgoing lineage carries mass inherited from one economical source pair.

The remaining difficulty is purely organizational:

```text
sum source-owned finite lineages;
merge recreations without losing ownership;
combine owner-scale descent with free production-token depth release;
control terminal sink recreation.
```

No new scalar pair debt is created by direct transport itself.

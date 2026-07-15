# Pair-only direct-discharge recurrence

## Status

State-independent composition of:

```text
direct maximal-ambient activated-pair discharge;
production-compatible full-edge token partition;
terminal/recursive heavy-shell split;
horizontal-chain transfer for recursive heavy shells;
physical-pair first appearance.
```

The composition removes free-standing recursive harmonic states from the local row. Every nonterminal output is a physical pair. The sole remaining recurrence term is repeated occurrence of a horizontal-chain pair, equipped with an affine lower-scale reference certificate.

---

## 1. Direct production-compatible row

Let `B` be inclusion-maximal four-AP-free and

```math
P=B\cap[N,2N).
```

Let

```math
A\subseteq\binom P2
```

be the entering activated physical pair union. The production-compatible direct-discharge theorem gives

```math
J(A)
+
W(\mathscr E_{\rm free})
\le
\frac52\mathcal L_3(P)
+
J(E_{\rm new})
+
\operatorname{TermSink}_{\rm first}
+
\sum_{T\in\mathcal R_{\rm heavy}}\alpha(T)H(T)
+
\operatorname{TermRecreate}.
```

Here:

- `E_new` is a physical pair union disjoint from `A`;
- `mathscr E_free` is the unused full-edge occurrence-token family;
- every `T` is a recursive heavy step shell;
- `alpha(T)` is `1` for adjacent completion roles and `1/2` for outer roles.

---

## 2. Horizontal-chain replacement

Write one recursive shell as

```math
T=\{d_1<\cdots<d_n\}\subseteq[M,2M).
```

Since `T` contains a three-AP,

```math
n\ge3.
```

The horizontal-chain theorem produces one physical pair occurrence for each adjacent step gap:

```math
\Gamma(T)
=
\{e_1(T),\ldots,e_{n-1}(T)\},
```

with

```math
\operatorname{gap}(e_i(T))=d_{i+1}-d_i<M
```

and

```math
\boxed{
\alpha(T)H(T)
<
\sum_{e\in\Gamma(T)}w(e).
}
```

Let

```math
\Gamma
```

be the resulting multiset of horizontal-chain pair occurrences over all recursive heavy shells.

Then

```math
\sum_{T\in\mathcal R_{\rm heavy}}\alpha(T)H(T)
<
J_{\rm occ}(\Gamma),
```

where `J_occ` counts occurrences.

---

## 3. Pair first appearance relative to the entering ledger

Reserve

```math
R_0=A\cup E_{\rm new}.
```

Order the horizontal-chain occurrences deterministically. An occurrence is **new** when its physical pair is not in `R_0` and has not appeared earlier in `Gamma`. Let

```math
E_{\rm chain}
```

be the physical union of new chain pairs.

Every other occurrence is recurrent. Define its exact recurrence mass

```math
R_{\rm chain}
=
\sum_{\substack{\gamma\in\Gamma:\
\text{physical pair of }\gamma\text{ is reserved or earlier}}}
w(\gamma).
```

Then

```math
\boxed{
J_{\rm occ}(\Gamma)
=
J(E_{\rm chain})
+
R_{\rm chain}.
}
```

By construction,

```math
E_{\rm chain}\cap(A\cup E_{\rm new})=\varnothing.
```

Thus the complete outgoing pair union

```math
E_{\rm out}
=
E_{\rm new}\cup E_{\rm chain}
```

is physical and disjoint from `A`.

---

## 4. Pair-only local row

Substituting the first-appearance partition gives

```math
\boxed{
\begin{aligned}
J(A)
+W(\mathscr E_{\rm free})
\le{}&
\frac52\mathcal L_3(P)
+J(E_{\rm out})\\
&+
R_{\rm chain}
+
\operatorname{TermSink}_{\rm first}
+
\operatorname{TermRecreate}.
\end{aligned}
}
```

No recursively continuing harmonic state remains. The nonterminal output is:

```text
one new physical pair union E_out;
one repeated-horizontal-pair occurrence ledger R_chain.
```

All first-appearance chain-pair gaps are strictly below the base of the heavy shell that generated them.

---

## 5. Affine certificate for repeated horizontal pairs

Fix one physical horizontal pair

```math
e=\{x,y\},
\qquad y-x=r,
```

one completion role, and one heavy step-shell base `M`. Suppose `e` occurs in horizontal chains for anchor steps

```math
D_e=\{d_1,\ldots,d_m\}\subseteq[M,2M).
```

For a right-adjacent lift, the first affine copy contains the fixed pair `e`, while the second copy contains points obtained from a translate of `D_e`. Concretely, after fixing the left endpoint `x`,

```math
x+D_e\subseteq B
```

up to the deterministic affine role normalization.

For a left-adjacent lift one obtains a reflected translate, and for an outer lift an affine image with scale two. In every case, affine invariance of four-term progressions gives

```math
\boxed{D_e\text{ is four-AP-free}.}
```

Choose

```math
d_0=\min D_e
```

and define the positive reference-difference reserve

```math
\Delta_e
=
\{d-d_0:d\in D_e,\ d>d_0\}.
```

Then

```math
\Delta_e\subset(0,M)
```

and `Delta_e` is four-AP-free. Therefore every repeated horizontal-pair fiber carries a strictly lower-scale reference-difference reserve.

The exact occurrence collision is

```math
\frac{|D_e|-1}{r}.
```

Its aspect decomposition is

```math
\boxed{
\frac{|D_e|-1}{r}
<
\sum_k2^{k+1}H(\Delta_{e,k}),
}
```

where

```math
\Delta_{e,k}
=
\{\delta\in\Delta_e:
2^kr\le\delta<2^{k+1}r\}.
```

Thus `R_chain` is not anonymous multiplicity. It is an explicit sum of lower-scale rectangle/reference tokens.

---

## 6. What remains

The local activation, completion, production, and recursive-heavy terms now have one common currency: physical pairs and their first-appearance/reference-difference tokens.

The remaining whole-tree theorem must establish a summable packing rule for

```math
R_{\rm chain},
```

or equivalently for the aspect-labeled tokens

```math
(e,\delta,k,\text{role}).
```

The critical facts available for that packing are:

1. the pair gap `r` is strictly below the generating heavy-shell base `M`;
2. every reference difference satisfies `delta<M`;
3. both `r` and `delta` therefore lie at lower scale than the parent shell;
4. the forbidden double-translate ratios exclude `delta/r in {1/2,1,2,4}` in the corresponding integral configurations;
5. the full ordered rectangle embedding is injective before projection to one physical pair.

The proof bottleneck has therefore been reduced to a two-scale first-appearance theorem for repeated horizontal pairs. No sponsor-target collision, anonymous ambient completion, or free-standing recursive harmonic mass remains in the local row.
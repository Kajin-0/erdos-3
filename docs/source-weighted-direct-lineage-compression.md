# Source-weighted direct-lineage compression

## Status

Transport-only macrostep theorem for occurrence-owned source-weighted direct pair lineages.

Every source occurrence reaches a local payment, a terminal sink, or the first repeated physical pair on its own lineage after finitely many first appearances. The path may be compressed without increasing source mass or physical-gap moment.

This theorem does **not** charge all later local payments to the entering shell. A later local witness uses an edge occurrence owned by the shell where that witness occurs.

---

## 1. Source-owned lineage

Write one entering occurrence as

```math
\omega_0=(o,e_0,m),
\qquad
0<m\le\frac1{\operatorname{gap}(e_0)}.
```

The production owner `o` remains attached to the transported mass. Cross-shell, light, and heavy transfers carry exact inherited source load rather than full target capacity.

Stop before treating an already seen physical pair as a new first appearance.

---

## 2. Finite macro-outcome

Physical gap never increases. Strict decreases cannot continue indefinitely. The two equal-gap mechanisms are finite:

```text
adjacent-root swaps form an involution;
exact-gap light episodes have uniformly bounded first-appearance length.
```

Therefore every source occurrence has one finite outcome:

```text
local payment in the current shell;
terminal occurrence token;
recreation token recording the first repeated pair and finite cycle segment.
```

---

## 3. Mass and gap moments

Let `mu_in` be a finite entering occurrence measure. Let `mu_term` and `mu_recreate` be its terminal and recreation macro-output measures.

Then

```math
\boxed{
W(\mu_{\rm term})+W(\mu_{\rm recreate})
\le W(\mu_{\rm in}).
}
```

Equality holds after adding mass consumed by local edge occurrences along the paths.

For every `p>=0`,

```math
\boxed{
\Phi_p(\mu_{\rm term})
+
\Phi_p(\mu_{\rm recreate})
\le
\Phi_p(\mu_{\rm in}),
}
```

where

```math
\Phi_p(\mu)=\sum_e\mu(e)G(e)^p.
```

A path containing a midpoint, multiplicity-at-least-two light transfer, or recursive heavy transfer is strictly contracting for every `p>0`.

---

## 4. Bounded equal-gap certificates

A scale-preserving adjacent-root cycle has length two. A scale-preserving light-support cycle has uniformly bounded simple support by exact-gap persistence. Mixed equal-gap episodes remain bounded because an actual-root completion invokes the involution.

Thus a recreation token needs only a bounded local certificate, not an unbounded path history.

---

## 5. Production-ownership boundary

The one-generation identity

```math
J(U)+W(E_{\rm free})
=
\frac52\mathcal L_3(P)
+
W(\mu_{\rm dir}^{\rm rec})
+
W(\mu_{\rm dir}^{\rm term})
```

uses edge occurrences owned by the entering shell `P` only.

After an occurrence leaves that row, a later local payment may occur in another shell. Its edge token belongs to that later shell. Hence a complete multi-shell lineage cannot be replaced by an identity involving only the entering production family.

The valid global construction is:

```text
one source-weighted row per owner shell;
correct edge-token ownership at every local payment;
macro compression only after those rows are assembled.
```

---

## 6. Remaining interface

The transport history can be compressed, but the global proof must still control:

```text
cross-owner recreation multiplicity;
terminal sink multiplicity;
production ownership across visited shells;
free edge-token telescoping;
critical and gap-depth release.
```

Source weighting removes target amplification. It does not remove the need to assign every local payment to its actual owner shell.

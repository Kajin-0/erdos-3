# First-appearance terminal-sink ledger

## Status

Elementary whole-tree accounting lemma. It removes terminal-token double counting once a valid token map has been chosen. It does not supply the missing bound on total terminal mass and does not prove that the current `(u,p)` token is globally collision-sound.

---

## 1. Finite-tree statement

Let `V` be a finite rooted branching tree. For every node `v`, let `T_v` be its terminal output family. Fix:

- a token map `tau_v : T_v -> Omega`;
- a nonnegative token weight `w : Omega -> [0,infinity)`;
- a deterministic total order `prec` on the tree nodes.

For each node define its first-appearance terminal ledger

```math
F_v
=
\left\{
\omega\in\tau_v(T_v):
 v=\min_{\prec}\{u:\omega\in\tau_u(T_u)\}
\right\}.
```

Then the families `F_v` are pairwise disjoint and

```math
\boxed{
\sum_{v\in V}\sum_{\omega\in F_v}w(\omega)
=
\sum_{\omega\in\bigcup_{v\in V}\tau_v(T_v)}w(\omega).
}
```

### Proof

Every token in the global union occurs at a nonempty finite set of nodes. The total order gives that set a unique least node. Assign the token to that node and to no other node. The first-appearance families are therefore disjoint and partition the token union. Summing the nonnegative token weights gives the identity.

---

## 2. Infinite locally finite trees

Let `V_n` be an increasing exhaustion by finite rooted subtrees. Applying the finite identity to `V_n` gives an increasing sequence of token unions. Monotone convergence yields

```math
\sum_v\sum_{\omega\in F_v}w(\omega)
=
\sum_{\omega\in\bigcup_v\tau_v(T_v)}w(\omega)
```

in `[0,infinity]`.

Thus first-appearance accounting remains exact on an infinite tree. It does not by itself prove that the right-hand side is finite or bounded by the root potential.

---

## 3. Application to the recorded retained family

For the certified second-generation terminal sinks, use the point token

```math
\tau(u)=(u,p),
```

where `u` is the terminal descendant label and `p` is its original `S_7` root provenance.

The exact identity exporter proves that the recorded family has

```text
13 terminal states
43 terminal points
43 distinct numerical labels u
43 distinct tokens (u,p).
```

Therefore all 43 tokens are first appearances under every node order inside this finite family. The first-appearance terminal charge equals the complete recorded terminal charge; no correction is required at this generation.

---

## 4. What remains open

The lemma separates bookkeeping from structure.

Bookkeeping is solved:

```text
fixed collision-sound token map
    -> exact first-appearance quotient
    -> no terminal token is charged twice.
```

The structural questions remain:

1. Is `(u,p)` collision-sound across different branches and later generations?
2. If two occurrences share `(u,p)`, do they represent the same terminal contribution or different affine embeddings?
3. Is a path signature, affine-map signature, source-step history, or parent-state identity required?
4. Can the weighted global token union be bounded by `RecPack`, obstruction credit, or a Carleson measure?
5. Does third-generation propagation recreate any of the 43 recorded tokens?

A token that is too coarse can merge genuinely distinct contributions. A token that is too fine makes first-appearance accounting tautologically injective but may destroy every useful global bound. The next theorem must find a token at the correct resolution.

---

## Affine pair-capacity interpretation

When a terminal point belongs to an affine root state, its coarse token

```math
(u,p)
```

already determines the affine reference

```math
r=p-u.
```

Therefore `(u,p)` is the root pair `(r,p)` with weight `1/(p-r)=1/u`. In a fixed root universe `P_0`, first-appearance terminal pair mass satisfies

```math
\sum_{\text{first terminal }(u,p)}\frac1u
\le
J(P_0).
```

A collision of `(u,p)` is genuine pair-resource reuse. Refining the token to `(u,p,i)` may distinguish genealogical histories, but does not create another pair credit. The refined token should be treated as metadata unless a separate non-pair resource is proved.

This interpretation applies only after the affine root-reference hypotheses are verified.

---

## 5. Candidate Bellman form

For a collision-sound token map, define

```math
\operatorname{TermSink}_{\rm first}(v)
=
\sum_{\omega\in F_v}w(\omega).
```

The target inequality becomes

```math
\Delta(S)
+
\operatorname{TermSink}_{\rm first}(S)
+
\sum_{S'\in\operatorname{RecChild}_\pi(S)}
\operatorname{RecPack}(S')
\le
\operatorname{RecPack}(S)
+
\Phi_{\rm obs}(S)
+
\operatorname{controlled\ error}.
```

The terminal coordinate is now globally nonduplicating by construction. The remaining burden is to prove that its cumulative union weight is controlled and that the token map identifies exactly the contributions that should be merged.

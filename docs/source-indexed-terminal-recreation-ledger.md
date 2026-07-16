# Source-indexed terminal and recreation ledger

## Status

State-independent occurrence-flow accounting theorem for source-weighted direct pair transport.

Terminal value is indexed by the already-paid source occurrence. A same-source recreation closes a zero-divergence cycle, but the mass entering that recurrent class remains once as a cycle-reserve token. It is not charged again on every traversal.

This theorem does **not** authorize repeated use of one destination edge occurrence or physical support capacity. Such capacities must be allocated before an occurrence is declared locally absorbed.

---

## 1. Source occurrence atoms

Let

```math
\Omega=\{\omega\}
```

be a finite family of source occurrence atoms. Each atom carries an immutable production owner, an entering physical pair, and mass `m(omega)>=0`. Its mass has already been paid by an economical activation row.

A transport step may split one atom into finitely many subatoms whose masses sum to the entering mass. Every descendant retains the original source identifier and a branch identifier.

Different atoms may have the same numerical physical pair.

---

## 2. Valid transport outcomes

After all required physical capacities have been reserved, each source branch has one of four macro-outcomes:

```text
local absorption:     consumes allocated edge-occurrence capacity;
terminal absorption:  enters a terminal or obstruction accumulator;
recursive frontier:   remains an outgoing source-owned occurrence;
recreation reserve:   reaches a state already visited by the same branch.
```

Numerically equal outcomes belonging to different source atoms remain distinct occurrence records. Their masses are never replaced by several copies of full target-pair capacity.

---

## 3. Source-indexed terminal token

For one terminalized branch define

```math
\tau_{\rm term}=(\omega,b,t),
```

where `omega` is the immutable source, `b` is the branch identifier, and `t` is terminal metadata. Give the token exactly the transported branch mass.

Because every source branch has at most one terminal outcome, these tokens are injective in `(omega,b)`.

Let:

```text
A_local = locally absorbed source mass;
T_source = source-indexed terminal mass;
F_rec = ordinary recursive-frontier mass;
C_cyc = one representative mass for each recreated source branch.
```

Then

```math
\boxed{
W(A_{\rm local})
+
W(T_{\rm source})
+
W(F_{\rm rec})
+
W(C_{\rm cyc})
\le
W(\Omega).
}
```

Equality holds when every source branch has one of these four outcomes and no mass is discarded.

This is an occurrence identity. It makes no claim that the numerical terminal target union has enough physical capacity to hold all terminal mass.

---

## 4. Recreation cycles

Fix one source branch and suppose its transport states are

```math
z_0,z_1,\ldots,z_j,
\qquad
z_j=z_i
```

for a first repetition `i<j`.

The closed segment

```math
z_i\to z_{i+1}\to\cdots\to z_j=z_i
```

has zero net transport divergence. Remove the repeated cycle edges and retain one representative occurrence at `z_i` in `C_cyc`.

Thus recreation contributes one already-paid recurrent reserve, not a new physical pair and not a terminal value. Repeated traversal of the same cycle contributes nothing further.

For a finite occurrence network, standard path-cycle decomposition leaves paths from source injections to local, terminal, ordinary-frontier, or cycle-reserve outcomes.

---

## 5. Numerical sink collisions

Several source atoms may terminate at the same numerical pair `e`, with masses

```math
m_1,\ldots,m_k.
```

The physical target capacity is only

```math
w(e)=\frac1{\operatorname{gap}(e)},
```

and it may happen that

```math
\sum_i m_i>w(e).
```

The source-indexed terminal ledger records the exact value `sum_i m_i` without claiming `k` copies of `w(e)` or even one target copy for every source.

A proof that instead uses the target as physical capacity must split

```math
\sum_i m_i
=
\min\!\left(w(e),\sum_i m_i\right)
+
\left(\sum_i m_i-w(e)\right)_+
```

and provide a separate overflow transfer law.

---

## 6. Relation to terminal first appearance

The numerical first-appearance terminal ledger answers:

```text
Which physical terminal tokens appear globally for the first time?
```

The source-indexed ledger answers:

```text
How much already-paid source occurrence mass reaches terminal output?
```

Therefore:

```text
physical terminal first appearance -> union-capacity coordinate;
source-indexed terminal value       -> occurrence-flow coordinate.
```

The source token is finer, but its total mass is controlled by source injection rather than by a new physical-token union estimate.

---

## 7. S7 exact diagnostic

On the certified split fifth-frontier terminal transport:

```text
source occurrences                    75,247
distinct numerical targets            40,512
collision targets                     19,593
fixed source sinks                    35,841
source-to-source nonfixed targets           0
source-to-external-sink occurrences    9,045
cross-parent numerical targets              0
```

The numerical target-capacity overflow is

```math
227.822626207390\ldots,
```

and the largest source-mass / target-capacity ratio is

```math
29.989556157022\ldots.
```

The overflow splits as

```text
anchored at a path-zero source sink  221.724011504502...
unanchored external sink               6.098614702889...
```

Thus numerical target capacity is not a complete terminal ledger even after source weighting. The source-target functional graph has fixed points and external sinks only; it has no nontrivial source-to-source cycle on this exact frontier.

Primary executable:

```text
src/probe_s7_source_weighted_sink_overflow.py
```

---

## 8. Bellman use

For one valid source-weighted transport row:

- place `W(T_source)` on the terminal-value side;
- retain `W(F_rec)` as ordinary recursive occurrence mass;
- retain `W(C_cyc)` once as recurrent reserve;
- never regenerate `C_cyc` by traversing its certified cycle again.

This removes numerical sink multiplicity and repeated cycle traversal as scalar error terms.

The remaining global requirements are:

1. coordinate destination edge/support capacities across owner shells;
2. telescope ordinary recursive occurrences at their actual destination scales;
3. carry cycle reserves once without regeneration;
4. preserve unused edge-occurrence capacity;
5. convert accumulated terminal source value and released depth into the original reciprocal-density bound.

The unresolved problem is global capacity scheduling and critical telescoping, not numerical terminal-target multiplicity itself.

# Source-indexed terminal and recreation ledger

## Status

State-independent occurrence-flow accounting theorem for source-weighted direct pair transport.

The theorem separates numerical sink multiplicity from actual source mass. Terminal value is indexed by the already-paid source occurrence. A same-source recreation cycle has zero net transport divergence and is removed from the recursive flow rather than charged as a new physical pair.

This theorem does **not** authorize repeated use of one destination edge occurrence or one physical support capacity. Local edge and support capacities must be allocated before an occurrence is declared absorbed.

---

## 1. Source occurrence atoms

Let

```math
\Omega=\{\omega\}
```

be a finite family of source occurrence atoms. Each atom carries:

```text
an immutable production owner;
an entering physical pair;
a nonnegative mass m(omega);
optional path and branch metadata.
```

The mass has already been paid by an economical activation row. Different atoms may have the same numerical physical pair.

A transport step may split one atom into finitely many subatoms, provided their masses sum to the entering mass. Every descendant retains the original source identifier together with a branch identifier.

---

## 2. Valid transport outcomes

After all required physical capacities have been reserved, each source subatom has one of four outcomes:

```text
local absorption:     consumes allocated edge-occurrence capacity;
terminal absorption:  enters a terminal or obstruction accumulator;
recursive frontier:   remains an outgoing source-owned occurrence;
recreation:           returns to a state already visited by the same subatom.
```

Numerically equal outcomes belonging to different source atoms remain distinct occurrence records. Their masses are never replaced by several copies of full target-pair capacity.

---

## 3. Source-indexed terminal token

For one terminalized subatom, define

```math
\tau_{\rm term}=(\omega,b,t),
```

where `omega` is the immutable source, `b` is its branch identifier, and `t` is terminal metadata such as the numerical target and witness class.

Give this token exactly the transported submass.

Because every source branch has at most one terminal outcome, the terminal tokens are injective in `(omega,b)`. Hence

```math
\boxed{
W(T_{\rm source})
\le
W(\Omega).
}
```

More generally, including locally absorbed and recursive-frontier mass gives

```math
\boxed{
W(A_{\rm local})
+
W(T_{\rm source})
+
W(F_{\rm rec})
\le
W(\Omega).
}
```

Equality holds when every source branch has one of these three outcomes after recreation cycles are removed.

This is an occurrence statement. It makes no claim that the numerical terminal target union has enough physical pair capacity to hold all terminal mass.

---

## 4. Recreation cycles

Fix one source branch and suppose its transport states are

```math
z_0,z_1,\ldots,z_j
```

with

```math
z_j=z_i
```

for some first repetition `i<j`.

The segment

```math
z_i\to z_{i+1}\to\cdots\to z_j=z_i
```

has zero net source-flow divergence. Removing that closed segment preserves:

```text
source injection;
local absorbed mass;
terminal mass;
recursive frontier mass.
```

Thus a same-source recreation is not a new pair debt and is not terminal value. It is a zero-divergence cycle certificate.

For a finite occurrence network, the standard path-cycle decomposition removes all directed cycle flow and leaves only paths from source injections to local, terminal, or frontier outcomes.

---

## 5. Numerical sink collisions

Several source atoms may terminate at the same numerical pair `e`. Write their transported masses as

```math
m_1,\ldots,m_k.
```

The numerical target capacity is only

```math
w(e)=\frac1{\operatorname{gap}(e)}.
```

It may happen that

```math
\sum_i m_i>w(e).
```

The source-indexed terminal ledger records the exact value

```math
\sum_i m_i
```

without claiming `k` copies of `w(e)` or even one physical target copy for every source.

If a proof instead wants to use the target as physical capacity, it must separately split

```math
\sum_i m_i
=
\min\!\left(w(e),\sum_i m_i\right)
+
\left(\sum_i m_i-w(e)\right)_+
```

and provide a transfer law for the overflow. The occurrence ledger avoids that unnecessary projection when the target is only terminal metadata.

---

## 6. Relation to terminal first appearance

The older numerical first-appearance terminal ledger remains valid when a collision-sound physical token is needed. The source-indexed ledger answers a different question:

```text
How much already-paid occurrence mass reaches terminal output?
```

Its token is intentionally finer because its total mass is controlled by source injection, not by a new numerical-token union bound.

Therefore:

```text
physical terminal first appearance -> union-capacity coordinate;
source-indexed terminal value       -> occurrence-flow coordinate.
```

They must not be conflated.

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
227.822626207390\ldots
```

and the largest source-mass / target-capacity ratio is

```math
29.989556157022\ldots.
```

Therefore numerical target capacity is not a valid complete terminal ledger even after source weighting.

The overflow splits as

```text
anchored at a path-zero source sink  221.724011504502...
unanchored external sink               6.098614702889...
```

The source-target functional graph has fixed points and external sinks only; it has no nontrivial source-to-source cycle on this exact frontier.

Primary executable:

```text
src/probe_s7_source_weighted_sink_overflow.py
```

---

## 8. Bellman use

For one valid source-weighted transport row, place

```math
W(T_{\rm source})
```

on the terminal-value side of the Bellman inequality and retain

```math
W(F_{\rm rec})
```

as the recursive occurrence measure. Recreation cycles are removed from both sides as zero-divergence flow.

This eliminates numerical sink multiplicity as a scalar error term. The remaining global requirements are:

1. coordinate destination edge/support capacities across owner shells;
2. telescope recursive source-owned occurrences at their actual destination scales;
3. preserve unused edge-occurrence capacity;
4. convert accumulated terminal source value and released depth into the original reciprocal-density bound.

The unresolved problem is global capacity scheduling and critical telescoping, not numerical terminal-target multiplicity itself.

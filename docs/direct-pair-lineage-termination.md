# Direct pair-lineage termination

## Status

State-independent pathwise termination theorem for occurrence-owned first-appearance pair lineages under direct maximal-ambient discharge.

Every lineage either reaches a terminal sink or recreates an already seen physical pair identity after finitely many transitions. No first-appearance pair lineage can continue indefinitely.

The theorem does not bound the total number of lineages created across the whole branching tree. It closes the pathwise recurrence problem.

---

## 1. Direct-discharge lineage

Start from one activated physical pair occurrence. At every nonterminal direct-discharge step, retain its production owner and follow one outgoing pair occurrence carrying the assigned mass.

If an outgoing physical pair identity has already occurred on that lineage, send it to the recreation ledger rather than treating it as a new first appearance.

Let

```math
D_k
```

be the physical gap of the `k`-th first-appearance pair.

---

## 2. Physical gap is nonincreasing

The dyadic pair-gap theorem gives the stronger integer statement needed here.

### Actual-root swap

An adjacent cross-shell swap preserves physical gap:

```math
D_{k+1}=D_k.
```

A midpoint completion is local to the shell and terminal; if represented as an edge transfer, it halves the gap.

### Light support

If the support multiplicity is `m`, then

```math
D_{k+1}\le\frac{D_k}{m}\le D_k.
```

### Recursive heavy fiber

Every horizontal-chain output gap lies below the step-shell base. It is strictly below every adjacent source physical gap and below half of every outer source physical gap. Hence

```math
D_{k+1}<D_k.
```

Terminal outputs stop.

Therefore

```math
\boxed{D_{k+1}\le D_k}
```

along every first-appearance lineage.

---

## 3. Strict decreases cannot continue forever

Whenever

```math
D_{k+1}<D_k,
```

the positive integer gap decreases by at least one.

Thus one lineage has at most `D_0-1` strict integer-gap decreases before reaching gap `1`. More importantly, there is no infinite strictly decreasing subsequence.

An infinite first-appearance lineage would therefore have to contain an infinite tail with constant physical gap.

---

## 4. Constant-gap actual-root swaps terminate

The cross-shell edge-swap involution theorem shows that an adjacent-root swap maps

```math
e\longmapsto\rho(e)
```

and the unique adjacent-root swap from `rho(e)` returns `e`.

Hence a constant-gap actual-root episode has at most one new pair identity after its entering pair. The next swap is recreation.

Local-root-first semantics prevents a hole transfer from bypassing this reverse actual root.

---

## 5. Constant-gap light episodes terminate

Exact physical-gap preservation in a light fiber forces:

```text
support multiplicity one;
a singleton source fiber;
source gap = support gap;
a canonical interior-witness transition, unless the output is locally terminal.
```

The exact-gap light-support persistence theorem proves that a nonterminal first-appearance episode has at most nine pair identities. A possible final endpoint-witness support is local and gives at most one additional identity.

Thus a constant-gap light episode has at most ten identities.

If an actual-root completion appears during the episode, the preceding involution theorem terminates it after at most one further new identity.

---

## 6. Pathwise termination theorem

Assume for contradiction that one first-appearance lineage is infinite.

Because the positive integer gaps are nonincreasing, they are eventually constant. On the constant-gap tail:

- an actual-root swap recreates the preceding pair within one further swap;
- a light-support episode has uniformly bounded length;
- a recursive heavy transition would strictly decrease the gap;
- a terminal output would stop.

Every possibility contradicts an infinite first-appearance tail.

Therefore

```math
\boxed{
\text{every direct pair-lineage reaches terminal output or pair recreation in finite time.}
}
```

---

## 7. Relation to previous gap monotonicity

The earlier full-edge dyadic theorem proved termination when the **same physical pair** remains latent while shell scale decreases.

The present theorem allows the physical pair identity to change through:

```text
actual-root edge swaps;
light canonical supports;
recursive heavy horizontal transfers.
```

It therefore closes a strictly larger pathwise system.

---

## 8. What remains open

Pathwise termination does not imply a whole-tree bound. A branching process may create many finite lineages, and many of them may recreate the same physical identity.

The remaining global theorem must control:

1. the production-owned number or total mass of lineages;
2. pair recreation across distinct owners;
3. terminal-sink recreation;
4. summation of the exact `7/4` first-appearance depth release;
5. the relation between the lineage ledger and the original reciprocal mass.

The active obstruction is now branching and recreation, not infinite pair transport along one path.

Primary components:

- `docs/direct-discharge-dyadic-pair-gap-moment.md`;
- `docs/cross-shell-edge-swap-involution.md`;
- `docs/exact-gap-light-support-persistence.md`.

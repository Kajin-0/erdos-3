# Full-edge incidence bound by physical pair energy

## Status

State-independent upper bound connecting full-edge three-AP production to physical pair energy in every four-AP-free state.

Every physical pair belongs to at most two three-term progressions: at most one as an adjacent edge and at most one as an outer edge. Consequently the complete full-edge occurrence load is at most twice the pair-energy union.

---

## 1. Physical pair energy

Let

```math
P\subseteq\mathbb Z
```

be finite and four-AP-free. Define

```math
J(P)
=
\sum_{x<y,\ x,y\in P}
\frac1{y-x}.
```

For one physical pair

```math
e=\{x,y\},
\qquad x<y,
\qquad D=y-x,
```

write `m_3(e)` for the number of three-term progressions in `P` containing both endpoints.

---

## 2. Possible three-AP completions

There are at most three candidate roots completing `e` to a three-AP.

### Left adjacent completion

```math
x-D.
```

### Right adjacent completion

```math
y+D.
```

### Midpoint completion

When `D` is even,

```math
x+\frac D2.
```

The two adjacent completion roots cannot both belong to `P`, because then

```math
x-D,
\quad x,
\quad y,
\quad y+D
```

would form a four-term arithmetic progression of step `D`.

Therefore `e` belongs to:

```text
at most one adjacent-edge three-AP;
at most one midpoint/outer-edge three-AP.
```

Hence

```math
\boxed{m_3(e)\le2.}
```

---

## 3. Exact full-edge incidence identity

For one three-AP

```math
Q=\{a,a+d,a+2d\},
```

the complete physical edge load is

```math
\frac1d
+
\frac1d
+
\frac1{2d}
=
\frac5{2d}.
```

Thus, writing

```math
\mathcal L_3(P)
=
\sum_{Q\in\operatorname{AP}_3(P)}\frac1{d(Q)},
```

one has the exact double-counting identity

```math
\boxed{
\frac52\mathcal L_3(P)
=
\sum_{e\in\binom P2}
\frac{m_3(e)}{D(e)}.
}
```

Every three-AP contributes its three physical pair edges, each with reciprocal physical gap.

---

## 4. Pair-energy upper bound

Using `m_3(e)<=2`,

```math
\begin{aligned}
\frac52\mathcal L_3(P)
&=
\sum_e\frac{m_3(e)}{D(e)}\\
&\le
2\sum_e\frac1{D(e)}\\
&=
2J(P).
\end{aligned}
```

Therefore

```math
\boxed{
\frac52\mathcal L_3(P)
\le
2J(P).
}
```

Equivalently,

```math
\boxed{
\mathcal L_3(P)
\le
\frac45J(P).
}
```

No dyadic-shell assumption is required.

---

## 5. Equality structure

Equality in the coefficient-two bound would require every physical pair in `P` to belong to exactly two three-APs. This is highly restrictive and is not claimed to occur.

The theorem uses only the universal incidence multiplicity bound. Improving the constant requires global compatibility among midpoint and adjacent completions, not merely local pair counting.

---

## 6. Bellman interface

The full-color/full-edge branching theorem produces exact occurrence capacity

```math
\frac52\mathcal L_3(P).
```

The present theorem places that complete production below the entering physical pair potential:

```math
\boxed{
\text{full-edge occurrence production}
\le
2J(P).
}
```

This does not solve the entering-pair-energy problem: a factor two is not a contraction. It supplies a universal finite branching bound compatible with the pair-lineage ledger.

Combined with direct pair-lineage termination, the remaining global problem becomes:

```text
control how the factor-two occurrence production is distributed among
finite terminating lineages and how recreation merges their ownership.
```

---

## 7. Scope

The theorem is an upper production bound, not a reciprocal-sum theorem. It does not imply that `J(P)` is summable over dyadic shells and does not control pair-energy recreation across different parents.

Its role is to connect the exact full-edge production operator to the same physical pair-energy coordinate used by the affine Bellman and direct-discharge theorems.

**Verifier:** `src/verify_full_edge_incidence_pair_energy_bound.py`.

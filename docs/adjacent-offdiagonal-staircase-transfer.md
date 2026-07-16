# Adjacent off-diagonal staircase transfer

## Status

State-independent sparse cross-copy transfer for every recursively continuing adjacent completion-step shell.

The two affine copies contain a canonical set of exactly `|T|` unmatched cross-copy pairs whose gaps are pointwise smaller than the step values they pay. Thus the complete adjacent-role harmonic debt transfers to strictly lower-gap physical pair capacity without using the matched activated target pairs.

This strengthens the complete off-diagonal reserve for adjacent roles. Global reuse of the selected staircase pairs remains a physical-pair first-appearance problem.

---

## 1. Two adjacent affine copies

Let

```math
T=\{d_1<d_2<\cdots<d_n\}\subseteq[M,2M)
```

with

```math
n\ge3.
```

For a right-adjacent completion role, write

```math
x_i=c+d_i,
\qquad
y_i=c+2d_i.
```

The matched pairs

```math
\{x_i,y_i\}
```

are the activated targets and have gaps `d_i`.

The left-adjacent role is the reflected copy and has the same absolute pair gaps, so it suffices to treat the right-adjacent case.

---

## 2. Canonical staircase pairs

For

```math
1\le i<n,
```

define

```math
p_i=\{x_{i+1},y_i\}.
```

Also define

```math
p_n=\{x_1,y_2\}.
```

Every pair is off-diagonal: its two indices are different. The pairs are physically distinct because the first-copy endpoint determines its index and the second-copy endpoint determines the other index.

---

## 3. Positivity and strict gap descent

For `i<n`,

```math
\operatorname{gap}(p_i)
=
2d_i-d_{i+1}.
```

Because

```math
d_{i+1}<2M\le2d_i,
```

one has

```math
0<2d_i-d_{i+1}<d_i.
```

Therefore

```math
w(p_i)
>
\frac1{d_i}.
```

For the final pair,

```math
\operatorname{gap}(p_n)
=
2d_2-d_1.
```

This is positive and satisfies

```math
2d_2-d_1<d_2<d_n.
```

Hence

```math
w(p_n)
>
\frac1{d_n}.
```

Every staircase-pair gap is strictly below the step value assigned to it, and therefore strictly below `2M`. More precisely, `p_i` for `i<n` has gap below `d_i`, while `p_n` has gap below `d_n`.

---

## 4. Pointwise harmonic payment

Assign the harmonic term `1/d_i` to `p_i` for `i<n`, and assign `1/d_n` to `p_n`. The preceding inequalities give

```math
\boxed{
H(T)
=
\sum_{i=1}^n\frac1{d_i}
<
\sum_{i=1}^n w(p_i).
}
```

Thus one adjacent recursive state is paid by exactly `n` unmatched cross-copy pairs.

The transfer is pointwise rather than aggregate: every harmonic term has its own strictly smaller-gap physical pair.

---

## 5. Relation to the complete off-diagonal reserve

The complete off-diagonal family contains `n(n-1)` pairs. The staircase uses only

```math
n
```

of them.

For dense complete-bipartite copy incidence, the selected staircase pairs remain state-specific because they connect one first-copy node and one second-copy node. They therefore retain the quadratic growth in the number of embedded states even though only linearly many pairs are used per state.

---

## 6. Bellman interpretation

The matched activated pairs are excluded. The staircase produces a new candidate child pair family with strict pointwise gap descent:

```text
activated target term 1/d_i
    -> unmatched cross-copy pair of gap < d_i.
```

If physical staircase pairs are first-appearance disjoint, the transfer gives immediate triangular cancellation. If the same physical pair is selected by several states, the excess is a genuine projected-pair collision carrying the full affine state indices.

The remaining theorem is therefore a first-appearance packing result for these canonical staircase pairs, not an inequality for the state harmonic mass itself.

---

## 7. Limitation

The construction is specific to adjacent completion roles. For an outer role, off-diagonal gaps are sums `d_i+d_j`, so no analogous pointwise smaller-gap matching exists in general. The complete off-diagonal energy theorem still pays the outer debt, but its scale behavior is nontriangular.
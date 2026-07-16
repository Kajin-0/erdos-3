# Adjacent off-diagonal staircase transfer

## Status

State-independent sparse cross-copy transfer for every recursively continuing adjacent completion-step shell.

The two affine copies contain a canonical set of exactly `|T|` unmatched cross-copy pairs whose gaps are pointwise smaller than the step values they pay. Thus the complete adjacent-role harmonic debt transfers to strictly lower-gap physical pair capacity without using the matched activated target pairs.

Global reuse of the selected staircase pairs remains a lineage-owned pair-collision problem.

---

## 1. Two adjacent affine copies

Let

```math
T=\{d_1<d_2<\cdots<d_n\}\subseteq[M,2M),
\qquad n\ge3.
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

are the activated targets and have gaps `d_i`. The left-adjacent role is the reflected copy and has the same absolute pair gaps.

---

## 2. Corrected canonical staircase

For

```math
1\le i<n,
```

define

```math
p_i=\{x_{i+1},y_i\}.
```

Close the staircase with

```math
p_n=\{x_n,y_1\}.
```

Every pair is off-diagonal. The pairs are physically distinct because the ordered pair of affine-copy indices is distinct:

```text
(2,1),(3,2),...,(n,n-1),(n,1).
```

The former candidate `p_n={x_1,y_2}` was incorrect: on a three-term progression its gap can equal `d_n`, so it does not provide strict descent.

---

## 3. Positivity and strict pointwise descent

For `i<n`,

```math
\operatorname{gap}(p_i)
=
2d_i-d_{i+1}.
```

Since `d_i>=M` and `d_{i+1}<2M`,

```math
0<2d_i-d_{i+1}<d_i.
```

Therefore

```math
w(p_i)>rac1{d_i}.
```

For the corrected closing pair,

```math
\operatorname{gap}(p_n)
=
2d_1-d_n.
```

Again `d_1>=M` and `d_n<2M`, so the gap is positive. Moreover `d_1<d_n`, hence

```math
2d_1-d_n<d_n.
```

Thus

```math
w(p_n)>rac1{d_n}.
```

Every assigned pair has strictly smaller gap than the harmonic denominator it pays.

---

## 4. Pointwise harmonic payment

Assign `1/d_i` to `p_i`. Then

```math
\boxed{
H(T)
=
\sum_{i=1}^n\frac1{d_i}
<
\sum_{i=1}^n w(p_i).
}
```

The transfer uses exactly `n` unmatched cross-copy pairs and excludes every matched activated target pair.

---

## 5. Bellman interpretation

The corrected staircase gives the occurrencewise transition

```text
activated lineage term 1/d_i
    -> unmatched cross-copy pair of gap < d_i.
```

If a selected pair is new to the lineage ledger, it becomes a lower-gap Bellman child. If several states select the same physical pair, physical union capacity alone cannot pay all occurrences; the repeated uses must retain production ownership or export a reference/grid token.

---

## 6. Scope and limitation

This theorem is local and state-independent. It proves the debt-to-smaller-gap conversion for one adjacent recursive state.

It does not prove a universal union-valued Hall inequality. The complete-bipartite and digit-grid no-go constructions show that finite collections of projected physical pair resources can have insufficient union capacity even when every state has strict local surplus.

For an outer role, cross-copy gaps are sums `d_i+d_j`, so no analogous pointwise smaller-gap staircase exists in general. Outer states instead use an unscaled-copy horizontal chain or a lineage-owned higher-order token.

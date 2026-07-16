# Lineage-owned gap-moment contraction

## Status

State-independent Bellman contraction for every recursively continuing heavy completion-step shell.

The theorem is occurrence-owned. It does not require physical pair disjointness across different states and does not claim a second copy of an already existing pair resource. Each source occurrence transfers its own debt label to lower-gap pair labels.

---

## 1. Recursive shell and debt

Let

```math
T=\{d_1<\cdots<d_n\}\subseteq[M,2M)
```

be recursively continuing. Then `T` contains a three-term progression, so `n>=3`.

Let

```math
D(T)=\alpha H(T),
\qquad
\alpha\in\{1,1/2\},
```

where `alpha=1` for an adjacent completion role and `alpha=1/2` for an outer role.

---

## 2. Horizontal-chain capacity

Put

```math
r_i=d_{i+1}-d_i,
\qquad 1\le i<n.
```

Every gap satisfies

```math
0<r_i<M.
```

The adjacent-chain inequality gives

```math
\sum_{i=1}^{n-1}\frac1{r_i}
>
H(T)
\ge
D(T).
```

Therefore there exist rational allocations

```math
0\le f_i\le\frac1{r_i}
```

such that

```math
\sum_{i=1}^{n-1}f_i=D(T).
```

For example, fill the chain capacities greedily in a deterministic order until the exact demand is reached.

---

## 3. Dyadic gap moment

Let `R_i` be the standard dyadic shell base of `r_i`:

```math
R_i\le r_i<2R_i.
```

Since `r_i<M` and `M` is a power of two,

```math
R_i\le\frac M2.
```

For every `p>=0`, define the outgoing lineage moment

```math
\Phi_p^{\rm out}(T)
=
\sum_i f_iR_i^p.
```

The incoming moment is

```math
\Phi_p^{\rm in}(T)
=
M^pD(T).
```

Then

```math
\begin{aligned}
\Phi_p^{\rm out}(T)
&=\sum_i f_iR_i^p\\
&\le\left(\frac M2\right)^p\sum_i f_i\\
&=2^{-p}M^pD(T).
\end{aligned}
```

Hence

```math
\boxed{
\Phi_p^{\rm out}(T)
\le
2^{-p}\Phi_p^{\rm in}(T).
}
```

At every positive exponent, recursive heavy debt contracts strictly.

---

## 4. Critical and logarithmic forms

At `p=1`,

```math
\boxed{
\Phi_1^{\rm out}(T)
\le
\frac12\Phi_1^{\rm in}(T).
}
```

Thus at least half of the scale-weighted incoming value is released at one recursive heavy transition.

Define the dyadic-depth release

```math
\Lambda(T)
=
\sum_i f_i\log_2\frac M{R_i}.
```

Every term has depth drop at least one, so

```math
\boxed{
\Lambda(T)\ge D(T).
}
```

This is the logarithmic derivative form of strict gap descent.

---

## 5. Physical lift

For each completion role, the selected horizontal chain is realized by physical pairs in one affine copy of `T`. The pair corresponding to `r_i` has reciprocal-gap capacity `1/r_i`, exactly the upper bound used for `f_i`.

Different source states may select the same physical pair. The theorem remains valid as a lineage transition:

```text
source occurrence label
    + allocated mass f_i
    + source shell M
        ->
physical pair identity
    + inherited source label
    + target gap shell R_i<=M/2.
```

Collapsing these labels to an unlabelled physical union is a separate Hall problem and is known to fail for unrestricted affine families.

---

## 6. Bellman interface

The direct maximal-ambient discharge row may treat a recursive heavy shell as follows:

```text
recursive heavy debt at scale M
    -> occurrence-owned pair debt at gap scale at most M/2.
```

Consequently recursive heavy fibers are not the source of same-scale growth once ownership is retained. The unresolved universal terms are now:

1. initial production of pair-lineage tokens;
2. same-scale light-support or cross-shell transfers;
3. terminal heavy-sink recreation;
4. release or merging rules for repeated physical identities.

The theorem supplies a strict geometric factor for the genuinely recursive heavy part without assuming bounded physical-pair multiplicity.

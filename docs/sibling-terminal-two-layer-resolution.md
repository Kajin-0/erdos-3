# Sibling terminal two-layer resolution

## Status

Exact sibling-level cross-state multiplicity theorem for the multiplicity-resolved deletion-DAG recursion.

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free. Consider the recursive child states produced from one parent state after:

1. resolving repeated middle labels by center fibers;
2. retaining at most one structural occurrence per parent element.

Every recursive child has the form

```math
S_j=B_j-t_j,
```

where

```math
B_j\subseteq D
```

and `t_j` is a fixed translation anchor. Moreover, every element of `D` belongs to at most two lifted child sets `B_j`.

Suppose the children `S_j` are recursively processed and emit terminal distinct steps. For a fixed numerical step `q`, the terminal occurrences of `q` across all sibling states can be resolved into at most two terminal copies of `q`, with every additional occurrence exported to lower-scale four-term-progression-free center-difference children.

---

# 1. Lift multiplicity of sibling child states

The recursive children come from three translated families.

## Component-translation children

A retained component child is

```math
\widetilde\Theta_j
=
\{x-m_j:x\in B_j\},
```

with `B_j subseteq D` and anchor `m_j in D`.

## Merge-difference children

A retained merge child is

```math
\widetilde\Delta_v
=
\{a-p_v:a\in B_v\},
```

with `B_v subseteq D` and anchor `p_v in D`.

## Middle multiplicity-fiber children

For a repeated middle step `r`, the fiber child is

```math
\Xi_r
=
\{a-a_r:a\in B_r\},
```

because the coordinated orientation for fixed `r` makes center differences equal sponsor differences. Again `B_r subseteq D` and `a_r in D`.

Thus every recursive child state is a translate of a subset of the same parent set `D`.

The thinning rules associate at most:

- one recursive structural occurrence with a parent element;
- one recursive middle-fiber occurrence with a deleted parent element.

Therefore

```math
\boxed{
\sum_j 1_{B_j}(x)\le2
\qquad(x\in D).
}
```

This pointwise lift-multiplicity bound is the only property of the child construction needed below.

---

# 2. Lifting a sibling terminal step

Suppose a child state `S_j` emits terminal step `q`. By construction, its side-anchor deletion selected a three-term progression

```math
c_{j,q}-q,
\qquad
c_{j,q},
\qquad
c_{j,q}+q
```

inside `S_j`.

Translate this progression back to the parent set using `t_j`. Its lifted center is

```math
x_{j,q}=t_j+c_{j,q}.
```

Then

```math
x_{j,q}-q,
\qquad
x_{j,q},
\qquad
x_{j,q}+q
```

all lie in `B_j subseteq D`.

For fixed `q`, the lifted center determines the lifted progression uniquely. If the same center `x` occurs in several sibling states, then `x` lies in each corresponding `B_j`. Since the lift multiplicity is at most two,

```math
\boxed{
\text{every lifted center occurs with multiplicity at most two.}
}
```

---

# 3. Two center layers

Fix `q`, and let `n(q)` be its number of terminal occurrences across the sibling states.

Define

```math
X_q^{(1)}
=
\{x_{j,q}:q\text{ is terminal in }S_j\},
```

as a set of distinct lifted centers, and define

```math
X_q^{(2)}
=
\{x:\text{the center }x\text{ occurs in exactly two sibling states}\}.
```

Because center multiplicity is at most two,

```math
\boxed{
n(q)=|X_q^{(1)}|+|X_q^{(2)}|.
}
```

Both layers are subsets of `D`, hence both are four-term-progression-free.

For `k in {1,2}`, whenever `X_q^{(k)}` is nonempty, choose

```math
x_{q,k}=\min X_q^{(k)}
```

and define the sibling center-difference child

```math
\Omega_{q,k}
=
\{x-x_{q,k}:x\in X_q^{(k)},\ x>x_{q,k}\}.
```

Then

```math
|\Omega_{q,k}|=|X_q^{(k)}|-1.
```

Since `X_q^{(k)} subseteq D subseteq[N,2N)`, every element of `Omega_{q,k}` lies in `[1,N)`. Translating a four-term progression in `Omega_{q,k}` by `x_{q,k}` would produce one in `D`, so

```math
\boxed{
\Omega_{q,k}\text{ is four-term-progression-free.}
}
```

---

# 4. Exact sibling multiplicity decomposition

Let

```math
r(q)
=
1_{X_q^{(1)}\ne\varnothing}
+
1_{X_q^{(2)}\ne\varnothing}.
```

Thus `r(q)` is either one or two whenever `n(q)>0`.

Retain one terminal copy of `q` for each nonempty center layer, and export all remaining occurrences in that layer to `Omega_{q,k}`. Then

```math
\begin{aligned}
r(q)
+
\sum_{k=1}^{2}|\Omega_{q,k}|
&=
\sum_{k:X_q^{(k)}\ne\varnothing}
\bigl(1+|X_q^{(k)}|-1\bigr)\\
&=
|X_q^{(1)}|+|X_q^{(2)}|\\
&=
n(q).
\end{aligned}
```

Therefore

```math
\boxed{
\text{all sibling occurrences of }q
\text{ are resolved into at most two terminal copies and lower-scale children.}
}
```

No sibling terminal occurrence is lost at the cardinality level.

---

# 5. Harmonic lower bound

Every child state lies below the parent scale, so a terminal step emitted by a child satisfies

```math
q\le N/2.
```

Hence every retained terminal copy contributes at least `2/N`. Every element of every `Omega_{q,k}` is below `N` and contributes more than `1/N`.

Thus the sibling-resolved output for fixed `q` has harmonic mass at least

```math
\begin{aligned}
\frac{r(q)}q
+
\sum_{k=1}^{2}H(\Omega_{q,k})
&\ge
\frac{2r(q)}N
+
\frac{n(q)-r(q)}N\\
&=
\frac{n(q)+r(q)}N\\
&\ge
\frac{n(q)}N.
\end{aligned}
```

Summing over all terminal labels produced by the sibling family gives

```math
\boxed{
H(\text{sibling terminal representatives})
+
\sum_{q,k}H(\Omega_{q,k})
\ge
\frac{T}{N},
}
```

where `T` is the total number of sibling terminal occurrences before resolution.

---

# 6. Half-contraction

Associate each center-layer output with the corresponding lifted center `x`.

A retained terminal step satisfies

```math
x-q\in D,
\qquad
x-q\ge N,
```

so

```math
q\le x-N\le x/2.
```

A center-difference output has the form

```math
x-x_{q,k},
```

with `x_{q,k}>=N`, and therefore

```math
0<x-x_{q,k}\le x-N\le x/2.
```

Hence every output of the sibling-resolution operation is at most half its associated lifted center.

Since each center occurs in at most two layers, it creates at most two sibling-resolution outputs.

---

# 7. Interpretation

The one-parent multiplicity-fiber theorem resolves repeated middle labels inside each child state. The present theorem advances one level further:

- equal terminal labels across sibling states are grouped by their lifted centers in the common parent set;
- the pointwise two-fold lift multiplicity produces exactly two center layers;
- each layer retains one terminal representative and exports every additional copy to a lower-scale four-term-progression-free difference child;
- all outputs remain half-contracted.

Thus arbitrary sibling multiplicity is reduced exactly to terminal multiplicity at most two.

The remaining unresolved repetition is between states with different parent nodes, which do not share a common four-term-progression-free ambient set. A global theorem must either create a common ancestral lift for such states or control how often a numerical label can survive through unrelated branches.

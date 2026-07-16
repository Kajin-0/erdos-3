# Heavy-shell horizontal-chain transfer

## Status

State-independent transfer lemma for recursive completion-step fibers.

Every step shell containing at least three points is paid by a physical horizontal adjacent chain already present in its double-affine completion lift. All chain-pair gaps lie strictly below the step-shell base. Therefore recursive heavy-fiber harmonic mass can be converted into smaller-gap physical pair capacity.

The lemma is occurrencewise. Reuse of the same horizontal pair across distinct completion fibers remains a first-appearance/reference-gap packing problem.

---

## 1. Dyadic step shell

Let

```math
T=\{d_1<d_2<\cdots<d_n\}
\subseteq[M,2M)
```

with

```math
n\ge3.
```

Put

```math
r_i=d_{i+1}-d_i,
\qquad 1\le i<n.
```

Then

```math
r_i>0
```

and

```math
\sum_{i=1}^{n-1}r_i
=d_n-d_1
<M.
```

In particular every adjacent gap satisfies

```math
0<r_i<M.
```

---

## 2. Harmonic chain domination

By Cauchy-Schwarz,

```math
\left(\sum_{i=1}^{n-1}\frac1{r_i}\right)
\left(\sum_{i=1}^{n-1}r_i\right)
\ge
(n-1)^2.
```

Since the total adjacent span is strictly less than `M`,

```math
\sum_{i=1}^{n-1}\frac1{r_i}
>
\frac{(n-1)^2}{M}.
```

Also every `d_i>=M`, so

```math
H(T)
=
\sum_{i=1}^n\frac1{d_i}
\le
\frac nM.
```

For `n>=3`,

```math
(n-1)^2\ge n.
```

Therefore

```math
\boxed{
H(T)
<
\sum_{i=1}^{n-1}\frac1{d_{i+1}-d_i}.
}
```

The strictness comes from `d_n-d_1<M`. No arithmetic-progression hypothesis is required beyond the cardinality condition `n>=3`.

The statement is intentionally not asserted for arbitrary two-point shells.

---

## 3. Physical horizontal lift

A completion-step fiber has one of the three double-affine forms.

### Right adjacent role

```math
c+T,
\qquad
c+2T.
```

### Left adjacent role

```math
c-T,
\qquad
c-2T.
```

### Outer role

```math
c-T,
\qquad
c+T.
```

All displayed points belong to the ambient root set because every `d in T` indexes one physical target pair.

Choose the first displayed copy deterministically. Its horizontal adjacent chain is

```math
E_{c,T}
=
\bigl\{
\{c+\sigma d_i,c+\sigma d_{i+1}\}:
1\le i<n
\bigr\},
```

with the evident sign convention for the role. Each pair has gap

```math
r_i=d_{i+1}-d_i.
```

Hence

```math
J(E_{c,T})
=
\sum_{i=1}^{n-1}\frac1{r_i}
>
H(T).
```

For an outer role the recursive debt is only `H(T)/2`, so the same chain also pays it. Writing the role coefficient as

```math
\alpha\in\{1,1/2\},
```

one obtains

```math
\boxed{
\alpha H(T)
<
J(E_{c,T}).
}
```

---

## 4. Strict gap descent

Every horizontal chain pair satisfies

```math
\operatorname{gap}(e)<M.
```

After standard dyadic resolution, its gap shell base is at most

```math
M/2.
```

Thus the transfer has strict pair-gap descent:

```text
recursive step shell at base M
    -> horizontal physical pairs of gap below M.
```

This is stronger than merely re-emitting the same recursive shell.

---

## 5. Terminal and recursive cases

A one- or two-point heavy shell need not satisfy the chain inequality. It is, however, automatically three-AP-free and belongs to the terminal ledger.

Any recursive heavy shell contains a three-AP and hence has at least three elements. The horizontal-chain transfer therefore applies to every recursively continuing heavy shell.

Consequently the direct maximal-discharge row may replace

```math
\sum_{T\in\mathcal R_{\rm heavy}}\alpha(T)H(T)
```

by horizontal pair occurrences of strictly smaller gap.

---

## 6. Multiplicity interface

For a fixed embedded fiber `(c,role,T)`, the horizontal chain is a physical pair set and contains no internal duplicate.

Across different embedded fibers, the same horizontal pair may reappear. This is a genuine pair-resource collision. It must not be hidden by summing occurrence energies.

Repeated horizontal chains have the same affine rectangle structure as the earlier collision fibers. For a fixed numerical state and orientation, varying completions produce translated copies; their reference set and reference-difference reserve are four-AP-free and lie below the parent scale.

Therefore the approved packing interface is:

```text
first horizontal-pair appearance
    -> carried smaller-gap physical pair;
repeated horizontal-pair occurrence
    -> reference-difference / rectangle token.
```

The present lemma proves the local mass transfer and strict gap descent. The reference-gap theorem supplies the multiplicity object.

---

## 7. Strategic consequence

After direct maximal completion, every activated pair has one of four outcomes:

```text
local three-AP edge token;
cross-shell new pair;
light canonical support pair;
heavy-shell horizontal chain.
```

The last three are physical pair resources. For recursive heavy shells, their gaps are strictly smaller than the shell base that generated them.

Thus the remaining treewise problem can be formulated entirely as first appearance and reuse of physical pairs, together with terminal sinks. No free-standing recursive harmonic state is necessary once the horizontal-chain lift is applied.
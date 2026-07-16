# Two-route recursive pair reserve

## Status

State-independent **local** resource theorem for recursively continuing completion-step shells.

Every recursive state has two independently sufficient canonical pair routes, but neither local surplus nor the union of the two route neighborhoods implies a universal Hall packing theorem. The universal two-route Hall target is false, and the corrected alternate route already has an exact 19-state min-cut obstruction on `S7`.

---

## 1. Recursive state

Let

```math
T=\{d_1<\cdots<d_n\}\subseteq[M,2M),
\qquad n\ge3,
```

and let

```math
\operatorname{debt}(T)=\alpha H(T),
```

where `alpha=1` for adjacent roles and `alpha=1/2` for the outer role.

---

## 2. Primary route: first-copy horizontal chain

In one unscaled affine copy, use adjacent pairs with gaps

```math
r_i=d_{i+1}-d_i.
```

Then

```math
\sum_{i=1}^{n-1}\frac1{r_i}>H(T)\ge\operatorname{debt}(T).
```

Every gap is below `M`, so the primary route has strict dyadic shell descent.

---

## 3. Adjacent alternate route: corrected staircase

For an adjacent role write

```math
x_i=c+\sigma d_i,
\qquad
y_i=c+2\sigma d_i.
```

Use

```math
\{x_{i+1},y_i\},\qquad1\le i<n,
```

and close with

```math
\{x_n,y_1\}.
```

The first `n-1` gaps are

```math
2d_i-d_{i+1},
```

which lie in `(0,d_i)`. The closing gap is

```math
2d_1-d_n,
```

which lies in `(0,d_n)` because `d_1>=M` and `d_n<2M`.

Hence each harmonic term has its own strictly smaller-gap unmatched cross-copy pair, and

```math
J(R_2(T))>H(T).
```

The former closing pair `{x_1,y_2}` was incorrect: on a three-term progression its gap can equal `d_n`.

---

## 4. Outer alternate route

For an outer role, the two copies are

```math
c-T,
\qquad
c+T.
```

Either copy has the same adjacent horizontal-chain capacity as `T`, so either route satisfies

```math
J(R_j(T))>H(T)>\frac12H(T)=\operatorname{debt}(T).
```

Both outer routes have strict dyadic shell descent.

---

## 5. What the local theorem proves

For every one embedded recursive state `s`,

```math
J(R_1(s))>\operatorname{debt}(s)
```

and

```math
J(R_2(s))>\operatorname{debt}(s).
```

These are singleton inequalities. They do not make the two routes independent copies of spendable physical capacity.

---

## 6. Exact `S7` comparison

The primary route packs the complete certified recursive frontier:

```text
states                     278
demand          2.365133143358...
maximum flow    2.365133143358...
unmet demand               0
```

The corrected alternate route does not:

```text
maximum flow    2.361437656917...
unmet demand    0.003695486441...
min-cut states             19
min-cut pairs             176
```

Thus local route sufficiency does not determine a globally feasible orientation.

Primary reference: `docs/s7-direct-gap-triangular-packing.md`.  
Alternate no-go: `docs/s7-alternate-route-min-cut-no-go.md`.

---

## 7. Universal physical-union no-go

The high-digit carry-free construction proves that even the union of the primary chains and corrected adjacent staircases can have insufficient physical capacity for all recursive state demands. For sufficiently large dimension,

```math
\sum_s\operatorname{debt}(s)
>
J\!\left(\bigcup_s(R_1(s)\cup R_2(s))\right).
```

Therefore the proposed universal two-route Hall theorem is false.

Primary reference: `docs/high-digit-two-route-hall-no-go.md`.

---

## 8. Surviving use of the routes

The routes remain valuable as **lineage transitions**:

```text
primary chain:
  strict dyadic gap-shell descent;

corrected adjacent staircase:
  strict pointwise integer-gap descent;

outer alternate chain:
  strict dyadic gap-shell descent.
```

A valid global potential may orient production-owned occurrences through these routes while retaining lineage labels. It may not collapse all occurrences to one unlabelled physical pair union.

The exact next object is the mixed-route incidence cut, not another locally sufficient route family.

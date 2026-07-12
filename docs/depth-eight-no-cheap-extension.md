# Complete cheap-extension exclusion for the depth-eight state

## Status

Exact finite computer-assisted theorem with structural witnesses.

Let

```math
S_8\subseteq[8388608,16777216),
\qquad
|S_8|=29523,
\qquad
\max S_8=14604604
```

be the state from `docs/contaminated-backbone-depth-eight-chain.md`.

This note proves

```math
\boxed{N_{8,2}=N_{8,4}=0.}
```

Thus every continuation of this recorded state in the standard-dyadic disjoint three-translate replay model either terminates or has scale factor at least `8`.

**Verifier:** `src/verify_depth8_no_cheap_extension.cpp`.

**Bounded-memory driver:** `src/run_verify_depth8_no_cheap_extension.sh`.

**Certificate:** `data/depth8_no_cheap_extension_certificate_2026-07-11.txt`.

---

## 1. Candidate domains

Put

```math
B=\{0\}\cup S_8.
```

For separation `R`, form

```math
G_R
=
B\cup(B+R)\cup(B+2R).
```

A candidate must have even `v_2(R)`, fit below the requested next dyadic scale, have disjoint translate layers, and be four-term-progression-free.

Layer disjointness is equivalent to requiring that neither `R` nor `2R` be a positive difference of two points of `B`.

### Factor two

The fit condition gives

```math
R\le1086305.
```

There are

```text
724204 sponsor-compatible candidates
172448 disjoint-layer candidates
```

### Factor four

The fit condition gives

```math
R\le9474913.
```

There are

```text
6316609 sponsor-compatible candidates
4190292 disjoint-layer candidates
```

---

## 2. Completion witnesses

Let three points of `B` form a positive three-term progression. Its missing left or right completion is a coordinate `z`. If another base point `b` satisfies

```math
|z-b|=kR,
\qquad
k\in\{1,2,3\},
```

then an available three-layer pattern supplies the missing fourth point and produces a nontrivial four-term progression in `G_R`.

The exact completion set contains

```text
2772873
```

distinct coordinates, ranging from

```text
6291444 to 17038008.
```

An exact bitset correlation of completion coordinates against base points gives:

```text
factor-two completion witnesses  = 172448
factor-four completion witnesses = 3442176
```

Therefore every disjoint factor-two candidate is invalid:

```math
\boxed{N_{8,2}=0.}
```

For factor four, completion witnesses leave

```text
748116
```

candidates.

---

## 3. Layer pattern `1001`

Suppose

```math
y,y+3d\in B,
\qquad
x,x+d\in B,
```

and

```math
R=x-y-d>0.
```

Then

```math
y+R,
\quad x,
\quad x+d,
\quad y+3d+R
```

is

```math
x-d,
\quad x,
\quad x+d,
\quad x+2d,
```

and hence forms a four-term progression. The layer pattern relative to the base points is `1001`.

This class covers another

```text
73
```

candidates, leaving

```text
748043.
```

The remaining-list FNV-64 hash is

```text
b8ddbb02d22c7ca4
```

---

## 4. Layer pattern `0011`

Suppose two base pairs have the same positive difference:

```math
x,x+d\in B,
\qquad
y,y+d\in B.
```

If

```math
R=x+2d-y>0,
```

then

```math
x,
\quad x+d,
\quad y+R,
\quad y+d+R
```

becomes

```math
x,
\quad x+d,
\quad x+2d,
\quad x+3d.
```

Thus it is a four-term progression with layer pattern `0011`.

The equal-difference join is reproduced in bounded-memory deterministic phases. Each phase runs in a fresh process and passes only the exact remaining candidate list to the next phase.

| Phase | Pair operations | Remaining candidates | FNV-64 |
|---:|---:|---:|---|
| initial | — | 748043 | `b8ddbb02d22c7ca4` |
| 1 | 2000000000 | 27182 | `7a7433cf08775279` |
| 2 | 2000000000 | 1266 | `2cd2e22c6768791d` |
| 3 | 2000000000 | 45 | `ec113295ef522398` |
| 4 | 2000000000 | 4 | `1c87eedd7756042d` |
| 5 | 5000000000 | 3 | `4ca400f49b2c73f1` |

The final three separations are

```text
5353028
5353089
5353229
```

and each also has an explicit `0011` witness.

### Terminal witness for `R=5353028`

```math
10161822,
11951729,
13741636,
15531543.
```

### Terminal witness for `R=5353089`

```math
8388608,
12029053,
15669498,
19309943.
```

### Terminal witness for `R=5353229`

```math
12035410,
13893656,
15751902,
17610148.
```

No factor-four candidate survives. Therefore

```math
\boxed{N_{8,4}=0.}
```

---

## 5. Quantitative consequence

If a ninth state exists, then its scale factor is at least `8`. Since

```math
|S_9|=3(|S_8|+1)=88572,
\qquad
P_9^{\mathrm{cert}}=512,
```

one obtains

```math
\boxed{
W_9\le\frac{22143}{32768}.
}
```

Equivalently,

```math
\boxed{
\frac{W_9}{W_8}
\le
\frac{7381}{9841}
\approx0.750025.
}
```

Relative to the depth-five state,

```math
\boxed{
\frac{W_9}{W_5}
\le
\frac{7381}{11648}
\approx0.633671.
}
```

The bound is attained by the exact depth-nine continuation recorded in `docs/contaminated-backbone-depth-nine-chain.md`.

---

## 6. Scope

This is a complete finite theorem for one recorded state. It does not imply that every contaminated state forbids cheap descendants, nor does it prove a universal long-run compensation theorem. Its significance is that the delayed release at depth seven is followed by two certified forced factor-eight repayments along this branch.

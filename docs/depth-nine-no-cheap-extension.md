# Complete cheap-extension exclusion for the depth-nine state

## Status

Exact finite computer-assisted theorem with structural witnesses.

Let

```math
S_9\subseteq[67108864,134217728),
\qquad
|S_9|=88572,
\qquad
\max S_9=115267902.
```

This note proves

```math
\boxed{N_{9,2}=N_{9,4}=0.}
```

Thus every continuation of this recorded state in the standard-dyadic disjoint three-translate replay-containment model either terminates or has dyadic scale factor at least `8`.

**Verifier:** `src/verify_depth9_no_cheap_extension.cpp`.

**Bounded-memory driver:** `src/run_verify_depth9_no_cheap_extension.sh`.

**Certificate:** `data/depth9_no_cheap_extension_certificate_2026-07-12.txt`.

**Transverse-difference data:** `data/depth9_transverse_differences_2026-07-12.txt`.

---

## 1. Candidate domains

Put

```math
B=\{0\}\cup S_9.
```

For an integer separation `R`, form

```math
G_R=B\cup(B+R)\cup(B+2R).
```

A candidate must:

1. have even `v_2(R)`, so coordinated deletion selects the left sponsor;
2. fit below the requested next dyadic scale;
3. have disjoint translate layers;
4. remain four-term-progression-free;
5. retain `S_9` in the relevant backbone shell.

Layer disjointness is equivalent to requiring that neither `R` nor `2R` is a positive difference of two points of `B`.

The exact difference domain is reconstructed from the smaller parent `S_8` and the identity

```math
S_9
=
L_9+
\bigl(A_8\cup(A_8+R_8)\cup(A_8+2R_8)\bigr),
```

where

```math
A_8=\{0\}\cup S_8,
\qquad
R_8=16777217.
```

This avoids explicitly materializing all pair differences of the 88,573-point set `B`.

### Factor two

The fit condition gives

```math
R\le9474912.
```

The finite domain contains

```text
6316608 sponsor-compatible candidates
2967413 disjoint-layer candidates.
```

### Factor four

The fit condition gives

```math
R\le76583776.
```

The finite domain contains

```text
51055851 sponsor-compatible candidates
39459384 disjoint-layer candidates.
```

---

## 2. Completion witnesses

Suppose three points of `B` form a positive three-term progression. Let `z` be its missing left or right completion. If another base point `b` satisfies

```math
|z-b|=kR,
\qquad
k\in\{1,2,3\},
```

then an available three-layer pattern supplies the missing fourth point, producing a nontrivial four-term progression in `G_R`.

The exact completion set contains

```text
13923661 distinct completion coordinates
```

in the range

```text
50331647 through 134478523.
```

A packed-bit correlation against all 88,573 points of `B`, split into nine deterministic chunks, produces

```text
71129286 distinct absolute completion-to-base differences.
```

This witness class covers every disjoint factor-two candidate:

```math
\boxed{N_{9,2}=0.}
```

For factor four it covers

```text
30221222 of 39459384 disjoint candidates,
```

leaving

```text
9238162 candidates.
```

---

## 3. Equal-difference rectangle witnesses

The surviving witnesses use the layer pattern `0011`.

Suppose

```math
x,x+d\in B,
\qquad
y,y+d\in B.
```

Writing

```math
\delta=x-y,
```

one obtains a shifted four-term progression whenever

```math
R=2d-\delta
```

or under the symmetric sign orientation. Indeed,

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

Equivalently, this is a rectangle

```math
x,
\quad x+d,
\quad x+\delta,
\quad x+d+\delta
```

inside `B`, converted into a four-term progression by placing the second equal-difference pair in the adjacent translate layer.

The zero-transverse subcase is especially simple. If `R=2d` and `B` contains `x,x+d`, then the same pair in adjacent layers yields

```math
x,
\quad x+d,
\quad x+2d,
\quad x+3d.
```

### Recursive compression

Although `B` has approximately 3.9 billion unordered pair starts, every equal-difference start group is reconstructed from at most three difference groups in the 29,524-point parent anchor set `A_8`. This reduces the stored pair-start count to approximately 435 million and makes exact bounded-memory processing possible.

A deterministic list of 288 high-yield transverse differences, together with the zero-transverse class, reduces the completion-resistant domain to

```text
15471 candidates
FNV-64 7e4bdb962920ad1c.
```

The remaining rectangle groups are then exhausted by multiplicity bands. Selected checkpoints are:

| Maximum processed multiplicity | Remaining candidates | FNV-64 |
|---:|---:|---|
| 30 | 13875 | `41c6a37e7a5cbaab` |
| 100 | 9423 | `94b222cc89420cd5` |
| 250 | 3404 | `1cbb6debab4cde02` |
| 300 | 2205 | `2c711b8a795edcfa` |
| 425 | 1207 | `a24557aa6e8632ad` |
| 432 | 909 | `7dc8d091009de569` |
| 500 | 711 | `fa2bfe93a59c5bfe` |
| 576 | 431 | `8e378645299ba92f` |
| 648 | 271 | `07563416517037dc` |
| 800 | 149 | `b502761bc380af0a` |
| 864 | 93 | `f4fd09a42686a230` |
| 1000 | 50 | `da6837c8df0b2088` |
| 1500 | 15 | `dcab870e3567b681` |
| 2000 | 7 | `36448695e481d4d0` |

Low- and moderate-multiplicity groups are enumerated directly. Dense recursive spikes are handled by target-directed difference tests, so work scales with the current residual rather than with all rectangles in the group.

---

## 4. Final seven candidates

After every relevant rectangle group of multiplicity at most `2000` is exhausted, seven separations remain. Each is checked against the complete 265,719-point raw parent and has an explicit four-term-progression witness.

| Separation `R` | Explicit four-term progression |
|---:|---|
| 74090852 | `78873376, 114755138, 150636900, 186518662` |
| 76281492 | `77131832, 115110758, 153089684, 191068610` |
| 76460249 | `76861739, 114934018, 153006297, 191078576` |
| 76468444 | `76869934, 114942213, 153014492, 191086771` |
| 76468753 | `76869589, 114942195, 153014801, 191087407` |
| 76519853 | `76776212, 115078719, 153381226, 191683733` |
| 76561979 | `77081746, 115247623, 153413500, 191579377` |

No factor-four candidate survives. Therefore

```math
\boxed{N_{9,4}=0.}
```

Combining the factor-two and factor-four classifications gives

```math
\boxed{N_{9,2}=N_{9,4}=0.}
```

---

## 5. Quantitative consequence

If a tenth state exists, then its scale factor is at least `8`. Since

```math
|S_{10}|=3(|S_9|+1)=265719,
\qquad
P_{10}^{\mathrm{cert}}=1024,
```

one obtains

```math
\boxed{
W_{10}\le\frac{265719}{524288}.
}
```

Equivalently,

```math
\boxed{
\frac{W_{10}}{W_9}
\le
\frac{88573}{118096}
\approx0.750008.
}
```

Relative to the depth-five state,

```math
\boxed{
\frac{W_{10}}{W_5}
\le
\frac{88573}{186368}
\approx0.475259.
}
```

The bound is attained by the exact depth-ten continuation recorded in `docs/contaminated-backbone-depth-ten-chain.md`.

---

## 6. Scope

This is a complete finite theorem for one recorded state. It does not imply that every contaminated state forbids cheap descendants, nor does it prove a universal long-run compensation theorem.

The driver is intentionally split into fresh bounded-memory processes. Full reproduction is computationally substantial: completion generation, nine packed-bit correlations, recursive rectangle reconstruction, and the multiplicity-band certificate are all exact rather than sampled.

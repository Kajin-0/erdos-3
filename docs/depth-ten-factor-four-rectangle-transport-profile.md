# Rectangle transport in the upper `S_10` factor-four domain

## Status

This note contains:

1. an elementary state-independent transport lemma for `0011` rectangles under three-translate replication;
2. an exact finite certificate for `128` equal-rank samples from the upper quartile of the genuinely new `S_10` factor-four domain.

The finite sample is not an interval theorem and does not prove `N_{10,4}=0`.

---

## 1. Rectangle incidence

Let

```math
B'=G_S(B)=B\cup(B+S)\cup(B+2S).
```

An `0011` rectangle in `B` at signed effective separation `U` is a quadruple

```math
x,
\quad x+d,
\quad x+2d-U,
\quad x+3d-U
```

contained in `B`, with `d>0`.

Equivalently, this is the affine-spectrum incidence

```math
\mathcal F_B(U,-U;0)>0.
```

---

## 2. Exact `k=4` transport lemma

### Plus transport

Set

```math
T=4S+U.
```

Use outer layer word

```text
lambda = 0011
```

and parent layer word

```text
mu = 0202.
```

The four transported points are

```math
x,
```

```math
x+d+2S,
```

```math
x+2d-U+T=x+2d+4S,
```

```math
x+3d-U+2S+T=x+3d+6S.
```

They form a four-term progression with common difference

```math
d+2S>0.
```

Therefore

```math
\boxed{
\mathcal F_B(U,-U;0)>0
\Longrightarrow
G_{4S+U}(G_S(B))\text{ contains a nontrivial four-term progression}.
}
```

### Minus transport

Assume

```math
0<U<2S
```

and set

```math
T=4S-U.
```

Use

```text
lambda = 0112
mu     = 2020.
```

The transported progression has common difference

```math
d+2S-U>0.
```

Hence

```math
\boxed{
\mathcal F_B(U,-U;0)>0,
\quad 0<U<2S
\Longrightarrow
G_{4S-U}(G_S(B))\text{ contains a nontrivial four-term progression}.
}
```

Reversal gives the companion normalized channels `1100/2020` and `2110/0202`. Exact signature enumeration shows that these four are the only normalized channels satisfying

```math
(a_\mu,b_\mu)=-4(a_\lambda,b_\lambda).
```

**Verifier:** `src/verify_rectangle_transport_channel.py`  
**Certificate:** `data/rectangle_transport_channel_certificate_2026-07-13.txt`

---

## 3. Application to the recorded `S_10`

The depth-ten state has

```math
S_{10}=L_{10}+G_{R_9}(\{0\}\cup S_9),
```

with

```math
R_9=134217729,
\qquad
4R_9=536870916.
```

The complete genuinely new factor-four domain has

```math
314986450
```

layer-disjoint candidates. Select `512` equal-rank samples at ranks

```math
\left\lfloor\frac{(2j+1)314986450}{1024}\right\rfloor,
\qquad 0\le j<512.
```

The upper quartile consists of indices `384` through `511`, giving `128` samples from

```text
T = 495796172
through
T = 612993283.
```

Every one has an explicit certified four-term progression.

More strongly, every witness descends through the `k=4` rectangle channel to a signed `0011` incidence in `B_9={0}\cup S_9`.

The exact raw layer-pair split is

```text
outer lambda / parent mu
0011 / 0202 : 49
1122 / 0202 : 37
0112 / 2020 : 42
```

Thus, after global outer-layer normalization,

```text
canonical outer class 0011 : 86
canonical outer class 0112 : 42
canonical parent class 0202: 128
```

For every row, the verifier reconstructs the four ancestor points in `B_9` and checks

```math
x,
\quad x+d,
\quad x+2d-A,
\quad x+3d-A,
```

where

```math
A=T-4R_9
```

for the `0011/0202` and `1122/0202` rows, and

```math
A=4R_9-T
```

for the `0112/2020` rows.

The sampled effective separations satisfy

```math
451791\le |A|\le76122367.
```

The upper endpoint is below the `S_9` factor-four fit endpoint

```math
76583776.
```

**Verifier:** `src/verify_depth10_factor4_top_quartile_rectangle_profile.cpp`  
**Witness data:** `data/depth10_factor4_top_quartile128_witnesses_2026-07-13.txt`

Witness-data hashes:

```text
records:  128
FNV-64:   69c322f3b61e1419
SHA-256:  6aa316f495f41b5a062b6c24eb65c0f56360b3ee58bebe8fa89e828fd09263df
```

---

## 4. Interpretation

The upper-domain witnesses are not distributed among many unrelated obstruction types. In this exact stratified sample, all `128` descend through one closed symbolic subsystem:

```text
S_9 rectangle at U
    -> parent word 0202 or 2020
    -> outer word 0011, 1122, or 0112
    -> S_10 obstruction at T=4R_9 plus or minus U.
```

This is the first concrete recurrence channel extracted from the full-range experiment.

The corresponding transport window is

```math
4R_9-76583776
\le T\le
4R_9+76583776,
```

namely

```math
460287140\le T\le613454692.
```

Intersecting with the fitting `S_10` factor-four range gives

```math
460287140\le T\le613454687.
```

The transport lemma alone does not exclude this interval. It reduces interval exclusion to the zero set of the `S_9` rectangle-coverage function

```math
U\mapsto\mathcal F_{B_9}(U,-U;0).
```

---

## 5. Next target

The next exact computation should determine the signed rectangle-coverage zero set of `B_9` for

```math
|U|\le76583776.
```

Then:

1. transport all covered `U` to the high `S_10` interval;
2. classify the uncovered `U` by the remaining 33 obstruction classes;
3. test whether completion and the other low-complexity channels close the residual;
4. derive a state-independent zero-set contraction statement rather than another `S_10` prefix count.

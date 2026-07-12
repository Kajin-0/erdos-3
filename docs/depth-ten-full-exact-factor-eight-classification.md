# Complete exact factor-eight classification from `S_10`

## Status

Exact finite classification of every sponsor-compatible exact-backbone factor-eight separation from the recorded depth-ten state.

For every positive offset in the fitting range, the candidate is classified as:

1. invalid by a three-term-progression completion obstruction;
2. invalid by the half-separation obstruction `R/2 in S_10`; or
3. a valid four-term-progression-free exact continuation.

**Pattern verifier:** `src/verify_exact_tail_pattern_lemmas.py`.

**Classification verifier:** `src/verify_depth10_full_exact_factor8_classification.cpp`.

**Certificate:** `data/depth10_full_exact_factor8_classification_certificate_2026-07-12.txt`.

---

## 1. Exact fitting range

The recorded state satisfies

```math
L_{10}=536870912,
```

```math
|S_{10}|=265719,
\qquad
\max S_{10}=920574272.
```

Write the exact separation as

```math
R=2L_{10}+k.
```

The raw state must fit below `8L_10`, so

```math
\max S_{10}+2R<8L_{10}.
```

This gives

```math
\boxed{0\le k\le613454687.}
```

For positive `k` in this range,

```math
v_2(R)=v_2(k),
```

so sponsor compatibility is equivalent to even `v_2(k)`. There are exactly

```text
408969792
```

sponsor-compatible positive offsets.

The zero offset `k=0`, corresponding to `R=2L_10`, is invalid because

```math
R/2=L_{10}\in S_{10}.
```

---

## 2. State-specific top-layer reduction

Normalize the state by `L_10`. Its exact upper endpoint is

```math
\frac{\max S_{10}}{L_{10}}
=
\frac{14383973}{8388608}.
```

The largest fitting separation has normalized value

```math
\frac{1687196511}{536870912}.
```

Exact rational polytope enumeration over every nondecreasing four-point layer pattern and every zero/nonzero base pattern leaves the same nine patterns as the small-offset theorem:

```text
0000, 1111, 2222
0001, 0012, 1112
0011, 0112, 1122.
```

Therefore every new four-term progression in an exact factor-eight candidate comes from exactly one of:

1. a four-term progression already inside the anchor set;
2. a three-term progression in `S_10` completed at `R`;
3. the half-separation point `R/2` inside `S_10`.

The first possibility is absent because `S_10` is four-term-progression-free and adjoining zero creates no four-term progression in this shell.

Thus completion and half-separation are the complete obstruction list.

---

## 3. Completion obstruction

A right completion in `S_10` cannot exceed

```math
2\max S_{10}-\min S_{10}.
```

Consequently a completion at

```math
2L_{10}+k
```

is possible only when

```math
k\le230535808.
```

The extended completion-descent theorem applies through target offset `4L`. It descends a completion from `S_10` to `S_9` by subtracting `3`, then from `S_9` to `S_8` by subtracting another `3`.

The `S_9` shell geometry shows that the second descent is needed only for

```math
k\le29209215.
```

Within that range, a completion at `2L_10+k` exists exactly when the certified signed `S_8` completion set contains

```math
2L_8+(k-6).
```

Among sponsor-compatible positive offsets, exactly

```math
\boxed{54999}
```

are blocked by this condition.

The blocked offsets range from

```text
13
```

to

```text
260795.
```

Their canonical comma-list hashes are

```text
FNV-64  e22bc4f8babba2ac
SHA-256 b0cdf6b95ee9f17f39560e182b5b1f9c72e6af7fa5b1ef41a51c35a49abdf6ec
```

Every such completion lifts through layers `0,1,2` to an explicit four-term-progression obstruction in the factor-eight raw state.

---

## 4. Half-separation obstruction

If `R` is even, the remaining nonconstant layer patterns occur exactly when

```math
R/2\in S_{10}.
```

Since

```math
R/2=L_{10}+k/2,
```

the verifier scans `S_10` and collects every sponsor-compatible offset

```math
k=2(s-L_{10}).
```

Exactly

```math
\boxed{59034}
```

positive offsets are blocked this way.

They range from

```text
150994944
```

to

```text
536870916.
```

Their canonical hashes are

```text
FNV-64  a1d342c2504bb966
SHA-256 45075ac0f88a7e591bdd6850846831d3d15f63db8016878e35bb0644eb739ca9
```

---

## 5. Disjointness of the obstruction classes

The exact finite calculation gives

```math
\boxed{
\text{completion-blocked}\cap\text{half-blocked}=\varnothing.
}
```

Thus the union contains

```text
114033
```

offsets, with hashes

```text
FNV-64  704c4821b177ab25
SHA-256 92614cc5ec33add8064ef0aedaf4f8fe758600b30912315bec45aa47d48c6861
```

---

## 6. Valid exact continuations

Subtracting the complete obstruction union from the sponsor-compatible positive domain gives

```math
408969792-114033
=
\boxed{408855759}.
```

Therefore the recorded state has

```math
\boxed{408855759}
```

valid positive-offset exact factor-eight continuations.

For every such offset:

1. the three translate layers are disjoint;
2. the raw state fits below `8L_10`;
3. the raw state is four-term-progression-free;
4. the middle multiplicity fiber is exactly `S_10`;
5. the backbone shell is exactly `S_10`;
6. certified replay multiplicity doubles.

---

## 7. Relation to the summable basin fan

The exact-tail basin criterion additionally requires

```math
0<k\le L_{10}/32.
```

Within that small-offset region, the complete classification gives

```math
\boxed{11129810}
```

valid basin entries, each carrying an explicit infinite summable tail.

The other valid exact factor-eight continuations are certified for one exact step but are not yet known to remain in a summable basin indefinitely.

Thus the complete exact factor-eight classification greatly widens the known continuation tree while preserving the distinction between:

- **valid exact child**;
- **certified infinite basin child**.

---

## 8. Scope

This is a complete theorem for exact factor-eight continuations from the recorded `S_10`. It does not classify:

1. factor-two descendants;
2. factor-four descendants;
3. the long-run behavior of exact children outside the certified small-offset basin fan;
4. the union of states across different dyadic shells.

The whole-tree Bellman compensation problem remains open.

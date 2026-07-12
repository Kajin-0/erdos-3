# Lifted `S_9` completion reduction for the depth-ten factor-four domain

## Status

Exact finite structural-witness reduction.

The recorded depth-ten state has

```math
348012826
```

layer-disjoint factor-four candidates. The factor-two inheritance theorem already excludes the lower interval containing `33026376` of them. This note lifts the certified `S_9` completion support through the three embedded depth-nine copies and removes another

```math
\boxed{137142200}
```

candidates from the genuinely new range.

The unresolved factor-four domain is reduced to

```math
\boxed{177844250}
```

candidates.

**Verifier:** `src/verify_depth10_lifted_s9_completion.cpp`.

**Driver:** `src/run_verify_depth10_lifted_s9_completion.sh`.

**Certificate:** `data/depth10_lifted_s9_completion_certificate_2026-07-12.txt`.

---

## 1. Embedded completion geometry

Write

```math
A_9=\{0\}\cup S_9,
\qquad
Q=R_9=134217729.
```

The depth-ten state is

```math
S_{10}
=
L_{10}
+
\bigl(A_9\cup(A_9+Q)\cup(A_9+2Q)\bigr).
```

The certified depth-nine computation gives:

```text
13923661 distinct signed 3-AP completion coordinates
71129286 distinct absolute completion-to-base differences.
```

Let `d` be one such absolute completion-to-base difference. Place the completion and the base point in embedded copies whose layer indices differ by `m`, where

```math
m\in\{-2,-1,0,1,2\}.
```

The resulting depth-ten absolute difference is one of

```math
\boxed{|d+mQ|.}
```

Thus every certified `S_9` completion witness generates a finite family of certified `S_{10}` completion witnesses.

Completions in an embedded copy may also be compared directly with the global anchor zero. These coordinates are included separately.

---

## 2. Exact lifted support

Taking the union over all certified depth-nine completion differences, all three copy positions, and the anchor-zero comparisons gives

```math
\boxed{354838701}
```

distinct lifted completion-to-base differences.

For a factor-four candidate separation `R`, a lifted completion witness exists whenever one of

```math
R,
\qquad
2R,
\qquad
3R
```

belongs to this support. The three possibilities correspond to the available second-difference coefficients in a three-translate layer pattern.

Every candidate removed by this test therefore contains an explicit four-term arithmetic progression. No probabilistic or sampled step is used.

---

## 3. Domain arithmetic

The complete depth-ten factor-four domain contains

```text
408969792 sponsor-compatible separations
348012826 layer-disjoint candidates.
```

The factor-two inheritance theorem excludes the interval

```math
R\le76583775,
```

which contains

```math
33026376
```

layer-disjoint candidates. Therefore the genuinely new domain contains

```math
348012826-33026376
=
\boxed{314986450}
```

candidates.

The lifted completion support covers

```math
\boxed{137142200}
```

of these genuinely new candidates.

Hence the new residual has size

```math
314986450-137142200
=
\boxed{177844250}.
```

Its endpoints are

```text
first  97474324
last   613454687
```

and its ordered-list FNV-64 hash is

```text
00369694f2d70526
```

---

## 4. Consequence

Combining the inherited lower interval with the lifted completion witnesses gives a complete factor-four exclusion through

```math
\boxed{R<97474324.}
```

The immediate finite target is therefore no longer the full 348-million-candidate domain, but the exact residual list of

```math
\boxed{177844250}
```

separations beginning at `R=97474324`.

The next structural classes to apply are:

1. anchor-completion patterns such as `0001`, `1001`, and `2002`;
2. equal-difference `0011` rectangles using transverse-difference compression;
3. explicit exact checks only for the final residual after those bulk witnesses.

---

## 5. Scope

This note uses only completions occurring inside one embedded depth-nine anchor copy. It does not yet include every completion formed by mixing points from different depth-nine copies. Therefore `177844250` is an upper bound on the unresolved domain, not evidence that any candidate survives.

The reduction is state-specific and does not establish a universal factor-four theorem.

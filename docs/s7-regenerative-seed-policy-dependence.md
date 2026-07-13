# Policy dependence of the `S_7` regenerative seed

## Status

Exact fixed-parent finite theorem comparing two complete coordinated deletion
schedules on `S_7`.

The lexicographic schedule emits the isolated child

```math
\{16,21,26\}\subset[16,32),
```

which returns to canonical `S_1` under the factor-four separation `R=1`.
A reverse-lexicographic complete coordinated schedule emits no such child and
has no factor-two or factor-four exact return to any canonical state
`S_1,...,S_10`.

Therefore the exact regeneration is schedule-dependent on the recorded parent.
It is not an unavoidable parent feature.

**Verifier:** `src/verify_s7_regenerative_seed_policy_dependence.py`.

**Certificate:**
`data/s7_regenerative_seed_policy_dependence_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
8b7465459f04d07bd67a7f198b3947ca94756ce988c0c73f4e59a5fac6b4b336
```

---

## 1. Two deterministic policies

Both schedules use the same coordinated sponsor rule:

```text
left endpoint when v2(step) is even;
right endpoint when v2(step) is odd.
```

They differ only in which currently available progression is selected next.

1. **Lexicographic:** smallest `(step,left,middle,right)`.
2. **Reverse lexicographic:** largest `(step,left,middle,right)`.

Deletion cannot create a new three-term progression, so both schedules may be
resolved from the initial exact progression list by discarding stale actions.
Each terminal residual is checked directly to contain no three-term
progression.

The parent has

```text
298,606
```

initial coordinated actions.

---

## 2. Lexicographic schedule

The lexicographic schedule has

```text
selected actions: 9,360
terminal residual: 480
terminal step classes: 25
middle-fiber shells: 124.
```

For step `q=1`, it selects `2,916` centers with minimum

```math
m_{\rm lex}=1354049.
```

The centers

```math
1354065,
\quad
1354070,
\quad
1354075
```

therefore generate the differences

```math
16,21,26.
```

After dyadic shell resolution, these differences form exactly one shell child

```math
X=\{16,21,26\}.
```

The complete canonical-regeneration catalog for this schedule contains exactly

```text
source q=1, scale=16, state={16,21,26}, factor=4, R=1, target=S1.
```

---

## 3. Reverse-lexicographic schedule

The reverse schedule has

```text
selected actions: 9,180
terminal residual: 660
terminal step classes: 2,252
middle-fiber shells: 2,374.
```

For `q=1`, it selects only `55` centers. Its minimum is

```math
m_{\rm rev}=1687866.
```

The corresponding `q=1` fiber does not contain the shell
`{16,21,26}`.

The verifier scans every reverse-schedule middle-fiber shell, both factors
`2` and `4`, and every canonical target scale. The exact regeneration catalog
is empty:

```text
reverse canonical regenerations = 0.
```

Thus reverse lexicographic deletion provides an explicit complete coordinated
schedule avoiding the canonical return.

---

## 4. Root-forced analysis

The existing root-forced theorem identifies `30` initial actions that every
complete coordinated schedule must select.

For step `q=1`, the forced centers are exactly

```math
1687866,
\quad
1781342,
\quad
1918030.
```

The lexicographic seed-producing centers

```math
1354065,
\quad
1354070,
\quad
1354075
```

are not root-forced.

There are `2,916` initially possible `q=1` centers, and `1,459` possible
centers lie at or below the first forced center. Hence the forced-center lower
bound does not determine the lexicographic minimum or the seed differences.

This agrees with the explicit reverse schedule: the parent-intrinsic
forced-fork theorem guarantees positive middle-fiber output, but not this
specific regenerative state.

---

## 5. Exact schedule identifiers

The certificate records exact hashes for independent replay:

```text
lex schedule:
12a369aa926f3ceac00943e8a383a9f635ec9f16b33565ec29f90c2d3d1d8ac1

reverse schedule:
92b9763e6f4edc408192a3e47a34d5ecdd397ee24da090f3050c7e1f8cdf9d11
```

It also records residual, `q=1` center-set, and `q=1` fiber hashes for both
policies.

---

## 6. Consequence

The isolated return

```math
\{16,21,26\}\xrightarrow[f=4]{R=1}S_1
```

is real, unique on the lexicographic cyclic-source frontier, and numerically
isolated within that raw transition. But it is not schedule-independent.

Therefore a parent-only reserve cannot assign unavoidable regenerative charge
to `S_7` merely because the lexicographic schedule exhibits this child.

The proof program must choose between two stronger routes:

1. construct and certify a global deletion policy whose schedule-dependent
   regenerative and obstruction outputs satisfy a whole-tree inequality; or
2. derive a schedule-independent lower envelope over all complete policies,
   using forced output, affine coverage, overlap, and residual continuation
   cost together.

---

## 7. Scope

This theorem does not show that reverse lexicographic deletion is globally
optimal, summable, or compatible with a closing Bellman potential. It only
proves that one complete valid schedule avoids the canonical regeneration.

It also does not show that the reverse schedule avoids all near-regenerations,
noncanonical returns, or expensive descendants.

The result rules out only the inference

```text
The isolated canonical S1 return is forced by the parent S7 state.
```

That inference is false.

---

## 8. Revised next target

The next finite comparison should compute the complete simultaneous transition
features for both policies in common Bellman units:

1. forced and total middle-fiber mass;
2. exact duplicate, containment, and partial-overlap load;
3. SCC spectral structure;
4. local and complete affine obstruction coverage;
5. regenerative and near-regenerative continuation cost;
6. terminal residual error.

This will test whether a constructive policy choice can reduce total future
cost even when it increases the number of shell occurrences, as the reverse
schedule does here.

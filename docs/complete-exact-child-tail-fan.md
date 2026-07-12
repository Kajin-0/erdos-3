# Complete exact-child infinite-tail fan from `S_10`

## Status

Exact finite classification plus an elementary repair-and-induction theorem with exact rational layer-pattern verification.

Every valid positive exact factor-eight child of the recorded state `S_10` has a certified infinite exact four-term-progression-free continuation.

The complete fan size is

```math
\boxed{408855759}.
```

**Verifier:** `src/verify_complete_exact_child_tail_fan.py`.

**Certificate:** `data/complete_exact_child_tail_fan_certificate_2026-07-12.txt`.

---

## 1. Starting classification

The complete fitting exact factor-eight classification from `S_10` gives

```math
R_0=2L_{10}+k,
\qquad
1\le k\le613454687.
```

There are

```text
408969792 sponsor-compatible positive offsets
54999 completion obstructions
59034 first-step half-separation obstructions
0 overlap.
```

Therefore

```math
\boxed{408855759}
```

offsets produce valid exact children.

The standard scheduled recurrence

```math
L_{n+1}=8L_n,
\qquad
k_{n+1}=4k_n
```

already gives infinite tails for

```math
\boxed{408767151}
```

of those valid children. The only failures are scheduled half-separation obstructions:

1. `88606` valid offsets with `2k in S_10`;
2. two valid offsets with `8(k-L_10) in S_10`.

This note repairs both classes.

---

## 2. Second-step repair

Let `k` be one of the `88606` valid offsets for which the scheduled second step fails because

```math
2k\in S_{10}.
```

The failed scheduled offset in the first child is

```math
k_1=4k.
```

Replace it by

```math
\boxed{\widetilde k_1=4k+1.}
```

### 2.1 Sponsor orientation and half obstruction

The repaired offset is odd, so

```math
v_2(\widetilde k_1)=0.
```

It is sponsor-compatible, and the repaired separation

```math
\widetilde R_1=2L_1+\widetilde k_1
```

is odd. Hence it has no integer half-separation point and therefore no half-separation obstruction.

### 2.2 Completion obstruction

A completion at the repaired child separation would correspond, under the two-level layer equations, to the perturbed target

```math
4k+1.
```

Exact rational vertex enumeration over the entire rescue interval

```math
268435456\le k\le460287135
```

finds no feasible layer/base pattern at all.

Thus the repaired child separation has no completion obstruction.

### 2.3 Entry into the invariant basin

The repaired child retains the standard nine top-layer patterns. Scheduled completion descent from the repaired step has the unique pattern `012`.

At the maximum rescue offset, the next normalized state satisfies

```math
q<\frac{15}{8},
\qquad
r<\frac14.
```

Therefore the repaired branch enters the invariant exact-tail basin after one additional exact step.

The complete second-step repair class contains

```math
\boxed{88606}
```

offsets, with ordered-list hashes

```text
FNV-64  2b0b508436f86afe
SHA-256 4778fcf2e5af35669209046938172b5d5bafc92a72297a8fdb3447193a5b23e5
```

---

## 3. Third-step repair

The only valid offsets for which the first scheduled successor works but the next scheduled half test fails are

```text
603979776
613416960.
```

For either offset, the first scheduled child uses `4k` successfully. The failed next offset is

```math
16k.
```

Replace it by

```math
\boxed{\widetilde k_2=16k+1.}
```

Again the repaired offset is odd, so the half-separation obstruction is impossible.

Exact rational enumeration over the complete two-offset interval finds no feasible completion pattern for the perturbed target. The repaired state retains the standard nine top-layer patterns, scheduled completion descent is uniquely `012`, and the next state satisfies

```math
q<\frac{15}{8},
\qquad
r<\frac14.
```

Thus both offsets enter the invariant exact-tail basin after the repair.

The two-value list has hashes

```text
FNV-64  91e961fb57e2e687
SHA-256 ae93a9f5f94348348c156b29e75074a61097723d2d98bd497629c3df5a16ba4f
```

---

## 4. Complete fan theorem

The three disjoint continuation classes are:

```text
standard scheduled basin       408767151
second-step +1 repairs             88606
third-step +1 repairs                  2
```

Therefore

```math
\boxed{
408767151+88606+2
=
408855759.
}
```

This equals the complete number of valid positive exact factor-eight children of `S_10`.

Hence:

```math
\boxed{
\text{every valid exact factor-eight child of }S_{10}
\text{ has an infinite exact tail.}
}
```

---

## 5. Terminal charge

Every branch begins at the same depth-ten state, with

```math
N=265719,
\qquad
P=1024,
\qquad
L=536870912.
```

Every continuation uses exact factor-eight steps after at most one `+1` repair. The cardinality, multiplicity, and scale recurrences are unchanged by the offset choice. Therefore every tail has total multiplicity-weighted density

```math
\boxed{
\sum_{n\ge0}W_{10+n}
=
\frac{4P(N+1)}L
=
\frac{33215}{16384}.
}
```

---

## 6. Consequences

The long-run behavior of exact factor-eight children from `S_10` is now completely classified:

1. invalid children are exactly the first-step completion and half-separation obstructions;
2. every valid child has an explicit infinite summable continuation;
3. the continuation is either the standard `x4` offset schedule or a single `+1` repair followed by that schedule.

The unresolved continuation problem is therefore confined to:

1. factor-two and factor-four cheap escape candidates from `S_10`;
2. contaminated and non-exact descendants elsewhere in the continuation tree;
3. whole-tree Bellman compensation.

This theorem does not by itself prove the full Erdős problem, because it classifies one exact-child fan rather than every possible recursive state.

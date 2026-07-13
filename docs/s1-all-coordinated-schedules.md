# Exhaustive coordinated deletion schedules on `S_1`

## Status

Exact finite exhaustive computation.

Every coordinated side-anchor deletion schedule on the recorded base state
`S_1` is enumerated. The result strengthens the schedule-specific overlap
ledger:

```math
\boxed{
\left(\bigcup_q\Xi_q\right)
\setminus
\mathcal B(S_1)
=
\varnothing
}
```

for **every** coordinated schedule, not merely the lexicographically selected
one.

**Verifier:** `src/verify_s1_all_deletion_schedules.py`.

**Certificate:**
`data/s1_all_deletion_schedules_certificate_2026-07-13.txt`.

The detailed child ledger for one representative schedule remains in
`docs/s1-deletion-dag-overlap-ledger.md`.

---

## 1. Enumeration semantics

The parent is

```math
S_1=
\{64,65,66,80,81,82,85,86,87,90,91,92\}.
```

At each current state:

1. enumerate every nontrivial three-term arithmetic progression;
2. for step `q`, select the left endpoint when `v_2(q)` is even and the right
   endpoint when `v_2(q)` is odd;
3. delete that coordinated sponsor;
4. recurse until the residual is three-term-progression-free.

The schedules are **progression-labeled**. If two different selected
progressions delete the same sponsor and produce the same next vertex set, they
remain distinct schedules because their middle points and step labels can
produce different terminal and multiplicity-fiber outputs.

This is the appropriate notion for the hybrid deletion recursion. Counting only
vertex subsets or sponsor sequences would erase middle-output information.

---

## 2. Complete schedule graph

The exact directed state graph contains

```math
\boxed{120}
```

reachable vertex subsets, including six terminal residual sets.

It has

```math
\boxed{1560}
```

complete progression-labeled schedules.

These collapse to

```math
\boxed{930}
```

distinct sponsor-deletion sequences. Their progression-label multiplicities
are:

| schedules per sponsor sequence | number of sponsor sequences |
|---:|---:|
| 1 | 444 |
| 2 | 414 |
| 4 | 72 |

The weighted count is

```math
444+2(414)+4(72)=1560.
```

Thus progression labeling is not cosmetic: 486 sponsor sequences support more
than one middle-output history.

The complete catalogs have hashes

```text
reachable states:
7c96b7e498353a08899a62e4c6a977b604934ae0a08b6deb0f771f4eafb77ec5
```

and

```text
progression-labeled schedules:
bbdc46cbe4d2bae61cc942c139beab4fe2872e66ce7e97cd0072241a66c6c05d
```

under the verifier's canonical serialization.

---

## 3. Schedule lengths and residuals

The process terminates after either five or six deletions:

```text
240 schedules have length 5;
1320 schedules have length 6.
```

There are six terminal residual sets:

| schedule count | residual |
|---:|---|
| 360 | `{65,66,80,86,87,91}` |
| 30 | `{65,66,82,86,87,91}` |
| 210 | `{65,66,86,87,90,91}` |
| 720 | `{65,66,86,87,91,92}` |
| 60 | `{65,66,80,82,86,87,91}` |
| 180 | `{65,66,80,86,87,90,91}` |

Every listed residual is three-term-progression-free.

The variation in residual cardinality shows that neither the number of
deletions nor the terminal set is schedule invariant. The overlap conclusion
below survives despite that variation.

---

## 4. Terminal step profiles

For each schedule, let `Q` be the set of distinct selected steps retained as
terminal representatives by the exact middle multiplicity resolution.

Only four terminal-step profiles occur:

| schedule count | `Q` |
|---:|---|
| 480 | `{1,5}` |
| 240 | `{1,4,5}` |
| 420 | `{1,5,6}` |
| 420 | `{1,4,5,6}` |

Step `1` and step `5` occur in every profile. Steps `4` and `6` depend on the
schedule.

This is another reason a deletion-DAG adapter must retain progression labels:
the same parent can export different terminal numerical labels under different
valid resolutions.

---

## 5. Middle-fiber union profiles

For each distinct selected step `q`, let

```math
\Xi_q
=
\{x-\min X_q:x\in X_q,\ x>\min X_q\},
```

where `X_q` is the set of selected centers with step `q`.

Across all 1560 schedules, the union

```math
F=\bigcup_q\Xi_q
```

has exactly nine possible profiles:

| schedule count | `F` | `H(F)` |
|---:|---|---:|
| 120 | `{21}` | `1/21` |
| 180 | `{1,21}` | `22/21` |
| 60 | `{16,21}` | `37/336` |
| 180 | `{21,26}` | `47/546` |
| 30 | `{1,2,21}` | `65/42` |
| 390 | `{1,21,26}` | `593/546` |
| 120 | `{16,21,26}` | `649/4368` |
| 240 | `{1,2,21,26}` | `433/273` |
| 240 | `{1,16,21,26}` | `5017/4368` |

The fibers belonging to different step labels are pairwise disjoint in every
schedule. Thus no within-middle-fiber duplicate correction is needed at this
base state.

The obstruction comes from alignment with the backbone.

---

## 6. Schedule-independent backbone containment

The minimum-translation backbone is fixed by the parent:

```math
\mathcal B(S_1)
=
\{1,2,16,17,18,21,22,23,26,27,28\}.
```

Every one of the nine possible fiber unions is a subset of this backbone.
Therefore all 1560 schedules satisfy

```math
\boxed{
\bigcup_q\Xi_q
\subseteq
\mathcal B(S_1).
}
```

Define the novel fiber support

```math
F_{\rm new}(D)
=
\left(\bigcup_q\Xi_q\right)
\setminus
\mathcal B(D)
```

and novel fiber mass

```math
\mathcal N(D)=H(F_{\rm new}(D)).
```

Then the exhaustive result is

```math
\boxed{
\mathcal N(S_1)=0
\quad
\text{for every coordinated deletion schedule on }S_1.
}
```

This is a finite schedule-independent theorem for the recorded base state.

---

## 7. What the result rules out

The result eliminates several possible explanations of the representative
schedule's overlap.

### Not a lexicographic artifact

The representative schedule chose the smallest available progression at each
step. Exhaustion shows that changing the progression order never produces
middle-fiber support outside the backbone.

### Not caused by one residual

Six different terminal residuals occur. Every residual class has the same zero
novel-fiber conclusion.

### Not caused by fixed terminal steps

The terminal set varies among four profiles, yet the recursive fiber union
always remains inside the backbone.

### Not removed by maximizing or minimizing deletions

Both five-deletion and six-deletion schedules have zero novel-fiber mass.

Consequently, the alignment is a structural property of `S_1` under the
coordinated deletion rule, not an accidental choice of schedule.

---

## 8. Consequence for reserve design

The exact within-parent identity

```math
|Q|+\sum_q|\Xi_q|=K
```

remains valid for every schedule. However, it does not imply new distinct
recursive support after the backbone is included.

At `S_1`, the entire center-difference export is already imported by the
minimum-translation child. Therefore a potential based on

```math
\sum_q H(\Xi_q)
```

without subtracting backbone overlap assigns reserve to labels that are not
new.

A first corrected coordinate is

```math
\mathcal N(D)
=
H\left(
\left(\bigcup_q\Xi_q\right)
\setminus
\mathcal B(D)
\right),
```

but the base result shows that this coordinate can vanish even when the raw
middle-fiber mass is substantial.

The reserve must therefore account for at least one of the following stronger
phenomena:

1. **future obstruction capacity:** imported fiber labels may still make the
   backbone harder to replicate later;
2. **provenance multiplicity:** the same numerical label can carry independent
   sponsor histories even when its support is not new;
3. **containment debt:** a smaller child contained in a larger child may
   represent future branching capacity not visible in the numerical union;
4. **terminal-recursive interaction:** a terminal step may already occur in a
   recursive child and cannot automatically be counted twice as distinct mass;
5. **multi-generation release:** zero novel support at one generation may
   create completion or rectangle support after another cheap step.

Thus simple set novelty is necessary for honest distinctness accounting but is
not sufficient as a whole-tree reserve.

---

## 9. Next exact target

The next finite computation should preserve the complete output provenance and
advance one generation from each distinct `S_1` fiber/backbone shell type.

The smallest relevant recursive states are

```math
\{1\},
\qquad
\{2\},
\qquad
\{21\},
\qquad
\{1,21\},
```

and the larger shell states contained in `[16,32)`.

The immediate question is not whether these tiny sets contain three-term
progressions—they generally do not. It is whether their imported provenance,
when lifted through the replay construction, creates measurable obstruction
capacity that can pay later factor-two or factor-four Bellman debt.

A useful next adapter should therefore carry both:

```text
numerical support;
provenance labels identifying parent sponsors and source child occurrences.
```

This is the first point at which a purely set-valued state may be too coarse.

---

## 10. Reproduction

Run

```bash
python3 src/verify_s1_all_deletion_schedules.py \
  /tmp/s1_all_deletion_schedules_certificate.txt
```

The exact certificate has SHA-256

```text
8a0726c30041eba72d047924922cfc7c1ba756c63d58da3a04d92f27919273cc
```

and is regenerated by the lightweight proof-check workflow.

---

## 11. Scope

The exhaustive computation proves schedule independence only for the finite
parent `S_1` under the stated coordinated rule. It does not prove:

- a corresponding theorem for arbitrary four-term-progression-free parents;
- monotonicity of novel fiber mass;
- that provenance multiplicity is a valid reserve;
- a complete multi-generation child-packing rule;
- a branching Carleson inequality;
- or the four-term Erdős conjecture.

Its role is diagnostic and exact: it identifies a base-state overlap mechanism
that every valid global potential must survive.

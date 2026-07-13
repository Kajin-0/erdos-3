# Schedule-independent imported-overlap floor on `S_1`

## Status

Exact finite exhaustive theorem.

Every coordinated side-anchor deletion schedule on the recorded base state `S_1` has zero novel middle-fiber support outside the minimum-translation backbone. Nevertheless, no schedule eliminates recursive overlap: every schedule produces positive middle-fiber mass already contained in that backbone.

Define the recursive overlap charge

```math
\Omega_\sigma(D)
=
H(\mathcal B(D))
+
\sum_qH(\Xi_q^\sigma)
-
H\left(
\mathcal B(D)\cup\bigcup_q\Xi_q^\sigma
\right).
```

The exhaustive result is

```math
\boxed{
\frac1{21}
\le
\Omega_\sigma(S_1)
\le
\frac{433}{273}
}
```

for every one of the `1,560` progression-labeled coordinated schedules.

**Verifier:** `src/verify_s1_schedule_overlap_floor.py`.

**Certificate:** `data/s1_schedule_overlap_floor_certificate_2026-07-13.txt`.

---

## 1. Why this charge is exact on `S_1`

The exhaustive schedule theorem proves two facts for every schedule `sigma`:

```math
\bigcup_q\Xi_q^\sigma
\subseteq
\mathcal B(S_1),
```

and the distinct fibers `Xi_q^sigma` are pairwise disjoint.

Therefore

```math
H\left(
\mathcal B(S_1)\cup\bigcup_q\Xi_q^\sigma
\right)
=
H(\mathcal B(S_1)),
```

so the overlap charge simplifies exactly to

```math
\boxed{
\Omega_\sigma(S_1)
=
\sum_qH(\Xi_q^\sigma).
}
```

This is not an approximate overlap statistic. It is the exact recursive occurrence mass duplicated inside the simultaneous backbone child.

---

## 2. Exact distribution

The complete charge distribution is:

| schedules | overlap charge |
|---:|---:|
| 120 | `1/21` |
| 180 | `47/546` |
| 60 | `37/336` |
| 120 | `649/4368` |
| 180 | `22/21` |
| 390 | `593/546` |
| 240 | `5017/4368` |
| 30 | `65/42` |
| 240 | `433/273` |

The counts sum to

```math
120+180+60+120+180+390+240+30+240=1560.
```

The minimum is attained by `120` schedules and the maximum by `240` schedules.

The canonical SHA-256 of the minimum-schedule catalog is

```text
d435520de8fec8c389ca14109bd0821075bcac4189e378b3294c1adc7a3b2103
```

---

## 3. Consequence for reserve design

Raw novelty alone fails as a schedule-independent reserve:

```math
\mathcal N_\sigma(S_1)=0
```

for every schedule, and `S_2` also admits a zero-novelty schedule.

The new exact result shows that novelty is not the only exported structure. On `S_1`, the missing novelty is replaced by unavoidable imported overlap:

```math
\boxed{
\mathcal N_\sigma(S_1)=0
\quad\text{but}\quad
\Omega_\sigma(S_1)\ge\frac1{21}.
}
```

This motivates a schedule-aware dichotomy of the form

```text
new numerical obstruction support
or
certified overlap with an existing simultaneous child.
```

A useful global theorem would need to show that either contribution can be charged without repeated payment across the full deletion tree. The finite `S_1` result establishes only the local floor.

---

## 4. Revised candidate coordinate

For one certified deletion resolution, retain the pair

```math
\left(
\mathcal N_\sigma(D),
\Omega_\sigma(D)
\right),
```

where

```math
\mathcal N_\sigma(D)
=
H\left(
\left(\bigcup_q\Xi_q^\sigma\right)
\setminus
\mathcal B(D)
\right).
```

The first component records genuinely new labels. The second records occurrence mass already represented in the backbone or another simultaneous child.

The pair is more honest than either raw fiber occurrence mass or novel support alone. It still is not a proved Bellman reserve, because overlap mass can itself be counted again in descendants.

---

## 5. Reproduction

Run

```bash
python3 src/verify_s1_schedule_overlap_floor.py \
  /tmp/s1_schedule_overlap_floor_certificate.txt
```

The recorded certificate SHA-256 is

```text
64d1680ce30699ef2c7ac53fa9b42e88e2085c442dd32ccd9178bf0c7be828aa
```

and the check is included in `src/run_verify_transport_reserve.sh`.

---

## 6. Scope

This theorem is finite and state-specific. It does not prove:

- a positive overlap floor for every parent;
- that novelty plus overlap is monotone;
- bounded reuse of the same overlap charge across generations;
- a complete retention or deduplication convention;
- a branching Bellman inequality;
- or the four-term Erdős conjecture.

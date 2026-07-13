# Exact recursive-occurrence multiplicity through `S_3`

## Status

Exact finite packing diagnostic for the raw simultaneous transition payloads of `S_1`, `S_2`, and `S_3`.

For recursive shell occurrences

```math
C_1,\ldots,C_r,
```

define the pointwise occurrence multiplicity

```math
m(u)=|\{i:u\in C_i\}|
```

and

```math
M=\max_um(u).
```

Then the exact identity

```math
\sum_iH(C_i)=\sum_u\frac{m(u)}u
```

immediately gives the local packing bound

```math
\boxed{
\sum_iH(C_i)
\le
M\,H\left(\bigcup_iC_i\right).
}
```

This statement requires no retention convention. It is valid for the complete raw simultaneous occurrence family.

**Verifier:** `src/verify_recursive_occurrence_multiplicity.py`.

**Certificate:** `data/recursive_occurrence_multiplicity_certificate_2026-07-13.txt`.

---

## 1. Exact multiplicity spectra

| state | labels of multiplicity 1 | multiplicity 2 | multiplicity 3 | multiplicity 6 | multiplicity 7 | maximum |
|---:|---:|---:|---:|---:|---:|---:|
| `S_1` | 7 | 4 | 0 | 0 | 0 | 2 |
| `S_2` | 36 | 7 | 3 | 0 | 0 | 3 |
| `S_3` | 162 | 10 | 2 | 1 | 1 | 7 |

The labels attaining maximum multiplicity are

```text
S1: 1,16,21,26
S2: 61,87,122
S3: 303.
```

At `S_3`, label `606` has multiplicity `6`, immediately below the maximum.

---

## 2. Inherited separation concentration

The largest multiplicities are not spread uniformly through the recursive union.

At `S_2`, the prior replication separation

```math
61
```

is among the three labels of multiplicity `3`.

At `S_3`, the prior replication separation

```math
303
```

has multiplicity `7`, and

```math
606=2\cdot303
```

has multiplicity `6`.

Thus maximum local overlap concentrates on inherited replication coordinates. This is consistent with the earlier anchor-compression picture, but the current finite certificate does not prove a general formula.

---

## 3. Duplicate excess

The exact difference between recursive occurrence mass and recursive union mass is

```math
\sum_iH(C_i)
-
H\left(\bigcup_iC_i\right)
=
\sum_u\frac{m(u)-1}{u}.
```

The certified values are

```math
S_1:\quad\frac{5017}{4368},
```

```math
S_2:\quad
\frac{1720946837057}{11385890360130},
```

and

```math
S_3:\quad
\frac{767969830085807}{5412538546014600}.
```

This excess includes every duplicate contribution after shell resolution, including overlap between the backbone and middle fibers and overlap among different middle fibers.

---

## 4. Harmonic-average multiplicity

Define

```math
\overline m_H
=
\frac{\sum_iH(C_i)}
{H(\bigcup_iC_i)}.
```

This is the harmonic-weighted average of `m(u)`. The exact computation proves

```math
\overline m_H(S_1)<\frac85,
```

```math
\overline m_H(S_2)<\frac{11}{10},
```

and

```math
\overline m_H(S_3)<\frac{11}{10}.
```

Therefore the maximum multiplicity and average multiplicity behave very differently:

```text
maximum: 2,3,7
harmonic average: <1.6,<1.1,<1.1.
```

The high-multiplicity labels are arithmetically large enough that they contribute relatively little reciprocal mass locally.

---

## 5. Consequence for retention design

A retention theorem based only on the worst local multiplicity would lose factors

```text
2,3,7
```

by `S_3`. The data do not support treating that maximum as uniformly bounded.

Conversely, replacing the occurrence family by the numerical union loses provenance and future-history multiplicity. The small harmonic-average multiplicity does not justify that quotient globally because the same labels may reappear in descendants.

The useful target is a provenance-sensitive Carleson estimate:

```math
\sum_{
 \text{descendant occurrences of }u
}
\operatorname{weight}(u,\text{origin})
\le
C\,\operatorname{capacity}(u,\text{root origin}).
```

Local multiplicity is one slice of this desired estimate. The missing issue is cross-generation reuse.

---

## 6. Exact safe conclusion

For each tested parent, the raw occurrence family satisfies

```math
\sum_iH(C_i)
\le
M\,H\left(\bigcup_iC_i\right),
```

with exact `M=2,3,7`.

This gives a correct local upper bound. It does **not** establish:

- a uniform bound on `M`;
- a retention quotient;
- a cross-generation packing constant;
- a valid Bellman child sum;
- or a branching Carleson inequality.

---

## 7. Reproduction

Run

```bash
python3 src/verify_recursive_occurrence_multiplicity.py \
  /tmp/recursive_occurrence_multiplicity_certificate.txt
```

The recorded certificate SHA-256 is

```text
9774ea7c8cbd3626b3120ade6b48344008b5f1706b05e253923393cc8495e7e8
```

and the check is included in `src/run_verify_transport_reserve.sh`.

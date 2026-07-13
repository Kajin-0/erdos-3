# Exact output load of the `S_7` cyclic component

## Status

Exact fixed-policy finite theorem.

The `S_7` terminal-fiber graph has cyclic component

```math
C=\{1,5,61,303,1597,8195,323640\}.
```

The component emits thousands of labels outside itself. Those labels are additional recursive output, not automatically Bellman repayment. After complete numerical deduplication, the total support emitted by the component still has more than `7/5` of the component's harmonic vertex mass.

**Verifier:** `src/verify_s7_scc_output_load.py`.

**Certificate:** `data/s7_scc_output_load_certificate_2026-07-13.txt`.

---

## 1. Output classification

For each source step `q in C`, classify every value in `Xi_q` as:

1. **internal terminal:** the value lies in `C`;
2. **external terminal:** it is a terminal step outside `C`;
3. **external imported:** it is nonterminal but already lies in the parent backbone;
4. **external novel:** it is neither terminal nor in the backbone.

The exact counts are:

| class | occurrences | distinct labels |
|---|---:|---:|
| internal terminal | 24 | 7 |
| external terminal | 12 | 2 |
| external imported | 106 | 81 |
| external novel | 7,728 | 6,020 |

The only external terminal labels are

```math
93476
\quad\text{and}\quad
230164.
```

The large novel class shows that the component exports substantial new numerical support. It does not show that this support is already usable as obstruction credit.

---

## 2. Source-by-source counts

Each row is ordered as

```text
internal terminal,
external terminal,
external imported,
external novel.
```

| source step | counts |
|---:|---:|
| `1` | `5,2,65,2843` |
| `5` | `6,2,33,1416` |
| `61` | `4,2,1,1288` |
| `303` | `4,2,1,883` |
| `1597` | `2,2,5,773` |
| `8195` | `1,2,1,524` |
| `323640` | `2,0,0,1` |

The output is not concentrated in one source step, although steps `1` and `5` generate the largest novel classes.

---

## 3. Internal mass

The component harmonic vertex mass is

```math
V(C)
=
\sum_{u\in C}\frac1u
=
\frac{6369649065416843}{5219119862617320}.
```

The internal terminal occurrence mass is

```math
I(C)
=
\sum_{
 q\in C,
 u\in C\cap\Xi_q
}
\frac1u
=
\frac{1098047763593723}{869853310436220}.
```

This is the same internal target mass used in the SCC recycling calculation.

---

## 4. Out-of-component mass

Let `E_occ(C)` be the harmonic mass of every out-of-component occurrence, retaining repeated values. Exact arithmetic proves

```math
\boxed{
\frac{12}{25}
<
\frac{E_{\rm occ}(C)}{I(C)}
<
\frac12.
}
```

Let `E_union(C)` be the harmonic mass after deduplicating all out-of-component labels. Then

```math
\boxed{
\frac{39}{100}
<
\frac{E_{\rm union}(C)}{I(C)}
<
\frac25.
}
```

Thus the component exports nontrivial support, but the raw external mass is smaller than the internal terminal target mass.

The exact reduced fractions are large. The certificate records SHA-256 hashes of their canonical numerator/denominator strings and verifies the compact rational brackets without floating-point arithmetic.

---

## 5. Total one-step output expansion

Let

```math
O_{\rm occ}(C)
=
I(C)+E_{\rm occ}(C)
```

be total fiber occurrence mass sourced by `C`. Then

```math
\boxed{
\frac32
<
\frac{O_{\rm occ}(C)}{V(C)}
<
\frac85.
}
```

Even after complete numerical deduplication, let

```math
O_{\rm union}(C)
=
H\left(\bigcup_{q\in C}\Xi_q\right).
```

Exact arithmetic gives

```math
\boxed{
\frac75
<
\frac{O_{\rm union}(C)}{V(C)}
<
\frac32.
}
```

Therefore a unit support-valued capacity expands by more than `40%` in one recorded transition even after every duplicate label is merged.

---

## 6. Correct interpretation

The earlier spectral theorem proves that the internal terminal adjacency has

```math
\rho(A)>\frac{23}{9}.
```

The current theorem shows that out-of-component support does not automatically neutralize that growth. It is additional recursive load unless a separate theorem converts it into durable obstruction coverage or controlled capacity consumption.

The correct mechanism must have the form

```text
cyclic terminal output
    -> nonterminal labels
    -> certified affine / completion / rectangle obstruction credit
    -> reduced future cheap-extension capacity.
```

Simply adding the harmonic mass of exported labels to a recursive child potential makes the inequality harder, not easier.

---

## 7. Exact no-go conclusion

The following candidate is false on the recorded `S_7` transition:

```text
Use the numerical union of all fibers emitted by the cyclic SCC as a unit-weight retained capacity.
```

Its output-to-input ratio exceeds

```math
\frac75.
```

The result closes another simple retention route. A viable potential must use at least one of:

1. obstruction credit attached to exported labels;
2. nonlinear component capacity;
3. multi-generation scale amortization;
4. provenance capacity consumed when labels recur;
5. controlled error paid by another Bellman term.

---

## 8. Reproduction

Run

```bash
python3 src/verify_s7_scc_output_load.py \
  /tmp/s7_scc_output_load_certificate.txt
```

The certificate SHA-256 is

```text
cb5dbba5f45c25b2c286fde17e9895d017abaa906f69f73255a5f0b5b62d081d
```

---

## 9. Scope

This theorem is exact for the recorded lexicographic `S_7` schedule. It does not prove:

- the same output ratios for other schedules or states;
- that exported novel labels fail to create obstruction coverage;
- that nonlinear or multi-generation potentials fail;
- a retained-child quotient;
- a branching Bellman inequality;
- or the four-term Erdős conjecture.

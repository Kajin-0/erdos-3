# Terminal-fiber SCC quotient and internal recycling

## Status

Exact fixed-policy finite quotient through `S_7`.

The terminal-fiber incidence graph is cyclic beginning at `S_3`. Collapsing each strongly connected component produces an acyclic condensation graph, but the quotient retains an internal recycling problem that cannot be paid by unit harmonic vertex mass at `S_7`.

**Exporter:** `src/export_terminal_fiber_scc_quotient.py`.

**Certificate:** `data/terminal_fiber_scc_quotient_certificate_2026-07-13.txt`.

---

## 1. Quotient definition

For terminal step set `Q`, draw an edge

```math
q\longrightarrow u
```

when

```math
u\in Q\cap\Xi_q.
```

Let

```math
\mathcal C_1,\ldots,\mathcal C_m
```

be the strongly connected components. The exported quotient records, for every component:

- its terminal labels;
- its internal edges;
- incoming and outgoing condensation edges;
- harmonic vertex mass;
- internal target mass;
- recycling excess.

The condensation graph is acyclic by construction. No internal component is discarded.

---

## 2. Exact quotient frontier

| state | SCCs | condensation edges | cyclic SCCs | internal cyclic edges |
|---:|---:|---:|---:|---:|
| `S_1` | 2 | 1 | 0 | 0 |
| `S_2` | 5 | 3 | 0 | 0 |
| `S_3` | 9 | 6 | 1 | 2 |
| `S_4` | 10 | 15 | 1 | 2 |
| `S_5` | 11 | 25 | 1 | 2 |
| `S_6` | 12 | 36 | 1 | 2 |
| `S_7` | 19 | 26 | 1 | 24 |

The unique cyclic component is

```math
\{61,303\}
```

from `S_3` through `S_6`. At `S_7` it becomes

```math
\{1,5,61,303,1597,8195,323640\}.
```

---

## 3. Internal harmonic accounting

For a component `C`, define its vertex capacity

```math
V(C)=\sum_{u\in C}\frac1u
```

and internal target mass

```math
T(C)=
\sum_{
 (q,u)\text{ internal edge}
}
\frac1u.
```

The recycling excess is

```math
E(C)=T(C)-V(C).
```

For the two-cycle

```math
C=\{61,303\},
```

the internal edges are

```math
61\to303,
\qquad
303\to61.
```

Therefore

```math
T(C)=\frac1{303}+\frac1{61}=V(C),
```

so

```math
\boxed{E(C)=0.}
```

This exact balance persists from `S_3` through `S_6`.

---

## 4. Capacity failure at `S_7`

For the seven-label cyclic component at `S_7`, there are `24` internal edges. Its exact vertex mass is

```math
V(C)
=
\frac{6369649065416843}{5219119862617320},
```

while its internal target mass is

```math
T(C)
=
\frac{1098047763593723}{869853310436220}.
```

Hence

```math
\boxed{
E(C)
=
\frac{43727503229099}{1043823972523464}
>0.
}
```

Equivalently,

```math
\frac{T(C)}{V(C)}
=
\frac{6588286581562338}{6369649065416843}
>1.
```

Thus one unit of harmonic capacity per terminal label is no longer sufficient to pay the internal recycling generated inside the component.

---

## 5. Exact no-go conclusion

The SCC quotient solves only the ordering problem outside cyclic components. It does not solve internal reuse.

The following candidate is false on the recorded `S_7` transition:

```text
Collapse each SCC and assign it capacity equal to the harmonic mass of its labels.
```

The component emits more internal target mass than that capacity by the exact positive excess above.

A valid component state must therefore include at least one additional mechanism:

1. internal edge capacity;
2. provenance-sensitive multiplicity capacity;
3. a nonlinear component potential;
4. export into affine obstruction, completion, or rectangle coverage;
5. controlled error funded elsewhere in the Bellman inequality.

---

## 6. Canonical quotient hashes

```text
S1 c8f9afb431e903b54c3e41fc6795fe7334e448dbe4b5b8975bb6a1c14c135b69
S2 e81ffd1df5bec410d3e3dd96e84c136792313bbb4c42a89a1488b3bcc3c05f4f
S3 2d6b760230cac0e79c9212c510b1114e5504ab1805432b5210abce342c4aa28f
S4 818f65fa27fd60809d6181bb5b1de7dc7873fee09d02cb8b489232c9b792245b
S5 5cdc05d87dd4fe9d0717012288a7d5859bda9273d51dc691758349c87f23a58c
S6 9738e822444c9776c36523d8bced55ca677eeeb5635a0520eacb069f08f111d3
S7 0249bce4a12db2e2faa40873d25cce9741fba7c5f2a2c94f16b42b1873bc7804
```

The compact certificate SHA-256 is

```text
3166cbb0801eb774e8b6691ace6a8612f5457a9415bd8ae3762a1260216d0fe2
```

---

## 7. Reproduction

Run

```bash
python3 src/export_terminal_fiber_scc_quotient.py self-test \
  /tmp/terminal_fiber_scc_quotient_certificate.txt
```

Export a complete quotient:

```bash
python3 src/export_terminal_fiber_scc_quotient.py export \
  --state-depth 7 \
  --output /tmp/S7_terminal_fiber_scc.json
```

---

## 8. Revised active target

The next finite-state experiment should attach an explicit internal capacity vector to each cyclic component and test whether

```math
\text{internal recycling}
+
\text{outgoing child capacity}
\le
\text{incoming capacity}
+
\text{new obstruction export}
```

holds on the certified transitions.

The quotient is a correct state compression for graph ordering. It is not yet a valid Bellman retention quotient.

---

## 9. Scope

This result is exact for the recorded lexicographic schedules through `S_7`. It does not prove:

- a uniform bound on SCC size;
- a sufficient internal capacity;
- schedule independence;
- a retained-child quotient;
- a branching Bellman inequality;
- or the four-term Erdős conjecture.

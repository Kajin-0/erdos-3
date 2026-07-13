# Terminal-fiber incidence graph through `S_7`

## Status

Exact fixed-policy finite theorem.

For a complete coordinated deletion schedule, let `Q` be the terminal step set and let `Xi_q` be the middle multiplicity fiber for step `q`. Define a directed graph

```math
\mathcal G(D)
```

with vertex set `Q` and edge

```math
q\longrightarrow u
```

when

```math
u\in Q\cap\Xi_q.
```

The graph records when one terminal step is simultaneously regenerated inside the recursive fiber of another terminal step.

**Verifier:** `src/verify_terminal_fiber_incidence.py`.

**Certificate:** `data/terminal_fiber_incidence_certificate_2026-07-13.txt`.

---

## 1. Exact graph frontier

| state | terminal vertices | directed edges | strongly connected components | largest component |
|---:|---:|---:|---:|---:|
| `S_1` | 2 | 1 | 2 | 1 |
| `S_2` | 5 | 3 | 5 | 1 |
| `S_3` | 10 | 10 | 9 | 2 |
| `S_4` | 11 | 20 | 10 | 2 |
| `S_5` | 12 | 31 | 11 | 2 |
| `S_6` | 13 | 43 | 12 | 2 |
| `S_7` | 25 | 75 | 19 | 7 |

The graphs for `S_1` and `S_2` are acyclic. Cycles appear at `S_3`.

---

## 2. First cycle

At `S_3`, the graph contains

```math
61\longrightarrow303
```

and

```math
303\longrightarrow61.
```

Thus

```math
\boxed{\{61,303\}}
```

is a strongly connected component. The same two-label component persists through `S_4`, `S_5`, and `S_6`.

This already disproves any argument assigning a strict decreasing rank to terminal labels along every fiber edge.

---

## 3. Expansion at `S_7`

At `S_7`, the cyclic component expands to

```math
\boxed{
\{1,5,61,303,1597,8195,323640\}.
}
```

The component includes the base step, several historical separations, and the new compound step

```math
323640=230164+93476.
```

Two explicit incidence relations are

```math
49158\longrightarrow230164,
```

because

```math
\Xi_{49158}=\{230164\},
```

and

```math
323640\longrightarrow5,
\qquad
323640\longrightarrow8195,
```

because

```math
\Xi_{323640}=\{5,8195,8200\}.
```

Together with the existing historical edges, these relations contribute to the larger strongly connected component.

---

## 4. Exact graph hashes

```text
S1 b05c4979e7b9347880bd9aa4a0587d968a3bec450490971d2ad13c319882a3cb
S2 6bbb44826bc5397d4df77158553be9151c231836c5dcea404918974b2a7d4cdc
S3 199ebc3e1857109ecee552c1317ebd76eff328fdb8c1806f32c55e3d47f4eead
S4 7587b87f3d5f0210cc8fc9d0e1a917c2508293461d44eaa2ad1c4c925879547e
S5 ba09e6ed05f256142a7a1f3ea7f90cde645c0c7765372ec965c083a5622a1dfb
S6 54fdd9ba95e5e4f86eb10ef54030dda46dd138059ea5489cb6e27be74d8f0b6f
S7 17ef6a4af54dfba4b3d97c305aeb705b20b5c9cda61a0f2d0b4de9920f052f78
```

The compact certificate SHA-256 is

```text
ddedf75bd52a6cc67cef6ecb0a635b836e9a1c7c5094a860449dd35dd2651c18
```

---

## 5. Consequence for potential design

A potential of the form

```math
\Phi(q)=f(\operatorname{rank}(q))
```

with strict decrease along every edge cannot exist once the incidence graph contains a directed cycle.

Therefore a viable retention state must operate on at least one of the following:

1. strongly connected components rather than individual labels;
2. a non-strict capacity that is consumed around cycles;
3. provenance-sensitive edge multiplicities;
4. a higher-dimensional obstruction vector;
5. export from a cyclic component into rectangle or completion coverage.

The condensation graph of strongly connected components is acyclic, but collapsing an entire component discards internal multiplicity and provenance. A proof must retain enough internal data to charge repeated cycling.

---

## 6. Revised finite-state target

The incidence graph suggests the following candidate state structure:

```text
SCC identifier
+ internal terminal labels
+ fiber-edge multiplicities
+ pointwise provenance capacities
+ outgoing edges to lower SCCs
+ affine obstruction coverage.
```

The next computational target is to construct this SCC quotient from each raw transition payload and test whether its internal repeated-use mass admits a finite capacity bound.

---

## 7. Scope

This result is exact for the recorded lexicographic schedules through `S_7`. It does not prove:

- that the same components occur under other schedules;
- a uniform bound on component size;
- a valid capacity within a component;
- a retained-child quotient;
- a branching Bellman inequality;
- or the four-term Erdős conjecture.

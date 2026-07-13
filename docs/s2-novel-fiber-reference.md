# Deterministic `S_2` novel-fiber reference

## Status

Exact finite, schedule-specific deletion-DAG computation.

The exhaustive `S_1` theorem proves that every coordinated schedule has zero
middle-fiber support outside the minimum-translation backbone. The first
recorded descendant behaves differently. Under the same deterministic
lexicographic coordinated rule, `S_2` exports eight novel middle-fiber labels
with positive harmonic mass.

**Verifier:** `src/verify_s2_novel_fiber_reference.py`.

**Certificate:**
`data/s2_novel_fiber_reference_certificate_2026-07-13.txt`.

---

## 1. Parent and schedule

The recorded state satisfies

```math
S_2\subseteq[256,512),
\qquad
|S_2|=39,
\qquad
\max S_2=470.
```

At each step, the verifier chooses the lexicographically smallest available
three-term progression by

```text
(step, left endpoint, middle, right endpoint)
```

and deletes the coordinated side anchor determined by the parity of `v_2`.

The schedule contains

```math
26
```

selected progressions and terminates with a three-term-progression-free
residual of size

```math
13.
```

The state and schedule hashes are

```text
state:
134d805cfd73cbee488eca475d70ce0cb02c63e60927c74643891de48ee0ede9
```

and

```text
schedule:
586f62323391a20555b2a452d1b1a20d55e9a5cf0387677fd2b7013cd1baa689.
```

---

## 2. Terminal steps and middle fibers

The distinct selected steps are

```math
Q=\{1,5,30,31,61\}.
```

The exact middle multiplicity fibers are

```math
\Xi_1
=
\{16,21,26,61,77,82,87,122,138,143,148\},
```

```math
\Xi_5
=
\{1,61,62,122,123\},
```

```math
\Xi_{30}=\Xi_{31}=\varnothing,
```

and

```math
\Xi_{61}
=
\{65,66,86,87,92\}.
```

Unlike the exhaustive `S_1` schedule family, these fibers are not pairwise
disjoint. Their exact overlaps are

```math
\Xi_1\cap\Xi_5=\{61,122\},
```

and

```math
\Xi_1\cap\Xi_{61}=\{87\}.
```

The resulting within-middle duplicate harmonic mass is

```math
\boxed{\frac{383}{10614}}.
```

Thus overlap already occurs before the backbone is included.

---

## 3. Imported and novel fiber support

Let

```math
F_2=\bigcup_q\Xi_q
```

and let

```math
\mathcal B(S_2)
=
\{d-\min S_2:d\in S_2,\ d>\min S_2\}.
```

The fiber union splits exactly into imported support

```math
F_2\cap\mathcal B(S_2)
=
\{61,65,66,82,86,87,92,122,143,148\}
```

and novel support

```math
F_2\setminus\mathcal B(S_2)
=
\boxed{\{1,16,21,26,62,77,123,138\}}.
```

The imported harmonic mass is

```math
\boxed{
\frac{218348937262}{1897648393355}
}
```

and the novel harmonic mass is

```math
\boxed{
\mathcal N(S_2)
=
\frac{239396453}{200655312}
>0.
}
```

This gives the first exact positive value of the novel-fiber coordinate in the
recorded contaminated genealogy.

---

## 4. Full fiber mass ledger

Counting each fiber occurrence separately gives

```math
\sum_qH(\Xi_q)
=
\boxed{
\frac{1265225421268357}{941233603104080}
}.
```

The harmonic mass of the numerical fiber union is

```math
H(F_2)
=
\boxed{
\frac{3693784666860791}{2823700809312240}
}.
```

Their difference is the within-middle duplicate mass

```math
\sum_qH(\Xi_q)-H(F_2)
=
\boxed{\frac{383}{10614}}.
```

The remaining union mass then splits as

```math
H(F_2)
=
H(F_2\cap\mathcal B(S_2))
+
H(F_2\setminus\mathcal B(S_2)).
```

This three-part decomposition is the minimum honest input for an overlap-aware
reserve:

```text
raw fiber occurrence mass
= within-middle duplicate mass
+ imported distinct fiber mass
+ novel distinct fiber mass.
```

---

## 5. Comparison with `S_1`

The exhaustive base-state result is

```math
\mathcal N(S_1)=0
```

for every coordinated schedule.

The deterministic descendant result is

```math
\mathcal N(S_2)
=
\frac{239396453}{200655312}>0.
```

This comparison establishes two facts.

First, novel fiber mass is not identically zero along the recorded genealogy.
It can detect new support that raw contamination count and shell slack do not
identify.

Second, this comparison is **not** a monotonicity theorem. The two values come
from different parent states, and only `S_1` has been exhausted over all
schedules. A different schedule on `S_2` may produce a different fiber union or
novel mass.

---

## 6. Consequence for the candidate reserve

Novel fiber mass is now a viable diagnostic coordinate because it separates
two exact regimes:

```text
S1: all middle-fiber support imported by the backbone;
S2 reference: positive support outside the backbone.
```

However, it cannot yet be inserted into the branching LP as a proved reserve.
The missing properties are:

1. schedule control or optimization at `S_2` and later states;
2. a transition inequality relating parent and simultaneous child novelty;
3. multiplicity control for labels shared by different `Xi_q`;
4. interaction with terminal steps already present recursively;
5. packing of novel labels across sibling parent states;
6. normalization against factor-two and factor-four Bellman debt.

The next computational target should minimize and maximize

```math
\mathcal N(S_2)
```

over the coordinated schedule graph, using branch-and-bound or dynamic
programming over reachable subsets. Full progression-labeled enumeration may be
large, but the objective depends only on selected center fibers and can be
carried incrementally.

A zero minimum would show that schedule choice can erase the apparent reserve.
A positive minimum would establish a schedule-independent obstruction export
at `S_2`, substantially strengthening the candidate potential.

---

## 7. Reproduction

Run

```bash
python3 src/verify_s2_novel_fiber_reference.py \
  /tmp/s2_novel_fiber_reference_certificate.txt
```

The exact certificate has SHA-256

```text
c552a6146531e02b19a1416c8913287d1efa86a0520eab031899630f8ecd33d7
```

and is regenerated by the lightweight proof-check workflow.

---

## 8. Scope

This result does not establish:

- schedule-independent positive novelty for `S_2`;
- monotonicity of novel fiber mass;
- a complete child-packing theorem;
- feasible Bellman reserve weights;
- a branching Carleson inequality;
- or the four-term Erdős conjecture.

It is an exact reference point showing that the first descendant already
contains both within-middle duplication and genuinely new fiber support.

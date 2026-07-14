# S7 provenance-preserving retained-child quotient

## Status

Exact finite one-generation retention theorem for the `S_7` 37-step local-optimum transition.

The rule converts the complete raw simultaneous occurrence family into a point-disjoint family while preserving an explicit representative provenance for every retained state.

**Verifier:** `src/verify_s7_provenance_retained_quotient.py`.

**Certificate:** `data/s7_provenance_retained_quotient_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
2a1dd14ee54a9a1b39cc19d4fefc70f54b1157be82f496e2107d3a717052ff92
```

---

## 1. Deterministic quotient

The raw transition has `131` dyadic shell occurrences. Retention proceeds in two exact stages.

### Exact-state quotient

Occurrences with identical numerical state are combined into one class. The deterministic representative order is:

1. backbone before middle fiber;
2. smaller source step;
3. smaller raw occurrence index.

This produces `87` exact state classes, each retaining the complete point-level provenance of its chosen representative.

### Point-conflict selection

Two exact state classes conflict when:

- they lie in the same dyadic shell; and
- their numerical point sets intersect.

The resulting conflict graph has:

```text
vertices = 87
edges = 290
connected components = 20
largest component = 13.
```

Each connected component is solved exhaustively for a maximum-harmonic independent set. Across all components, `14,342` candidate subsets are examined, of which `123` are feasible independent subsets.

Every component has a unique optimum.

---

## 2. Retained family

The componentwise optima combine into a unique retained family with:

```text
retained state classes = 21
backbone representatives = 2
middle-fiber representatives = 19
retained distinct labels = 11,753
dropped distinct labels = 5,018.
```

The retained state classes are pairwise point-disjoint. Every retained point has an explicit parent or sponsor provenance inherited from its deterministic representative.

The retained-family SHA-256 is

```text
824b2748bc81ad5668543dbc2137221532a8dacfb585defe65c730dc5bdfa691.
```

---

## 3. Retained harmonic mass

Let `H_ret` be the harmonic mass of the retained point-disjoint family.

Relative to the numerical union of all raw occurrences,

```math
\frac{731}{1000}
<
\frac{H_{\rm ret}}{H_{\rm raw\ union}}
<
\frac{732}{1000}.
```

Relative to the exact-state-quotiented occurrence mass,

```math
\frac{654}{1000}
<
\frac{H_{\rm ret}}{H_{\rm exact\ classes}}
<
\frac{655}{1000}.
```

Relative to the complete raw occurrence mass,

```math
\frac{582}{1000}
<
\frac{H_{\rm ret}}{H_{\rm raw\ occurrences}}
<
\frac{583}{1000}.
```

The retained family contains between `70.0%` and `70.1%` of the distinct numerical labels in the raw union.

---

## 4. What this proves

This is the first certified retained-child quotient in the current program that simultaneously provides:

- exact duplicate resolution;
- point-disjoint retained states;
- deterministic representative selection;
- explicit point provenance;
- exact maximum-harmonic optimality within every conflict component.

It is therefore a legitimate **one-generation** retained family for this recorded transition.

It does not yet prove:

- bounded reuse of the same provenance labels in descendants;
- compatibility of independently selected retained families across generations;
- a Carleson packing estimate;
- or the whole-tree Bellman inequality.

The next theorem must propagate retained representative provenance into the next generation and bound how often the same parent or sponsor capacity can reappear.
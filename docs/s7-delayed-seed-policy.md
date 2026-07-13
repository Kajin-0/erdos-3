# Delaying three seed actions improves the `S_7` transition

## Status

Exact fixed-parent finite theorem.

Start from the lexicographic coordinated schedule on `S_7`, but move only the
three unforced `q=1` actions with centers

```text
1354065, 1354070, 1354075
```

to the end of the priority order. All other initial actions retain their
lexicographic order.

The three delayed actions become stale and are not selected. The resulting
complete schedule emits no `{16,21,26}` shell and has no exact factor-two or
factor-four return to canonical `S_1,...,S_10`.

Unlike reverse lexicographic deletion, this targeted modification also improves
most raw recursive-load coordinates.

**Verifier:** `src/verify_s7_delayed_seed_policy.py`.

**Certificate:** `data/s7_delayed_seed_policy_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
37ed54c207820478fb5b2b2843342b2aebd9b274b4dd5ef1e6cf79e3d627f4e9
```

---

## Exact comparison with lexicographic deletion

| coordinate | lexicographic | delayed-seed |
|---|---:|---:|
| selected actions | `9,360` | `9,358` |
| residual size | `480` | `482` |
| terminal steps | `25` | `31` |
| middle-fiber shells | `124` | `123` |
| label occurrences | `9,335` | `9,327` |
| distinct labels | `6,683` | `7,511` |
| largest SCC | `7` | `7` |
| maximum multiplicity | `15` | `14` |
| canonical regenerations | `1` | `0` |

The distinct-label cardinality rises, but the harmonic union mass falls. The
new labels are, on average, larger and less repeatedly reused.

Exact harmonic ratios satisfy

```math
\frac9{10}
<
\frac{M_{\rm occ}^{\rm delay}}{M_{\rm occ}^{\rm lex}}
<
\frac{14}{15},
```

```math
\frac{19}{20}
<
\frac{M_{\rm union}^{\rm delay}}{M_{\rm union}^{\rm lex}}
<
\frac{24}{25},
```

and

```math
\frac23
<
\frac{M_{\rm dup}^{\rm delay}}{M_{\rm dup}^{\rm lex}}
<
\frac7{10}.
```

Thus occurrence mass falls by about `7.3%`, union mass by about `4.7%`, and
duplicate mass by about `30.3%`.

The tradeoff is:

- terminal-step mass increases by roughly `24.8%`;
- six additional terminal step classes appear;
- normalized residual error increases from `240/4096` to `241/4096`.

The residual-error penalty is exactly

```math
\boxed{\frac1{4096}}.
```

---

## Interpretation

This is the first exact policy modification in the current program that:

1. removes the recognizable canonical regeneration;
2. reduces middle-fiber occurrence mass;
3. reduces duplicate mass;
4. reduces maximum multiplicity;
5. does not enlarge the largest terminal-fiber SCC.

It is not a complete Bellman improvement because terminal mass and residual
error increase. It establishes an exact Pareto tradeoff.

The result also shows that raw cardinalities are unreliable policy objectives:
the delayed policy has more distinct fiber labels but less harmonic union mass.

---

## Revised policy target

A useful schedule score must balance at least

```math
\text{terminal mass}
+
\text{recursive occurrence mass}
+
\text{duplicate capacity}
+
\text{residual error}
-
\text{certified obstruction credit}.
```

The delayed policy provides the first local move against which candidate
weights can be tested exactly. A proposed policy cost should explain when its
large reduction in duplicate and occurrence mass outweighs the small residual
penalty and increased terminal mass.

This remains a one-parent finite theorem. It does not prove that the same
priority modification works at other states or that repeated local
improvements yield a whole-tree contraction.

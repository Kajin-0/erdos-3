# Retained-chain current-latent closure through `F5`

## Status

Exact finite theorem for the four certified point-disjoint retained transitions ending at the residual-sponsor split fifth frontier.

Every repeated parent pair resource has exactly one terminal current owner and one recursive latent owner. No parent pair has two recursive latent owners. Consequently the complete latent-latent activation residual is zero throughout the recorded retained chain.

This is a finite theorem for the certified retained families, not a universal structural theorem.

---

## 1. Transitions profiled

The exact probe reconstructs:

```text
historical F1 -> F2;
recursive R2 -> F3;
recursive R3 -> F4;
recursive R4 -> split F5.
```

The first row is the historical pre-terminal-stopping transition: its retained `F2` certificate was generated from all `21` first-frontier parents. The later rows propagate only recursive parents.

Probe:

```text
src/probe_retained_current_latent_profiles.py
```

Workflow:

```text
.github/workflows/retained-current-latent-check.yml
```

---

## 2. Exact transition table

| Transition | Parents | Children | Terminal | Recursive | Repeated parent resources | Max owner degree | Max latent degree | Branching excess | Latent-latent residual |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| historical `F1 -> F2` | 21 | 27 | 13 | 14 | 9 | 2 | 1 | `1.085433560329...` | `0` |
| `R2 -> F3` | 14 | 32 | 18 | 14 | 8 | 2 | 1 | `1.068766893663...` | `0` |
| `R3 -> F4` | 14 | 23 | 11 | 12 | 13 | 2 | 1 | `0.133953757799...` | `0` |
| `R4 -> F5 split` | 12 | 37 | 22 | 15 | 3 | 2 | 1 | `0.019917616169...` | `0` |

Every nonzero repeated-resource profile is exactly

```text
current owners = 1;
latent owners  = 1;
total owners   = 2.
```

There are no profiles of type

```text
current=0, latent>=2;
current=1, latent>=2.
```

---

## 3. Exact mass decomposition

For one parent resource `f`, let

```math
c_f\in\{0,1\}
```

be its current-owner count and `ell_f` its recursive latent-owner count.

The universal identity is

```math
(c_f+\ell_f-1)_+
=
c_f\mathbf 1_{\ell_f>0}
+
(\ell_f-1)_+.
```

On every recorded repeated resource,

```math
c_f=1,
\qquad
\ell_f=1.
```

Therefore

```math
\boxed{
(\ell_f-1)_+=0
}
```

resourcewise.

The aggregate exact masses are

```text
branching excess         = 2.308071827961...
current-latent overlap   = 2.308071827961...
latent-latent residual   = 0
```

with exact aggregate fraction

```math
\frac{1206999750169151641}{522947221809681123}.
```

Thus

```math
\boxed{
R_{\rm branch}
=
R_{\rm terminal\ current-latent}
}
```

on the complete recorded chain.

---

## 4. Terminal ownership is exact

The current owner is terminal in every repeated-resource profile. The recursive-current overlap mass is exactly zero on all four transitions.

Hence each repeated parent-pair term is already one harmonic term in a terminal retained child. Point-disjointness makes these current terms injective.

The branching excess can be moved from the pair-activation ledger to the terminal first-appearance ledger without changing total mass and without paying any terminal term twice.

This is reclassification, not deletion of mass.

---

## 5. Transition-specific exact values

### Historical `F1 -> F2`

```text
child resource occurrences  = 6,311,032
parent resource union       = 6,311,023
repeated parent resources   = 9
branching excess            = 1.085433560329...
latent-latent residual      = 0
```

### `R2 -> F3`

```text
child resource occurrences  = 2,155,408
parent resource union       = 2,155,400
repeated parent resources   = 8
branching excess            = 1.068766893663...
latent-latent residual      = 0
```

### `R3 -> F4`

```text
child resource occurrences  = 372,299
parent resource union       = 372,286
repeated parent resources   = 13
branching excess            = 0.133953757799...
latent-latent residual      = 0
```

### `R4 -> F5 split`

```text
child resource occurrences  = 75,287
parent resource union       = 75,284
repeated parent resources   = 3
branching excess            = 0.019917616169...
latent-latent residual      = 0
```

The final three resources are independently certified in

```text
docs/terminal-current-branch-absorption.md
```

and

```text
src/probe_s7_terminal_current_branch_absorption.py.
```

---

## 6. Relation to the universal no-go

Point-disjointness alone does not force latent-latent residual to vanish. The explicit family in

```text
docs/point-disjoint-latent-reuse-no-go.md
```

has two point-disjoint recursive children sharing three latent resources.

The far-aspect family in

```text
docs/far-aspect-latent-reuse-no-go.md
```

shows that the residual cannot always be paid by one unweighted reference pair.

Therefore the recorded zero residual is meaningful structure of the certified deletion/retention policy, not a tautology of affine point-disjointness.

---

## 7. Strategic consequence

The recorded retained chain has no unresolved repeated latent pair activation through `F5`.

The active obstruction moves to proving one of the following state-independently:

1. the coordinated deletion plus point-disjoint retention rule always produces `ell_f<=1`;
2. violations `ell_f>=2` emit a scale-weighted three-translate obstruction sufficient for payment;
3. a policy can always be chosen so that latent-latent residual is terminalized or dominated;
4. the exact current-latent closure persists under a corrected terminal-stopped continuation.

Another finite retained generation is not justified until one of these transfer laws is proved.
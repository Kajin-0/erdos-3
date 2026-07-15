# S7 terminal-completion saturation

## Status

Exact finite classification of the terminal completion integers requested by the
source-weighted sponsor-pair transport frontier.

The classification is performed inside the certified depth-seven state

```math
S_7\subseteq[1048576,2097152),
\qquad
|S_7|=9840,
\qquad
\max S_7=2021668.
```

It does not propagate a sixth retained generation.

---

## 1. Completion request family

The terminal-payment v2 probe assigns every direct, backward, or residual
terminal target its prescribed completion integer. Targets completed in their
own parent are already paid by parent three-AP edge capacity. Only fourteen
additional targets complete elsewhere inside `S7`.

The remaining terminal targets request

```text
14104 distinct completion integers
```

in the range

```text
1455569 through 2019787.
```

Every requested integer lies inside the same standard dyadic shell as `S7`, but
is absent from `S7`.

---

## 2. Exhaustive four-AP saturation test

For one requested integer `c`, adding `c` to `S7` creates a four-term
progression precisely when there are `a,d` and a missing position `j` such that

```math
\{a,a+d,a+2d,a+3d\}\setminus\{c\}
\subseteq S_7
```

and `c` is the `j`-th point of that progression.

The classifier exhausts all

```text
48407880
```

unordered pairs of points in `S7`. Every possible three-of-four witness has one
of four forms:

```text
missing left endpoint;
missing right endpoint;
missing first interior point;
missing second interior point.
```

Each form is reconstructed from an adjacent pair and one membership test. Thus
the classification is exhaustive rather than sampled.

---

## 3. Exact split

The `14104` completion integers divide as follows:

```text
certified S7 holes        = 9334
S7-admissible extensions  = 4770
```

A certified `S7` hole has an explicit four-AP witness using three points of
`S7`. Therefore, in every four-AP-free ambient set containing `S7`, that
completion integer is genuinely absent.

An `S7`-admissible extension has no such three-root witness. It may be added to
`S7` individually without creating a four-AP. Relative to a maximal ambient
four-AP-free set, it remains a dichotomy:

```text
present outside the recorded lineage;
or absent because of a witness using at least one ambient point outside S7.
```

It must not be counted as immediate hole credit.

---

## 4. Terminal-target mass split

The previously unresolved terminal-target family contains

```text
targets                 = 38579
source occurrences      = 71033
target union mass       = 345.019947619801...
source collision mass   = 159.320392140119...
```

The saturation classification gives:

| Completion class | Distinct integers | Targets | Target union mass | Source collision mass |
|---|---:|---:|---:|---:|
| Certified `S7` hole | 9334 | 25284 | `285.209985114934...` | `126.956957535084...` |
| `S7`-admissible extension | 4770 | 13295 | `59.809962504867...` | `32.363434605035...` |

The certified-hole class contains:

```text
24997 backward targets
  287 residual targets
```

and carries `46728` source occurrences with initial source mass

```math
401.140520764914\ldots.
```

The admissible-extension class contains:

```text
13131 backward targets
  164 residual targets
```

and carries `24305` source occurrences with initial source mass

```math
85.010670280041\ldots.
```

---

## 5. Consequence for the activation row

The source-weighted terminal-payment inequality is

```math
\sum_{e\in A}w(e)
\le
\frac52\mathcal L_3(P)
+
M_{\rm out}(A)
+
R_{\rm src}(A).
```

On the certified frontier, the former undifferentiated outside-parent target
mass splits into:

```math
M_{\rm out}
=
M_{\rm hole}^{S_7}
+
M_{\rm ext/ambient},
```

where

```math
M_{\rm hole}^{S_7}
=
285.209985114934\ldots
```

has explicit three-root four-AP witnesses, while

```math
M_{\rm ext/ambient}
=
59.809962504867\ldots
```

is the genuine ambient decision term.

This removes approximately `82.66%` of the previously unresolved terminal-target
union mass from the ambiguous external-completion class.

---

## 6. Remaining theorem

The finite frontier is now concentrated in two terms:

1. source-weighted collision reuse, especially backward sponsor-sponsor merge
   fibers;
2. the `4770` individually admissible completion integers.

For a maximal ambient four-AP-free set `B` containing `S7`, every admissible
completion `c` satisfies exactly one of:

```text
c belongs to B outside the recorded parent lineage;
c does not belong to B and has a four-AP witness using at least one point of B\S7.
```

The next valid object is therefore a completion first-appearance ledger keyed
by

```text
completion integer c;
terminal targets requesting c;
ambient membership or first outside-S7 witness;
source-weighted collision fiber;
first generation at which c or its witness appears.
```

A local `S7` saturation result alone does not prove global summability, but it
reduces the unresolved completion mass to a substantially smaller and precisely
labeled ambient term.

---

## 7. Reproduction

The read-only PR computation uses:

```text
src/export_s7_terminal_completion_requests.py
src/classify_s7_terminal_completion_saturation.cpp
src/summarize_s7_terminal_completion_saturation.py
```

The deterministic classification hashes are:

```text
classification TSV SHA-256:
fba652e68be48f5ed7863ac4a7f4bdd9887872da74163af3620d02ef66ce9831

target assignment SHA-256:
7559c5bd4bbf7943dd2a211d72654c64cca5d4ee3e83da6374f65c7470f18c97

summary payload SHA-256:
6e4306508ba06a087929d318a4ba51a6d33b3ffb9ae752d67105155f0f66009d
```

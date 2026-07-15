# S7 terminal-completion saturation

## Status

Exact finite classification and first-use ledger for terminal completion integers
requested by the source-weighted sponsor-pair transport frontier.

The computation is performed inside the certified depth-seven state

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
own parent are controlled by parent three-AP edge capacity. Only fourteen
additional targets complete elsewhere inside `S7`.

The remaining terminal targets request

```text
14104 distinct completion integers
```

in the range

```text
1455569 through 2019787.
```

Every requested integer lies inside the standard dyadic shell containing `S7`,
but is absent from `S7`.

---

## 2. Exhaustive four-AP saturation test

For a requested integer `c`, adding `c` to `S7` creates a four-term progression
precisely when there are `a,d` and a missing position `j` such that

```math
\{a,a+d,a+2d,a+3d\}\setminus\{c\}
\subseteq S_7
```

and `c` is the `j`-th point of that progression.

The classifier exhausts all

```text
48407880
```

unordered pairs of points in `S7`. Every possible three-of-four witness is
covered by one of four cases:

```text
missing left endpoint;
missing right endpoint;
missing first interior point;
missing second interior point.
```

Each case is reconstructed from an adjacent pair and one membership test. The
classification is exhaustive rather than sampled.

---

## 3. Exact saturation split

The `14104` requested completion integers divide as follows:

```text
certified S7 holes        = 9334
S7-admissible extensions  = 4770
```

A certified `S7` hole has an explicit four-AP witness using three points of
`S7`. Therefore it is absent from every four-AP-free ambient set containing
`S7`.

An `S7`-admissible extension has no such three-root witness and may be added to
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

| Completion class | Integers | Targets | Target union mass | Source collision mass |
|---|---:|---:|---:|---:|
| Certified `S7` hole | 9334 | 25284 | `285.209985114934...` | `126.956957535084...` |
| `S7`-admissible extension | 4770 | 13295 | `59.809962504867...` | `32.363434605035...` |

The certified-hole class consists of `24997` backward targets and `287`
residual targets. It carries `46728` source occurrences with initial source mass

```math
401.140520764914\ldots.
```

The admissible-extension class consists of `13131` backward targets and `164`
residual targets. It carries `24305` source occurrences with initial source mass

```math
85.010670280041\ldots.
```

Thus explicit `S7` witnesses remove approximately `82.66%` of the former
outside-parent target union from the ambiguous ambient class. They identify the
obstruction; they do not by themselves prove that the entire associated pair
mass is paid without reuse.

---

## 5. Completion first appearance and reuse

Several terminal targets can request the same completion integer. Choose, for
each completion, one deterministic maximum-weight target as its first target.
Then

```math
M_{\rm target}
=
M_{\rm first}
+
M_{\rm completion\ reuse}.
```

The exact split is:

| Completion class | First-target mass | Completion-reuse mass | Singleton integers | Reused integers |
|---|---:|---:|---:|---:|
| Certified `S7` hole | `218.754197271041...` | `66.455787843892...` | 3328 | 6006 |
| `S7`-admissible extension | `42.635504537459...` | `17.174457967408...` | 1688 | 3082 |

The maximum number of terminal targets requesting one completion is `21` in the
certified-hole class and `20` in the admissible-extension class.

This is a second reuse layer, distinct from sponsor-pair transport collision:

```text
source pairs may merge into one terminal target;
terminal targets may merge into one requested completion integer.
```

Both layers must remain explicit in a whole-tree ledger.

---

## 6. Witness-step aspect identity

Fix a certified hole `c`. Let its recorded four-AP witness have common step `h`,
and let a terminal target requesting `c` have pair gap `D`. Then

```math
w_{\rm target}=\frac1D
=
\frac hD\frac1h.
```

Thus each target is an exact aspect-ratio multiple of its witness-step weight.
For the deterministic first target of each certified hole, the profile is:

| Witness regime | Completion integers | First-target mass |
|---|---:|---:|
| `h <= D` | 4452 | `128.373650251777...` |
| `D < h <= 2D` | 2530 | `29.776616523618...` |
| `2D < h <= 4D` | 1592 | `20.339078161129...` |
| `4D < h <= 8D` | 301 | `8.030462775442...` |
| `h > 8D` | 459 | `32.234389559076...` |

In the first regime,

```math
h\le D
\quad\Longrightarrow\quad
\frac1D\le\frac1h,
```

so one witness-step token directly dominates the first target. This immediately
covers `128.373650251777...`, or approximately `58.68%`, of certified-hole
first-target mass at the level of raw weight.

For all certified-hole targets, including completion reuse, the profile is:

| Witness regime | Targets | Target union mass |
|---|---:|---:|
| `h <= D` | 15634 | `179.403190360787...` |
| `D < h <= 2D` | 5214 | `35.664674098508...` |
| `2D < h <= 4D` | 3163 | `25.040536749685...` |
| `4D < h <= 8D` | 585 | `9.826034030244...` |
| `h > 8D` | 688 | `35.275549875709...` |

The far-aspect class is small in count but not negligible in mass. It requires
an aspect-weighted witness ledger rather than an unweighted saturation count.

---

## 7. Consequence for the activation row

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

On the certified frontier,

```math
M_{\rm out}
=
M_{\rm hole}^{S_7}
+
M_{\rm ext/ambient},
```

with

```math
M_{\rm hole}^{S_7}
=
285.209985114934\ldots
```

and

```math
M_{\rm ext/ambient}
=
59.809962504867\ldots.
```

The first term has explicit three-root four-AP witnesses and a complete
completion-level first-use ledger. The second is the genuine ambient decision
term.

---

## 8. Remaining theorem

The finite frontier is now concentrated in four precisely labeled obligations:

1. source-weighted sponsor-pair collision reuse;
2. completion-target reuse `66.455787843892...` within certified holes;
3. far-aspect witness payment, especially the `h>8D` first-target mass
   `32.234389559076...`;
4. the `4770` individually admissible completion integers carrying target union
   mass `59.809962504867...`.

The next valid theorem should be a completion/witness transfer law keyed by

```text
completion integer c;
first terminal target and completion reuse targets;
four-AP witness step h;
target gap D and dyadic aspect h/D;
ambient membership or first outside-S7 witness;
first generation at which c or its witness appears.
```

A local saturation result alone does not prove global summability. It does,
however, reduce the previously undifferentiated completion obstruction to an
exact first-appearance, reuse, and aspect-ratio problem.

---

## 9. Reproduction

The read-only PR computation uses:

```text
src/export_s7_terminal_completion_requests.py
src/classify_s7_terminal_completion_saturation.cpp
src/summarize_s7_terminal_completion_saturation.py
```

The deterministic hashes are:

```text
classification TSV SHA-256:
fba652e68be48f5ed7863ac4a7f4bdd9887872da74163af3620d02ef66ce9831

target assignment SHA-256:
7559c5bd4bbf7943dd2a211d72654c64cca5d4ee3e83da6374f65c7470f18c97

completion first-use rows SHA-256:
dc573a88770162ca25b958c6b86a651ac2351089e37aa8b68963a77bf5551790

summary payload SHA-256:
d9b8ba67e980f7d5982eeea76a17dac5a73ab768f146785cc3df7a4a3550d023
```

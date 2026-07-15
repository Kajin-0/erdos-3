# S7 edge-first terminal-completion saturation

## Status

Exact finite classification and first-use ledger for terminal targets on the
certified residual-sponsor fourth-to-fifth retained diagnostic frontier.

The classification uses the correct payment hierarchy:

```text
parent-local three-AP edge capacity;
then any three-AP edge capacity elsewhere in S7;
then prescribed-completion saturation;
then completion and support-pair reuse.
```

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

## 1. Why edge capacity precedes prescribed completion

The terminal transport map assigns each direct, backward, or residual target a
prescribed completion. That completion is useful for obstruction geometry, but
it is not the only way a pair can be an edge of a three-term progression.

For a terminal pair

```math
e=\{x,y\},
\qquad x<y,
\qquad D=y-x,
```

all possible three-AP completions are

```math
x-D,
\qquad
y+D,
\qquad
x+D/2
```

when the midpoint is integral.

Therefore a target whose prescribed completion is absent may still be paid by
the `5/2` edge capacity of another three-AP already present in `S7`.
Saturation is applied only after this full edge test.

---

## 2. Edge-first split

The prescribed-completion probe initially reports

```text
38579 terminal targets
```

whose prescribed completion is outside their parent and absent from `S7`, with
target union mass

```math
345.019947619801\ldots.
```

Among them,

```text
2865 targets
```

are nevertheless edges of another three-AP already present in `S7`. Their union
mass is

```math
72.867994406210\ldots.
```

These targets remain in the ordinary three-AP edge-capacity ledger and are not
sent to saturation.

The genuinely edge-unresolved family is therefore

```text
35714 targets
```

with union mass

```math
272.151953213591\ldots.
```

The target-mass partition is exact:

```math
345.019947619801\ldots
=
72.867994406210\ldots
+
272.151953213591\ldots.
```

---

## 3. Completion request family

The `35714` edge-unresolved targets request

```text
13560 distinct prescribed completion integers
```

inside the standard dyadic shell containing `S7`.

Every requested integer is absent from `S7`. The saturation classifier asks
whether adding that integer to `S7` immediately creates a four-term arithmetic
progression using three existing `S7` points.

---

## 4. Exhaustive S7 saturation test

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

## 5. Corrected saturation split

The `13560` edge-unresolved completion integers divide as follows:

```text
certified S7 holes        = 8870
S7-admissible extensions  = 4690
```

A certified `S7` hole has an explicit four-AP witness using three points of
`S7`. It is therefore absent from every four-AP-free ambient set containing
`S7`.

An `S7`-admissible extension has no three-root `S7` witness and may be added to
`S7` individually without creating a four-AP. Relative to a maximal ambient
four-AP-free set, it remains a dichotomy:

```text
present outside the recorded lineage;
or absent because of a witness using at least one ambient point outside S7.
```

It is not immediate hole credit.

---

## 6. Exact mass partition

The edge-unresolved family has

```text
targets                    = 35714
source occurrences         = 65647
target union mass          = 272.151953213591...
source initial mass        = 387.456087517972...
source target occurrence   = 511.408323658613...
source collision mass      = 130.143328802921...
terminal collision mass    = 239.256370445023...
transport amplification    = 109.113041642102...
```

The saturation classes are:

| Completion class | Integers | Targets | Target union mass | Source collision mass |
|---|---:|---:|---:|---:|
| Certified `S7` hole | 8870 | 22804 | `213.607508081532...` | `98.063506377289...` |
| `S7`-admissible extension | 4690 | 12910 | `58.544445132059...` | `32.079822425631...` |

The certified-hole class carries

```text
source occurrences = 41862
source initial mass = 303.994546790143...
```

and the admissible-extension class carries

```text
source occurrences = 23785
source initial mass = 83.461540727830...
```

The source-weighted collision term remains strictly smaller than the
terminal-weight collision term in both classes.

---

## 7. Completion first appearance and reuse

Several terminal targets can request the same completion integer. For each
completion choose one deterministic maximum-weight target as its first target.
Then

```math
M_{\rm target}
=
M_{\rm first}
+
M_{\rm completion\ reuse}.
```

The exact split is:

| Completion class | First-target mass | Completion-reuse mass |
|---|---:|---:|
| Certified `S7` hole | `168.669469494649...` | `44.938038586882...` |
| `S7`-admissible extension | `42.175918639512...` | `16.368526492547...` |

This is a second reuse layer, distinct from sponsor-pair transport collision:

```text
source pairs may merge into one terminal target;
terminal targets may merge into one requested completion integer.
```

Both must remain explicit in a whole-tree ledger.

---

## 8. Witness-step aspect identity

Fix a certified hole `c`. Let its recorded four-AP witness have common step `h`,
and let a terminal target requesting `c` have pair gap `D`. Then

```math
w_{\rm target}
=
\frac1D
=
\frac hD\frac1h.
```

For the first target of every certified hole, the corrected profile is:

| Witness regime | Completion integers | First-target mass |
|---|---:|---:|
| `h <= D` | 4232 | `99.667156821497...` |
| `D < h <= 2D` | 2483 | `29.680011410137...` |
| `2D < h <= 4D` | 1448 | `7.514202901945...` |
| `4D < h <= 8D` | 303 | `8.677362095051...` |
| `h > 8D` | 404 | `23.130736266018...` |

In the near regime,

```math
h\le D
\quad\Longrightarrow\quad
\frac1D\le\frac1h.
```

Thus the witness-step pair dominates the target weight pointwise. The far
aspect class is smaller but remains a genuine weighted obligation.

---

## 9. Canonical support-pair reuse

Assign each certified hole to the first adjacent pair of present points in its
chosen four-AP witness. The state-independent canonical-pair theorem proves
that one support pair serves at most two distinct holes.

On the corrected edge-unresolved frontier:

```text
certified holes                       = 8870
distinct canonical support pairs      = 7929
reused canonical support pairs        = 941
maximum support-pair multiplicity     = 2
```

The support-pair masses are

```text
union mass       = 386.699243131284...
occurrence mass  = 502.942546688386...
reuse mass       = 116.243303557102...
```

After one maximum-weight target is chosen per support pair, only

```math
5.523243331592\ldots
```

of certified-hole first-target mass remains as support-pair assignment reuse.

For the near regime `h<=D`:

```text
distinct support pairs  = 3670
reused support pairs    = 562
maximum multiplicity    = 2
```

with target mass

```math
99.667156821497\ldots
```

and support-pair assignment reuse

```math
4.181354423532\ldots.
```

The multiplicity problem is therefore controlled at the hole-witness support
layer. The remaining issue is collision-sound payment of the support-pair union.

---

## 10. Consequence for the activation row

The source-weighted terminal-payment inequality is

```math
\sum_{e\in A}w(e)
\le
\frac52\mathcal L_3(P)
+
M_{\rm edge\ unresolved}(A)
+
R_{\rm src}(A).
```

On the certified frontier,

```math
M_{\rm edge\ unresolved}
=
M_{\rm hole}^{S_7}
+
M_{\rm ext/ambient},
```

where

```math
M_{\rm hole}^{S_7}
=
213.607508081532\ldots
```

has explicit three-root four-AP witnesses, while

```math
M_{\rm ext/ambient}
=
58.544445132059\ldots
```

is the genuine ambient decision term.

The edge-first correction removes an additional

```math
72.867994406210\ldots
```

from the saturation problem before any obstruction charge is used.

---

## 11. Remaining theorem

The finite frontier is now concentrated in four labeled obligations:

1. source-weighted sponsor-pair collision reuse `130.143328802921...` on the
   edge-unresolved family;
2. completion-target reuse `44.938038586882...` within certified holes;
3. far-aspect witness payment, especially the `h>8D` first-target mass
   `23.130736266018...`;
4. the `4690` individually admissible completion integers carrying target union
   mass `58.544445132059...`.

The next valid theorem should be a collision-sound support-pair first-appearance
law keyed by

```text
terminal target pair;
completion integer;
canonical witness support pair;
witness step h and target gap D;
existing pair capacity or first appearance;
ambient membership or first outside-S7 witness.
```

Another retained generation is not justified.

---

## 12. Reproduction

The read-only PR computation uses:

```text
src/export_s7_terminal_completion_requests.py
src/classify_s7_terminal_completion_saturation.cpp
src/summarize_s7_edge_unresolved_completion_saturation.py
```

The corrected deterministic hashes are:

```text
classification TSV SHA-256:
ed14eb2f4dc4f3fce2d03cc9da617f2f78475856110942edbcc2281a0aa2f72a

edge-unresolved assignment SHA-256:
893e598e47e4036222bcfe27059a39954c31fc5233207cfa3dad03a83ce4555d

summary payload SHA-256:
480f7522004bdbadedb8888cc5d1f970598100718d209082ea7cbfa952cc7173
```

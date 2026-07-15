# S7 edge-first terminal-completion saturation

## Status

Exact finite classification and first-use ledger for terminal targets on the
certified residual-sponsor fourth-to-fifth retained diagnostic frontier.

The payment hierarchy is:

```text
parent-local three-AP edge capacity;
any three-AP edge capacity elsewhere in S7;
prescribed-completion saturation;
completion and support-pair reuse.
```

The computation uses the certified state

```math
S_7\subseteq[1048576,2097152),
\qquad |S_7|=9840,
\qquad \max S_7=2021668.
```

Generation six is not propagated.

---

## 1. Edge capacity precedes prescribed completion

For a terminal pair

```math
e=\{x,y\},
\qquad x<y,
\qquad D=y-x,
```

all possible three-AP completion roots are

```math
x-D,
\qquad y+D,
\qquad x+D/2
```

when the midpoint is integral.

The terminal transport map chooses one prescribed completion, but an absent
prescribed completion does not imply that the pair is absent from all parent or
`S7` three-AP edge capacity. The full edge test is performed first.

The prescribed-completion probe reports `38579` targets whose prescribed
completion is outside their parent and absent from `S7`, with union mass

```math
345.019947619801\ldots.
```

Of these, `2865` are edges of another three-AP already present in `S7`, carrying

```math
72.867994406210\ldots.
```

They remain in the ordinary `5/2` three-AP edge-capacity ledger.

The actual edge-unresolved family is therefore

```text
35714 targets
```

with union mass

```math
272.151953213591\ldots.
```

The partition is exact:

```math
345.019947619801\ldots
=
72.867994406210\ldots
+
272.151953213591\ldots.
```

---

## 2. Exhaustive S7 saturation

The `35714` edge-unresolved targets request `13560` distinct prescribed
completion integers inside the standard dyadic shell containing `S7`.

For a requested integer `c`, adding `c` to `S7` creates a four-term progression
precisely when

```math
\{a,a+d,a+2d,a+3d\}\setminus\{c\}
\subseteq S_7
```

for some `a,d`, with `c` occupying the missing position.

The classifier exhausts all

```text
48407880
```

unordered pairs of `S7` points and covers all four missing positions. The result
is exact rather than sampled:

```text
certified S7 holes        = 8870
S7-admissible extensions  = 4690
```

A certified hole has an explicit four-AP witness using three `S7` points and is
therefore absent from every four-AP-free ambient set containing `S7`.

An admissible extension may be added to `S7` individually without creating a
four-AP. In a maximal ambient set it is either present outside the recorded
lineage or absent because of a witness using at least one point outside `S7`.
It is not immediate hole credit.

---

## 3. Exact edge-unresolved mass partition

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

| Completion class | Integers | Targets | Target union | Source collision |
|---|---:|---:|---:|---:|
| Certified `S7` hole | 8870 | 22804 | `213.607508081532...` | `98.063506377289...` |
| `S7`-admissible extension | 4690 | 12910 | `58.544445132059...` | `32.079822425631...` |

The certified-hole class contains `22571` backward and `233` residual targets,
with `41862` source occurrences. The admissible class contains `12746` backward
and `164` residual targets, with `23785` source occurrences.

---

## 4. Completion first appearance

Several terminal targets can request the same completion integer. Choose one
deterministic maximum-weight target per completion. Then

```math
M_{\rm target}
=
M_{\rm first}
+
M_{\rm completion\ reuse}.
```

| Completion class | First-target mass | Reuse mass | Reused integers | Max targets/completion |
|---|---:|---:|---:|---:|
| Certified `S7` hole | `168.669469494649...` | `44.938038586882...` | 5497 | 21 |
| `S7`-admissible extension | `42.175918639512...` | `16.368526492547...` | 2995 | 20 |

This is distinct from sponsor-pair transport collision:

```text
source pairs merge into terminal targets;
terminal targets merge into completion integers.
```

---

## 5. Witness-step aspect profile

For a certified hole with witness step `h` and first target gap `D`,

```math
w_{\rm target}
=
\frac1D
=
\frac hD\frac1h.
```

| Regime | Holes | First-target mass |
|---|---:|---:|
| `h <= D` | 4232 | `99.667156821497...` |
| `D < h <= 2D` | 2483 | `29.680011410137...` |
| `2D < h <= 4D` | 1448 | `7.514202901945...` |
| `4D < h <= 8D` | 303 | `8.677362095051...` |
| `h > 8D` | 404 | `23.130736266018...` |

In the near regime, `1/D <= 1/h`; the canonical witness pair dominates the
target weight pointwise. Far-aspect targets require an aspect-weighted transfer.

---

## 6. Canonical witness support pairs

Assign each certified hole to the first adjacent present pair in its chosen
four-AP witness. The state-independent canonical-pair theorem proves that one
support pair serves at most two holes.

On the edge-unresolved frontier:

```text
certified holes                   = 8870
distinct canonical support pairs  = 7929
reused support pairs              = 941
maximum multiplicity              = 2
```

```text
support-pair union mass       = 386.699243131284...
support-pair occurrence mass  = 502.942546688386...
support-pair reuse mass       = 116.243303557102...
```

After one maximum-weight target is selected per support pair, support-pair
assignment reuse is only

```math
5.523243331592\ldots.
```

For the near regime:

```text
distinct support pairs  = 3670
reused support pairs    = 562
maximum multiplicity    = 2
first-target mass       = 99.667156821497...
assignment reuse        = 4.181354423532...
```

The multiplicity problem is controlled at the hole-witness support layer. The
remaining issue is collision-sound payment of the support-pair union.

---

## 7. Refined activation interface

The source-weighted terminal-payment row is now organized as

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
213.607508081532\ldots
+
58.544445132059\ldots,
```

where the first term has explicit three-root `S7` witnesses and the second is
the genuine ambient decision term.

The next theorem must combine:

1. collision-sound first appearance of canonical support pairs;
2. completion-target reuse `44.938038586882...`;
3. far-aspect witness payment, especially `23.130736266018...` in `h>8D`;
4. the `4690` admissible completion integers;
5. source-weighted transport collision `130.143328802921...` on the
   edge-unresolved family.

Another retained generation is not justified.

---

## 8. Reproduction

```text
src/export_s7_terminal_completion_requests.py
src/classify_s7_terminal_completion_saturation.cpp
src/summarize_s7_edge_unresolved_completion_saturation.py
```

Deterministic PR-artifact hashes:

```text
classification TSV SHA-256:
a701bcebbd6860baf98e2f26516f6bedc13f7c68bb07d5dc29a9365ae3ca8f7b

edge-unresolved assignment SHA-256:
893e598e47e4036222bcfe27059a39954c31fc5233207cfa3dad03a83ce4555d

summary payload SHA-256:
4778f5fd934818411ec7ef7e7ec28800f2bcb3b83f20a5ccd190ef9e5be400b5
```

# Sponsor-pair transport frontier on the refined retained transition

## Status

Exact finite classification of activated sponsor-core pair transport on the certified residual-sponsor `R_4 -> F_5` retained transition.

The result uses the state-independent forward-transport theorem from `docs/sponsor-pair-forward-transport.md`. It does not propagate generation six and does not fit a potential.

---

## 1. Activated resource family

The refined complete retained family has `37` states. Its current and recursive latent affine pair resources contain

```text
75,287 pair occurrences
75,284 distinct pair tokens.
```

Exactly `75,247` distinct tokens meet the sponsor core and are activated. The remaining `37` are residual-residual pairs and require no sponsor transport.

The activated family is overwhelmingly recursive latent sponsor-backbone capacity:

```text
latent-recursive only     74,188 pairs, mass 1177.643059944907...
current-recursive only       864 pairs, mass    1.873962098445...
current-terminal only        192 pairs, mass    2.085226848558...
mixed current/latent           3 pairs, mass    0.019917616169...
```

By retained child source,

```text
sponsor backbone only     75,055 pairs, mass 1179.930455501841...
residual backbone only       174 pairs, mass    1.619603708883...
middle fiber only             15 pairs, mass    0.052189681185...
mixed sponsor/middle           3 pairs, mass    0.019917616169...
```

Thus the active analytical object is sponsor-backbone latent pair capacity, not middle-fiber mass.

---

## 2. Exact terminal classes

Every activated distinct pair is transported until it terminates as a direct selected edge, a backward obstruction, or a residual pair.

| terminal class | pair count | initial union mass | target occurrence mass |
|---|---:|---:|---:|
| backward | 72,363 | 760.440265648176 | 1228.079324208665 |
| direct | 1,513 | 417.530512851610 | 420.905273251794 |
| residual | 1,371 | 3.651388008292 | 32.419088303288 |

By count, more than `96%` of activated pairs terminate backward. Residual termination is negligible in initial harmonic mass.

The maximum transport path length is `6`. The initial mass in paths of lengths `4,5,6` is only

```text
0.804288614422...
0.041172825353...
0.001485114823...
```

respectively. The obstruction is therefore not a long-path tail; it is the large immediate and short-path backward family.

---

## 3. Completion and collision structure

The activated pairs split into

```text
in-parent completed        8,725 pairs, initial mass 768.731175812637...
parent-external completion 66,522 pairs, initial mass 412.890990695441...
```

Parent-external completions dominate cardinality, while in-parent completions carry more initial harmonic mass.

The transported family has

```text
40,512 distinct terminal target pairs
19,593 collision targets
maximum target multiplicity 32.
```

The exact first-use/reuse decomposition is

```math
\sum_e w(T(e))
=
\sum_{z:\mu(z)>0}w(z)
+
\sum_z(\mu(z)-1)_+w(z).
```

Numerically,

```text
terminal target occurrence mass = 1681.403685763747...
terminal target union mass       =  970.461110516518...
transport collision reuse        =  710.942575247229...
```

Collision reuse is therefore a primary term, not a lower-order artifact.

---

## 4. Certified transport inequality

The activated initial union mass is

```text
1181.622166508078...
```

The distinct direct target mass is

```text
399.890641838252...
```

and is bounded by the selected-action incidence capacity

```text
853.192982305550....
```

The exact set-valued transport inequality is verified:

```math
\sum_{e\in A}w(e)
\le
\frac32\sum_j\frac1{q_j}
+
\sum_{z\in B(A)}w(z)
+
\sum_{z\in Q(A)}w(z)
+
R_{\rm trans}(A).
```

The recorded right side is `2824.633970064733...`, with positive slack `1643.011803556655...`.

This inequality is structurally correct but not yet economical because backward target mass and transport-collision reuse remain large.

---

## 5. Concentration

Four parent classes carry almost all activated mass:

| parent class | activated pairs | initial mass |
|---:|---:|---:|
| 93 | 46,723 | 447.876668823032 |
| 82 | 23,325 | 430.119460278459 |
| 77 | 2,853 | 145.054664229550 |
| 65 | 2,208 | 128.824732215617 |

The first sponsor side is also highly asymmetric:

```text
positive side: 71,766 pairs, mass 1137.678283024928...
negative side:  3,481 pairs, mass   43.943883483150...
```

This concentration gives a substantially smaller target for the next exact obstruction analysis.

---

## 6. Consequence for the proof program

The sponsor-pair transport theorem has reduced the activation problem to two dominant terms:

1. backward obstruction mass;
2. terminal-target collision reuse.

Residual target mass is small on this frontier. Middle-fiber activation is negligible. The next work should therefore:

1. split backward pairs by in-parent completion versus parent-external completion;
2. classify external completions into ambient roots outside the parent lineage and genuine ambient holes;
3. attach genuine holes to completion, rectangle, or cheap-extension exclusion witnesses;
4. place the `19,593` collision targets in a union-valued first-appearance ledger and bound repeated target use.

No additional retained generation is required.

---

## 7. Reproduction

Permanent verifier:

```bash
python3 src/run_exact_python.py \
  src/verify_sponsor_pair_transport_frontier.py \
  /tmp/sponsor_pair_transport_frontier_certificate.txt
```

Extended retained-frontier suite:

```bash
bash src/run_verify_terminal_sink_ledger.sh
```

Recorded certificate:

```text
data/sponsor_pair_transport_frontier_certificate_2026-07-14.txt
```

Certificate SHA-256:

```text
d63dd46d02e7539c31f04bac6a393a585d69f25730eabe5ff4942ae1c4b5125d
```

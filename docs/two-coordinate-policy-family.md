# Two-coordinate policy family through `S_7`

## Status

Exact finite ranking theorem for a deterministic family of complete coordinated schedules.

The tested score is

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi,
```

where:

- `T` is terminal-step harmonic mass;
- `O` is middle-fiber occurrence mass;
- `E` is normalized terminal-residual error;
- `G` is the certified charge of the isolated canonical regenerative child.

The exact witness is

```math
\boxed{\lambda=3,\qquad\gamma=\frac1{10}.}
```

**Verifier:** `src/verify_two_coordinate_policy_family.py`.

**Certificate:** `data/two_coordinate_policy_family_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
bd16d379e78feadcd32efb349302874367183101a32c9178eb439bda576e6e31
```

---

## 1. Tested policy family

The finite family contains:

- lexicographic deletion;
- reverse lexicographic deletion;
- single-step delays for `30`, `40`, `142`, and `161`;
- delay step `5`;
- delay steps `{5,40}`;
- delay steps `{5,40,30}`;
- on `S_7`, the corresponding policies with the three seed-producing `q=1` actions also delayed.

Every schedule is completed exactly. Policy rankings use exact rational arithmetic.

---

## 2. Exact winners at the witness weights

At

```math
(\lambda,\gamma)=\left(3,\frac1{10}\right),
```

the exact finite winners are:

| state | winning policy | selected | residual | terminal steps | fiber occurrences |
|---:|---|---:|---:|---:|---:|
| `S_1` | all non-reverse tested policies tie | `6` | `6` | `2` | `4` |
| `S_2` | `step5`, `step540` tie | `25` | `14` | `7` | `18` |
| `S_3` | `step540` | `91` | `29` | `12` | `79` |
| `S_4` | `step540` | `304` | `59` | `20` | `284` |
| `S_5` | `step540` | `974` | `118` | `25` | `949` |
| `S_6` | `step540` | `3041` | `238` | `27` | `3014` |
| `S_7` | non-regenerative `hybrid5` | `9346` | `494` | `51` | `9295` |

Thus one fixed two-coordinate score selects a coherent tested policy family across the recorded frontier and rejects reverse deletion everywhere.

This is a finite ranking statement. It does not establish global optimality over all complete schedules.

---

## 3. The regeneration coefficient must increase

The earlier pairwise comparison between `step5` and `hybrid5` required only

```text
0.057 < gamma < 0.058 threshold.
```

Adding the stronger regenerative policy `step540` changes the active constraint. The non-regenerative `hybrid5` policy beats `step540` exactly when

```math
\gamma>\gamma_{540},
```

with

```math
\boxed{
\frac{837}{10000}
<
\gamma_{540}
<
\frac{419}{5000}
}.
```

Therefore

```math
\frac1{16}<\gamma_{540}<\frac1{10}.
```

The exact comparisons confirm:

```text
gamma = 1/16: step540 remains cheaper
gamma = 1/10: hybrid5 becomes cheaper
```

This is the first example where enlarging the tested policy family tightens the continuation-weight requirement.

---

## 4. Favorable policy moves are not composable

Delaying step `30` by itself improves

```math
C_3=T+3O+E
```

relative to lexicographic deletion on every `S_2,...,S_7`.

However, after steps `5` and `40` are already delayed, adding step `30` makes the score worse on every `S_2,...,S_7`:

```math
C_3(\pi_{5,40,30})
>
C_3(\pi_{5,40}).
```

Thus the marginal sign of the same policy modification reverses according to the existing priority set.

Consequently, policy construction is not additive or greedily composable. A local rule cannot be selected from independent single-step improvements. Exact full-schedule recomputation or a theorem controlling policy interactions is required.

---

## 5. Consequence for the proof program

The current finite candidate score is

```math
C_{3,1/10}
=
T+3O+E+\frac1{10}G.
```

It survives the present deterministic policy family, but three gaps remain:

1. additional policy families may impose stronger half-spaces;
2. `G` is a pathwise continuation charge and still lacks a provenance-preserving retention theorem;
3. containment, partial overlap, and repeated use are not represented by these two coordinates.

The next exact task is to export every policy comparison as a rational half-space in `(lambda,gamma)` and feed the complete finite system into the LP harness. The first infeasible subsystem should identify the next missing coordinate.

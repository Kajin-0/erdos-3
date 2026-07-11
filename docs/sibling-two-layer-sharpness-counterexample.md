# Sibling two-layer sharpness counterexample

## Status

Explicit finite counterexample to the proposed one-layer sibling terminal theorem.

The sibling two-layer resolution theorem is sharp: the same terminal step can occur simultaneously in

1. a middle multiplicity-fiber child, and
2. a spanning-forest component child,

while the parent set remains four-term-progression-free.

This disproves the proposed universal claim that the relevant repeated-step sponsor fiber intersects every spanning-forest component in a three-term-progression-free set.

---

## 1. Parent set

Take

```math
N=300
```

and

```math
\begin{aligned}
D=\{&309,324,342,360,365,386,419,434,438,440,452,453,460,466,470,475,\\
&490,494,498,510,514,515,529,540,543,544,550,560,562,580,585\}.
\end{aligned}
```

A direct exhaustive check shows that `D` contains no nontrivial four-term arithmetic progression.

---

## 2. Valid side-anchor deletion sequence

For a step `q`, the coordinated orientation is

```math
\sigma(q)=
\begin{cases}
+1,&v_2(q)\equiv0\pmod2,\\
-1,&v_2(q)\equiv1\pmod2.
\end{cases}
```

A selected sponsor `a` therefore uses the progression

```math
(a,\ a+\sigma(q)q,\ a+2\sigma(q)q).
```

Delete the following sponsors in the displayed order:

| index | sponsor `a` | step `q` | selected progression |
|---:|---:|---:|---|
| 0 | 494 | 54 | `(494,440,386)` |
| 1 | 386 | 52 | `(386,438,490)` |
| 2 | 490 | 25 | `(490,515,540)` |
| 3 | 515 | 35 | `(515,550,585)` |
| 4 | 540 | 20 | `(540,560,580)` |
| 5 | 585 | 110 | `(585,475,365)` |
| 6 | 440 | 13 | `(440,453,466)` |
| 7 | 560 | 50 | `(560,510,460)` |
| 8 | 453 | 45 | `(453,498,543)` |
| 9 | 466 | 48 | `(466,514,562)` |
| 10 | 514 | 15 | `(514,529,544)` |
| 11 | 529 | 110 | `(529,419,309)` |
| 12 | 544 | 110 | `(544,434,324)` |
| 13 | 562 | 110 | `(562,452,342)` |
| 14 | 580 | 110 | `(580,470,360)` |

At every deletion, both surviving points of the selected progression are still present. Thus this is a valid side-anchor deletion sequence.

---

## 3. One spanning-forest component

Choose the following incoming forest edges:

```text
494 -> 440,386
386 -> 438,490
490 -> 515,540
515 -> 550,585
540 -> 560,580
585 -> 475,365
440 -> 453,466
560 -> 510,460
453 -> 498,543
466 -> 514,562
514 -> 529,544
529 -> 419,309
544 -> 434,324
562 -> 452,342
580 -> 470,360
```

These edges form one rooted spanning tree with root `494`. In particular, the four sponsors

```math
529,\ 544,\ 562,\ 580
```

all lie in the same spanning-forest component.

The numerical minimum of that component is

```math
m_C=309.
```

---

## 4. A repeated middle step

The last four selected progressions all have common difference

```math
r=110.
```

Since `v_2(110)=1`, their orientation is negative. Their centers are

```math
419,\ 434,\ 452,\ 470.
```

The representative center is the minimum,

```math
x_r=419,
```

corresponding to sponsor `529`.

The nonrepresentative multiplicity-fiber child is therefore

```math
\Xi_{110}
=
\{434-419,\ 452-419,\ 470-419\}
=
\{15,33,51\}.
```

This child contains the three-term progression

```math
15,\ 33,\ 51
```

with terminal step

```math
q=18.
```

---

## 5. The same terminal step in the component child

The same three nonrepresentative sponsors are

```math
544,\ 562,\ 580,
```

which form a three-term progression of step `18` inside the spanning-forest component.

After translating the component by its minimum `309`, these points become

```math
235,\ 253,\ 271.
```

Thus the component-translation child also contains a three-term progression of step

```math
q=18.
```

Therefore the same sibling terminal label `18` appears in both

```math
\Xi_{110}
```

and

```math
\Theta_C.
```

---

## 6. Consequence

This example proves that the proposed one-layer collapse is false:

```math
A_r^+\cap C^+
```

need not be three-term-progression-free.

Equivalently, a sibling terminal step can genuinely survive in two layers:

1. one middle multiplicity-fiber layer;
2. one spanning-forest component layer.

Hence the earlier two-layer sibling theorem is sharp in general.

The remaining global problem cannot be resolved by eliminating the second sibling layer universally. It must instead control how these sharp two-layer events repeat across unrelated parent states and across scales.

---

## 7. Reproducibility

The companion script

```text
src/verify_sibling_two_layer_sharpness.py
```

checks:

1. four-term-progression-freeness of `D`;
2. validity of every deletion step;
3. validity of the chosen spanning-tree edges;
4. the middle-fiber progression `{15,33,51}`;
5. the component-child progression `{235,253,271}`.

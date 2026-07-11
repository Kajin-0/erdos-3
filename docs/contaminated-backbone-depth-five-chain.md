# Contaminated-backbone cheap replication chain

## Status

Exact finite computer-assisted construction.

This note gives a depth-five chain of four-term-progression-free states in which the middle child is the previous state exactly, while the relevant backbone shell contains the previous state together with additional points. The contamination permits three scale-factor `4` steps among four outer replication steps.

The construction proves that the sharp `3/4` contraction for the exact equal-translate model does **not** extend to contaminated-backbone persistence one step at a time, or even over every fixed window of four steps.

It does not prove an infinite family with growing multiplicity-weighted density, and it does not produce a divergent reciprocal-sum counterexample.

**Verifier:** `src/verify_contaminated_backbone_depth5.py`.

---

## 1. Base state

Let

```math
H
=
\{0,1,2,16,17,18,21,22,23,26,27,28\}
```

and define

```math
L_1=64,
\qquad
S_1=L_1+H.
```

The base aligned diamond contains the terminal core

```math
C=\{16,21,26\}.
```

The step-one middle fiber is exactly `C`, and the minimum-translation backbone shell `[16,32)` contains `C`. Hence `S_1` certifiably produces at least two identical-history copies of the terminal step `5`.

Write

```math
P_1^{\mathrm{cert}}=2.
```

---

## 2. Outer recurrence

For each state `S_h subseteq[L_h,2L_h)`, put

```math
A_h=\{0\}\cup S_h
```

and form

```math
G_{h+1}
=
A_h
\cup
(A_h+R_h)
\cup
(A_h+2R_h).
```

The explicit scales and separations are

```math
(L_1,L_2,L_3,L_4,L_5)
=
(64,256,2048,8192,32768),
```

```math
(R_1,R_2,R_3,R_4)
=
(61,303,1597,8195).
```

Define

```math
S_{h+1}=L_{h+1}+G_{h+1}.
```

The dyadic scale factors are therefore

```math
\boxed{4,8,4,4.}
```

Every `R_h` has even two-adic valuation, in fact `v_2(R_h)=0`, so coordinated side-anchor deletion selects the left endpoint as sponsor.

The three translate layers are disjoint at every recorded step, giving

```math
|S_{h+1}|=3(|S_h|+1).
```

Thus

```math
|S_h|
=
\frac{9\cdot3^h-3}{2}
```

for `1<=h<=5`.

---

## 3. Why contamination still permits persistence

For one outer step, select the step-`R_h` progression

```math
a,
\quad
a+R_h,
\quad
a+2R_h
```

for every

```math
a\in A_h.
```

The selections are feasible in increasing sponsor order. When sponsor `a` is processed, the larger center and endpoint have not yet been deleted as later sponsors.

The selected centers are

```math
R_h+a,
\qquad a\in A_h.
```

Subtracting the minimum center `R_h` gives the middle multiplicity fiber

```math
\boxed{\Xi_{R_h}=S_h.}
```

Now let

```math
B_h
=
G_{h+1}\cap[L_h,2L_h)
```

be the relevant minimum-translation backbone shell. In the exact scale-eight model one has `B_h=S_h`. Here the weaker relation holds:

```math
\boxed{S_h\subseteq B_h.}
```

The extra points are not needed for the certified continuation. The full deletion schedule already verified inside `S_h` can be replayed using that subset of `B_h`; additional points do not remove any required progression.

The middle copy and the replayed backbone copy inherit the same new root anchor. Therefore every certified identical-history continuation inside `S_h` occurs in both children, and

```math
P_{h+1}^{\mathrm{cert}}
\ge
2P_h^{\mathrm{cert}}.
```

Inductively,

```math
\boxed{
P_h^{\mathrm{cert}}=2^h
}
```

is a certified lower bound. The actual persistence could be larger because the contaminating points are not exhaustively analyzed.

---

## 4. Exact finite data

| `h` | `L_h` | `|S_h|` | certified `P_h` | `P_h|S_h|/L_h` | next `R_h` | next scale factor | backbone extras |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 64 | 12 | 2 | `3/8` | 61 | 4 | 4 |
| 2 | 256 | 39 | 4 | `39/64` | 303 | 8 | 1 |
| 3 | 2048 | 120 | 8 | `15/32` | 1597 | 4 | 33 |
| 4 | 8192 | 363 | 16 | `363/512` | 8195 | 4 | 1 |
| 5 | 32768 | 1092 | 32 | `273/256` | — | — | — |

The state hashes are

```text
S1 272061e4e2d7ea7f0ea4298c69e437c87631407baea59084fc5d81e62ca5c978
S2 cff7a986bfeb8def36b5597655a585f261f8a58facdb1ee9339d72a9eaa78e37
S3 5c0b2483d958e061fdad7c963ada9b3f942286fa27e29b106fdfcba621827783
S4 14c7479efe245b72430a0505b0983be1080166fb13108228159f02b2759dd093
S5 a315deca0997d946ca9bb5058d2a04bfe3e585332d4db5260e7d9edc9142f841
```

The verifier checks every state and every raw parent for four-term-progression-freeness.

---

## 5. Failure of local weighted-density contraction

Define the certified multiplicity-weighted density

```math
W_h
=
P_h^{\mathrm{cert}}
\frac{|S_h|}{L_h}.
```

The recorded values are

```math
W_1=\frac38,
\quad
W_2=\frac{39}{64},
\quad
W_3=\frac{15}{32},
\quad
W_4=\frac{363}{512},
\quad
W_5=\frac{273}{256}.
```

Consequently

```math
\boxed{
\frac{W_5}{W_1}
=
\frac{91}{32}
=2.84375.
}
```

The individual outer-step ratios are

```math
\frac{W_2}{W_1}=\frac{13}{8},
\qquad
\frac{W_3}{W_2}=\frac{10}{13},
\qquad
\frac{W_4}{W_3}=\frac{121}{80},
\qquad
\frac{W_5}{W_4}=\frac{182}{121}.
```

Thus three of the four outer steps increase weighted density, and the complete four-step segment increases it by almost a factor of three.

For a disjoint three-translate step with dyadic scale factor

```math
c_h=\frac{L_{h+1}}{L_h},
```

the exact ratio is

```math
\boxed{
\frac{W_{h+1}}{W_h}
=
\frac{6}{c_h}
\left(1+\frac1{|S_h|}\right).
}
```

A factor-four step therefore expands this quantity by slightly more than `3/2`. The one factor-eight step in this chain does not compensate for the three factor-four steps.

---

## 6. Consequences

The construction rules out the following proposed extensions of the exact-model theorem:

1. a universal one-step bound `W_{h+1}<=3W_h/4` for contaminated backbone shells;
2. any universal strict one-step contraction based only on binary persistence, three support layers, and dyadic shelling;
3. a theorem asserting contraction over every block of four consecutive replication steps;
4. a near-exact/defective dichotomy in which every non-exact step automatically pays a stronger local contraction.

The exact scale-eight theorem remains correct under its stated hypothesis `B_h=S_h`. The new chain operates outside that hypothesis because only containment `S_h subseteq B_h` is required.

---

## 7. Revised active bottleneck

The next theorem must be a **long-run compensation theorem**, not a local contraction theorem.

A useful target is to prove that every sufficiently long contaminated-backbone genealogy satisfies one of the following:

1. the cumulative dyadic scale expansion eventually exceeds the `6`-per-level threshold needed to offset `3`-for-`2` replication;
2. contamination creates additional lower-scale difference structure that can be exported and charged;
3. repeated cheap scale factors force a four-term progression;
4. the genealogy enters a finite structural class whose long-run spectral growth can be bounded.

Ignoring the lower-order `+1` in the cardinality recurrence, contraction over `H` steps requires

```math
\prod_{h=1}^{H}c_h
>
6^H.
```

The present chain has

```math
\prod_{h=1}^{4}c_h
=4\cdot8\cdot4\cdot4
=512
<
6^4
=1296.
```

Therefore compensation, if universal, must occur on a longer horizon than four steps.

The immediate computational target is to determine whether the factor pattern can be extended indefinitely, periodically, or only through bounded bursts. The immediate proof target is to identify a monotone contamination or overlap potential that forces eventual expensive recovery steps.

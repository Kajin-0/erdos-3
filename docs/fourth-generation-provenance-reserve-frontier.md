# Fourth-generation provenance-reserve frontier

## Status

Exact finite theorem for the fixed `local37` retained construction through the fourth retained generation.

The calculation uses:

- the `local37` first-generation policy;
- lexicographic coordinated deletion on every recursively continuing retained state;
- global exact-state quotienting;
- maximum-harmonic independent-set selection in each same-shell conflict component;
- original `S_7` root provenance and immediate provenance propagated pointwise.

**Verifier:** `src/verify_fourth_generation_potential_frontier.py`.

**Certificate:** `data/fourth_generation_potential_frontier_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
2c2f2103de57bd8fdcc4c32448ea9e1cf662b325e590da5e1b0758c62298c9e5
```

---

## 1. Exact fourth retained quotient

The 14 recursively continuing third-generation states contain 4,789 points. Their complete lexicographic resolutions have:

```text
selected actions = 4,120
terminal residual points = 669
raw shell occurrences = 408
raw occurrence points = 8,807
exact state classes = 103
same-shell conflict edges = 407
conflict components = 20
largest conflict component = 17
DP states examined = 126.
```

Every conflict component has a unique optimum. The fourth retained family is point-disjoint and splits as follows:

| output type | states | points |
|---|---:|---:|
| terminal, three-term-progression-free | 11 | 77 |
| recursive | 12 | 1,717 |
| total | 23 | 1,794 |

---

## 2. Recursive harmonic mass expands again

Let `H_3^rec` and `H_4^rec` denote the recursively continuing retained masses at generations three and four. Exact arithmetic gives

```math
\boxed{
\frac{2849279}{1000000}
<
\frac{H_4^{\mathrm{rec}}}{H_3^{\mathrm{rec}}}
<
\frac{8904}{3125}.
}
```

Thus

```text
2.849279 < H4_recursive / H3_recursive < 2.849280.
```

The total fourth retained output satisfies

```math
6.996249
<
\frac{H_4}{H_3^{\mathrm{rec}}}
<
6.996250.
```

Terminal output carries `59.2741%–59.2742%` of fourth retained mass, while recursive output carries `40.7258%–40.7259%`.

Terminal extraction therefore reduces the full output substantially, but the recursive branch itself still expands by almost a factor of 2.85.

---

## 3. The repeated-root reserve fails

The three-generation candidate was

```math
\Phi_g^{\mathrm{rep}}=H_g+2R_g,
```

where

```math
R_g
=
\sum_{(u,p)\in F_g\,:\,m_g(p)>1}\frac1u
```

is current descendant harmonic mass supported on root provenance labels repeated within generation `g`.

At the fourth recursive generation:

```text
recursive points = 1,717
root-provenance labels = 1,717
repeated root-provenance labels = 0
maximum root multiplicity = 1.
```

Hence

```math
R_4=0
```

and the stored reserve vanishes exactly when raw recursive mass rises. The potential ratio satisfies

```math
\boxed{
\frac{677977}{250000}
<
\frac{\Phi_4^{\mathrm{rep}}}{\Phi_3^{\mathrm{rep}}}
<
\frac{2711909}{1000000}.
}
```

Therefore

```text
2.711908 < Phi4_rep / Phi3_rep < 2.711909.
```

The repeated-root reserve was a valid finite three-level witness, but it is not an iterating potential.

Its failure mechanism is structural:

```text
repeated-root capacity is released at generation three
root multiplicity becomes one at generation four
new harmonic mass is generated without replenishing that reserve.
```

---

## 4. The immediate-depth-tail reserve also fails

The second candidate was

```math
\Phi_g^{\mathrm{tail}}=H_g+4T_g,
```

where

```math
T_g
=
\sum_{(u,i)\in F_g\,:\,\lfloor\log_2(i/u)\rfloor\ge4}\frac1u.
```

The immediate depth-four tail was nearly exhausted at generation three:

```text
T3 approximately 0.000244006596.
```

At generation four it regenerates:

```text
T4 approximately 0.917165670132.
```

Consequently,

```math
\boxed{
\frac{963661}{100000}
<
\frac{\Phi_4^{\mathrm{tail}}}{\Phi_3^{\mathrm{tail}}}
<
\frac{9636611}{1000000}.
}
```

Thus

```text
9.636610 < Phi4_tail / Phi3_tail < 9.636611.
```

Thresholded immediate-depth mass is not monotone stored capacity. It can be recreated in a later generation after appearing nearly depleted.

---

## 5. Refined terminal tokens survive through generation four

The earlier terminal token

```math
\tau(u)=(u,p)
```

has seven collisions between prior terminal sinks and fourth-generation terminal output:

```text
(61, 1,584,290)
(62, 1,584,291)
(122, 1,584,351)
(123, 1,584,352)
(147, 1,584,356)
(152, 1,584,361)
(153, 1,584,362).
```

No such token reappears in the fourth recursive family.

The refined token

```math
\boxed{\tau^+(u)=(u,p,i)}
```

with immediate provenance `i` has:

```text
zero collisions with fourth terminal output
zero collisions with fourth recursive output.
```

Adding source type and source step changes nothing further on this finite frontier. Immediate provenance remains sufficient through generation four.

This is a finite signature-survival result, not a global injectivity theorem.

---

## 6. Numerical recreation remains extensive

Ignoring provenance:

```text
73 prior terminal numerical labels reappear in fourth terminal output
31 prior terminal numerical labels reappear in fourth recursive output
6 complete earlier terminal numerical states regenerate exactly.
```

Numerical state identity is therefore unsuitable as a terminal-sink token. Root provenance removes most collisions, and immediate provenance removes every recorded collision through generation four.

---

## 7. Consequence for the proof program

The fourth generation rules out both simple candidates from the three-generation screen:

```text
H + 2 repeated-root descendant mass
H + 4 immediate depth-four descendant mass.
```

The failure modes are complementary:

```text
repeated-root reserve vanishes before the next expansion
immediate-depth reserve regenerates during the next expansion.
```

A viable potential must therefore track a quantity whose release cannot be followed by uncharged recreation. Plausible next coordinates include:

1. cumulative first-appearance provenance reuse rather than within-generation repetition;
2. path-depth or ancestor-chain capacity that persists after multiplicity disappears;
3. terminal first-appearance credit coupled to recursive output;
4. completion, rectangle, or cheap-extension exclusion generated when reserve is released;
5. a multi-transition amortized potential rather than one-step monotonicity.

The next exact task is to export all three recursive transitions into a common rational feature LP. The LP should determine whether any nonnegative combination of the current feature family survives through generation four. If infeasible, the smallest exact dual obstruction should be recorded before adding new coordinates.

This theorem is fixed-policy, fixed-retention, and finite. It does not rule out other policies, other retained quotients, nonlinear potentials, or multi-generation amortization.

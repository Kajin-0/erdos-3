# Complete factor-four exclusion from the recorded depth-ten state

## Status

Exact finite computer-assisted theorem plus elementary transport identities.

For the recorded state `S_10`, every sponsor-compatible, layer-disjoint factor-four separation produces a nontrivial four-term arithmetic progression. Therefore

```math
\boxed{N_{10,4}=0.}
```

Together with the previously proved factor-two inheritance theorem,

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

This closes the cheap-extension problem at the specific recorded state `S_10`. It does not by itself prove the whole-tree compensation theorem or the full Erdős problem.

---

## 1. Complete factor-four domain

The exact factor-four domain has

```text
maximum separation:       613454687
sponsor-compatible:       408969792
layer-disjoint:           348012826
FNV-64:                   ae1d9e1ec77b2dfb
```

The proof partitions these `348012826` layer-disjoint candidates into three disjoint certified classes:

```math
\boxed{
33026376
+
137142200
+
177844250
=
348012826.
}
```

They are:

1. the inherited lower interval;
2. candidates removed by lifted depth-nine completion support;
3. the remaining lifted-completion residual, removed by rectangle transport.

---

## 2. Inherited lower interval

The exact embedding

```math
L_{10}+(\{0\}\cup S_9)\subseteq S_{10}
```

implies

```math
L_{10}+G_R(S_9)\subseteq G_R(S_{10}).
```

The factor-four fit endpoint from `S_9` equals the factor-two fit endpoint from `S_10` plus one. Hence the complete theorem

```math
N_{9,4}=0
```

lifts to exclude every factor-four candidate satisfying

```math
R\le76583775.
```

This removes exactly

```math
33026376
```

layer-disjoint candidates.

---

## 3. Lifted completion support

Write

```math
B_9=\{0\}\cup S_9,
\qquad
S=R_9=134217729.
```

The recorded depth-ten state has the form

```math
S_{10}=L_{10}+G_S(B_9).
```

The certified depth-nine computation supplies

```text
13923661 signed three-term-progression completion coordinates
71129286 absolute completion-to-base differences.
```

Lifting these completion differences through the three embedded `B_9` copies gives

```text
354838701 lifted completion-to-base differences.
```

Testing the coefficients `R`, `2R`, and `3R` removes

```math
137142200
```

additional genuinely new candidates. The exact residual is

```math
\boxed{177844250}
```

candidates, with

```text
first separation:  97474324
last separation:   613454687
FNV-64:            00369694f2d70526.
```

This is the valid lifted-completion reduction. It is independent of the subsequently rejected exploratory anchor rule.

---

## 4. Direct rectangle support of `B_9`

For `d>0`, define

```math
P_d(B_9)=\{x:x,x+d\in B_9\}.
```

If `x,y` lie in the same pair-start fiber, then the four base points

```math
x,
\quad x+d,
\quad y,
\quad y+d
```

produce signed effective separations

```math
U=2d-(y-x)
```

and, after reversing the two pair starts,

```math
U=2d+(y-x).
```

Equivalently, the direct rectangle-support set is

```math
\mathcal R(B_9)
=
\{U>0:\mathcal F_{B_9}(U,-U;0)>0\}.
```

The exact bounded-memory verifier proves

```math
\boxed{
[1,76583776]\subseteq\mathcal R(B_9).
}
```

### Structural support

The verifier reconstructs every relevant pair-start fiber exactly. Special `R_8`-aligned families and all fibers of size at most `512` cover

```math
76581484
```

of the `76583776` effective separations.

The remaining exact zero list has

```math
2292
```

values. A deterministic witness generator, followed by independent point-membership and rectangle-equation checks, certifies

```math
2285
```

of them. The final seven have stored exact large-fiber witnesses.

Thus

```math
\boxed{
76581484+2285+7=76583776.
}
```

**Primary references:**

- `src/verify_b9_direct_rectangle_support.cpp`;
- `data/b9_direct_rectangle_support_certificate_2026-07-13.txt`;
- `data/b9_direct_rectangle_terminal7_witnesses_2026-07-13.txt`.

---

## 5. Four-ratio transport

Suppose `B` contains

```math
x,
\quad x+d,
\quad x+2d-U,
\quad x+3d-U,
```

with

```math
d>0,
\qquad
0<U<S.
```

Exact layer-word cancellation gives transport at precisely the four positive integer ratios

```math
\boxed{k=1,2,3,4.}
```

For every such `k`, both

```math
T=kS+U
```

and

```math
T=kS-U
```

produce a nontrivial four-term progression in

```math
G_T(G_S(B)).
```

There are no integer rectangle-cancellation channels with `k>=5`.

For

```math
S=R_9=134217729,
\qquad
U_{\max}=76583776,
```

the four windows are

```text
k=1:   57633953 <= T <= 210801505
k=2:  191851682 <= T <= 345019234
k=3:  326069411 <= T <= 479236963
k=4:  460287140 <= T <= 613454692.
```

They overlap and their union contains the complete residual interval

```math
[97474324,613454687].
```

Therefore every residual separation has a representation

```math
T=kR_9\pm U,
\qquad
0\le U\le76583776,
\qquad
1\le k\le4.
```

If `U>0`, the complete direct-support theorem supplies the required `B_9` rectangle. If `U=0`, the pure layer-index sumset

```math
\{0,1,2\}+k\{0,1,2\}
```

already contains a nontrivial four-term progression for every `k=1,2,3,4`.

Hence every one of the

```math
177844250
```

residual candidates is blocked.

**Primary references:**

- `src/verify_four_ratio_rectangle_transport.py`;
- `data/four_ratio_rectangle_transport_certificate_2026-07-13.txt`;
- `src/verify_s10_factor4_rectangle_closure.py`;
- `data/s10_factor4_rectangle_closure_certificate_2026-07-13.txt`.

---

## 6. Conclusion

Combining the three exact classes gives

```math
\boxed{
N_{10,4}=0.
}
```

Together with factor-two inheritance,

```math
\boxed{
N_{10,2}=N_{10,4}=0.
}
```

Thus every nonterminating continuation from the recorded `S_10` must avoid both cheap scale factors `2` and `4`.

The one-command reproduction entry point is

```bash
bash src/run_verify_s10_factor4_rectangle_closure.sh
```

---

## 7. Scope and remaining problem

This is a complete state-specific theorem at `S_10`. It is stronger than the earlier finite prefixes and replaces the invalid exploratory anchor reduction with actual structural and explicit witnesses.

It does **not** prove that every arbitrary contaminated state eventually reaches an `S_10`-type barrier. The main unresolved theorem remains treewise:

```math
W(S)
+
\sum_{S'\in\mathrm{Child}(S)}
\left(\mathfrak B(S')+\Phi(S')\right)
\le
\mathfrak B(S)+\Phi(S)
+
\text{controlled error}.
```

The new result supplies a concrete repayment mechanism:

```text
completion contamination
    plus dense inherited rectangle coverage
    -> complete elimination of factor-four debt at S_10.
```

The next conceptual task is to turn this state-specific coverage phenomenon into a normalized reserve or zero-set recurrence applicable across the branching continuation tree.

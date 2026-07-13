# Current proof program: obstruction export and whole-tree packing

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case. Claims below are proved internally or computationally certified as stated, but await independent expert review.

---

## 1. Dyadic reduction and deletion genealogy

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

one has, up to absolute constants,

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty.
```

For a four-term-progression-free block `D`, coordinated side-anchor deletion and the minimum-translation backbone give

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N,
```

and, after exact middle-multiplicity resolution,

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

Every recursive output is resolved into standard dyadic shells. For `p>=1`,

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

These facts control local multiplicity and positive moments. Reciprocal mass requires a whole-tree packing theorem.

---

## 2. Exact benchmark and contaminated obstruction

The aligned-diamond recursion has

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
```

so

```math
P_h\asymp |S_h|^{\log_3 2}.
```

The exact scale-eight family satisfies

```math
L_h=8^{h+1},
\qquad
P_h=\frac12L_h^{1/3},
```

and

```math
P_h\alpha_h\le C_0(3/4)^h,
\qquad
\sum_hP_h\alpha_h\le4C_0.
```

Thus the uncontaminated model is summable.

A certified contaminated genealogy has scale word

```math
\boxed{4,8,4,4,8,4,8,8,8}
```

through `S_10`, and

```math
\frac{W_5}{W_1}=\frac{91}{32}>1.
```

Universal one-step contraction, fixed short-window contraction, and universal two-generation recovery are false.

---

## 3. Exact factor-eight basin and Bellman debt

Every valid positive exact factor-eight child of `S_10` has a certified infinite exact continuation. The complete fan contains

```math
\boxed{408855759}
```

valid children, and every exact tail has charge

```math
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
```

For constant exact scale factor `c>6`,

```math
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac6{c-2}\right).
```

The positive cheap-step debt for `c<8` is

```math
\Delta_c
=
\frac{P(3N+4)}L\left(\frac8c-1\right).
```

Factors `2` and `4` create debt, factor `8` is neutral, and larger factors create surplus.

---

## 4. Affine obstruction language and the depth-ten barrier

Three-translate layer words reduce to exactly

```math
\boxed{34}
```

affine obstruction classes. With

```math
r_\lambda=\lambda_1-\lambda_0,
```

```math
a_\lambda=\lambda_0-2\lambda_1+\lambda_2,
```

```math
b_\lambda=\lambda_1-2\lambda_2+\lambda_3,
```

and

```math
\mathcal F_B(A,C;Q)
=
\#\{(x,d):x,x+d,x+2d-A,x+3d-(2A+C)\in B,\ d+Q\ne0\},
```

one has

```math
\Gamma_\lambda(B;R)
=
\mathcal F_B(a_\lambda R,b_\lambda R;r_\lambda R)
```

and an exact two-scale recurrence.

At `S_10`, the complete factor-four candidate domain splits as

```math
33026376+137142200+177844250=348012826.
```

Inheritance removes the first block, lifted completion support removes the second, and direct rectangle transport removes the residual interval

```math
I_{10}=[97474324,613454687].
```

For target interval `I`, define

```math
q_S(I)=\max_{T\in I}\min_{1\le k\le4}|T-kS|.
```

At the recorded residual,

```math
q_S(I_{10})=76583771,
```

while available direct support reaches `76583776`. The exact closure margin is

```math
\boxed5.
```

Therefore

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

This is a complete state-specific barrier, not a whole-tree theorem.

---

## 5. Schedule dependence and forced output

Replay catalogs enumerate alternative continuation choices, not simultaneous children.

For schedule `sigma`, define

```math
\mathcal N_\sigma(D)
=
H\left(
\left(\bigcup_q\Xi_q^\sigma\right)
\setminus\mathcal B(D)
\right).
```

Every coordinated schedule on `S_1` has zero novelty. The lexicographic `S_2` schedule has positive novelty, but another valid `S_2` schedule has zero novelty. Hence

```math
\min_\sigma\mathcal N_\sigma(S_2)=0.
```

Raw novelty is not parent-intrinsic.

A root-forced progression must be selected in every complete coordinated schedule. This gives

```math
\sum_qH(\Xi_q^\sigma)\ge\Psi(D).
```

Positive lower bounds are certified through `S_7`, but

```math
F(S)=P\Psi(S)
```

is not a standalone Bellman potential: `F(S_1)-F(S_2)<0` while the factor-four debt is positive.

---

## 6. Raw simultaneous transition frontier

The fixed-policy exporter records the complete raw simultaneous occurrence family, including schedule, shell resolution, point-level provenance, exact duplicate classes, strict containments, partial overlap, terminal-recursive overlap, and exact mass ledgers.

| parent | occurrences | state classes | duplicate classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 25 | 21 | 3 | 23 | 15 |
| `S_4` | 46 | 34 | 7 | 91 | 35 |
| `S_5` | 68 | 51 | 11 | 145 | 88 |
| `S_6` | 94 | 71 | 15 | 209 | 150 |
| `S_7` | 127 | 95 | 20 | 345 | 214 |

The payload is before any retention quotient and is not a Bellman child list.

---

## 7. Local occurrence packing

For raw recursive occurrences `C_i`, define

```math
m(u)=|\{i:u\in C_i\}|,
\qquad
M=\max_um(u).
```

Then

```math
\sum_iH(C_i)=\sum_u\frac{m(u)}u
\le
M H\left(\bigcup_iC_i\right).
```

The certified maxima through `S_7` are

```text
2,3,7,11,12,13,16.
```

The harmonic-average multiplicity remains below the certified constants `8/5`, `11/10`, or `9/8`. Worst-case multiplicity is unstable; local harmonic control does not imply bounded cross-generation reuse.

---

## 8. Terminal-fiber incidence and SCC quotient

Draw an edge

```math
q\longrightarrow u
```

when `q` and `u` are terminal steps and `u in Xi_q`.

The graph contains the cycle

```math
61\longleftrightarrow303
```

at `S_3`, persisting through `S_6`. At `S_7`, the cyclic component becomes

```math
\boxed{\{1,5,61,303,1597,8195,323640\}}.
```

Thus no strict decreasing rank of terminal labels can orient every recursive incidence.

Collapsing strongly connected components gives an acyclic condensation graph. For a component `C`, define

```math
V(C)=\sum_{u\in C}\frac1u
```

and

```math
T(C)=\sum_{(q,u)\text{ internal edge}}\frac1u.
```

For `C={61,303}` through `S_6`, `T(C)=V(C)`. At `S_7`,

```math
T(C)-V(C)
=
\frac{43727503229099}{1043823972523464}>0.
```

Therefore harmonic vertex mass alone is not sufficient component capacity.

---

## 9. Exact spectral-growth obstruction

Let `A` be the internal adjacency matrix of a cyclic component. A positive linear capacity vector satisfying

```math
Aw\le\lambda w
```

requires `lambda` at least the Perron spectral radius.

For the two-label component through `S_6`,

```math
A=
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
\rho(A)=1.
```

For the seven-label `S_7` component, the integer vector

```math
w=(43,59,31,31,14,10,26)^T
```

satisfies

```math
9Aw-23w>0
```

and

```math
8w-3Aw>0.
```

By Collatz-Wielandt,

```math
\boxed{
\frac{23}{9}<\rho(A)<\frac83.
}
```

Consequently no positive linear internal capacity is nonexpanding or even factor-two contractive on the recorded `S_7` component. External obstruction export, nonlinear capacity, or multi-generation amortization is mandatory.

---

## 10. Missing retention theorem

By `S_7`, the raw transition contains

```text
20 exact duplicate classes
345 strict containments
214 partial overlaps.
```

The missing theorem must specify:

1. which exact duplicates merge;
2. how provenance multiplicity is retained;
3. how containment and partial overlap are charged;
4. how terminal-recursive overlap is handled;
5. how SCC internal recycling is funded;
6. how imported labels are matched across generations;
7. how repeated numerical or provenance support is bounded;
8. which discarded mass becomes controlled error.

Only then may the raw payload become the `children` array of a branching LP row.

---

## 11. Active theorem

The target is a scale-compensated whole-tree inequality

```math
\boxed{
\Delta(S)
+
\sum_{S'\in\operatorname{Child}(S)}
\left(
\operatorname{Pack}(S')+
\Phi_{\rm obs}(S')
\right)
\le
\operatorname{Pack}(S)+
\Phi_{\rm obs}(S)+
\operatorname{controlled\ error}.
}
```

Here `Pack` must track provenance, overlap, SCC internal capacity, and bounded reuse. `Phi_obs` must track affine obstruction, completion, rectangle support, and target demand.

The next finite experiment should test whether

```math
\text{internal recycling}
+
\text{outgoing capacity}
\le
\text{incoming capacity}
+
\text{obstruction export}
```

holds on the certified `S_1` through `S_7` transitions.

---

## 12. Approved next targets

1. Attach explicit internal and outgoing capacity vectors to the SCC quotients.
2. Quantify export from cyclic terminal labels into nonterminal fibers and affine obstruction classes.
3. Preserve provenance while merging exact numerical state classes.
4. Introduce capacity constraints for containment and partial-overlap graphs.
5. Feed a proved retention convention into the exact rational LP harness.
6. Emit the smallest exact failing transition for each candidate convention.
7. Establish the branching Carleson inequality for all pre-basin states.

---

## 13. Superseded or false targets

Do not use without materially new hypotheses:

1. universal local `3/4` contraction;
2. fixed short-window contraction;
3. universal two-generation recovery;
4. extrapolating one path or exact fan to the full tree;
5. replay siblings as simultaneous children;
6. pathwise summability as sufficient;
7. radius without target demand;
8. raw novelty as schedule independent;
9. `P Psi` as a standalone Bellman potential;
10. raw occurrences copied directly into an LP child list;
11. exact-state quotienting as a containment solution;
12. a uniform maximum-overlap constant;
13. a strict decreasing terminal-label rank;
14. latest- or historical-separation-only state;
15. unit harmonic SCC capacity;
16. any positive linear SCC capacity with contraction factor at most two on the recorded `S_7` component;
17. the rejected depth-ten anchor reduction.

---

## 14. Reproduction

Run the complete lightweight suite:

```bash
bash src/run_verify_transport_reserve.sh
```

Run only the transition frontier:

```bash
bash src/run_verify_transition_frontier.sh
```

Key documents:

- `docs/transport-interval-capacity.md`;
- `docs/branching-reserve-lp.md`;
- `docs/simultaneous-transition-frontier-s7.md`;
- `docs/recursive-occurrence-multiplicity.md`;
- `docs/terminal-fiber-incidence-graph.md`;
- `docs/terminal-fiber-scc-quotient.md`;
- `docs/terminal-fiber-scc-spectral-growth.md`;
- `docs/certainty-ledger.md`;
- `docs/research-decision-history.md`.

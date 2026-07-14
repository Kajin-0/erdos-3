# Current proof program: scale-aware provenance packing

## Status

This is the authoritative overview of the active program for the four-term case of Erdős Problem #3. The full reciprocal-sum problem remains open. Exact theorem status is tracked in `docs/certainty-ledger.md`.

---

## 1. Foundation

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

reciprocal divergence is equivalent up to constants to

```math
\sum_j\alpha_j=\infty.
```

Coordinated side-anchor deletion and the minimum-translation backbone give

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N,
```

and

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

Every recursive output is resolved into standard dyadic shells. These are local accounting statements, not a whole-tree reciprocal-mass theorem.

---

## 2. Exact recorded path

The uncontaminated equal-translate model is summable:

```math
P_h\alpha_h\le C_0(3/4)^h.
```

The certified contaminated path reaches `S_10` with scale word

```text
4,8,4,4,8,4,8,8,8
```

and has `W_5/W_1=91/32>1`, disproving universal local and fixed-window contraction.

At `S_10`, inheritance, lifted completion support, and direct rectangle transport prove

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

Every valid exact factor-eight child has a certified summable exact tail. This closes the recorded state, not the full deletion tree.

---

## 3. Raw simultaneous-output obstruction

The lexicographic raw transition frontier is certified through `S_7`.

| parent | occurrences | state classes | duplicate classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 25 | 21 | 3 | 23 | 15 |
| `S_4` | 46 | 34 | 7 | 91 | 35 |
| `S_5` | 68 | 51 | 11 | 145 | 88 |
| `S_6` | 94 | 71 | 15 | 209 | 150 |
| `S_7` | 127 | 95 | 20 | 345 | 214 |

Replay siblings are alternative choices, not simultaneous Bellman children.

Lexicographic `S_7` also contains the cyclic terminal-fiber component

```math
C=\{1,5,61,303,1597,8195,323640\},
\qquad
\frac{23}{9}<\rho(A)<\frac83.
```

Its numerically deduplicated output/input harmonic ratio exceeds `7/5`. Raw output is recursive load, not stored repayment.

---

## 4. Policy optimization

Lexicographic deletion produces the isolated return

```math
\{16,21,26\}\xrightarrow[f=4]{R=1}S_1
```

with recorded continuation charge

```math
G=\frac{36953}{4096}.
```

The finite policy score is

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi,
```

with exact witness

```math
\boxed{\lambda=3,\qquad\gamma=\frac1{10}}.
```

The complete five-step subset lattice `{5,40,30,161,142}` is certified through `S_7`, including both seed-delay modes and reverse deletion. The resulting policy LP has `250` exact inequalities and the witness satisfies every row. Its five-step `S_7` winner is the non-regenerative policy `seed_5_142`.

A broader deterministic search gives a seed-delayed `S_7` policy with `37` delayed progression steps:

```text
selected actions = 9,323
terminal residual = 517
terminal step classes = 28
middle-fiber occurrences = 9,295
canonical regeneration = false.
```

Within its exact 59-toggle terminal/delayed neighborhood it has no improving move. The minimum strict slack is

```math
\boxed{\frac{384}{111292259161}}.
```

This is local optimality in the stated neighborhood, not global schedule optimality.

---

## 5. Raw transition of the local optimum

| coordinate | lexicographic | five-step winner | local optimum |
|---|---:|---:|---:|
| terminal step classes | 25 | 50 | 28 |
| shell occurrences | 127 | 227 | 131 |
| exact state classes | 95 | 144 | 87 |
| duplicate groups | 20 | 45 | 22 |
| strict containments | 345 | 1,028 | 229 |
| partial overlaps | 214 | 1,180 | 390 |
| maximum point multiplicity | 16 | 34 | 18 |
| cyclic terminal-fiber SCCs | 1 | 1 | **0** |

The local policy removes the recorded SCC and cuts complete recursive occurrence mass to between `25.4%` and `25.5%` of the lexicographic value. It still has substantial duplicate, containment, and overlap structure.

---

## 6. Provenance-preserving retention

The local-optimum raw family is reduced by a deterministic rule:

1. quotient exact numerical duplicate states;
2. choose representatives by backbone first, then source step, then raw occurrence index;
3. connect exact state classes that intersect within the same dyadic shell;
4. solve every conflict component for a maximum-harmonic independent set.

The exact graph has `87` state classes, `290` edges, `20` components, and largest component `13`. Every component has a unique optimum.

The first retained family has

```text
retained state classes = 21
retained distinct labels = 11,753
dropped distinct labels = 5,018.
```

The retained states are pairwise point-disjoint and carry explicit representative provenance. Their harmonic mass is between `73.1%` and `73.2%` of the raw numerical-union mass.

The 21 retained states are then resolved by lexicographic coordinated deletion and the same quotient is applied globally. The second retained family has

```text
retained state classes = 27
retained distinct labels = 7,925
dropped distinct labels = 5,900.
```

Original `S_7` root provenance has multiplicity spectrum

| multiplicity | provenance labels |
|---:|---:|
| 1 | 7,376 |
| 2 | 267 |
| 3 | 5 |

Repeated-provenance harmonic overhead is only between `4.0%` and `4.1%` of unique-provenance mass, yet

```math
\frac{6828}{1000}
<
\frac{H_{\rm retained}^{(2)}}{H_{\rm retained}^{(1)}}
<
\frac{6829}{1000}.
```

Bounded multiplicity alone is therefore not a Bellman coordinate.

---

## 7. Exact scale-concentration theorem

For each of the `7,925` retained descendant points `u`, the new certificate records its original root-provenance label `p`, immediate provenance, source, source step, and shell.

Define

```math
d_-(p,u)=\left\lfloor\log_2\frac pu\right\rfloor,
\qquad
d_+(p,u)=\left\lceil\log_2\frac pu\right\rceil.
```

The pointwise contraction range is

```math
\frac{505417}{112004}
\le
\frac pu
\le
1354066.
```

### Unit depth charges fail

Let `D=H_2-H_1` be the intergeneration retained-mass debt. Exact arithmetic gives

```math
86
<
\frac{D}{\sum d_{\rm shell}(p,u)/p}
<
87,
```

```math
99
<
\frac{D}{\sum d_-(p,u)/p}
<
100,
```

and even

```math
77
<
\frac{D}{\sum d_+(p,u)/p}
<
78.
```

Thus unit dyadic-depth and logarithmic charges fail by large factors. Even the optimistic ceil-log charge would need coefficient greater than `77` on this transition.

### Repeated provenance contains the dangerous tail

There are `272` repeated root labels, producing `549` retained occurrences. The remaining `7,376` occurrences have unique root provenance.

The exact implication is

```math
d_-(p,u)\ge8
\quad\Longrightarrow\quad
p\text{ is repeated provenance}.
```

Repeated provenance carries only

```math
0.076
<
\frac{H_{\rm root,repeat}}{H_{\rm root,all}}
<
0.077
```

of occurrence-weighted root mass, but produces

```math
0.948
<
\frac{H_{\rm descendant,repeat}}{H_2}
<
0.949
```

of second retained harmonic mass.

Its descendant/root expansion lies between `4928` and `4929`; unique provenance expansion lies only between `22` and `23`.

The scale tail is extremely concentrated:

```math
0.943
<
\frac{H_2[d_-\ge8]}{H_2}
<
0.944,
```

```math
0.698
<
\frac{H_2[d_-\ge16]}{H_2}
<
0.699.
```

A single repeated-provenance point with `u=1`, `p=1,354,066`, and `d_-=20` contributes between `51.2%` and `51.3%` of the entire second retained harmonic mass.

The dangerous mechanism is therefore

```text
repeated provenance × extreme scale contraction.
```

Primary references:

- `docs/retained-provenance-scale-profile.md`;
- `docs/retained-provenance-second-generation.md`;
- `docs/s7-provenance-retained-quotient.md`.

---

## 8. Active theorem

The required whole-tree inequality remains

```math
\boxed{
\Delta(S)
+
\sum_{S'\in\operatorname{Child}_\pi(S)}
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

Within-generation point-disjoint retention is solved for the adversarial transition. Two-generation root-provenance reuse and scale ratios are now exact. The next coordinate must be **jointly provenance- and scale-sensitive**.

A natural finite feature family is

```math
R_k
=
\sum_{(p,u)}
\frac{\mathbf 1_{\{m(p)>1\}}\mathbf 1_{\{d_-(p,u)\ge k\}}}{u},
```

or a root-weighted stored-capacity analogue whose release occurs only after repeated provenance crosses depth `k`. This is a candidate family, not yet a theorem. It must be shown to be stored at the parent, released at most once, and compatible with completion or cheap-extension exclusion.

---

## 9. Approved next targets

1. Add exact repeated-provenance depth-tail coordinates `R_k` to the rational LP harness, starting with `k=8,16,20`.
2. Separate stored root capacity from released descendant charge so the same repeated provenance cannot pay more than once.
3. Attach completion, rectangle, or future cheap-extension exclusion credit to the extreme-contraction descendants.
4. Export the first genuine two-generation retained-child Bellman row.
5. Test the scale-aware feature family on another exact parent transition or extract the smallest exact failure.
6. Prove a branching Carleson inequality or identify the next missing coordinate.

---

## 10. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- one-toggle local optimality implies global policy optimality;
- acyclic terminal-fiber incidence implies disjoint retained children;
- lower raw harmonic occurrence mass implies Bellman contraction;
- exact duplicate quotienting alone resolves all overlap;
- one-generation point-disjoint retention bounds indefinite provenance reuse;
- maximum provenance multiplicity three implies contraction;
- low provenance-overhead mass pays for scale-driven harmonic growth;
- unit dyadic-depth or logarithmic charge repays the retained-mass debt;
- a coefficient above `77` is globally legitimate merely because it fits this transition;
- all repeated provenance is dangerous, or all unique provenance is harmless, outside the recorded family;
- maximum-harmonic local retention is globally Bellman-optimal;
- policy-LP feasibility implies Bellman-LP feasibility;
- the recorded continuation charge is justified without scale-aware packing;
- one finite witness proves an all-policy theorem.

---

## 11. Reproduction

Push-gating lightweight suite:

```bash
bash src/run_verify_ci_lightweight.sh
```

Complete extended suite:

```bash
bash src/run_verify_transport_reserve.sh
```

Standalone scale-profile check:

```bash
python3 src/run_exact_python.py \
  src/verify_retained_provenance_scale_profile.py \
  /tmp/retained_provenance_scale_profile_certificate.txt
```

Current detailed notes:

- `docs/certainty-ledger.md`;
- `docs/retained-provenance-scale-profile.md`;
- `docs/retained-provenance-second-generation.md`;
- `docs/s7-provenance-retained-quotient.md`;
- `docs/s7-local-optimum-transition-profile.md`;
- `docs/s7-terminal-step-local-optimum.md`;
- `docs/branching-reserve-lp.md`.

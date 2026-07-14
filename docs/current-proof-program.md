# Current proof program: policy-aware whole-tree packing

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

## 4. Policy coordinates and finite optimization

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

The full five-step lattice `{5,40,30,161,142}` is certified through `S_7`. The resulting policy LP has `250` exact inequalities and the witness satisfies every row.

A broader deterministic search gives a seed-delayed `S_7` policy with `37` delayed steps:

```text
selected actions = 9323
terminal residual = 517
terminal step classes = 28
middle-fiber occurrences = 9295
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

## 6. First provenance-preserving retained quotient

The local-optimum raw family is reduced by a deterministic rule:

1. quotient exact numerical duplicate states;
2. choose representatives by backbone first, then source step, then raw occurrence index;
3. connect exact state classes that intersect within the same dyadic shell;
4. solve every conflict component for a maximum-harmonic independent set.

Exact results:

```text
raw shell occurrences = 131
exact state classes = 87
conflict edges = 290
conflict components = 20
largest component = 13
components with nonunique optimum = 0.
```

The unique retained family has

```text
retained state classes = 21
retained distinct labels = 11,753
dropped distinct labels = 5,018.
```

The retained states are pairwise point-disjoint and carry explicit representative provenance. Their harmonic mass is between `73.1%` and `73.2%` of the raw numerical-union mass.

This is the first legitimate one-generation retained-child quotient in the program.

---

## 7. Second-generation provenance reuse

The 21 retained states are resolved by lexicographic coordinated deletion. Their descendant occurrences are aggregated globally and the same quotient is applied again.

```text
child selected actions = 10,426
child terminal residual points = 1,327
raw descendant shell occurrences = 442
exact descendant state classes = 173
conflict edges = 1,046
conflict components = 22
largest component = 21.
```

Every component again has a unique optimum. The second retained family has

```text
retained state classes = 27
retained distinct labels = 7,925
dropped distinct labels = 5,900.
```

### Provenance reuse

The 7,925 retained descendant points use 7,648 distinct original `S_7` provenance labels.

| multiplicity | provenance labels |
|---:|---:|
| 1 | 7,376 |
| 2 | 267 |
| 3 | 5 |

Thus maximum provenance multiplicity is `3`. The repeated-provenance harmonic overhead is only between `4.0%` and `4.1%` of unique-provenance mass.

### Harmonic scale expansion

Despite that small reuse overhead,

```math
\frac{6828}{1000}
<
\frac{H_{\rm retained}^{(2)}}{H_{\rm retained}^{(1)}}
<
\frac{6829}{1000}.
```

The retained harmonic mass expands by approximately `6.82863`.

This separates the two mechanisms:

```text
provenance reuse: modest in this finite propagation
scale-driven harmonic growth: large.
```

Bounded multiplicity alone is therefore not a Bellman coordinate.

Primary references:

- `docs/retained-provenance-second-generation.md`;
- `docs/s7-provenance-retained-quotient.md`;
- `docs/s7-local-optimum-transition-profile.md`.

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

Within-generation point-disjoint retention is solved for the adversarial transition, and one-step root-provenance reuse is exactly bounded in its first propagation. The remaining coordinate must couple provenance with **scale contraction and obstruction credit**.

A plausible state variable must distinguish a retained point at label `u` from the much larger root provenance label `p` that generated it. Candidate charges include:

```math
\log_2(p/u),
\qquad
\frac{p}{u},
\qquad
\text{dyadic depth drop},
```

combined with completion or cheap-extension exclusion. These are candidates only; none is yet a theorem.

---

## 9. Approved next targets

1. Export the exact root-provenance-to-descendant scale ratios for all 7,925 second-generation retained points.
2. Test dyadic depth-drop and logarithmic scale charges against the `6.828`–`6.829` harmonic expansion.
3. Identify whether repeated provenance concentrates at small depth drops or large contractions.
4. Add the first scale-aware provenance coordinate to the rational LP harness.
5. Export a genuine two-generation retained-child Bellman row.
6. Prove a branching Carleson inequality or extract the smallest exact failure.

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

Standalone second-generation check:

```bash
python3 src/run_exact_python.py \
  src/verify_retained_provenance_second_generation.py \
  /tmp/retained_provenance_second_generation_certificate.txt
```

Current detailed notes:

- `docs/certainty-ledger.md`;
- `docs/retained-provenance-second-generation.md`;
- `docs/s7-provenance-retained-quotient.md`;
- `docs/s7-local-optimum-transition-profile.md`;
- `docs/s7-terminal-step-local-optimum.md`;
- `docs/branching-reserve-lp.md`.

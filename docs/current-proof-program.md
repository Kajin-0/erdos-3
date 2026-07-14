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

## 2. Exact benchmark and recorded closure

The uncontaminated equal-translate model is summable:

```math
P_h\alpha_h\le C_0(3/4)^h.
```

The certified contaminated path reaches `S_10` with scale word

```text
4,8,4,4,8,4,8,8,8
```

and satisfies

```math
\frac{W_5}{W_1}=\frac{91}{32}>1.
```

Universal local contraction, fixed short-window contraction, and universal two-generation recovery are false.

At `S_10`, inheritance, lifted completion support, and direct rectangle transport exclude every factor-two and factor-four candidate:

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

The exact transport closure margin is `5`. Every valid exact factor-eight child has a certified summable exact tail. This closes the recorded state, not the full deletion tree.

---

## 3. Raw transition obstruction

The lexicographic raw simultaneous transition frontier is certified through `S_7`.

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

At lexicographic `S_7`, the terminal-fiber graph contains

```math
C=\{1,5,61,303,1597,8195,323640\},
```

with

```math
\frac{23}{9}<\rho(A)<\frac83.
```

Its numerically deduplicated output/input harmonic ratio exceeds `7/5`. Local and affine obstruction export is substantial but incomplete. A provenance-preserving retention quotient remains missing.

---

## 4. Regeneration and policy coordinates

Lexicographic deletion produces the isolated child

```math
\{16,21,26\}\xrightarrow[f=4]{R=1}S_1
```

with recorded continuation charge

```math
G=\frac{36953}{4096}.
```

The seed-producing actions are not root-forced. Reverse deletion avoids the return but creates severe terminal, cyclic, and duplicate load.

The current finite policy score is

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi,
```

where `T` is terminal-step harmonic mass, `O` is middle-fiber occurrence mass, `E` is normalized residual error, and `G` is the recorded regenerative continuation charge.

The current exact witness is

```math
\boxed{\lambda=3,\qquad\gamma=\frac1{10}}.
```

The continuation coordinate is necessary, and favorable local priority changes are not greedily composable.

---

## 5. Full five-step policy lattice

All `32` subsets of

```text
{5,40,30,161,142}
```

are certified on `S_1,...,S_7`; all `32` seed-delayed versions and reverse deletion are also included on `S_7`.

The exact policy-ranking LP contains

```text
250 rational constraints
2 features: lambda, gamma
47 active equalities at the witness.
```

The witness `(3,1/10)` satisfies every row. Representative selected policies are:

| state | selected policy |
|---:|---|
| `S_1` | `plain_none`, representative of a tie |
| `S_2` | `plain_5`, representative of a tie |
| `S_3` | `plain_5_161_142`, unique |
| `S_4` | `plain_5_40`, modulo inactive ties |
| `S_5` | `plain_5_40`, modulo inactive ties |
| `S_6` | `plain_5_40`, modulo inactive ties |
| `S_7` | `seed_5_142`, unique in this lattice |

This completes the explicit five-step subset lattice, not arbitrary policy search.

---

## 6. Exact S7 terminal-step local optimum

A deterministic search outside the five-step lattice produced a seed-delayed policy with `37` delayed progression steps. The final theorem independently recomputes the policy and every neighbor with exact rational arithmetic.

Complete resolution gives

```text
selected actions = 9323
terminal residual = 517
terminal step classes = 28
middle-fiber occurrences = 9295
canonical regeneration = false.
```

Its exact one-toggle neighborhood is the union of its terminal-step set and delayed-step set, containing `59` labels. The result is

```text
improving toggles = 0
zero-slack toggles = 384, 323640
strictly worsening toggles = 57.
```

The smallest strict slack is

```math
\boxed{\frac{384}{111292259161}}
```

at toggle `333432`.

Relative to the five-step-lattice winner,

```math
\frac{1915}{1000}
<
C_{3,1/10}(\texttt{seed\_5\_142})-C_{3,1/10}(\pi_*)
<
\frac{1916}{1000}.
```

This is exact local optimality only in the stated neighborhood.

---

## 7. Raw transition of the local optimum

The complete raw occurrence family of the local optimum is compared with lexicographic deletion and `seed_5_142`.

| coordinate | lexicographic | `seed_5_142` | local optimum |
|---|---:|---:|---:|
| terminal step classes | 25 | 50 | 28 |
| shell occurrences | 127 | 227 | 131 |
| exact state classes | 95 | 144 | 87 |
| duplicate groups | 20 | 45 | 22 |
| strict containments | 345 | 1,028 | 229 |
| partial overlaps | 214 | 1,180 | 390 |
| maximum point multiplicity | 16 | 34 | 18 |
| terminal-fiber incidence edges | 75 | 141 | 83 |
| cyclic SCCs | 1 | 1 | **0** |
| largest SCC | 7 | 2 | **1** |

The local-optimum terminal-fiber graph is acyclic.

Its middle-fiber occurrence mass satisfies

```math
\frac{247}{1000}
<
\frac{O_{\rm mid}^{\rm local}}{O_{\rm mid}^{\rm lex}}
<
\frac{248}{1000},
```

and its complete recursive shell occurrence mass satisfies

```math
\frac{254}{1000}
<
\frac{O_{\rm raw}^{\rm local}}{O_{\rm raw}^{\rm lex}}
<
\frac{255}{1000}.
```

Thus the optimized policy eliminates the recorded SCC obstruction and sharply lowers harmonic occurrence load. It still does not produce a disjoint family: relative to lexicographic deletion, partial overlaps rise from `214` to `390` and maximum point multiplicity rises from `16` to `18`.

This mixed profile is now the principal adversarial test for retention.

Primary references:

- `docs/s7-terminal-step-local-optimum.md`;
- `docs/s7-local-optimum-transition-profile.md`;
- `docs/policy-subset-lattice-s1-s7.md`.

---

## 8. Active theorem

The required whole-tree object remains

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

Policy optimization can remove cyclic terminal-label reuse and reduce raw harmonic load, but exact duplicates, containment, partial overlap, and point multiplicity remain. The dominant missing theorem is a provenance-preserving retention quotient.

---

## 9. Approved next targets

1. Define a deterministic retained-child rule on shell occurrences with explicit point provenance.
2. Test exact-duplicate quotienting followed by containment pruning on `S_1,...,S_7` and the local-optimum transition.
3. Measure the remaining partial-overlap conflict graph and exact retained harmonic mass.
4. Prove bounded provenance reuse or extract the smallest exact counterexample.
5. Add the required packing coordinate to the rational LP harness.
6. Export the first legitimate retained-child Bellman row.
7. Establish a policy-aware or minimax branching Carleson inequality.

---

## 10. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- raw novelty is schedule-independent;
- one-generation affine coverage repays cyclic output;
- canonical regeneration is forced by `S_7`;
- avoiding regeneration makes a policy cheaper;
- raw occurrence or distinct-label count ranks policies correctly;
- locally favorable policy moves compose greedily;
- one-toggle local optimality implies global policy optimality;
- acyclic terminal-fiber incidence implies disjoint retained children;
- lower harmonic occurrence mass implies a Bellman contraction;
- exact duplicate quotienting alone resolves containment or partial overlap;
- policy-LP feasibility implies Bellman-LP feasibility;
- adding the recorded path charge is justified without retention;
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

Standalone local-optimum checks:

```bash
python3 src/run_exact_python.py \
  src/verify_s7_terminal_step_local_optimum.py \
  /tmp/s7_terminal_step_local_optimum_certificate.txt

python3 src/run_exact_python.py \
  src/verify_s7_local_optimum_transition_profile.py \
  /tmp/s7_local_optimum_transition_profile_certificate.txt
```

Current detailed notes:

- `docs/certainty-ledger.md`;
- `docs/s7-terminal-step-local-optimum.md`;
- `docs/s7-local-optimum-transition-profile.md`;
- `docs/policy-subset-lattice-s1-s7.md`;
- `docs/s7-cyclic-scc-output-load.md`;
- `docs/branching-reserve-lp.md`.

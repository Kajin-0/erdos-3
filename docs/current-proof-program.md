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

## 3. Why raw simultaneous output is insufficient

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

## 4. Policy coordinates and exact finite search

Lexicographic deletion produces the isolated return

```math
\{16,21,26\}\xrightarrow[f=4]{R=1}S_1
```

with recorded continuation charge

```math
G=\frac{36953}{4096}.
```

The current finite policy score is

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi,
```

with exact witness

```math
\boxed{\lambda=3,\qquad\gamma=\frac1{10}}.
```

The continuation coordinate is necessary, and favorable local priority changes are not greedily composable.

The full five-step lattice `{5,40,30,161,142}` is certified through `S_7`, including all seed-delayed versions on `S_7`. The exact policy LP has `250` rational inequalities and the witness satisfies every row.

---

## 5. Exact S7 local policy optimum

A deterministic search outside the five-step lattice produced a seed-delayed policy with `37` delayed progression steps. Exact recomputation gives

```text
selected actions = 9323
terminal residual = 517
terminal step classes = 28
middle-fiber occurrences = 9295
canonical regeneration = false.
```

Its exact one-toggle neighborhood is the union of its terminal and delayed step sets, containing `59` labels:

```text
improving toggles = 0
zero-slack toggles = 384, 323640
strictly worsening toggles = 57.
```

The minimum strict slack is

```math
\boxed{\frac{384}{111292259161}}
```

at toggle `333432`.

This is local optimality in the stated neighborhood, not global schedule optimality.

---

## 6. Raw transition of the local optimum

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

The local policy removes the recorded SCC and cuts complete recursive occurrence mass to between `25.4%` and `25.5%` of the lexicographic value. It still has substantial exact duplicates, containment, and partial overlap.

---

## 7. First provenance-preserving retained-child quotient

The local-optimum raw family is converted into a legitimate one-generation retained family by the following deterministic rule:

1. quotient exact numerical duplicate states;
2. retain a representative ordered by backbone first, then source step, then raw occurrence index;
3. connect exact state classes that intersect numerically within the same dyadic shell;
4. solve each conflict component for a maximum-harmonic independent set.

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
backbone representatives = 2
middle-fiber representatives = 19
retained distinct labels = 11,753
dropped distinct labels = 5,018.
```

The retained states are pairwise point-disjoint and every retained point has explicit representative provenance.

Its harmonic mass satisfies

```math
\frac{731}{1000}
<
\frac{H_{\rm ret}}{H_{\rm raw\ union}}
<
\frac{732}{1000},
```

and

```math
\frac{582}{1000}
<
\frac{H_{\rm ret}}{H_{\rm raw\ occurrences}}
<
\frac{583}{1000}.
```

This is the first certified one-generation retained-child quotient in the program. It resolves duplicate, containment, and partial-overlap conflicts for this recorded transition.

Primary references:

- `docs/s7-provenance-retained-quotient.md`;
- `docs/s7-local-optimum-transition-profile.md`;
- `docs/s7-terminal-step-local-optimum.md`.

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

Within-generation retention is now solved for the adversarial local-optimum transition. The unresolved issue is **cross-generation provenance reuse**: a parent or sponsor label chosen as provenance may reappear in retained descendants and be charged repeatedly.

The next theorem must establish a Carleson-type bound on retained provenance, or produce the smallest exact reuse cycle that requires another packing coordinate.

---

## 9. Approved next targets

1. Propagate the 21 retained states one generation with their representative provenance labels.
2. Apply the same exact duplicate quotient and conflict selection to every retained child transition that is computationally tractable.
3. Build the provenance-reuse graph from parent/sponsor labels to retained descendant representatives.
4. Prove bounded reuse, or extract the smallest exact directed cycle or multiplicity blow-up.
5. Add the resulting provenance-capacity coordinate to the rational LP harness.
6. Export the first legitimate retained-child Bellman row.
7. Establish a policy-aware branching Carleson inequality.

---

## 10. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- raw novelty is schedule-independent;
- one-generation affine coverage repays cyclic output;
- one-toggle local optimality implies global policy optimality;
- acyclic terminal-fiber incidence implies disjoint retained children;
- lower raw harmonic occurrence mass implies Bellman contraction;
- exact duplicate quotienting alone resolves all overlap;
- one-generation point-disjoint retention bounds cross-generation reuse;
- maximum-harmonic local retention is globally Bellman-optimal;
- policy-LP feasibility implies Bellman-LP feasibility;
- the recorded continuation charge is justified without cross-generation packing;
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

Standalone retained quotient:

```bash
python3 src/run_exact_python.py \
  src/verify_s7_provenance_retained_quotient.py \
  /tmp/s7_provenance_retained_quotient_certificate.txt
```

Current detailed notes:

- `docs/certainty-ledger.md`;
- `docs/s7-provenance-retained-quotient.md`;
- `docs/s7-local-optimum-transition-profile.md`;
- `docs/s7-terminal-step-local-optimum.md`;
- `docs/policy-subset-lattice-s1-s7.md`;
- `docs/branching-reserve-lp.md`.

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

## 2. Exact benchmark and contaminated obstruction

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

For exact scale factor `c>6`,

```math
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac6{c-2}\right),
```

with cheap-step debt

```math
\Delta_c
=
\frac{P(3N+4)}L\left(\frac8c-1\right).
```

---

## 3. Finished state-specific theorem

At `S_10`, inheritance, lifted completion support, and direct rectangle transport exclude every factor-two and factor-four candidate:

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

The exact transport closure margin is `5`. Every valid exact factor-eight child has a certified summable exact tail. This closes the recorded state, not the full deletion tree.

---

## 4. Raw transition and retention obstruction

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

At `S_7`, the terminal-fiber graph contains

```math
C=\{1,5,61,303,1597,8195,323640\},
```

with

```math
\frac{23}{9}<\rho(A)<\frac83.
```

The component emits `6,020` distinct novel labels, and its numerically deduplicated output/input harmonic ratio exceeds `7/5`. Local and affine obstruction export is substantial but incomplete. A provenance-preserving retention quotient remains missing.

---

## 5. Regeneration and policy coordinates

Under lexicographic deletion, the isolated child

```math
X=\{16,21,26\}\subset[16,32)
```

satisfies

```math
X\xrightarrow[f=4]{R=1}S_1.
```

Its recorded continuation charge is

```math
G=\frac{36953}{4096}.
```

The seed-producing actions are not root-forced. Reverse lexicographic deletion avoids the return but creates severe terminal, cyclic, and duplicate load. Avoiding a recognizable descendant is not a sufficient policy objective.

The current finite policy score is

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi,
```

where `T` is terminal-step harmonic mass, `O` is middle-fiber occurrence mass, `E` is normalized residual error, and `G` is the recorded regenerative continuation charge.

The exact witness used throughout the current finite frontier is

```math
\boxed{
\lambda=3,
\qquad
\gamma=\frac1{10}.
}
```

The continuation coordinate is necessary: `T+3O+E` alone prefers a policy retaining the canonical return. Favorable local priority changes are not greedily composable.

---

## 6. Full five-step policy subset lattice through S7

The delayed-step universe

```text
{5,40,30,161,142}
```

is exhausted on `S_1,...,S_7`, with all `32` seed-delayed versions and reverse deletion added on `S_7`.

The resulting policy-ranking LP contains

```text
250 exact rational constraints
2 features: lambda, gamma
47 active equalities at the witness.
```

The rational LP harness verifies `(lambda,gamma)=(3,1/10)` against every row.

Representative selected policies are:

| state | selected policy |
|---:|---|
| `S_1` | `plain_none`, representative of a complete tie |
| `S_2` | `plain_5`, representative of an eight-policy tie |
| `S_3` | `plain_5_161_142`, unique |
| `S_4` | `plain_5_40`, modulo inactive-step ties |
| `S_5` | `plain_5_40`, modulo inactive-step ties |
| `S_6` | `plain_5_40`, modulo inactive-step ties |
| `S_7` | `seed_5_142`, unique in this lattice |

The five-step `S_7` winner is non-regenerative. Its advantage over `seed_5` is approximately `0.0015010996`.

This completes the explicit five-step subset lattice. It does not establish optimality over arbitrary delayed steps or all complete coordinated schedules.

---

## 7. Exact S7 terminal-step local optimum

A deterministic coordinate search outside the five-step lattice produced a seed-delayed policy with `37` delayed progression steps. The theorem does not rely on the search arithmetic: the final policy and its neighborhood are recomputed exactly.

Complete coordinated resolution gives

```text
selected actions = 9323
terminal residual = 517
terminal step classes = 28
middle-fiber occurrences = 9295
canonical regeneration = false.
```

The exact one-toggle neighborhood is

```math
\mathcal Q
=
\{\text{terminal steps}\}
\cup
\{\text{delayed steps}\},
```

with `|Q|=59`. Every toggle is resolved as a complete schedule and scored exactly.

The result is

```text
improving toggles = 0
zero-slack toggles = 384, 323640
strictly worsening toggles = 57.
```

The smallest strict positive slack is

```math
\boxed{
\frac{384}{111292259161}
}
```

at toggle `333432`. Thus the local certificate is close at one boundary but exact.

Relative to the five-step-lattice winner,

```math
\frac{1915}{1000}
<
C_{3,1/10}(\texttt{seed\_5\_142})
-
C_{3,1/10}(\pi_*)
<
\frac{1916}{1000}.
```

The new policy reduces terminal step classes from `50` to `28` and remains non-regenerative.

This is only a local optimum in the explicit 59-toggle neighborhood. It is not a global policy theorem.

Primary references:

- `docs/s7-terminal-step-local-optimum.md`;
- `docs/policy-subset-lattice-s1-s7.md`;
- `docs/expanded-policy-subset-lp.md`;
- `docs/policy-halfspace-lp.md`.

---

## 8. Active theorem

The required whole-tree object remains

```math
\boxed{
\Delta(S)
+
\sum_{S'\in\mathrm{Child}_\pi(S)}
\left(
\mathrm{Pack}(S')+
\Phi_{\rm obs}(S')
\right)
\le
\mathrm{Pack}(S)+
\Phi_{\rm obs}(S)+
\mathrm{controlled\ error}.
}
```

The finite score can now be optimized to a complex exact local fixed point. That does not validate the score as a Bellman potential. The dominant missing theorem is a retention quotient that assigns simultaneous raw outputs without unbounded duplicate, containment, or cyclic reuse.

The local optimum should next be used as an adversarial transition for testing retention rules, rather than as evidence that continued policy search alone will close the proof.

---

## 9. Approved next targets

1. Export the complete raw transition for the 37-step local optimum with point provenance, duplicates, strict containments, partial overlaps, and SCC structure.
2. Compare that transition exactly with lexicographic and `seed_5_142` transitions.
3. Define a provenance-preserving retained-child quotient and test it on `S_1,...,S_7` and the local-optimum transition.
4. If the quotient fails, extract the smallest exact duplicate/containment/cycle obstruction.
5. Add the missing packing coordinate identified by that obstruction.
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
- a nonempty occurrence-weight cone makes continuation cost unnecessary;
- `gamma=1/16` survives enlarged policy families;
- locally favorable policy moves compose greedily;
- the earlier `S_3` `{5,40}` policy remains optimal after family expansion;
- the earlier `S_7` `seed_5` or `seed_5_142` policies remain optimal after neighborhood expansion;
- one-toggle local optimality implies global policy optimality;
- the 59-step neighborhood covers arbitrary delayed progression steps;
- policy-LP feasibility implies Bellman-LP feasibility;
- adding the recorded path charge is justified without retention;
- the tested policy family is globally optimal;
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

Standalone local-optimum certificate:

```bash
python3 src/run_exact_python.py \
  src/verify_s7_terminal_step_local_optimum.py \
  /tmp/s7_terminal_step_local_optimum_certificate.txt
```

Current detailed notes:

- `docs/certainty-ledger.md`;
- `docs/s7-terminal-step-local-optimum.md`;
- `docs/policy-subset-lattice-s1-s7.md`;
- `docs/expanded-policy-subset-lp.md`;
- `docs/policy-halfspace-lp.md`;
- `docs/s7-cyclic-scc-output-load.md`;
- `docs/s7-regenerative-seed-policy-dependence.md`;
- `docs/branching-reserve-lp.md`.

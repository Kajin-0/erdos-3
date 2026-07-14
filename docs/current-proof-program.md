# Current proof program: retained recursive contraction and terminal sinks

## Status

This is the authoritative overview for the four-term case of Erdős Problem #3. The full reciprocal-sum problem remains open. Durable exact claims are recorded in `docs/certainty-ledger.md`.

---

## 1. Foundation and recorded path

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

Coordinated side-anchor deletion gives a three-term-progression-free residual and recursive middle/backbone outputs. The exact local accounting inequalities are

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

The uncontaminated equal-translate model is summable, but the certified contaminated path has scale word

```text
4,8,4,4,8,4,8,8,8
```

and `W_5/W_1=91/32>1`, so universal local and fixed-window contraction are false.

At `S_10`, exact inheritance, completion support, and rectangle transport prove

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

Every valid exact factor-eight child has a certified summable tail. This closes the recorded state, not the full tree.

---

## 2. Policy and retention frontier

Lexicographic `S_7` contains both an isolated canonical return

```math
\{16,21,26\}\xrightarrow[f=4]{R=1}S_1
```

and a cyclic terminal-fiber component with spectral radius greater than `23/9`. Raw output is therefore not a Bellman child family.

The exact policy score

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi
```

has finite witness

```math
\boxed{\lambda=3,\qquad\gamma=\frac1{10}}.
```

A complete five-step subset lattice is certified through `S_7`, and a broader deterministic search produces a seed-delayed 37-step `S_7` policy with

```text
selected actions = 9,323
terminal residual = 517
terminal step classes = 28
middle-fiber occurrences = 9,295
canonical regeneration = false.
```

It has no improving move in its exact 59-toggle neighborhood. This is local, not global, policy optimality.

Its raw transition has `131` shell occurrences and `87` exact state classes. Exact duplicate quotienting followed by maximum-harmonic independent-set selection in the same-shell conflict graph produces a unique point-disjoint retained family:

```text
first retained states = 21
first retained labels = 11,753.
```

Propagating those states lexicographically and reapplying the quotient gives

```text
second retained states = 27
second retained labels = 7,925.
```

---

## 3. Provenance and scale profile

Original `S_7` provenance multiplicity in the 7,925 retained descendant points is

| multiplicity | root labels |
|---:|---:|
| 1 | 7,376 |
| 2 | 267 |
| 3 | 5 |

Despite modest multiplicity, total second retained harmonic mass is between `6.828` and `6.829` times first retained mass.

For every retained descendant `u`, the exact scale certificate records its root-provenance label `p`. Every contraction

```math
\left\lfloor\log_2(p/u)\right\rfloor\ge8
```

has repeated root provenance. Repeated roots carry only `7.6%`–`7.7%` of occurrence-weighted root mass but produce `94.8%`–`94.9%` of second retained harmonic mass.

Unit root-weighted shell-depth, floor-log, and ceil-log charges fail: the intergeneration debt is respectively more than `86`, `99`, and `77` times those charges.

The extreme tail is concentrated:

```text
floor-log depth >= 16: 69.8%–69.9% of second retained mass
single point u=1, p=1,354,066: 51.2%–51.3%.
```

This identifies the mechanism as repeated provenance combined with extreme scale contraction. It does not yet identify which output continues recursively.

---

## 4. Terminal/recursive split

The 27 second-generation retained states divide exactly into

| type | states | labels |
|---|---:|---:|
| terminal, three-term-progression-free | 13 | 43 |
| recursive | 14 | 7,882 |

The terminal states have no coordinated-deletion action. They carry between `86.2%` and `86.3%` of total second retained harmonic mass.

After removing those terminal sinks,

```math
\boxed{
0.937
<
\frac{H_2^{\rm rec}}{H_1}
<
0.938.
}
```

Therefore the genuinely recursive retained branch contracts by

```math
\boxed{
0.062
<
\frac{H_1-H_2^{\rm rec}}{H_1}
<
0.063.
}
```

All points with at least sixteen binary orders of contraction, including `u=1`, are terminal. The apparent `6.828`–`6.829` expansion is predominantly terminal sink mass, not persistent recursive load.

This is the first exact two-generation contraction of the recursive retained branch for the adversarial `S_7` transition.

Primary references:

- `docs/retained-terminal-recursive-split.md`;
- `docs/retained-provenance-scale-profile.md`;
- `docs/retained-provenance-second-generation.md`;
- `docs/s7-provenance-retained-quotient.md`.

---

## 5. Active theorem

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

The current exact transition suggests two separate ledgers:

```math
\operatorname{RecPack}
\qquad\text{and}\qquad
\operatorname{TermSink}.
```

`RecPack` must contract under retained recursive propagation. `TermSink` must record three-term-progression-free output exactly once and prevent numerical or provenance-supported terminal mass from being charged again elsewhere in the tree.

The scale profile remains relevant for identifying which sinks carry the large mass, but the full scale tail must not be treated as recursive debt.

---

## 6. Approved next targets

1. Export the terminal sink family with exact numerical-state and root-provenance identities.
2. Define a global terminal-sink ledger that charges each retained terminal state or point at most once.
3. Propagate only the 14 recursive second-generation states and test third-generation retained contraction.
4. Export the first two-generation Bellman row with separate recursive and terminal-sink coordinates.
5. Attach completion, rectangle, or future cheap-extension exclusion credit to terminal sinks that can reappear.
6. Prove a terminal-output Carleson bound or extract the smallest exact failure.

---

## 7. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- local policy optimality is global;
- acyclic terminal-fiber incidence implies disjoint retained children;
- raw harmonic reduction alone gives Bellman contraction;
- duplicate quotienting alone resolves overlap;
- one-generation retention bounds indefinite provenance reuse;
- maximum provenance multiplicity three implies contraction;
- low provenance-overhead mass pays for scale-driven growth;
- unit depth or logarithmic root charge repays the debt;
- the full `6.828`–`6.829` ratio is recursive load;
- terminal mass may be discarded rather than charged once;
- the `6.2%`–`6.3%` recursive contraction is universal;
- maximum-harmonic retention is globally Bellman-optimal;
- policy-LP feasibility implies Bellman-LP feasibility;
- one finite transition proves the whole theorem.

---

## 8. Reproduction

Push-gating lightweight suite:

```bash
bash src/run_verify_ci_lightweight.sh
```

Complete extended suite:

```bash
bash src/run_verify_transport_reserve.sh
```

Standalone latest checks:

```bash
python3 src/run_exact_python.py \
  src/verify_retained_provenance_scale_profile.py \
  /tmp/retained_provenance_scale_profile_certificate.txt

python3 src/run_exact_python.py \
  src/verify_retained_terminal_split.py \
  /tmp/retained_terminal_split_certificate.txt
```

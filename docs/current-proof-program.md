# Current proof program: recursive contraction and terminal-sink accounting

## Status

This is the authoritative overview for the four-term case of Erdős Problem #3. The full reciprocal-sum problem remains open. Durable exact claims are tracked in `docs/certainty-ledger.md`.

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

Coordinated side-anchor deletion gives a three-term-progression-free residual and recursive middle/backbone outputs. The exact local inequalities are

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

## 2. Policy and retained-child frontier

Lexicographic `S_7` contains an isolated canonical return

```math
\{16,21,26\}\xrightarrow[f=4]{R=1}S_1
```

and a cyclic terminal-fiber component with spectral radius greater than `23/9`. Raw output is therefore not a Bellman child family.

The finite policy score

```math
C_{\lambda,\gamma}(\pi)
=
T_\pi+\lambda O_\pi+E_\pi+\gamma G_\pi
```

has witness

```math
\boxed{\lambda=3,\qquad\gamma=\frac1{10}}.
```

A complete five-step subset lattice is certified through `S_7`. A broader deterministic search produces a seed-delayed 37-step `S_7` policy with

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

## 3. Provenance, scale, and the terminal correction

Original `S_7` provenance multiplicity among the 7,925 second-generation points is

| multiplicity | root labels |
|---:|---:|
| 1 | 7,376 |
| 2 | 267 |
| 3 | 5 |

Total second retained harmonic mass is between `6.828` and `6.829` times first retained mass. The scale profile explains that apparent expansion:

- every contraction with `floor(log2(p/u)) >= 8` has repeated root provenance;
- repeated roots carry only `7.6%`–`7.7%` of root occurrence mass;
- they produce `94.8%`–`94.9%` of second retained harmonic mass;
- unit root-weighted depth or logarithmic charges fail by factors greater than `77`.

The 27 second-generation retained states divide exactly into

| type | states | labels |
|---|---:|---:|
| terminal, three-term-progression-free | 13 | 43 |
| recursive | 14 | 7,882 |

The terminal states have no coordinated-deletion action and carry `86.2%`–`86.3%` of total second retained harmonic mass. After removing them,

```math
\boxed{
0.937
<
\frac{H_2^{\rm rec}}{H_1}
<
0.938.
}
```

Thus the genuinely recursive retained branch contracts by

```math
\boxed{
0.062
<
\frac{H_1-H_2^{\rm rec}}{H_1}
<
0.063.
}
```

All points with at least sixteen binary orders of contraction, including `u=1`, are terminal. The full `6.828`–`6.829` ratio is predominantly terminal sink mass, not persistent recursive load.

---

## 4. Exact terminal-sink identity ledger

The 13 terminal states now have a deterministic identity export. Each state record contains:

```text
numerical value set
root-provenance vector
immediate-provenance vector
parent retained class
source type and source step
dyadic shell
pointwise (u,p) scale records.
```

The export is anchored to the certified second-generation retained-family hash

```text
dbb6d888c790cf5a67f2e3a6ed86400506c93baac3701f39d15d858c19b21596
```

and the complete 7,925-point provenance record hash

```text
904b0b9f8906d196ea02369cb60153341eda5a562340ba8615dbcdb769dc92e3.
```

Within the certified family:

```text
terminal sink states = 13
terminal sink points = 43
terminal numerical labels are pairwise unique
terminal labels are disjoint from recursive retained labels
terminal point tokens (u,p) are pairwise unique.
```

Therefore every terminal point can be charged exactly once **inside this recorded family**. This is not yet a global terminal-sink theorem: another branch or later generation could recreate the same numerical or provenance-supported sink.

Primary references:

- `docs/retained-terminal-sink-identity-ledger.md`;
- `docs/retained-terminal-recursive-split.md`;
- `docs/retained-provenance-scale-profile.md`;
- `docs/retained-provenance-second-generation.md`;
- `docs/s7-provenance-retained-quotient.md`.

---

## 5. Active theorem

The target whole-tree inequality is now separated into recursive and terminal coordinates:

```math
\boxed{
\Delta(S)
+
\operatorname{TermSink}(S)
+
\sum_{S'\in\operatorname{RecChild}_\pi(S)}
\operatorname{RecPack}(S')
\le
\operatorname{RecPack}(S)
+
\Phi_{\rm obs}(S)
+
\operatorname{controlled\ error}.
}
```

`RecPack` must contract under retained recursive propagation. `TermSink` must charge three-term-progression-free outputs once and prevent recreation through another numerical, provenance, or affine path.

The exact two-generation transition establishes the first part locally:

```text
recursive retained ratio < 0.938.
```

The unresolved theorem is the second part: bound the global multiplicity of terminal sink identities.

---

## 6. Approved next targets

1. Compare the 43 terminal `(u,p)` tokens with all earlier raw and retained point tokens.
2. Propagate only the 14 recursive second-generation states and test third-generation contraction and terminal-token recreation.
3. Test whether `(root provenance, descendant label)` is sufficient globally or requires a path/affine signature.
4. Export the first Bellman row with separate recursive and first-appearance terminal coordinates.
5. Attach completion, rectangle, or future cheap-extension exclusion credit to recreated sinks.
6. Prove a terminal-output Carleson bound or extract the smallest exact collision.

---

## 7. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- local policy optimality is global;
- raw harmonic reduction alone gives Bellman contraction;
- duplicate quotienting alone resolves overlap;
- one-generation retention bounds indefinite provenance reuse;
- maximum provenance multiplicity three implies contraction;
- unit depth or logarithmic root charge repays the full second-generation mass;
- the full `6.828`–`6.829` ratio is recursive load;
- terminal mass may be discarded rather than charged once;
- within-family terminal-token uniqueness implies global uniqueness;
- `(u,p)` is globally injective without a collision theorem;
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

Complete established extended suite:

```bash
bash src/run_verify_transport_reserve.sh
```

Terminal identity export and verification:

```bash
bash src/run_verify_terminal_sink_ledger.sh
```

The manually triggered extended workflow runs both commands. The terminal identity check is not part of push-gating lightweight CI.

# Current proof program: recursive Bellman contraction and terminal sinks

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

Lexicographic `S_7` contains an isolated return

```math
\{16,21,26\}\xrightarrow[f=4]{R=1}S_1
```

and a cyclic terminal-fiber component with spectral radius greater than `23/9`. Raw outputs cannot therefore be inserted directly into a Bellman child sum.

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

A complete five-step subset lattice is certified through `S_7`. A broader deterministic search gives a seed-delayed 37-step `S_7` policy with

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

## 3. Provenance, scale, and terminal correction

Original `S_7` provenance multiplicity among the 7,925 second-generation points is

| multiplicity | root labels |
|---:|---:|
| 1 | 7,376 |
| 2 | 267 |
| 3 | 5 |

Total second retained harmonic mass is between `6.828` and `6.829` times first retained mass. The scale profile explains the concentration:

- every contraction with `floor(log2(p/u)) >= 8` has repeated root provenance;
- repeated roots carry only `7.6%`–`7.7%` of root occurrence mass;
- they produce `94.8%`–`94.9%` of second retained harmonic mass;
- unit root-weighted depth or logarithmic charges fail by factors greater than `77`.

The 27 states divide exactly into

| type | states | labels |
|---|---:|---:|
| terminal, three-term-progression-free | 13 | 43 |
| recursive | 14 | 7,882 |

Terminal states have no coordinated-deletion action and carry `86.2%`–`86.3%` of second retained mass. Removing them gives

```math
\boxed{
0.937
<
\frac{H_2^{\rm rec}}{H_1}
<
0.938.
}
```

Thus the recursively continuing branch contracts by

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

## 4. Exact terminal identities

The 13 terminal states have a deterministic identity export. Each record contains:

```text
numerical value set
root- and immediate-provenance vectors
parent retained class
source type and source step
dyadic shell
pointwise (u,p) scale records.
```

The export is anchored to the certified second-generation retained-family hash

```text
dbb6d888c790cf5a67f2e3a6ed86400506c93baac3701f39d15d858c19b21596
```

and the complete 7,925-point provenance-record hash

```text
904b0b9f8906d196ea02369cb60153341eda5a562340ba8615dbcdb769dc92e3.
```

Within the certified family:

```text
terminal states = 13
terminal points = 43
terminal numerical labels are pairwise unique
terminal labels are disjoint from recursive labels
terminal point tokens (u,p) are pairwise unique.
```

Every terminal point can therefore be charged once inside this family. Global recreation by another branch or generation remains open.

---

## 5. First-appearance terminal ledger

For any fixed terminal-token map on a finite or locally finite rooted tree, assign each token to the first node containing it in a deterministic total order. The first-appearance sets are pairwise disjoint and their weighted sum equals the weighted global token union.

For the recorded family, use

```math
\tau(u)=(u,p),
```

where `p` is original `S_7` root provenance. All 43 tokens are unique, so the full recorded terminal charge is a first-appearance charge under every node order.

This solves bookkeeping once a collision-sound token map is fixed. It does not prove that `(u,p)` is globally collision-sound or that the global token-union mass is bounded.

---

## 6. First strict retained Bellman row

The certified recursive ratio implies

```math
H_2^{\rm rec}<\frac{469}{500}H_1.
```

Therefore

```math
\boxed{
\frac{31}{500}H_1+H_2^{\rm rec}<H_1.
}
```

This is the first strict rational Bellman row for the genuinely recursive retained output of the adversarial transition.

Carrying the first-appearance terminal coordinate separately gives

```math
\boxed{
\frac{31}{500}H_1
+
H_2^{\rm rec}
+
\operatorname{TermSink}_{\rm first}
<
H_1
+
\operatorname{TermSink}_{\rm first}.
}
```

Terminal mass is neither discarded nor counted as recursive load. The row is fixed-policy and fixed-retention, not universal.

Primary references:

- `docs/two-generation-recursive-bellman-row.md`;
- `docs/terminal-sink-first-appearance-ledger.md`;
- `docs/retained-terminal-sink-identity-ledger.md`;
- `docs/retained-terminal-recursive-split.md`;
- `docs/retained-provenance-scale-profile.md`.

---

## 7. Active theorem

The whole-tree target is

```math
\boxed{
\Delta(S)
+
\operatorname{TermSink}_{\rm first}(S)
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

The recorded transition now supplies:

```text
legitimate retained children
separate terminal and recursive families
strict recursive credit 31/500 of parent retained mass
exact terminal identities
first-appearance no-double-counting bookkeeping.
```

The unresolved structural theorem is terminal-token collision control across branches and generations.

---

## 8. Approved next targets

1. Compare the 43 terminal `(u,p)` tokens with all earlier raw and retained tokens.
2. Propagate only the 14 recursive second-generation states and apply the quotient a third time.
3. Measure third-generation recursive contraction and recreation of the 43 recorded terminal tokens.
4. Test whether `(u,p)` requires an affine/path signature to be collision-sound.
5. Export a three-generation Bellman row or the smallest exact failure.
6. Prove a terminal-output Carleson bound or extract the first unbounded collision mechanism.

---

## 9. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- local policy optimality is global;
- duplicate quotienting alone resolves overlap;
- one-generation retention bounds indefinite provenance reuse;
- maximum provenance multiplicity three implies contraction;
- unit depth or logarithmic root charge repays total second-generation mass;
- the full `6.828`–`6.829` ratio is recursive load;
- terminal mass may be discarded;
- within-family terminal-token uniqueness implies global uniqueness;
- `(u,p)` is globally injective without a collision theorem;
- first-appearance bookkeeping bounds token-union mass;
- the `31/500` Bellman credit is universal;
- maximum-harmonic retention is globally optimal;
- policy-LP feasibility implies branching Bellman-LP feasibility;
- one finite transition proves the whole theorem.

---

## 10. Reproduction

Push-gating lightweight suite:

```bash
bash src/run_verify_ci_lightweight.sh
```

Established extended frontier:

```bash
bash src/run_verify_transport_reserve.sh
```

Terminal identity and Bellman-row checks:

```bash
bash src/run_verify_terminal_sink_ledger.sh
```

The manually triggered extended workflow runs both commands. None of the terminal-ledger or Bellman-row work is part of push-gating lightweight CI.

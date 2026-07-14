# Current proof program: generation-aware retained potential

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

Its raw transition has `131` shell occurrences and `87` exact state classes. Exact duplicate quotienting followed by maximum-harmonic independent-set selection in the same-shell conflict graph produces a unique point-disjoint first retained family:

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

## 3. Second-generation terminal correction

Original `S_7` provenance multiplicity among the 7,925 second-generation points is

| multiplicity | root labels |
|---:|---:|
| 1 | 7,376 |
| 2 | 267 |
| 3 | 5 |

Total second retained harmonic mass is between `6.828` and `6.829` times first retained mass. The scale profile shows that the apparent expansion is concentrated in repeated provenance and extreme contraction.

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
\frac{H_2^{\mathrm{rec}}}{H_1}
<
0.938.
}
```

Thus the recursively continuing branch contracts by

```math
\boxed{
0.062
<
\frac{H_1-H_2^{\mathrm{rec}}}{H_1}
<
0.063.
}
```

This yields the strict one-transition row

```math
\boxed{
\frac{31}{500}H_1+H_2^{\mathrm{rec}}<H_1.
}
```

The 13 terminal states have an exact pointwise identity ledger. Within that family, all 43 numerical labels and all tokens

```math
\tau_2(u)=(u,p)
```

are unique, where `p` is original `S_7` root provenance.

A first-appearance ledger gives exact no-double-counting bookkeeping for any fixed token map. It does not bound the global token union and does not prove that `(u,p)` is collision-sound.

---

## 4. Third-generation exact no-go

Only the 14 recursive second-generation states are propagated. Their global third-generation quotient has

```text
raw occurrences = 474
exact state classes = 108
conflict edges = 386
conflict components = 29
largest component = 15
components with nonunique optimum = 0.
```

The unique retained family has

| type | states | points |
|---|---:|---:|
| terminal | 18 | 110 |
| recursive | 14 | 4,789 |
| total | 32 | 4,899 |

Terminal output again dominates total harmonic mass:

```math
0.788208
<
\frac{H_3^{\mathrm{term}}}{H_3}
<
0.788209.
```

However the recursive output now expands:

```math
\boxed{
2.011553
<
\frac{H_3^{\mathrm{rec}}}{H_2^{\mathrm{rec}}}
<
2.011554.
}
```

It also satisfies

```math
\boxed{
1.886248
<
\frac{H_3^{\mathrm{rec}}}{H_1}
<
1.886249.
}
```

Therefore the `31/500` row is a valid local transition statement but does not iterate under the same fixed policy and retained quotient. A successful Bellman state must be generation-aware, path-aware, or carry additional obstruction credit.

This is an exact fixed-policy, fixed-retention no-go result. It does not exclude a larger multi-coordinate potential.

---

## 5. Terminal signature correction

The 43 second-generation terminal `(u,p)` tokens have no collision with any first-generation raw or retained token.

At the third generation exactly one token recurs:

```text
(u,p) = (60, 1,354,490).
```

Both occurrences are step-5 middle-fiber terminal singletons, so source type and source step do not separate them. Their immediate provenance differs:

| generation | immediate provenance |
|---:|---:|
| 2 | 2,810 |
| 3 | 440 |

Hence

```math
\tau(u)=(u,p)
```

is too coarse, while

```math
\tau^+(u)=(u,p,i)
```

with immediate provenance `i` separates the recorded collision.

No second-generation terminal `(u,p)` token reappears in the third-generation recursive family.

Numerical identity alone is much worse: 28 earlier terminal labels reappear, including seven complete terminal numerical states

```text
{1}
{5}
{10}
{60}
{61,62}
{122,123}
{147,152,153}.
```

The next token theorem must therefore be path-sensitive. Immediate provenance is the first viable refinement, not yet a globally proved signature.

---

## 6. Active theorem

The target whole-tree inequality remains

```math
\boxed{
\Delta(S)
+
\mathrm{TermSink}_{\mathrm{first}}(S)
+
\sum_{S'\in\mathrm{RecChild}_\pi(S)}
\mathrm{RecPack}(S')
\le
\mathrm{RecPack}(S)
+
\Phi_{\mathrm{obs}}(S)
+
\mathrm{controlled\ error}.
}
```

The current exact frontier supplies:

```text
legitimate point-disjoint retained children
exact terminal/recursive partitions at generations two and three
one strict recursive contraction transition
one strict recursive expansion transition
exact terminal identities
an explicit failure of the (u,p) token
an immediate-provenance refinement that separates the first collision.
```

The decisive open object is now a finite weighted state that couples:

```text
recursive harmonic mass
retained generation or scale
root provenance
immediate/path provenance
first-appearance terminal mass
obstruction or future-extension exclusion credit.
```

A candidate must absorb both

```math
H_2^{\mathrm{rec}}/H_1<0.938
```

and

```math
H_3^{\mathrm{rec}}/H_2^{\mathrm{rec}}>2.011553.
```

---

## 7. Approved next targets

1. Export exact generation-two and generation-three transition rows in a common rational feature schema.
2. Add generation/scale, root provenance, and immediate provenance coordinates to the exact LP harness.
3. Test whether any nonnegative linear potential fits both the second-generation contraction and third-generation expansion.
4. If infeasible, extract the smallest exact dual obstruction.
5. Propagate the 14 third-generation recursive states one further generation only if the finite feature LP remains feasible.
6. Test whether `(u,p,i)` remains collision-sound at the next generation.
7. Attach completion, rectangle, or cheap-extension exclusion credit to recurring terminal signatures.
8. Prove a branching terminal-output Carleson bound or isolate the first unbounded path-reuse mechanism.

---

## 8. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- local policy optimality is global;
- duplicate quotienting alone resolves overlap;
- one-generation retention bounds indefinite provenance reuse;
- maximum provenance multiplicity three implies contraction;
- unit depth or logarithmic root charge repays total retained mass;
- the full `6.828`–`6.829` ratio is recursive load;
- terminal mass may be discarded;
- within-family terminal-token uniqueness implies global uniqueness;
- `(u,p)` is globally collision-sound;
- source type and source step repair the recorded token collision;
- first-appearance bookkeeping bounds token-union mass;
- the `31/500` Bellman credit iterates;
- the third-generation expansion is universal over all policies or quotients;
- immediate provenance is globally sufficient after one finite success;
- maximum-harmonic retention is globally optimal;
- policy-LP feasibility implies branching Bellman-LP feasibility;
- one finite transition proves the whole theorem.

---

## 9. Reproduction

Push-gating lightweight suite:

```bash
bash src/run_verify_ci_lightweight.sh
```

Established extended frontier:

```bash
bash src/run_verify_transport_reserve.sh
```

Terminal identities, the two-generation row, and the third-generation frontier:

```bash
bash src/run_verify_terminal_sink_ledger.sh
```

The manually triggered extended workflow runs the established and terminal-ledger suites. None of the third-generation work is part of push-gating lightweight CI.

Primary recent references:

- `docs/third-generation-recursive-frontier.md`;
- `docs/two-generation-recursive-bellman-row.md`;
- `docs/terminal-sink-first-appearance-ledger.md`;
- `docs/retained-terminal-sink-identity-ledger.md`;
- `docs/retained-terminal-recursive-split.md`;
- `docs/retained-provenance-scale-profile.md`.

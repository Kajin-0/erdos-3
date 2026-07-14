# Current proof program: provenance-reserve retained potential

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

Lexicographic `S_7` contains both an isolated return

```math
\{16,21,26\}\xrightarrow[f=4]{R=1}S_1
```

and a cyclic terminal-fiber component with spectral radius greater than `23/9`. Raw outputs cannot therefore be inserted directly into a Bellman child sum.

A deterministic policy search produces a seed-delayed 37-step `S_7` policy with

```text
selected actions = 9,323
terminal residual = 517
terminal step classes = 28
middle-fiber occurrences = 9,295
canonical regeneration = false.
```

It has no improving move in its exact 59-toggle neighborhood. This is local, not global, policy optimality.

Its raw transition has `131` shell occurrences and `87` exact state classes. Exact duplicate quotienting followed by maximum-harmonic independent-set selection in the same-shell conflict graph gives a unique point-disjoint first retained family:

```text
first retained states = 21
first retained labels = 11,753.
```

Lexicographic propagation and the same global quotient give:

| retained level | states | points |
|---|---:|---:|
| first retained | 21 | 11,753 |
| second total | 27 | 7,925 |
| second recursive | 14 | 7,882 |
| third total | 32 | 4,899 |
| third recursive | 14 | 4,789 |

All retained families are point-disjoint within their generation, and every conflict component used in the second and third quotient has a unique optimum.

---

## 3. Terminal sinks and the raw-mass no-go

The second retained family splits into

| type | states | points |
|---|---:|---:|
| terminal, three-term-progression-free | 13 | 43 |
| recursive | 14 | 7,882 |

Terminal output carries `86.2%`–`86.3%` of total second retained harmonic mass. Removing it gives

```math
0.937
<
\frac{H_2^{\mathrm{rec}}}{H_1}
<
0.938,
```

and the local row

```math
\frac{31}{500}H_1+H_2^{\mathrm{rec}}<H_1.
```

That row does not iterate. Propagating only the 14 recursive second-generation states yields

```math
\boxed{
2.011553
<
\frac{H_3^{\mathrm{rec}}}{H_2^{\mathrm{rec}}}
<
2.011554.
}
```

Thus raw recursive harmonic mass contracts once and then expands by more than a factor of two under the same fixed policy and retained quotient.

The third retained family again has substantial terminal output:

| type | states | points |
|---|---:|---:|
| terminal | 18 | 110 |
| recursive | 14 | 4,789 |

Terminal mass must be carried through a separate first-appearance ledger; it cannot be discarded or counted as persistent recursive load.

---

## 4. Terminal identity correction

The 43 second-generation terminal points have exact numerical, root-provenance, immediate-provenance, source, and shell identities.

Within that family, all tokens

```math
\tau(u)=(u,p)
```

are unique, where `p` is original `S_7` root provenance. Across the third generation, however, exactly one token recurs:

```text
(u,p) = (60, 1,354,490).
```

Both occurrences are step-5 middle fibers. Their immediate provenance differs:

```text
generation 2: i = 2,810
generation 3: i = 440.
```

Therefore `(u,p)` and `(u,p,source,source_step)` are too coarse, while

```math
\tau^+(u)=(u,p,i)
```

separates the first recorded collision. Immediate provenance is a viable next signature component, not yet a global injectivity theorem.

Numerical identity alone is much worse: 28 earlier terminal labels and seven complete terminal numerical states recur.

---

## 5. Provenance-reserve potential

Raw recursive harmonic mass fails, but the exact feature screen found two simple same-form potentials that decrease across both recorded recursive transitions.

### Repeated-root descendant reserve

Let `m_g(p)` be the number of retained recursive points in generation `g` carrying root provenance `p`. Define

```math
R_g
=
\sum_{(u,p)\in F_g\,:\,m_g(p)>1}\frac1u.
```

The primary candidate is

```math
\boxed{
\Phi_g^{\mathrm{rep}}=H_g+2R_g.
}
```

It satisfies

```math
\frac{145059}{200000}
<
\frac{\Phi_2^{\mathrm{rep}}}{\Phi_1^{\mathrm{rep}}}
<
\frac{45331}{62500},
```

and

```math
\boxed{
\frac{939443}{1000000}
<
\frac{\Phi_3^{\mathrm{rep}}}{\Phi_2^{\mathrm{rep}}}
<
\frac{234861}{250000}.
}
```

Hence the same potential contracts by `27.4704%–27.4705%` and then `6.0556%–6.0557%`.

The mechanism is reserve release: repeated-root descendant mass falls from approximately

```text
0.272749423160
0.167467988429
0.013654746193
```

across the three retained recursive levels, absorbing the third-generation increase in raw harmonic mass.

### Immediate-depth-tail reserve

Let

```math
d_i(u)=\left\lfloor\log_2\frac{i}{u}\right\rfloor
```

for immediate provenance `i`, and define

```math
T_g
=
\sum_{(u,i)\in F_g\,:\,d_i(u)\ge4}\frac1u.
```

The secondary candidate is

```math
\boxed{
\Phi_g^{\mathrm{tail}}=H_g+4T_g.
}
```

It satisfies

```math
\frac{499343}{500000}
<
\frac{\Phi_3^{\mathrm{tail}}}{\Phi_2^{\mathrm{tail}}}
<
\frac{998687}{1000000},
```

so the difficult transition still contracts by `0.1313%–0.1314%`.

This coordinate is path-aware and uses the same immediate-provenance information that repaired the first terminal-token collision.

---

## 6. Exact single-feature screen

With current harmonic mass coefficient fixed to one, eleven nonnegative single-coordinate corrections were tested against both recursive transitions.

Exactly four are feasible:

```text
immediate_tail_ge4_descendant_mass
root_occurrence_mass
root_repeat_descendant_mass
root_repeat_occurrence_mass.
```

The following are infeasible as standalone corrections:

```text
immediate_depth_charge
immediate_occurrence_mass
immediate_repeat_descendant_mass
immediate_repeat_occurrence_mass
root_depth_charge
root_tail_ge4_descendant_mass
root_tail_ge8_descendant_mass.
```

The simple integer witnesses are coefficient `2` for repeated-root descendant mass and coefficient `4` for the immediate depth-four tail.

---

## 7. Active theorem

The whole-tree target remains

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

The first concrete candidate for `RecPack` is now

```math
\mathrm{RecPack}(F)=H(F)+2R(F).
```

A secondary candidate is

```math
\mathrm{RecPack}_{\mathrm{tail}}(F)=H(F)+4T(F).
```

The recorded frontier supplies:

```text
legitimate point-disjoint retained children
terminal/recursive partitions through generation three
an explicit raw-mass failure
an exact terminal-token collision and immediate-provenance repair
two same-form retained potentials that contract across both observed transitions.
```

These are fixed-policy, fixed-retention finite witnesses. The missing theorem is uniform control across later generations, policies, and branches.

---

## 8. Approved next targets

1. Propagate the 14 third-generation recursive states to a fourth retained generation.
2. Test `H+2R` and `H+4T` before introducing any new coordinate.
3. Record terminal recreation under the refined token `(u,p,i)`.
4. Export the two candidate potentials into the exact rational LP schema.
5. Test policy sensitivity of repeated-root reserve on the smallest retained families.
6. Prove bounded release/recreation of repeated-root capacity or extract the first exact failure.
7. Attach completion, rectangle, or cheap-extension exclusion credit if either potential fails.
8. Prove a branching terminal-output Carleson bound using first-appearance refined tokens.

---

## 9. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- local policy optimality is global;
- duplicate quotienting alone resolves overlap;
- one-generation retention bounds indefinite reuse;
- maximum provenance multiplicity implies contraction by itself;
- unit depth or logarithmic charge repays total retained mass;
- the full `6.828`–`6.829` ratio is recursive load;
- terminal mass may be discarded;
- `(u,p)` is collision-sound;
- immediate provenance is globally sufficient after one finite success;
- first-appearance bookkeeping bounds token-union mass;
- raw harmonic contraction or expansion persists to later generations;
- `H+2R` or `H+4T` is a universal Bellman potential after two finite transitions;
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

Terminal identities, third-generation frontier, and provenance-reserve potentials:

```bash
bash src/run_verify_terminal_sink_ledger.sh
```

The manually triggered extended workflow runs both extended suites. None of the generation-aware potential work is part of push-gating lightweight CI.

Primary recent references:

- `docs/generation-aware-retained-potentials.md`;
- `docs/third-generation-recursive-frontier.md`;
- `docs/two-generation-recursive-bellman-row.md`;
- `docs/terminal-sink-first-appearance-ledger.md`;
- `docs/retained-terminal-sink-identity-ledger.md`;
- `docs/retained-terminal-recursive-split.md`.

# Current proof program: four-generation retained-feature LP

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

## 2. Policy and retained-child construction

Lexicographic `S_7` contains an isolated canonical return and a cyclic terminal-fiber component, so raw outputs cannot be inserted directly into a Bellman child sum.

A deterministic policy search gives a seed-delayed 37-step `S_7` policy with

```text
selected actions = 9,323
terminal residual = 517
terminal step classes = 28
middle-fiber occurrences = 9,295
canonical regeneration = false.
```

It has no improving move in its exact 59-toggle neighborhood. This is local, not global, policy optimality.

For every generation the retained quotient is defined by:

1. exact numerical state quotienting;
2. deterministic provenance representatives;
3. same-shell intersection conflicts;
4. componentwise maximum-harmonic independent-set selection.

The resulting retained frontier is:

| retained level | total states | total points | terminal states | terminal points | recursive states | recursive points |
|---|---:|---:|---:|---:|---:|---:|
| first | 21 | 11,753 | — | — | 21 | 11,753 |
| second | 27 | 7,925 | 13 | 43 | 14 | 7,882 |
| third | 32 | 4,899 | 18 | 110 | 14 | 4,789 |
| fourth | 23 | 1,794 | 11 | 77 | 12 | 1,717 |

Every recorded retained family is point-disjoint within its generation. Every second-, third-, and fourth-generation conflict component has a unique optimum.

---

## 3. Raw recursive mass alternates

Let `H_g^rec` denote recursively continuing retained harmonic mass.

The second generation contracts:

```math
0.937
<
\frac{H_2^{\mathrm{rec}}}{H_1}
<
0.938.
```

This yields the valid local row

```math
\frac{31}{500}H_1+H_2^{\mathrm{rec}}<H_1.
```

The third generation expands:

```math
\boxed{
2.011553
<
\frac{H_3^{\mathrm{rec}}}{H_2^{\mathrm{rec}}}
<
2.011554.
}
```

The fourth generation expands again:

```math
\boxed{
2.849279
<
\frac{H_4^{\mathrm{rec}}}{H_3^{\mathrm{rec}}}
<
2.849280.
}
```

Raw recursive harmonic mass is therefore not a one-step or short observed-window Bellman potential under the fixed policy and quotient.

Terminal output remains substantial but changes by generation:

```text
second retained terminal share: 86.2%–86.3%
third retained terminal share:  78.8208%–78.8209%
fourth retained terminal share: 59.2741%–59.2742%.
```

Terminal mass must be accounted through a separate first-appearance ledger; it cannot be discarded or treated as persistent recursive load.

---

## 4. Terminal identities and refined tokens

Each terminal point carries:

```text
current label u
original S7 root provenance p
immediate provenance i
parent retained class
source type and source step
dyadic shell.
```

The token

```math
\tau(u)=(u,p)
```

fails across generations:

- one collision appears at generation three;
- seven prior-terminal collisions appear in generation-four terminal output;
- no recorded `(u,p)` collision appears in generation-four recursive output.

The refined token

```math
\boxed{\tau^+(u)=(u,p,i)}
```

has no recorded collision through generation four, terminal or recursive.

Numerical identity alone is far too coarse:

```text
generation 3: 28 prior terminal labels and 7 complete terminal states recur
generation 4: 104 prior terminal labels recur across terminal/recursive output and 6 complete states recur.
```

Immediate provenance is therefore the first successful finite collision refinement. It is not yet a global injectivity theorem.

---

## 5. Three-generation reserve witnesses

An exact 11-feature screen over the first three recursive levels found four feasible single-coordinate corrections to current harmonic mass.

Two simple integer witnesses were certified.

### Repeated-root descendant reserve

Let

```math
R_g
=
\sum_{(u,p)\in F_g\,:\,m_g(p)>1}\frac1u.
```

Then

```math
\Phi_g^{\mathrm{rep}}=H_g+2R_g
```

contracts by `27.4704%–27.4705%` and then `6.0556%–6.0557%` across the first two recorded recursive transitions.

### Immediate-depth-tail reserve

Let

```math
T_g
=
\sum_{(u,i)\in F_g\,:\,\lfloor\log_2(i/u)\rfloor\ge4}\frac1u.
```

Then

```math
\Phi_g^{\mathrm{tail}}=H_g+4T_g
```

also contracts across those transitions, with a second-transition margin of `0.1313%–0.1314%`.

These are exact three-level witnesses, not iterating potentials.

---

## 6. Fourth-generation reserve failure

At the fourth recursive level:

```text
recursive points = 1,717
root provenance labels = 1,717
repeated root labels = 0
immediate provenance labels = 1,717
repeated immediate labels = 0.
```

The repeated-root reserve vanishes:

```math
R_4=0.
```

Consequently,

```math
\boxed{
2.711908
<
\frac{\Phi_4^{\mathrm{rep}}}{\Phi_3^{\mathrm{rep}}}
<
2.711909.
}
```

The immediate depth-four tail instead regenerates from approximately `0.000244` to `0.917166`, giving

```math
\boxed{
9.636610
<
\frac{\Phi_4^{\mathrm{tail}}}{\Phi_3^{\mathrm{tail}}}
<
9.636611.
}
```

The two candidates fail for complementary reasons:

```text
repeated-root capacity disappears before new growth
immediate-depth capacity is recreated during new growth.
```

This supersedes the three-generation candidates as possible one-step iterating potentials. Their three-generation certificate remains valid as a finite positive result.

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

The current frontier supplies:

```text
legitimate point-disjoint retained children through generation four
exact terminal/recursive partitions
three alternating recursive-mass transitions
an exact first-appearance terminal ledger
an (u,p) token failure and an (u,p,i) finite repair
two three-generation reserve witnesses
a fourth-generation exact failure of both witnesses.
```

The next mathematical object is an exact rational feature LP over all three recursive transitions:

```text
generation 1 -> generation 2 recursive
generation 2 recursive -> generation 3 recursive
generation 3 recursive -> generation 4 recursive.
```

The LP must test whether any nonnegative combination of the existing feature family makes every transition nonexpanding. If infeasible, the smallest exact Farkas/dual obstruction becomes the next theorem. New coordinates should be introduced only after that exhaustion.

Likely missing mechanisms are cumulative rather than within-generation:

```text
first-appearance provenance reuse
ancestor-chain/path capacity
terminal credit released when reserve disappears
completion or rectangle obstruction created by reserve release
multi-transition amortization rather than one-step monotonicity.
```

---

## 8. Approved next targets

1. Export the three recursive transitions into one exact rational feature matrix.
2. Solve the nonnegative feature-feasibility LP with current harmonic coefficient fixed to one.
3. Extract a sparse rational witness or the smallest exact dual obstruction.
4. Test refined terminal token `(u,p,i)` in the same first-appearance accounting schema.
5. Add cumulative provenance or path-capacity coordinates only if the current LP is infeasible.
6. Test policy sensitivity on the smallest retained families before propagating generation five.
7. Attach completion, rectangle, or cheap-extension exclusion credit to reserve release.
8. Prove a branching terminal-output Carleson bound or isolate the first unbounded refined-token reuse mechanism.

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
- terminal mass may be discarded;
- `(u,p)` is collision-sound;
- `(u,p,i)` is globally collision-sound after four finite levels;
- first-appearance bookkeeping bounds token-union mass;
- the `31/500` row iterates;
- raw recursive mass follows a stable short-period pattern;
- `H+2R` or `H+4T` survives beyond generation three;
- maximum-harmonic retention is globally optimal;
- policy-LP feasibility implies branching Bellman-LP feasibility;
- one finite path proves the whole theorem.

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

Terminal identities and retained generations through the fourth frontier:

```bash
bash src/run_verify_terminal_sink_ledger.sh
```

The manually triggered extended workflow runs both extended suites. None of the retained-generation work is part of push-gating lightweight CI.

Primary recent references:

- `docs/fourth-generation-provenance-reserve-frontier.md`;
- `docs/generation-aware-retained-potentials.md`;
- `docs/third-generation-recursive-frontier.md`;
- `docs/two-generation-recursive-bellman-row.md`;
- `docs/terminal-sink-first-appearance-ledger.md`;
- `docs/retained-terminal-sink-identity-ledger.md`.

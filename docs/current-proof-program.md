# Current proof program: obstruction export and whole-tree packing

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case. Claims below are proved internally or computationally certified as stated, but await independent expert review.

---

## 1. Foundational reduction and recursive genealogy

For

```math
A_j=A\cap[2^j,2^{j+1}),
\qquad
\alpha_j=\frac{|A_j|}{2^j},
```

one has, up to absolute constants,

```math
\sum_{n\in A}\frac1n=\infty
\quad\Longleftrightarrow\quad
\sum_j\alpha_j=\infty.
```

For a four-term-progression-free block

```math
D\subseteq[N,2N),
```

coordinated side-anchor deletion and the minimum-translation backbone give

```math
H(\mathcal B(D))+\sum_xH(M_x)
\ge
3H(D)-2\frac{r_3(N)}N-\frac1N,
```

and, after exact middle-multiplicity resolution,

```math
H(Q)+\sum_qH(\Xi_q)+H(\mathcal B(D))
\ge
2H(D)-\frac{r_3(N)}N-\frac1N.
```

Here

```math
\mathcal B(D)
=
\{d-\min D:d\in D,\ d>\min D\}
```

and `Xi_q` is the center-difference fiber for repeated selected step `q`.

Every retained output must be resolved into standard dyadic shells. The genealogy is binary, and for `p>=1`,

```math
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
```

Center, root-anchor, predecessor-anchor, and antichain decompositions control many local multiplicities. They do not by themselves control total reciprocal mass across the full branching tree.

---

## 2. Sharp exact benchmark

The aligned-diamond recursion has

```math
|S_h|=\frac{9\cdot3^h-3}{2},
\qquad
P_h=2^h,
```

so

```math
P_h\asymp |S_h|^{\log_3 2}.
```

There is a computer-certified infinite exact scale-eight family with

```math
L_h=8^{h+1},
\qquad
P_h=\frac12L_h^{1/3}.
```

Inside the exact standard-dyadic equal-translate model,

```math
L'\ge8L,
```

```math
P_h\alpha_h\le C_0(3/4)^h,
```

and

```math
\sum_hP_h\alpha_h\le4C_0.
```

Thus the exact uncontaminated model is sharply classified and summable.

**Primary references:**

- `docs/scale-eight-self-replicating-aligned-diamond.md`;
- `docs/three-translate-dyadic-scale-barrier.md`;
- `docs/exact-three-translate-weighted-density-theorem.md`.

---

## 3. Contaminated path dependence

A certified contaminated genealogy has scale word

```math
\boxed{4,8,4,4,8,4,8,8,8}
```

through the recorded state `S_10`.

With

```math
W_h=P_h^{\mathrm{cert}}\frac{|S_h|}{L_h},
```

one has

```math
\frac{W_5}{W_1}=\frac{91}{32}>1.
```

At depth ten,

```math
L_{10}=536870912,
\qquad
|S_{10}|=265719,
\qquad
P_{10}=1024,
```

and

```math
W_{10}=\frac{265719}{524288}.
```

Universal one-step contraction, contraction over every four- or six-generation window, and universal two-generation recovery are false. Recovery is path-dependent.

The recorded states satisfy

```math
N_{7,2}=N_{7,4}=0,
```

```math
N_{8,2}=N_{8,4}=0,
```

```math
N_{9,2}=N_{9,4}=0,
```

and

```math
N_{10,2}=N_{10,4}=0.
```

These are state-specific finite theorems. They do not imply that every branch reaches the same barrier.

---

## 4. Exact factor-eight basin and Bellman accounting

Every valid positive exact factor-eight child of `S_10` has a certified infinite exact continuation. The complete fan contains

```math
\boxed{408855759}
```

valid children. The unmodified schedule handles `408767151`; the remaining `88608` are covered by finite `+1` repairs.

Every exact tail has charge

```math
\boxed{
\sum_{n\ge0}W_{10+n}
=
\frac{33215}{16384}.
}
```

For constant exact scale factor `c>6`, the affine future-cost function is

```math
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac{6}{c-2}\right).
```

At `c=8`,

```math
\mathfrak B_8=\frac{4P(N+1)}L.
```

For one disjoint three-translate step,

```math
\mathfrak B-W-\mathfrak B'
=
\frac{P(3N+4)}L
\left(1-\frac8c\right).
```

It is convenient to define the positive cheap-step debt

```math
\Delta_c
=
\left[W+\mathfrak B'-\mathfrak B\right]_+
=
\frac{P(3N+4)}L
\left(\frac8c-1\right)
```

for `c<8`. Factors `2` and `4` create debt, factor `8` is neutral, and factors at least `16` create surplus.

The unresolved theorem must pay the sum of these debts over the complete branching family, not merely along one selected path.

---

## 5. State-independent affine obstruction framework

For

```math
G_R(B)=B\cup(B+R)\cup(B+2R),
```

write a candidate progression as

```math
z_i=b_i+\lambda_iR,
\qquad
\lambda_i\in\{0,1,2\}.
```

After layer normalization and reversal, the `80` nonconstant layer words reduce to exactly

```math
\boxed{34}
```

obstruction classes.

Define

```math
r_\lambda=\lambda_1-\lambda_0,
```

```math
a_\lambda=\lambda_0-2\lambda_1+\lambda_2,
```

```math
b_\lambda=\lambda_1-2\lambda_2+\lambda_3,
```

and

```math
\mathcal F_B(A,C;Q)
=
\#\{(x,d):
 x,x+d,x+2d-A,x+3d-(2A+C)\in B,
\ d+Q\ne0\}.
```

Then

```math
\Gamma_\lambda(B;R)
=
\mathcal F_B(a_\lambda R,b_\lambda R;r_\lambda R).
```

The exact two-scale labeled recurrence is

```math
\widetilde\Gamma_\lambda(G_S(B);T)
=
\sum_{\mu\in\{0,1,2\}^4}
\mathcal F_B(
 a_\lambda T+a_\mu S,
 b_\lambda T+b_\mu S;
 r_\lambda T+r_\mu S
).
```

This is the state-independent arithmetic language for contamination growth and obstruction transport.

**Primary reference:** `docs/three-translate-obstruction-coverage-recurrence.md`.

---

## 6. Complete depth-ten cheap-extension barrier

The complete factor-four layer-disjoint domain from `S_10` contains

```math
348012826
```

candidates and splits as

```math
33026376+137142200+177844250.
```

The first block is inherited from the translated `S_9` factor-four theorem. Lifted completion support excludes the second block. The remaining interval is

```math
I_{10}
=
[97474324,613454687].
```

Let

```math
B_9=\{0\}\cup S_9.
```

The exact direct rectangle-support theorem gives

```math
\mathcal F_{B_9}(U,-U;0)>0
\quad
\text{for every }1\le U\le76583776.
```

For separation

```math
S=R_9=134217729,
```

the four transport windows centered at `S,2S,3S,4S` coalesce exactly when

```math
2U+1\ge S.
```

For a target interval `I`, define its exact demand

```math
q_S(I)
=
\max_{T\in I}\min_{1\le k\le4}|T-kS|.
```

At the recorded residual,

```math
q_S(I_{10})=76583771,
```

so the true closure margin is only

```math
76583776-76583771
=
\boxed5.
```

The simpler window-overlap excess is

```math
9474912,
```

which is not the same reserve quantity. The target interval must be part of the state.

This closes the residual and proves

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

**Primary references:**

- `docs/complete-depth-ten-factor-four-exclusion.md`;
- `docs/transport-interval-capacity.md`;
- `src/verify_transport_interval_capacity.py`.

---

## 7. Exact transition and overlap semantics

The restricted replay catalogs enumerate alternative continuation choices. They are not simultaneous deletion-DAG children.

Exact small-state replay counts include

```text
S1 factor 2: 0 valid
S1 factor 4: 4 valid
S2 factor 2: 0 valid
S2 factor 4: 0 valid
S2 factor 8: 203 valid
```

These alternatives cannot be summed in one Bellman row without a separate retention theorem.

For one deterministic coordinated resolution of `S_1`, the simultaneous middle fibers are

```math
\Xi_1=\{16,21,26\},
\qquad
\Xi_5=\{1\},
```

and both are contained in the minimum-translation backbone.

Exhausting all coordinated schedules on `S_1` gives

```text
120 reachable vertex sets
1560 progression-labeled schedules
930 sponsor sequences.
```

Every schedule satisfies

```math
\bigcup_q\Xi_q\subseteq\mathcal B(S_1).
```

Thus raw occurrence mass, distinct-label mass, exact-state quotienting, and set containment are different accounting layers. A valid whole-tree row must state which layer it uses.

---

## 8. Schedule dependence of novel fiber mass

For one schedule `sigma`, define

```math
\mathcal N_\sigma(D)
=
H\left(
\left(\bigcup_q\Xi_q^\sigma\right)
\setminus\mathcal B(D)
\right).
```

On `S_1`, every coordinated schedule has

```math
\mathcal N_\sigma(S_1)=0.
```

On `S_2`, the lexicographic coordinated schedule has

```math
\mathcal N_{\rm lex}(S_2)
=
\frac{239396453}{200655312}>0,
```

but another explicit valid schedule has

```math
\mathcal N_{\sigma_0}(S_2)=0.
```

Therefore

```math
\boxed{
\min_\sigma\mathcal N_\sigma(S_2)=0.
}
```

Raw novel fiber mass is not a parent-only reserve unless the deletion policy is fixed and propagated through the full recursive construction.

The canonical lexicographic policy nevertheless exports positive novel support on each recorded state `S_2` through `S_5`. This keeps policy-dependent export viable, but does not make it schedule invariant.

---

## 9. Parent-intrinsic forced-fork reserve

For a point `x`, let

```math
\mathcal A_x(D)
```

be the set of initial coordinated actions whose sponsor is `x`.

An initial progression

```math
P=\{a,b,c\}
```

is **root-forced** when

```math
\mathcal A_a(D)
\cup
\mathcal A_b(D)
\cup
\mathcal A_c(D)
=
\{P\}.
```

Deletion only removes progressions. If a complete schedule never selected a root-forced `P`, no point of `P` could be deleted and `P` would remain in the terminal residual. Hence every complete coordinated schedule selects every root-forced progression.

Let `Y_q(D)` be the centers of root-forced progressions with step `q`, and let `C_q(D)` be all initially possible centers with that step. Define

```math
\psi_q(D)
=
\min_{
 m\in C_q(D),
 m\le\min Y_q(D)
}
\sum_{
 y\in Y_q(D),
 y>m
}
\frac1{y-m},
```

and

```math
\boxed{
\Psi(D)=\sum_q\psi_q(D).
}
```

Every complete schedule satisfies

```math
\boxed{
\sum_qH(\Xi_q^\sigma)\ge\Psi(D).
}
```

Exact certified lower bounds through the recorded `S_7` are

| state | initial actions | forced actions | lower bound for `Psi` |
|---:|---:|---:|---:|
| `S_1` | 9 | 3 | `1/21` |
| `S_2` | 60 | 5 | `1/18` |
| `S_3` | 398 | 9 | `1/51` |
| `S_4` | 2,195 | 12 | `1/200` |
| `S_5` | 11,523 | 19 | `1/624` |
| `S_6` | 58,708 | 28 | `1/4321` |
| `S_7` | 298,606 | 30 | `1/14046` |

For schedule `sigma`, let `Omega_sigma(D)` be the exact simultaneous overlap charge. Then

```math
\boxed{
\mathcal N_\sigma(D)+\Omega_\sigma(D)
=
\sum_qH(\Xi_q^\sigma)
\ge
\Psi(D).
}
```

This is the first positive parent-intrinsic novelty-or-overlap floor in the current program.

**Primary reference:** `docs/forced-fork-reserve-s1-s7.md`.

---

## 10. Forced-fork Bellman no-go

The direct Bellman-unit feature suggested by the forced-fork mass is

```math
F(S)=P\Psi(S).
```

It is not a standalone stored potential. On the recorded factor-four transition `S_1 -> S_2`,

```math
\Delta_4(S_1)=\frac54,
```

but

```math
F(S_1)-F(S_2)
=
-\frac{18667522}{146796195}<0.
```

Therefore no nonnegative multiple of `P*Psi` can pay that transition as a telescoping stored reserve.

At unit weight, the debt-to-parent-credit ratios on the recorded factor-four steps through `S_5` are greater than `8`, `13`, and `26` respectively. Forced-fork mass remains useful only as transition output feeding a stronger packing or obstruction theorem.

**Primary reference:** `docs/forced-fork-bellman-no-go.md`.

---

## 11. Active theorem: scale-compensated whole-tree packing

The exact finite results now isolate the missing statement.

Cheap replication creates Bellman debt. Every complete deletion schedule exports a positive parent-intrinsic forced-fork novelty-or-overlap charge on the recorded states, but:

1. raw novelty can be erased by changing the schedule;
2. raw overlap can be counted again in descendants;
3. the unnormalized forced-fork reserve decays with scale;
4. `P*Psi` does not telescope as a standalone potential;
5. alternative replay choices are not simultaneous children.

The active target is therefore a scale-compensated packing theorem of the form

```math
\boxed{
\Delta(S)
+
\sum_{S'\in\operatorname{Child}(S)}
\left(
\operatorname{Pack}(S')
+
\Phi_{\rm obs}(S')
\right)
\le
\operatorname{Pack}(S)
+
\Phi_{\rm obs}(S)
+
\operatorname{controlled\ error},
}
```

where:

- `Child(S)` is the complete simultaneous retained family;
- `Pack` tracks imported and duplicated fiber provenance;
- `Phi_obs` tracks target-specific rectangle, completion, and affine-obstruction deficits;
- forced-fork mass supplies unavoidable transition output;
- the same numerical support cannot be charged more than a bounded total amount across the tree.

The concrete mechanism to quantify is

```text
cheap replication
    -> forced middle-fiber output
    -> new obstruction support or imported overlap
    -> completion / rectangle coverage
    -> elimination of later cheap replication.
```

A pathwise statement is insufficient. The inequality must aggregate all simultaneous children after shell resolution and overlap identification.

---

## 12. Approved next targets

1. Build the exact small-state simultaneous-child transition generator, including progression provenance, shell resolution, exact duplicates, strict containments, and imported-prefix identifiers.
2. Define a scale-normalized packing coordinate for forced-fork overlap and test it on complete child aggregates, not selected paths.
3. Connect forced-fork fibers to the 34 affine obstruction classes and direct rectangle support.
4. Prove bounded reuse of imported fiber labels across descendants, or export repeated reuse into smaller difference fibers.
5. Combine target interval demand, completion deficit, and packing charge in the exact rational LP harness.
6. Extract the smallest exact failing state whenever a candidate feature family is infeasible.
7. Establish the branching Carleson inequality required to sum all pre-basin states.

---

## 13. Superseded or false targets

Do not use without materially new hypotheses:

1. bounded or polylogarithmic identical-history persistence;
2. cardinality-only subpower bounds below exponent `log_3 2`;
3. universal one-step `3/4` contraction for contaminated backbones;
4. universal strict contraction at every non-exact step;
5. contraction over every four- or six-step window;
6. universal two-generation recovery after an exact factor-eight step;
7. extrapolating one selected continuation to the whole tree;
8. treating one or many exact tails as a whole-tree theorem;
9. treating replay siblings as simultaneous deletion-DAG children;
10. treating pathwise summability as sufficient;
11. treating `nu(B)/S>1/2` as a complete transport reserve;
12. treating novel fiber mass as schedule independent;
13. treating `P*Psi` as a standalone stored Bellman potential;
14. the rejected depth-ten anchor reduction;
15. additional contiguous `S_10` candidate-prefix certification.

The complete `S_10` cheap-extension theorem is a finished state-specific component. The unresolved problem is now precise: convert unavoidable deletion output into a scale-compensated, bounded-reuse whole-tree packing reserve.

---

## 14. Reproduction and navigation

Run all lightweight exact reserve checks with

```bash
bash src/run_verify_transport_reserve.sh
```

Key documents:

- `docs/transport-interval-capacity.md`;
- `docs/branching-reserve-lp.md`;
- `docs/s1-deletion-dag-overlap-ledger.md`;
- `docs/exhaustive-s1-deletion-schedules.md`;
- `docs/s2-zero-novelty-schedule.md`;
- `docs/lexicographic-novelty-s1-s5.md`;
- `docs/s1-schedule-overlap-floor.md`;
- `docs/forced-fork-reserve-s1-s7.md`;
- `docs/forced-fork-bellman-no-go.md`;
- `docs/certainty-ledger.md`;
- `docs/research-decision-history.md`.

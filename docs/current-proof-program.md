# Current proof program: obstruction export and whole-tree packing

## Status

This is the authoritative overview of the active program for Erdős Problem #3:

> If `A subseteq N` and `sum_{n in A} 1/n = infinity`, must `A` contain arbitrarily long arithmetic progressions?

The full problem remains open. This repository studies the four-term case. Claims below are proved internally or computationally certified as stated, but await independent expert review.

---

## 1. Dyadic reduction and deletion genealogy

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

For a four-term-progression-free block `D`, coordinated side-anchor deletion and the minimum-translation backbone give

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

Every recursive output must be resolved into standard dyadic shells. For `p>=1`, the binary genealogy satisfies

```math
\sum_{u\text{ output of }a}u^p\le2^{1-p}a^p.
```

These results control local multiplicity and positive moments. Reciprocal mass requires a genuinely treewise packing theorem.

---

## 2. Exact uncontaminated benchmark

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

There is a certified infinite exact scale-eight family with

```math
L_h=8^{h+1},
\qquad
P_h=\frac12L_h^{1/3}.
```

Inside the exact equal-translate model,

```math
P_h\alpha_h\le C_0(3/4)^h,
```

and therefore

```math
\sum_hP_h\alpha_h\le4C_0.
```

Thus the exact uncontaminated model is summable.

---

## 3. Contaminated path obstruction

A certified contaminated genealogy has scale word

```math
\boxed{4,8,4,4,8,4,8,8,8}
```

through `S_10`.

With

```math
W_h=P_h\frac{|S_h|}{L_h},
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

Universal one-step contraction, fixed short-window contraction, and universal two-generation recovery are false. Recovery is path-dependent.

---

## 4. Exact factor-eight basin and Bellman debt

Every valid positive exact factor-eight child of `S_10` has a certified infinite exact continuation. The complete fan contains

```math
\boxed{408855759}
```

valid children, and every exact tail has charge

```math
\sum_{n\ge0}W_{10+n}=\frac{33215}{16384}.
```

For constant exact scale factor `c>6`, the affine future-cost function is

```math
\mathfrak B_c(N,P,L)
=
\frac{cP}{(c-6)L}
\left(N+\frac6{c-2}\right).
```

For one disjoint three-translate step,

```math
\mathfrak B-W-\mathfrak B'
=
\frac{P(3N+4)}L\left(1-\frac8c\right).
```

The positive cheap-step debt for `c<8` is

```math
\Delta_c
=
\frac{P(3N+4)}L\left(\frac8c-1\right).
```

Factors `2` and `4` create debt, factor `8` is neutral, and larger factors create surplus.

---

## 5. State-independent affine obstruction language

For

```math
G_R(B)=B\cup(B+R)\cup(B+2R),
```

nonconstant layer words reduce, after normalization and reversal, to exactly

```math
\boxed{34}
```

affine obstruction classes.

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
\mathcal F_B(a_\lambda R,b_\lambda R;r_\lambda R),
```

and the exact two-scale recurrence is

```math
\widetilde\Gamma_\lambda(G_S(B);T)
=
\sum_\mu
\mathcal F_B(
 a_\lambda T+a_\mu S,
 b_\lambda T+b_\mu S;
 r_\lambda T+r_\mu S
).
```

This is the state-independent arithmetic framework for contamination growth.

---

## 6. Complete depth-ten cheap-extension barrier

The complete factor-four domain from `S_10` contains

```math
348012826
```

candidates, partitioned as

```math
33026376+137142200+177844250.
```

Inheritance removes the first block and lifted completion support removes the second. The residual interval is

```math
I_{10}=[97474324,613454687].
```

For

```math
B_9=\{0\}\cup S_9,
```

the exact direct rectangle-support theorem gives

```math
\mathcal F_{B_9}(U,-U;0)>0
\quad
\text{for }1\le U\le76583776.
```

With

```math
S=134217729,
```

the four transport windows centered at `S,2S,3S,4S` coalesce when

```math
2U+1\ge S.
```

For a target interval `I`, define

```math
q_S(I)=\max_{T\in I}\min_{1\le k\le4}|T-kS|.
```

At `I_{10}`,

```math
q_S(I_{10})=76583771,
```

so the true closure margin is

```math
76583776-76583771=\boxed{5}.
```

This proves

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

The state-specific `S_10` barrier is complete. It is not a whole-tree theorem.

---

## 7. Replay siblings, schedules, and forced output

The replay catalog enumerates alternative outer separation choices. For example:

```text
S1 factor 4: 4 alternatives
S2 factor 8: 203 alternatives.
```

These are not automatically simultaneous deletion-DAG children.

For schedule `sigma`, define novel middle-fiber mass

```math
\mathcal N_\sigma(D)
=
H\left(
\left(\bigcup_q\Xi_q^\sigma\right)
\setminus\mathcal B(D)
\right).
```

Every coordinated schedule on `S_1` has zero novelty. The lexicographic `S_2` schedule has

```math
\mathcal N_{\rm lex}(S_2)
=
\frac{239396453}{200655312}>0,
```

but another valid `S_2` schedule has zero novelty. Hence

```math
\min_\sigma\mathcal N_\sigma(S_2)=0.
```

Raw novelty is not parent-intrinsic.

A root-forced progression is an initial progression whose own action is the only initial coordinated action capable of deleting any of its three points. Every complete schedule must select every root-forced progression. This yields

```math
\sum_qH(\Xi_q^\sigma)\ge\Psi(D).
```

Positive exact lower bounds are certified through `S_7`:

```text
1/21,1/18,1/51,1/200,1/624,1/4321,1/14046.
```

However,

```math
F(S)=P\Psi(S)
```

is not a standalone Bellman potential. On `S_1 -> S_2`,

```math
F(S_1)-F(S_2)<0
```

while the factor-four debt is positive.

---

## 8. Raw simultaneous transition exporter

The fixed-policy exporter

```text
src/export_simultaneous_deletion_transition.py
```

records:

- every selected progression and sponsor;
- terminal outputs and residual;
- backbone and middle fibers;
- every standard-dyadic recursive shell occurrence;
- point-level provenance;
- exact duplicate state classes;
- strict containments;
- partial overlaps;
- terminal-recursive overlap;
- exact occurrence, union, imported, novel, and duplicate masses.

The certified frontier is:

| parent | raw occurrences | state classes | duplicate classes | containments | partial overlaps |
|---:|---:|---:|---:|---:|---:|
| `S_1` | 5 | 4 | 1 | 1 | 0 |
| `S_2` | 11 | 10 | 1 | 3 | 5 |
| `S_3` | 25 | 21 | 3 | 23 | 15 |
| `S_4` | 46 | 34 | 7 | 91 | 35 |
| `S_5` | 68 | 51 | 11 | 145 | 88 |
| `S_6` | 94 | 71 | 15 | 209 | 150 |
| `S_7` | 127 | 95 | 20 | 345 | 214 |

The exporter is complete for the fixed policy at each tested parent. It emits the raw occurrence family **before** a retention quotient.

---

## 9. Exact local occurrence packing

For raw recursive shell occurrences `C_i`, define

```math
m(u)=|\{i:u\in C_i\}|,
\qquad
M=\max_um(u).
```

Then

```math
\sum_iH(C_i)=\sum_u\frac{m(u)}u
\le
M H\left(\bigcup_iC_i\right).
```

The certified maximum multiplicities are

```text
S1,...,S7: 2,3,7,11,12,13,16.
```

The harmonic-average multiplicity

```math
\overline m_H
=
\frac{\sum_iH(C_i)}{H(\bigcup_iC_i)}
```

is bounded by

```text
8/5,11/10,11/10,9/8,9/8,9/8,9/8.
```

Worst-case multiplicity is not stable. High multiplicity concentrates on relatively large inherited labels, so local reciprocal-mass inflation remains modest. This does not control cross-generation reuse.

---

## 10. Terminal-fiber incidence and cycle obstruction

Let `Q` be the terminal step set. Draw an edge

```math
q\longrightarrow u
```

when

```math
u\in Q\cap\Xi_q.
```

The graph is acyclic at `S_1` and `S_2`. At `S_3`, it contains the cycle

```math
61\longleftrightarrow303,
```

which persists through `S_6`.

At `S_7`, the cyclic component expands to

```math
\boxed{\{1,5,61,303,1597,8195,323640\}}.
```

Therefore any retention potential based on a strict decreasing rank of terminal labels is false on the recorded genealogy.

The `S_7` terminal-recursive overlap also includes nonhistorical labels:

```text
5,49158,323640.
```

A state containing only the latest separation or the list of historical separations is inadequate.

---

## 11. SCC quotient and internal-capacity no-go

Collapsing the terminal-fiber graph into strongly connected components gives an acyclic condensation graph. For a component `C`, define

```math
V(C)=\sum_{u\in C}\frac1u
```

and

```math
T(C)=
\sum_{
(q,u)\text{ internal edge}
}
\frac1u.
```

For the two-cycle `C={61,303}` from `S_3` through `S_6`,

```math
T(C)=V(C),
```

so unit harmonic vertex capacity is exactly balanced.

At `S_7`, the seven-label component has `24` internal edges and

```math
T(C)-V(C)
=
\boxed{
\frac{43727503229099}{1043823972523464}
}>0.
```

Equivalently,

```math
\frac{T(C)}{V(C)}
=
\frac{6588286581562338}{6369649065416843}
>1.
```

Thus the SCC quotient solves graph ordering but not internal recycling. Capacity equal only to harmonic vertex mass fails at `S_7`.

---

## 12. Missing layer: retention and bounded reuse

Exact duplicate states can be identified mechanically. They cannot automatically be discarded because different occurrences can carry different provenance and future histories.

By `S_7`, the raw transition has

```text
20 exact duplicate classes
345 strict containment relations
214 partial overlap relations.
```

The missing theorem must specify:

1. which exact duplicates merge;
2. how provenance multiplicity is retained;
3. how strict containment is charged;
4. how partial overlap is charged;
5. how terminal-recursive overlap is handled;
6. how cyclic SCC internal recycling is funded;
7. how imported labels are matched across generations;
8. how often the same numerical or provenance label may be charged;
9. which discarded mass becomes controlled error.

Only after this theorem may the raw payload be converted into the `children` array of a branching LP row.

---

## 13. Active theorem: scale-compensated whole-tree packing

The current target is

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
\operatorname{controlled\ error}.
}
```

Here:

- `Child(S)` is the complete retained simultaneous family;
- `Pack` tracks provenance, containment, partial overlap, and SCC internal capacity;
- `Phi_obs` tracks target-specific rectangle, completion, and affine-obstruction deficits;
- forced-fork mass supplies unavoidable transition output;
- bounded reuse prevents repeated payment by the same support.

The mechanism to quantify is

```text
cheap replication
    -> forced middle-fiber output
    -> new obstruction support or imported overlap
    -> cyclic component recycling or outward export
    -> completion / rectangle coverage
    -> elimination of later cheap replication.
```

A pathwise estimate is insufficient.

---

## 14. Approved next targets

1. Attach explicit internal capacity vectors to the certified SCC quotients.
2. Test whether internal recycling plus outgoing capacity is paid by incoming capacity plus obstruction export.
3. Keep provenance edges while merging exact numerical state classes.
4. Introduce label-reuse capacities for containment and partial-overlap graphs.
5. Connect cyclic-component output to the 34 affine obstruction classes and rectangle support.
6. Feed the proved retention convention into the exact rational LP harness.
7. Emit the smallest exact failing transition for every candidate convention.
8. Establish the branching Carleson inequality for all pre-basin states.

---

## 15. Superseded or false targets

Do not use without materially new hypotheses:

1. universal local `3/4` contraction in contaminated states;
2. fixed short-window contraction;
3. universal two-generation recovery;
4. extrapolating one path or one exact fan to the full tree;
5. treating replay siblings as simultaneous children;
6. treating pathwise summability as sufficient;
7. treating `nu(B)/S>1/2` as a complete target reserve;
8. treating novel fiber mass as schedule independent;
9. treating `P*Psi` as a standalone stored Bellman potential;
10. copying raw simultaneous occurrences directly into an LP child sum;
11. merging provenance-distinct exact duplicates without a convention;
12. assuming a uniform local maximum-overlap constant;
13. assigning a strict decreasing rank to terminal-fiber labels;
14. assigning each SCC only its harmonic vertex mass as capacity;
15. tracking only the latest or historical replication separations;
16. the rejected depth-ten anchor reduction.

---

## 16. Reproduction and navigation

Run the complete lightweight suite:

```bash
bash src/run_verify_transport_reserve.sh
```

Run only the transition frontier:

```bash
bash src/run_verify_transition_frontier.sh
```

Key documents:

- `docs/complete-depth-ten-factor-four-exclusion.md`;
- `docs/transport-interval-capacity.md`;
- `docs/branching-reserve-lp.md`;
- `docs/simultaneous-deletion-transition-exporter.md`;
- `docs/simultaneous-transition-frontier-s7.md`;
- `docs/recursive-occurrence-multiplicity.md`;
- `docs/terminal-fiber-incidence-graph.md`;
- `docs/terminal-fiber-scc-quotient.md`;
- `docs/forced-fork-reserve-s1-s7.md`;
- `docs/forced-fork-bellman-no-go.md`;
- `docs/certainty-ledger.md`;
- `docs/research-decision-history.md`.

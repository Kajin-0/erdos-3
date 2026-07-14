# Current proof program: affine pair-resource activation

## Status

This is the authoritative overview for the four-term case of Erdős Problem #3. The full reciprocal-sum problem remains open. Durable claims are tracked in `docs/certainty-ledger.md`.

The project is no longer searching for another finite-depth fitted feature or a new overlap quotient. Affine closure and pair-token containment now give exact whole-tree no-double-payment semantics. The active theorem target is an economical pair-activation or multiscale exposure bound that avoids paying the full latent root-pair energy of the initial dyadic block.

## Latest exact refinement: backbone-anchor transfer

The fourth-to-fifth survivor classification is complete for the certified baseline transition:

```text
surviving roots              = 1,015
surviving backbone roots     = 1,015
surviving middle-fiber roots = 0
minimum-anchor roots         = 12
minimum anchors with no raw output = 12
```

For a recursive parent state `S` with `m=min(S)`, the exact prospective translation reserve is

```math
A(S)
=
\sum_{u\in S,\ u>m}
\left(
\frac1{u-m}-\frac1u
\right).
```

Every retained survivor gain is the harmonic measure of an anchor-survivor interval `(u-m,u]`. The aggregate baseline values are

```text
sum A(S)                 = 9.928706884742...
retained survivor gain   = 1.816777911848...
minimum-anchor release   = 0.364729899662...
```

Thus scalar anchor mass is not complete payment. The missing state must control provenance-labeled anchor-survivor intervals, their reuse, and the release created when they terminate or are removed.

Primary reference: `docs/backbone-anchor-root-transfer.md`.

---

## Symbolic affine pivot packing theorem

For an affine root state

```math
S_r(P)=\{p-r:p\in P\},
\qquad
r<\min P,
```

minimum translation at `a=min(P)` is exactly the reference pivot

```math
r\longrightarrow a,
\qquad
p-r\longrightarrow p-a.
```

Define root-pair energy

```math
J(P)
=
\sum_{x<y,\ x,y\in P}
\frac1{y-x}.
```

For pairwise root-disjoint retained children `S_a(Q_i)`,

```math
\boxed{
\sum_i
\left(
H(S_a(Q_i))+J(Q_i)
\right)
\le
J(P).
}
```

Every harmonic child term is charged to one ordered pivot pair `(a,p)`, while each child pair energy uses a distinct pair internal to one `Q_i`. Thus cross-generation reuse is exactly controlled inside an affine pivot forest.

This does **not** bound the entering `J(P)`. The active theorem has separated into two tasks:

1. certify and generalize entry into the affine root-pivot regime;
2. pay for entering pair energy through earlier recursive production, terminal first appearance, or arithmetic obstruction export.

Primary reference: `docs/affine-pivot-pair-energy.md`.

---

## Affine pair-token first-appearance theorem

For every affine point with current label `u` and root provenance `p`,

```math
r=p-u
```

is its root reference. Thus the coarse point token `(u,p)` is exactly the root pair `(r,p)` and has pair weight `1/(p-r)=1/u`.

For any affine forest over root universe `P_0`,

```math
\boxed{
\sum_{\text{first-appearance }(u,p)}\frac1u
\le
J(P_0).
}
```

A repeated coarse token is true reuse of the same pair capacity. Immediate provenance may distinguish occurrence histories, but it must not be treated as a second copy of the pair resource.

This gives a precise decomposition

```text
raw point mass
=
first-appearance pair mass
+
pair-reuse mass.
```

The first term is controlled by `J(P_0)`. The remaining structural target is pair-reuse mass plus payment for the entering pair energy.

Primary reference: `docs/affine-root-pair-token-ledger.md`.

---

## First exact pair-energy Bellman row

The adversarial fourth-to-fifth retained transition is now closed by a state-independent symbolic potential.

Both recursive frontiers are fully affine and have no root or pair duplication:

```text
R4: 12 states, 1717 roots, 370505 distinct pairs
R5: 13 states, 1015 roots, 106381 distinct pairs
```

The complete fifth output satisfies

```math
\boxed{
H(F_5)+J(R_5^{\rm rec})
\le
J(R_4^{\rm rec}).
}
```

Exact values:

```text
H(F5)+J(R5_rec) = 1586.466623468978...
J(R4_rec)       = 2743.858245303490...
surplus          = 1157.391621834512...
ratio            = 0.578188259610...
```

This is a legitimate retained-child Bellman row with no fitted coefficient. It explains why raw recursive harmonic mass may expand while cumulative affine capacity contracts strongly.

The active frontier moves earlier: determine where affine coordinates and pair uniqueness first emerge, and control occurrence-versus-union pair energy before generation four.

Primary reference: `docs/fifth-generation-pair-energy-bellman-row.md`.

---

## Exact pair-resource ownership at the fifth frontier

The scalar pair-energy row has been upgraded to an explicit set-valued resource partition.

The fourth recursive frontier contains

```text
1,717 current pairs
370,505 latent pairs
372,222 total pair resources.
```

The complete fifth retained family uses

```text
1,032 current pairs
106,381 recursive latent pairs
107,413 total pair resources.
```

Every fifth resource is a distinct fourth **latent** pair. No fifth resource uses a fourth current pair and no pair is paid twice.

```math
\boxed{
\operatorname{Used}(F_5)
+
\operatorname{Unused}(R_4\to F_5)
=
H(R_4)+J(R_4).
}
```

Exact masses:

```text
used   = 1586.466623468978...
unused = 1158.927755372724...
total  = 2745.394378841703...
```

This closes containment, terminal-recursive interaction, and repeated-payment semantics on the recorded transition.

Primary reference: `docs/fifth-generation-pair-resource-partition.md`.

---

## Universal affine closure and pair-resource containment

Affine structure is not a late-generation accident. It is preserved exactly by every output type in the coordinated deletion construction.

For an affine parent

```math
S_r(P)=\{p-r:p\in P\},
```

one has:

```text
terminal residual: S_r(P_R)
backbone shell:    S_a(Q), a=min(P)
middle-fiber shell:S_{t_0}(Q),
```

where `t_0` is the sponsor root attached to the minimum selected center for that step.

For the middle fiber, if centers are `c_j=p_j-r` and sponsors have roots `t_j=p_j+epsilon(q)q`, then

```math
c_j-c_0
=p_j-p_0
=t_j-t_0.
```

Thus every descendant remains affine under the repository provenance convention.

Define the parent resource universe

```math
\mathcal U_r(P)
=
\{(r,p):p\in P\}
\cup
\binom P2.
```

Every terminal current pair, recursive current pair, and recursive latent pair emitted by the parent belongs to `\mathcal U_r(P)`. Therefore for any simultaneous retained family,

```math
\boxed{
\mathcal U_\cup(\mathrm{Child}(\mathcal F))
\subseteq
\mathcal U_\cup(\mathcal F).
}
```

The global overlap and repeated-payment problem is therefore solved at the level of distinct pair tokens. Occurrence-valued expansion is exactly

```math
R_{\rm pair}
=
W_{\rm occ}-W_\cup.
```

The remaining theorem is no longer a retention quotient or cross-generation reuse theorem. It is an economical **pair-activation theorem**: avoid prepaying the full latent pair energy, or charge activated pair mass to summable production, terminal, or arithmetic obstruction terms.

Primary reference: `docs/affine-output-closure-and-pair-containment.md`.

---

## Third-to-fourth pair-resource contraction

The affine pair-resource regime already holds before root uniqueness. All fourteen third recursive parents are affine, every fourth current or latent resource is contained, and pair multiplicity is at most two.

```text
R3 occurrence resource = 7828.862146571999...
F4 occurrence resource = 2747.630136815823...

R3 union resource      = 7821.150527735019...
F4 union resource      = 2747.496183058024...
```

Repeated-pair mass contracts from

```text
7.711618836980... -> 0.133953757799...
```

with zero missing resource tokens. Therefore `R_3 -> F_4` is removed from the obstruction frontier in both occurrence and union conventions.

Primary reference: `docs/third-to-fourth-pair-resource-contraction.md`.

---

## Certified residual-sponsor backbone refinement

A completed deletion schedule partitions each affine parent root set as

```math
P=Q\sqcup\Sigma,
```

where `Q` is the three-AP-free residual and `Sigma` is the deleted sponsor core. Splitting the minimum backbone before dyadic shelling into translated residual-root and sponsor-root pieces preserves the complete raw numerical and harmonic output. Every residual-root shell is terminal.

On the certified `R_4 -> F_5` transition the exact split preserves

```text
raw support union          = 1,489
raw point occurrences      = 2,972
raw harmonic occurrence    = 25.589294609269...
```

while changing the retained recursive frontier by

```text
recursive points           1,015 -> 864
recursive harmonic mass    2.042771729559... -> 1.873962098445...
latent pair occurrences    106,381 -> 74,191
union pair-resource mass   1,586.466623468978... -> 1,181.930568734065...
```

Terminal mass rises by `0.369683464666...`; recursive mass falls by `0.168809631114...`. The refinement therefore exposes additional terminal support without importing a new unshifted residual output and removes `404.536054734914...` of union-valued continuing pair capacity.

The active analytical object is now the sponsor core. Future transfer inequalities should charge

```math
\{(a,s):s\in\Sigma\}
\cup
inom\Sigma2
```

to selected-progression incidence, terminal first appearance, or arithmetic obstruction export, rather than prepaying all pairs in the original root set.

Primary reference: `docs/residual-sponsor-backbone-refinement.md`.

---

## Certified residual-sponsor backbone refinement

A completed deletion schedule partitions each affine parent root set as

```math
P=Q\sqcup\Sigma,
```

where `Q` is the three-AP-free residual and `Sigma` is the deleted sponsor core. Splitting the minimum backbone before dyadic shelling into translated residual-root and sponsor-root pieces preserves the complete raw numerical and harmonic output. Every residual-root shell is terminal.

On the certified `R_4 -> F_5` transition the exact split preserves

```text
raw support union          = 1,489
raw point occurrences      = 2,972
raw harmonic occurrence    = 25.589294609269...
```

while changing the retained recursive frontier by

```text
recursive points           1,015 -> 864
recursive harmonic mass    2.042771729559... -> 1.873962098445...
latent pair occurrences    106,381 -> 74,191
union pair-resource mass   1,586.466623468978... -> 1,181.930568734065...
```

Terminal mass rises by `0.369683464666...`; recursive mass falls by `0.168809631114...`. The refinement therefore exposes additional terminal support without importing a new unshifted residual output and removes `404.536054734914...` of union-valued continuing pair capacity.

The active analytical object is now the sponsor core. Future transfer inequalities should charge

```math
\{(a,s):s\in\Sigma\}
\cup
\binom\Sigma2
```

to selected-progression incidence, terminal first appearance, or arithmetic obstruction export, rather than prepaying all pairs in the original root set.

Primary reference: `docs/residual-sponsor-backbone-refinement.md`.

---

## Certified residual-sponsor backbone refinement

A completed deletion schedule partitions each affine parent root set as

```math
P=Q\sqcup\Sigma,
```

where `Q` is the three-AP-free residual and `Sigma` is the deleted sponsor core. Splitting the minimum backbone before dyadic shelling into translated residual-root and sponsor-root pieces preserves the complete raw numerical and harmonic output. Every residual-root shell is terminal.

On the certified `R_4 -> F_5` transition the exact split preserves

```text
raw support union          = 1,489
raw point occurrences      = 2,972
raw harmonic occurrence    = 25.589294609269...
```

while changing the retained recursive frontier by

```text
recursive points           1,015 -> 864
recursive harmonic mass    2.042771729559... -> 1.873962098445...
latent pair occurrences    106,381 -> 74,191
union pair-resource mass   1,586.466623468978... -> 1,181.930568734065...
```

Terminal mass rises by `0.369683464666...`; recursive mass falls by `0.168809631114...`. The refinement therefore exposes additional terminal support without importing a new unshifted residual output and removes `404.536054734914...` of union-valued continuing pair capacity.

The active analytical object is now the sponsor core. Future transfer inequalities should charge

```math
\{(a,s):s\in\Sigma\}
\cup
\binom\Sigma2
```

to selected-progression incidence, terminal first appearance, or arithmetic obstruction export, rather than prepaying all pairs in the original root set.

Primary reference: `docs/residual-sponsor-backbone-refinement.md`.

---

## 1. Foundation and recorded exact path

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

Coordinated side-anchor deletion produces a three-term-progression-free residual and recursive backbone/middle-fiber outputs. The exact local inequalities are

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

and `W_5/W_1=91/32>1`. Universal local and fixed-window contraction are false.

At `S_10`, exact inheritance, completion support, and rectangle transport prove

```math
\boxed{N_{10,2}=N_{10,4}=0.}
```

Every valid exact factor-eight child has a certified summable tail. This closes the recorded state, not the full branching tree.

---

## 2. Retained-child construction

The retained quotient used on the adversarial `S_7` construction is:

1. quotient numerically identical states;
2. retain deterministic provenance representatives;
3. form same-shell point-intersection conflict graphs;
4. choose a maximum-total-harmonic independent set in each component.

The resulting certified frontier is:

| retained level | total states | total points | terminal states | terminal points | recursive states | recursive points |
|---|---:|---:|---:|---:|---:|---:|
| first | 21 | 11,753 | — | — | 21 | 11,753 |
| second | 27 | 7,925 | 13 | 43 | 14 | 7,882 |
| third | 32 | 4,899 | 18 | 110 | 14 | 4,789 |
| fourth | 23 | 1,794 | 11 | 77 | 12 | 1,717 |
| fifth | 21 | 1,032 | 8 | 17 | 13 | 1,015 |

Every recorded family is point-disjoint within its generation. The baseline retention optimum is unique through generation five. Nearby policy tests include two nonunique components, but their tied maximum-harmonic optima have identical recursive mass.

This quotient is a rigorous finite test object. It is not proved globally optimal or canonical.

---

## 3. Recursive and terminal mass

Let `H_g^rec` denote recursively continuing retained harmonic mass. The four recorded ratios are:

```math
0.937
<
\frac{H_2^{\mathrm{rec}}}{H_1}
<
0.938,
```

```math
2.011553
<
\frac{H_3^{\mathrm{rec}}}{H_2^{\mathrm{rec}}}
<
2.011554,
```

```math
2.849279
<
\frac{H_4^{\mathrm{rec}}}{H_3^{\mathrm{rec}}}
<
2.849280,
```

and

```math
1.329813
<
\frac{H_5^{\mathrm{rec}}}{H_4^{\mathrm{rec}}}
<
1.329814.
```

Raw recursive harmonic mass is not an iterating Bellman potential.

Terminal output must be carried separately through a first-appearance ledger. It cannot be discarded, and it must not be counted as persistent recursive debt.

---

## 4. Terminal identities

Each terminal point carries

```text
current label u
original S7 root provenance p
immediate provenance i
parent retained class
source type and source step
dyadic shell.
```

The coarse token `(u,p)` collides across generations. The refined token

```math
\tau^+(u)=(u,p,i)
```

has no recorded collision through generation five. This is finite evidence, not a global injectivity theorem.

For any fixed token map, deterministic first appearance gives an exact disjoint global bookkeeping ledger. The unresolved theorem is to prove that a bounded natural token is collision-sound and that its weighted union is summable.

---

## 5. Static reserve witnesses are exhausted

Two small three-generation witnesses were exact:

```math
\Phi_g^{\mathrm{rep}}=H_g+2R_g
```

and

```math
\Phi_g^{\mathrm{tail}}=H_g+4T_g.
```

Both fail at generation four.

The exact four-generation feature LP found a sparse witness

```math
H_g+74R_g
```

with ratios approximately

```text
0.618519
0.122394
0.991321.
```

The minimum fitted coefficient is approximately `73.015129`, so the final margin is already small.

Generation five gives the decisive no-go:

```math
R_4=R_5=0,
```

while

```math
\frac{H_5^{\mathrm{rec}}}{H_4^{\mathrm{rec}}}>1.329813.
```

Therefore no finite coefficient in `H+kR` can repair the fourth-to-fifth transition.

The exact eleven-feature four-transition LP may be retained as a diagnostic, but it is no longer the strategic driver. Another fitted feature without a state-independent transfer law would repeat the same failure pattern.

---

## 6. Fourth-to-fifth policy sensitivity

The first failing transition was tested under fourteen exact local deletion policies:

```text
all lexicographic
all reverse lexicographic
one single-parent reverse flip for each of the 12 fourth recursive parents.
```

Every raw family was passed through the same maximum-harmonic retention quotient, including all tied optima.

All tested policies expand recursively. The best is `reverse_parent_82`:

```math
\boxed{
\frac{9579}{8000}
<
\frac{H_{5,82\text{-reverse}}^{\mathrm{rec}}}
     {H_4^{\mathrm{rec}}}
<
\frac{18709}{15625}
}
```

or `1.197375982982...`.

Thus the failure is quantitatively policy-sensitive but is not removed by the nearest natural lexicographic/reverse perturbations. This is not an all-policy theorem.

---

## 7. Root-lineage transfer identity

At generations four and five, every retained root provenance has multiplicity one. Let `S` be the roots that survive recursively and `E` the roots that exit. If `u_g(p)` is the unique current descendant of root `p`, then

```math
\boxed{
H_{g+1}^{\mathrm{rec}}-H_g^{\mathrm{rec}}
=
\sum_{p\in S}
\left(\frac1{u_{g+1}(p)}-\frac1{u_g(p)}\right)
-
\sum_{p\in E}\frac1{u_g(p)}.
}
```

Define survivor scale gain `G` and exiting parent release `L` by the two sums. The certified fourth-to-fifth decomposition is

```text
surviving roots = 1,015
exiting roots = 702
  terminalized = 17
  dropped      = 685
```

and

```text
G_4→5 = 1.816777911848...
L_4→5 = 1.310139720502...
H5_rec-H4_rec = 0.506638191346...
```

with

```math
1.386705
<
\frac{G_{4\to5}}{L_{4\to5}}
<
1.386706.
```

No root splits between recursive and terminal output, and the complete fifth retained family has root multiplicity one.

The failure mechanism is therefore:

```text
unique-lineage scale gain > released parent mass.
```

It is not repeated-root branching.

---

## 8. Active theorem target

The whole-tree objective remains

```math
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
```

The missing coordinate must be cumulative and path-aware. It must remember future scale-gain capacity after local multiplicity disappears.

The desired transition law has the form

```math
H_{g+1}^{\mathrm{rec}}
+A_{g+1}
+T_{g+1}^{\mathrm{first}}
\le
H_g^{\mathrm{rec}}
+A_g
+\Phi_{\mathrm{obs},g}
+\varepsilon_g,
```

where:

- `A_g` is state-independent ancestor-path capacity;
- `T_{g+1}^{first}` is newly terminal first-appearance credit;
- `Phi_obs` is completion, rectangle, or cheap-extension exclusion credit;
- `sum_g epsilon_g` must be controlled.

A candidate `A` is admissible only if it has:

1. a state-independent definition;
2. a one-step transfer identity or inequality;
3. a bounded-reuse interpretation;
4. a clear telescoping role.

LP correlation alone is insufficient.

---

## 9. Approved next targets

1. Quantify occurrence versus union pair resources on `R_1,R_2,R_3` and isolate exact repeated-pair mass.
2. Replace full latent `J(P)` by an activated-pair ledger that opens a token only when a pivot, terminal point, or recursive child actually uses it.
3. Prove a multiscale bound for activated pair mass using four-AP-freeness, fixed-step run structure, coordinated deletion, or stopping-time sparsity.
4. Relate activated pair mass to the existing one-generation harmonic production and summable `r_3(N)/N` error.
5. Determine whether completion, rectangle support, and cheap-extension exclusion pay for dense clusters of short root pairs.
6. Compute exact first-appearance and reused `(u,p)` mass by transition; immediate provenance remains metadata, not additional pair credit.
7. Use earlier-generation finite diagnostics only to discover the activation law or its smallest obstruction.
8. Do not propagate generation six.

Generation six is blocked until a specific state-independent transfer lemma exists.

---

## 10. Stop list

Do not infer:

- pathwise summability implies whole-tree summability;
- replay siblings are simultaneous children;
- local policy optimality is global;
- duplicate quotienting alone resolves overlap;
- maximum-harmonic retention is globally optimal;
- terminal mass may be discarded;
- `(u,p,i)` is globally collision-sound;
- first-appearance bookkeeping bounds token-union mass;
- the `31/500` row iterates;
- raw recursive mass follows a stable short-period pattern;
- any finite `H+kR` witness iterates;
- nearby-policy expansion is an all-policy theorem;
- a fitted feature is a theorem without a transfer law;
- another retained generation is useful without a predeclared conceptual test.

---

## 11. Reproduction

Push-gating lightweight suite:

```bash
bash src/run_verify_ci_lightweight.sh
```

Established extended frontier:

```bash
bash src/run_verify_transport_reserve.sh
```

Retained-generation, policy-sensitivity, and root-transfer frontier:

```bash
bash src/run_verify_terminal_sink_ledger.sh
```

None of the retained-generation work is part of push-gating lightweight CI.

Primary recent references:

- `docs/fourth-to-fifth-root-transfer.md`;
- `docs/fourth-to-fifth-policy-sensitivity.md`;
- `docs/fifth-generation-repeated-root-no-go.md`;
- `docs/fourth-generation-provenance-reserve-frontier.md`;
- `docs/terminal-sink-first-appearance-ledger.md`;
- `docs/retained-terminal-sink-identity-ledger.md`.

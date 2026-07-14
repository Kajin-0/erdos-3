# Current proof program: affine pair-resource activation

## Status

This is the authoritative overview for the four-term case of Erdős Problem #3. The full reciprocal-sum problem remains open. Durable claims are tracked in `docs/certainty-ledger.md`.

The active program now has a scale-critical three-AP transfer row. First side, middle, and doubled preimages partition one parent target with capacities `1/2,1/4,1/4`; unbounded collisions transfer to lower-scale reference-gap and rectangle-aspect tokens. The remaining theorem is global first-appearance control of the critical collision excess, plus external-completion and terminal release.

## Corrected first retained frontier

Terminal stopping is structural. A retained state with no three-term progression selects no deletion action, has no middle fibers, and emits only three-AP-free translated backbone shells. It must be recorded once as terminal and never propagated recursively.

The certified first retained family is therefore

```text
all states        = 21, points = 11,753, mass = 0.285821566728...
terminal states   =  6, points =     52, mass = 0.127088543982...
recursive states  = 15, points = 11,701, mass = 0.158733022746...
```

The six terminal parent classes are

```text
0, 1, 2, 8, 74, 86.
```

Recomputing the second frontier from only the fifteen recursive parents gives

```text
ordinary corrected F2: 27 states, 7,923 points
  terminal: 12 states, 38 points, mass 1.478795226105...
  recursive: 15 states, 7,885 points, mass 0.416597543898...

residual-sponsor F2: 45 states, 8,164 points
  terminal: 33 states, 944 points, mass 1.601039076668...
  recursive: 12 states, 7,220 points, mass 0.322355467082...
```

Thus the corrected ordinary recursive ratio is `2.624517171606...`, while residual-sponsor refinement lowers it to `2.030802800232...`, a `22.6218512798%` reduction. The historical second-to-fifth chain remains an exact finite diagnostic of the old construction, but it is not the continuation of the terminal-stopped tree.

Primary references:

- `docs/terminal-parent-stopping-lemma.md`;
- `data/first_frontier_terminal_correction_certificate.txt`;
- `src/verify_first_frontier_terminal_correction.py`.

---

## Full-color branching and pair-edge capacity

The middle-role factor-three loss was artificial. Split every middle star into all three classes

```math
\chi(s)=v_2(s)-v_3(s)\pmod3
```

and emit all nonempty color children. Every progression then has exactly two child memberships:

```text
one parity-selected side child;
one uniquely colored middle child.
```

Every child is four-AP-free and has pairwise-disjoint first three dilates. Therefore

```math
\boxed{
\sum_{\rm children}H(C)
=
2\mathcal L(B)
\ge
4H(B)-4\frac{r_3(N)}N.
}
```

The side token `d`, doubled side reserve `2d`, and middle token `d` correspond exactly to the three pair edges of one progression. Hence

```math
\boxed{
\sum_{\rm side}\left(H(C)+H(2C)\right)
+
\sum_{\rm middle}H(C)
=
\frac52\mathcal L(B).
}
```

This closes the local coefficient gap for distinct completed in-parent pair targets. The whole-tree obligations are now edge-capacity first appearance, transport-target collision reuse, parent-external ambient completions, and genuine ambient holes.

Primary references:

- `docs/full-color-coordinated-branching.md`;
- `data/full_color_coordinated_branching_summary.txt`;
- `docs/full-color-pair-edge-capacity.md`;
- `docs/sponsor-pair-forward-transport.md`;
- `docs/terminal-pair-ap-witness-bound.md`.

---

## Full-edge collision frontier

The full-edge construction emits the three edge weights of every parent
three-AP:

```math
\frac1d,\qquad\frac1d,\qquad\frac1{2d}.
```

Consequently

```math
\sum_{
m full\mbox{-}edge\ children}H(C)
=
\frac52\mathcal L(B)
\ge
5H(B)-5\frac{r_3(N)}N.
```

A physical parent pair belongs to at most two three-APs, so the distinct
current pair union satisfies

```math
W_\cup(E(B))
\ge
\frac54\mathcal L(B)
\ge
\frac52H(B)-\frac52\frac{r_3(N)}N.
```

This does not imply bounded recursive latent reuse. Uniform finite
multiplicity is false. For every `m`, there is a four-AP-free parent in one
standard dyadic block with `m` recursive side shells sharing one root
three-AP. The certified `m=4` instance uses a 19-point parent in
`[4096,8192)` and four recursive children in `[1024,2048)`.

The reuse geometry is nevertheless rigid. Fix a transported parent witness
`T` and its collision reference set `R_T`. The complete child witness fiber is
one of

```math
\frac12(R_T+T),
\qquad
2R_T-T,
\qquad
2T-R_T,
```

for side, middle, and doubled-side transport. Each expression is three equal
translates of an affine image of `R_T`. Fixed-step witnesses are pairwise
disjoint, so the layer family has exactly `3|R_T|` points.

Mandatory shelling supplies a path coordinate. If a physical pair has gap `D`
in a shell of base `M`, then `D<M`; along every descendant lineage `D/M` at
least doubles. Thus every latent lineage terminates, although arbitrarily many
branches may carry the pair at one scale.

The active theorem is now a weighted three-translate exposure inequality that
charges collision multiplicity to the forced reference-set layers and their
later scale descent. Neither another constant-overlap lemma nor another
retained generation is admissible.

Primary references:

- `docs/full-edge-coordinated-branching.md`;
- `data/full_edge_coordinated_branching_summary.txt`;
- `docs/full-edge-dyadic-gap-monotonicity.md`;
- `docs/full-edge-collision-fiber-theorem.md`;
- `docs/parametric-shelled-pair-reuse-gadget.md`;
- `docs/unbounded-shelled-latent-pair-reuse.md`;
- `data/shelled_pair_reuse_gadget_summary.txt`;
- `data/unbounded_shelled_pair_reuse_instance_summary.txt`.

---

## Scale-critical three-AP transfer

The collision frontier admits an exact scalar first-appearance allocation.
For a child three-AP `Q` transported to a parent target `T`, use

```math
\alpha_{\rm side}=\frac12,
\qquad
\alpha_{\rm middle}=1,
\qquad
\alpha_{\rm double}=2.
```

Then

```math
\frac{\alpha_t}{d(Q)}
=
\frac1{d(T)}.
```

For one fixed type this gives

```math
\alpha_t\sum_C\mathcal L_3(C)
\le
\mathcal L_3(P)+X_t,
```

where `X_t` is exactly the excess target multiplicity written as
rectangle-aspect tokens.

Shell scale removes the apparent triple spending. Weight each child witness by
`M(C)/d(Q)`. For a parent target of step `h` in a block of base `N`, one first
preimage of each type costs at most

```math
\frac{N}{2h},
\qquad
\frac{N}{4h},
\qquad
\frac{N}{4h}.
```

Therefore

```math
\boxed{
\Psi_1(\text{first child witnesses})
\le
N\mathcal L_3(P).
}
```

At general scale moment `p`, the first-appearance coefficient is

```math
c_p
=
\frac3{4^p}
+
\frac1{2^{p+1}}.
```

The exponent-one row is exactly critical and every `p>1` row contracts before
collision excess.

Unbounded collision multiplicity is transferred to a strictly lower-scale
reference reserve. If one root configuration `Q` of span `Delta` is carried by
references `R` in `[M,2M)`, then

```math
\operatorname{diam}(R)<M-\Delta
```

and

```math
D(R)=\{r-r_0:r\in R,\ r>r_0\}
```

is four-AP-free below scale `M`. For every repeated pair gap `D_e`,

```math
\frac{|R|-1}{D_e}
<
\frac{M-\Delta}{D_e}H(D(R)).
```

Pointwise, each extra reference gives the exact rectangle identity

```math
\frac1{D_e}
=
\frac\delta{D_e}\frac1\delta.
```

The sole unresolved scalar term is the scale-critical collision excess
`Y(P)`: reuse of reference-difference and rectangle tokens across distinct
root configurations. This is the next theorem. It is narrower than the former
full pair-activation problem and has explicit first-appearance, scale, and
aspect coordinates.

Primary references:

- `docs/reference-gap-collision-charge.md`;
- `docs/collision-rectangle-aspect-identity.md`;
- `docs/type-weighted-ap-transport.md`;
- `docs/scale-weighted-ap-load-criticality.md`.

---

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

Terminal stopping changes the first retained transition. The active certified frontiers are:

| frontier | total states | total points | terminal states | terminal points | recursive states | recursive points | status |
|---|---:|---:|---:|---:|---:|---:|---|
| first | 21 | 11,753 | 6 | 52 | 15 | 11,701 | active parent frontier |
| corrected ordinary second | 27 | 7,923 | 12 | 38 | 15 | 7,885 | active exact comparison |
| corrected residual-sponsor second | 45 | 8,164 | 33 | 944 | 12 | 7,220 | active refined frontier |

The earlier construction propagated all twenty-one first states, including six terminal parents. Its exact diagnostic continuation is:

| historical retained level | total states | total points | terminal states | terminal points | recursive states | recursive points |
|---|---:|---:|---:|---:|---:|---:|
| second | 27 | 7,925 | 13 | 43 | 14 | 7,882 |
| third | 32 | 4,899 | 18 | 110 | 14 | 4,789 |
| fourth | 23 | 1,794 | 11 | 77 | 12 | 1,717 |
| fifth | 21 | 1,032 | 8 | 17 | 13 | 1,015 |

These historical families remain point-disjoint exact finite test objects, and all theorems stated specifically about their recorded transitions remain valid. They must not be interpreted as the terminal-stopped recursive tree or spliced onto either corrected second frontier.

---

## 3. Recursive and terminal mass

Let `H_1^rec` denote the mass of the fifteen genuinely recursive first-frontier states. The corrected first transition satisfies

```math
\frac{H_{2,\rm ordinary}^{\rm rec}}{H_1^{\rm rec}}
=
2.624517171606...,
```

and the residual-sponsor refinement gives

```math
\frac{H_{2,\rm sponsor}^{\rm rec}}{H_1^{\rm rec}}
=
2.030802800232....
```

The refinement removes `0.094242076816...` of recursive mass, or `22.6218512798%` of the corrected ordinary recursive load, while increasing terminal mass by `0.122243850563...`.

The formerly quoted ratio

```math
0.937
<
\frac{H_{2,\rm historical}^{\rm rec}}{H_1^{\rm total}}
<
0.938
```

compared a historical child to total first-frontier mass and arose from propagating six terminal parents. It is not a recursive contraction theorem.

The later historical ratios `2.011553...`, `2.849279...`, and `1.329813...` remain exact statements for the old diagnostic chain only. No corrected third frontier has been constructed, and none should be constructed before a state-independent activation-transfer lemma is fixed.

Raw recursive harmonic mass remains nonmonotone and is not an iterating Bellman potential. Terminal output must be charged once through a first-appearance ledger and must never be propagated as recursive debt.

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

1. Define a first-appearance ledger for collision rectangle tokens `(T,{r_0,r},type,M)` and reference-difference tokens `(delta,D_e,k)`.
2. Prove a bound for the critical excess `Y(P)` in the scale-weighted row, using unused role capacity, strict shell slack, and terminal/external-completion release.
3. Quantify reuse of one reference pair across distinct repeated root configurations; this is now the only unidentified multiplicity layer.
4. Use the exact aspect identity `1/D=(delta/D)(1/delta)` to separate near rectangles, far rectangles, and dyadic aspect bands.
5. Merge sponsor direct/backward/residual targets into the same rectangle/external-completion ledger rather than maintaining a separate scalar pair-energy reserve.
6. Resolve the independent CL-087 generation-consistency audit before using those finite metrics.
7. Do not propagate the corrected second frontier, and do not generate generation six.

The predeclared transfer architecture now exists. Further finite propagation remains deferred because the scale-critical collision excess has not yet been proved summable.

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

# Backbone-anchor root transfer at the fourth-to-fifth frontier

## Status

Exact finite theorem for the certified baseline fourth-to-fifth retained transition.

The construction uses:

- the `local37` first-generation policy;
- lexicographic coordinated deletion on recursively continuing retained states;
- exact-state quotienting;
- componentwise maximum-total-harmonic same-shell independent sets;
- original `S_7` root provenance and immediate provenance.

This note refines the root-lineage identity in `docs/fourth-to-fifth-root-transfer.md`. It does not propagate generation six and does not claim a state-independent whole-tree inequality.

Primary verifier and data:

- `src/verify_root_lineage_transfer_classification.py`;
- `data/root_lineage_transfer_classification_certificate_2026-07-14.txt`;
- `src/verify_backbone_anchor_transfer.py`;
- `data/backbone_anchor_transfer_summary.txt`.

---

## 1. Exact backbone-only continuation theorem

Let `F_4^{rec}` and `F_5^{rec}` be the certified fourth and fifth recursively continuing retained families. Every root provenance label occurs exactly once in both families.

Of the `1717` roots in `F_4^{rec}`:

```text
1015 survive recursively;
17 terminate into retained terminal output;
685 disappear from the retained family.
```

For every surviving root `p`, write `u_4(p)` and `u_5(p)` for its unique fourth- and fifth-generation labels. The exact classification proves:

```math
\boxed{
\text{every surviving root is carried by a backbone occurrence.}
}
```

There are:

```text
1015 surviving backbone roots;
0 surviving middle-fiber roots.
```

Moreover, immediate provenance agrees pointwise:

```math
\operatorname{imm}(u_5(p))=u_4(p)
```

for all `1015` surviving roots.

Thus the first failing retained transition is not a mixed backbone/fiber phenomenon. It is a minimum-translation phenomenon.

---

## 2. Minimum-translation identity

Fix one fourth-generation recursive retained state

```math
S\subseteq\mathbb N,
\qquad
m=\min S.
```

Its raw backbone is

```math
\mathcal B_m(S)=\{u-m:u\in S,\ u>m\}.
```

For a parent point `u>m`, exact backbone continuation gives the harmonic interval gain

```math
\frac1{u-m}-\frac1u
=
\int_{u-m}^{u}\frac{dt}{t^2}
=
\frac{m}{u(u-m)}.
```

Define the full translation reserve

```math
A(S)
=
\sum_{u\in S,\ u>m}
\left(
\frac1{u-m}-\frac1u
\right).
```

Then

```math
\boxed{
A(S)=H(\mathcal B_m(S))-H(S\setminus\{m\}).
}
```

This is an exact algebraic identity. It is the prospective gain if every nonminimum parent point survives through the backbone before retention.

For the actually retained survivors of `S`, let

```math
G_{\rm ret}(S)
=
\sum_{p\text{ surviving from }S}
\left(
\frac1{u_5(p)}-
\frac1{u_4(p)}
\right),
```

and let

```math
L(S)
=
\sum_{p\text{ exiting from }S}
\frac1{u_4(p)}.
```

The local recursive mass balance is

```math
\boxed{
H(\operatorname{RecChild}(S))-H(S)
=
G_{\rm ret}(S)-L(S).
}
```

Summing over the twelve fourth-generation recursive parents recovers

```math
H_5^{\rm rec}-H_4^{\rm rec}
=
G_{4\to5}-L_{4\to5}.
```

---

## 3. The minimum anchors

There are exactly twelve fourth-generation recursive parent states and therefore twelve minimum anchors.

The exact raw-output audit gives:

```math
\boxed{
\text{all twelve minimum-anchor roots are dropped with no raw output.}
}
```

These are exactly the twelve roots in the earlier `dropped_no_raw_output` class.

The aggregate anchor release is

```text
sum 1/m = 0.364729899662...
```

while retained survivor gain is

```text
G_ret = 1.816777911848...
```

so

```math
\frac{G_{\rm ret}}{\sum 1/m}
=4.981159793944\ldots.
```

The scalar anchor mass `1/m` is therefore not sufficient payment for the translation gain it enables.

The full translation reserve is even larger:

```text
sum A(S) = 9.928706884742...
```

with

```math
\frac{\sum A(S)}{\sum 1/m}
=27.222081035667\ldots.
```

Only

```math
\frac{G_{\rm ret}}{\sum A(S)}
=0.182982329213\ldots
```

of the full prospective translation reserve survives the retained quotient.

This distinction is essential:

```text
full translation reserve
    != retained recursive gain
    != anchor release.
```

---

## 4. Parent-state decomposition

Six fourth-generation recursive parents expand locally and six contract locally.

Expanding classes:

```text
24, 48, 65, 68, 77, 82
```

Contracting classes:

```text
6, 8, 12, 28, 42, 93
```

There are no neutral classes.

The local recursive net changes are:

| parent class | local recursive net |
|---:|---:|
| `77` | `+0.944033903564...` |
| `68` | `+0.352686712797...` |
| `24` | `+0.241761428763...` |
| `82` | `+0.063230645618...` |
| `48` | `+0.055582216875...` |
| `65` | `+0.033476902052...` |
| `93` | `-0.000885974620...` |
| `42` | `-0.086112082763...` |
| `28` | `-0.105030676578...` |
| `12` | `-0.208338650597...` |
| `8` | `-0.274242424242...` |
| `6` | `-0.509523809524...` |

The three largest survivor-gain classes, `77`, `68`, and `24`, carry

```math
0.877945476095\ldots
```

of all survivor gain.

Thus the failing transition is highly localized in a small number of minimum-translation geometries.

---

## 5. Shell-drop and concentration profile

The surviving shell drops are exactly

```text
1, 2, 5, 7, 9, 10
```

with root counts

```text
622, 351, 27, 9, 3, 3.
```

The corresponding gain masses are approximately:

| shell drop | roots | gain |
|---:|---:|---:|
| `10` | `3` | `0.508793704847` |
| `2` | `351` | `0.400858261463` |
| `7` | `9` | `0.366140560845` |
| `9` | `3` | `0.273513206907` |
| `1` | `622` | `0.140579591154` |
| `5` | `27` | `0.126892586632` |

Gain is strongly concentrated:

```text
top 10 roots:  53.5180381624% of gain
top 25 roots:  73.8996562217% of gain
top 100 roots: 89.2166532723% of gain
```

The largest three intervals arise from

```text
4108 -> 5
4109 -> 6
4110 -> 7
```

under the common minimum translation `m=4103` in parent class `77`.

---

## 6. Exit mechanisms

Among the `685` roots that disappear from the retained recursive family:

```text
12  have no raw descendant output;
673 have at least one raw descendant output.
```

The `673` roots with raw output split as:

```text
280: raw labels fully numerically covered by retained output;
263: raw labels partially numerically covered by retained output;
130: raw labels not numerically covered by retained output.
```

Numerical coverage is not yet a provenance-preserving payment theorem. A raw label can be covered by a retained label with a different root or immediate provenance. The classification identifies the required cases but does not license charging them as released capacity.

---

## 7. Structural interpretation

For every retained survivor pair `(m,u)`, associate the harmonic interval

```math
I(m,u)=(u-m,u]
```

with measure

```math
\mu_H(I(m,u))
=
\int_{u-m}^{u}\frac{dt}{t^2}
=
\frac1{u-m}-\frac1u.
```

The exact survivor gain is the total harmonic measure of the retained anchor-survivor intervals.

The prospective whole-tree problem is therefore:

> Bound repeated use of provenance-labeled intervals `I(m,u)` across the retained tree, or prove that excessive interval reuse forces terminal first appearance, retention release, completion, rectangle support, or cheap-extension exclusion.

This is more precise than charging the minimum anchor alone. One anchor can enable many intervals, and their total harmonic measure can greatly exceed `1/m`.

A viable ancestor-path capacity must therefore retain at least:

1. the minimum-anchor provenance;
2. the surviving parent provenance;
3. the current affine interval `(u-m,u]` or an equivalent compressed state;
4. whether the interval has already been paid for;
5. what terminal, retention, or arithmetic obstruction is created when it disappears.

---

## 8. Exact non-consequences

This theorem does not prove:

- that all retained transitions are backbone-only;
- that the twelve-parent classification is state independent;
- that maximum-harmonic retention is globally optimal;
- that numerical coverage of dropped raw output is valid payment;
- that `A(S)` is an iterating potential;
- that anchor intervals have bounded whole-tree multiplicity;
- that a scalar coefficient on `A(S)` yields a Bellman inequality;
- or that the four-term reciprocal-sum problem is solved.

Generation six remains blocked until a state-independent transfer statement is formulated and tested on the existing transitions.

---

## 9. Approved next target

The next theorem candidate is an anchor-pair interval transfer law, not another arbitrary finite feature.

The immediate exact test is to evaluate the structurally defined reserve

```math
A(S)
=
\sum_{u>\min S}
\left(
\frac1{u-\min S}-\frac1u
\right)
```

on the already certified recursive families `R_1,...,R_5` and determine whether any fixed nonnegative coefficient in

```math
H+\kappa A
```

survives all four recorded transitions.

Whether positive or negative, that test has a state-independent definition and an exact transfer interpretation. It is therefore admissible under the current research protocol.

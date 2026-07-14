# Local completion credit from the `S_7` cyclic component

## Status

Exact fixed-policy finite theorem.

The cyclic terminal-fiber component

```math
C=\{1,5,61,303,1597,8195,323640\}
```

exports `63` shell-resolved middle-fiber occurrences, representing `62` exact
numerical child states. The only exact duplicate is the singleton state
`{61}`, emitted by source steps `1` and `303`.

This note measures a rigorous subset of the future obstruction credit created
by labels outside the `S_7` minimum-translation backbone. It does not yet
compute the complete 34-class affine obstruction spectrum.

**Verifier:** `src/verify_s7_scc_local_completion_credit.py`.

**Certificate:**
`data/s7_scc_local_completion_credit_certificate_2026-07-13.txt`.

---

## 1. Child candidate domain

Let

```math
X\subseteq[L,2L)
```

be one shell-resolved fiber child. As in the restricted coordinated replay
model, define

```math
\mathcal D_f(X)
=
\left\{
R:
1\le R\le
\left\lfloor
\frac{fL-1-\max X}{2}
\right\rfloor,
\quad
v_2(R)\equiv0\pmod2
\right\},
```

for `f=2` or `f=4`.

The fit bound ensures that

```math
(\{0\}\cup X)
\cup
(\{0\}\cup X+R)
\cup
(\{0\}\cup X+2R)
```

fits below the next dyadic scale `fL`. The valuation condition is the
coordinated orientation used by the replay model.

---

## 2. Imported baseline and novel increment

Let

```math
B_7
```

be the `S_7` minimum-translation backbone and put

```math
X_{\rm imp}=X\cap B_7.
```

The comparison is between the full anchor set

```math
A_X=\{0\}\cup X
```

and the imported-only anchor set

```math
A_{\rm imp}=\{0\}\cup X_{\rm imp}.
```

A candidate excluded by `A_X` but not by `A_imp` has a local witness that
cannot be supplied using imported labels alone.

This is an exact attribution to the novel part of the child for the two local
mechanisms below. It is not a claim that every such witness uses a unique novel
label or that the credit may be summed freely across descendants.

---

## 3. Layer-collision support

The three translated copies fail to be disjoint when two base labels differ by

```math
R
\quad\text{or}\quad
2R.
```

Thus the exact collision support is obtained from positive pair differences in
`A_X`.

Collision invalidity is part of the restricted replay candidate test. It is
not itself an arithmetic-progression witness, so it is recorded separately
from completion support.

---

## 4. Same-layer completion support

For a finite set `A`, define `Comp(A)` to be the coordinates missing from a
four-term arithmetic progression having exactly three points in `A`.

If

```math
c\in\mathrm{Comp}(A_X),
\qquad
a\in A_X,
```

and

```math
|c-a|=R
\quad\text{or}\quad
|c-a|=2R,
```

then three progression points can be placed in one translated copy and the
missing point can be supplied by another copy. Therefore the raw
three-translate extension at separation `R` contains a nontrivial four-term
progression.

The verifier computes all four possible missing positions exactly and checks
the completion enumerator exhaustively on every subset of `{0,...,6}`.

---

## 5. Exact results

Counts below are summed over the `62` exact numerical child states, so the
singleton duplicate `{61}` is counted once.

| quantity | factor two | factor four |
|---|---:|---:|
| candidate domain | `950,202` | `4,986,696` |
| full local invalidity | `140,722` | `399,445` |
| imported-only invalidity | `370` | `700` |
| novel incremental invalidity | `140,352` | `398,745` |
| novel collision support | `46,467` | `121,755` |
| novel completion support | `135,943` | `385,457` |
| novel completion support outside full collision support | `93,885` | `276,994` |
| candidates remaining | `809,480` | `4,587,251` |

The collision and completion columns overlap and therefore must not be added.
Their union is the `novel incremental invalidity` column.

The exact novel incremental fractions are

```math
\frac{140352}{950202}
=
\frac{23392}{158367}
```

and

```math
\frac{398745}{4986696}
=
\frac{132915}{1662232}.
```

Novel local credit is positive on `54` of the `59` nonempty factor-two child
domains and on `61` of the `62` factor-four child domains. Only one state is
fully excluded in each factor.

---

## 6. Interpretation

The `6,020` distinct novel labels exported by the cyclic component are not
merely additional harmonic load. They create exact future invalidity and
same-layer completion witnesses on most shell children.

However, this certified local subset removes only about `14.8%` of the
factor-two candidate count and `8.0%` of the factor-four candidate count after
exact-state deduplication. Most candidates remain.

Therefore the following stronger inference is false:

```text
Novel output from the S7 cyclic component is already sufficient, through
layer collisions and same-layer completions alone, to repay its recursive
expansion.
```

The result is genuine obstruction export, but not a closing reserve.

---

## 7. Scope and next target

The aggregate counts are a finite diagnostic over distinct child states. They
are not a Bellman child sum and do not resolve containment, partial overlap,
provenance reuse, or cross-generation packing.

The next exact calculation should retain the residual candidate set for every
child and test the remaining affine layer classes. In particular:

1. compute all 34-class witnesses on the residual after collision and
   same-layer completion removal;
2. separate imported-only affine witnesses from witnesses requiring novel
   labels;
3. identify the smallest exact child state on which the enlarged obstruction
   family still leaves factor-two or factor-four candidates;
4. determine whether repeated residual candidates descend into rectangle or
   completion support in the next generation.

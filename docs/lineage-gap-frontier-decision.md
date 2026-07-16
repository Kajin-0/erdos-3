# Five-quarter moment-depth frontier decision

## Status

Authoritative supplement to `docs/current-proof-program.md` for the direct-discharge and affine-owner branch.

This note supersedes earlier active-frontier statements based on:

```text
coefficient-two full-edge production;
quarter-scale coordinated middle outputs;
p=2 as the first collision-free owner exponent;
a universal p=1 overlap coefficient below one;
physical-union Hall packing as the next theorem.
```

The full four-term reciprocal-sum problem remains open.

---

## 1. Completed source-weighted direct row

After passing to an inclusion-maximal four-AP-free ambient set, every economical activated physical pair is classified as:

```text
local parent edge;
injective adjacent cross-shell swap;
maximality-certified hole with capacity-aware light/heavy transfer.
```

Every local payment consumes one tagged parent edge occurrence. Every unused edge occurrence remains explicit. Cross, light, and heavy outputs carry exact inherited source mass rather than full target-pair capacity.

Direct physical-gap moments are nonexpanding. The only scale-preserving mechanisms are adjacent swaps and multiplicity-one light support; both have finite first-appearance episodes. Every source-owned first-appearance lineage terminates or recreates after finitely many identities.

Primary references:

- `docs/direct-maximal-ambient-pair-discharge.md`;
- `docs/source-weighted-production-compatible-direct-discharge.md`;
- `docs/direct-discharge-dyadic-pair-gap-moment.md`;
- `docs/direct-pair-lineage-termination.md`.

---

## 2. Exact affine owner degree

For one physical parent pair, let `c_f` be its current-owner count and `ell_f` its recursive latent-owner count. The coordinated-deletion architecture gives

```math
\boxed{c_f+\ell_f\le2.}
```

The only repeated profiles are:

```text
one current owner + one latent owner;
one backbone latent owner + one middle latent owner.
```

This theorem is universal for the completed coordinated deletion schedule. It does not imply contraction at owner exponent one.

Primary reference:

```text
docs/coordinated-deletion-total-owner-degree-two.md
```

---

## 3. Correct child owner scale

Every retained affine child label is a positive difference of two parent roots in `[N,2N)`. Therefore every standard child shell base satisfies

```math
\boxed{L\le\frac N2.}
```

This is sharp for both backbone and coordinated middle children.

The former bound

```math
L_{\rm middle}\le\frac N4
```

is false. It incorrectly transferred outer-role direct heavy-fiber physical-gap geometry to the owner scale of retained affine middle children.

A shell-valid retained-policy witness attains half-scale middle and backbone latent owners simultaneously, leaving one full parent critical pair unit of overlap residual in the former doubled `p=1` coordinate.

Primary reference:

```text
docs/coordinated-middle-half-scale-critical-no-go.md
```

---

## 4. Raw reserve theorem remains exact

Duplicated backbone-middle latent pairs have equal-gap center and opposite reserves.

Raw reserve pseudoforest packing is false. The correct raw theorem is:

```text
match a duplicate to one unused physical reserve;
otherwise retain its original middle occurrence.
```

For duplicated demand mass `D`, used reserve union `R_used`, and unmatched middle export `X_middle`,

```math
\boxed{W(D)=J(R_{\rm used})+W(X_{\rm middle}).}
```

The unmatched raw middle occurrence descends by at least one owner level:

```math
L_{\rm middle}\le N/2.
```

It does not universally descend by two levels.

Primary references:

- `docs/reserve-pseudoforest-recursive-export.md`;
- `docs/pair-activation-reserve-export-row.md`;
- `docs/lexicographic-reserve-rank-two-no-go.md`.

---

## 5. Five-quarter production theorem

For every finite four-AP-free set,

```math
\boxed{
\frac52\mathcal L_3(P)
\le
\frac54J(P).
}
```

A pair of incidence multiplicity two must be one adjacent edge and one outer edge. Mapping every duplicated outer pair to its two adjacent half pairs is injective; a cross-orientation collision would form a four-term progression.

The half-pair images have four times the duplicated pair energy, so duplicate incidence energy is at most `J(P)/4`. Adding the first physical incidence gives the coefficient `5/4`.

The independent verifier exhausts every four-AP-free subset of `[1,16]`.

Primary references:

- `docs/five-quarter-full-edge-incidence-bound.md`;
- `src/verify_full_edge_incidence_five_quarter_bound.py`.

The coefficient `5/4` is certified, not claimed optimal.

---

## 6. Certified owner exponent

Use the monomial child potential

```math
\mathcal V_p(Q)
=
L^p\left(H(Q)+\frac54J(Q)\right).
```

The pair coefficient pays complete future full-edge production. At child half-scale, the two repeated owner profiles satisfy

```math
q_{\rm cur-lat}(p)
\le
\frac94\,2^{-p},
```

```math
q_{\rm lat-lat}(p)
\le
\frac52\,2^{-p}.
```

Thus the first exponent certified by the five-quarter monomial argument is

```math
\boxed{
p_0
=
\log_2\!\left(\frac52\right)
\approx1.321928094887\ldots.
}
```

At the boundary,

```math
q_{\rm lat-lat}(p_0)=1,
```

```math
q_{\rm cur-lat}(p_0)=\frac9{10},
```

and first appearance has coefficient

```math
\boxed{c_{p_0}=\frac{17}{25}.}
```

For every `p>p_0`, first appearance and both owner-overlap profiles contract strictly.

Primary references:

- `docs/critical-economical-activation-bellman.md`;
- `src/verify_five_quarter_owner_exponent_threshold.py`.

The older threshold `p=2` remains a valid stronger special case but is no longer the active boundary.

---

## 7. Exact supercritical-to-raw interpolation

Let one raw occurrence of mass `m` descend from parent scale `N` to

```math
L=N/2^s,
\qquad s\ge1.
```

For every `p>0`,

```math
\boxed{
m
\le
2^pm\left(\frac LN\right)^p
+
\left(1-2^{-p}\right)m(s-1).
}
```

At `p=p_0`,

```math
\boxed{
m
\le
\frac52m\left(\frac LN\right)^{p_0}
+
\frac35m(s-1).
}
```

Summing gives

```math
\boxed{
W(\mu)
\le
\frac52M_{p_0}(\mu;N)
+
\frac35\Delta_+(\mu;N),
}
```

where `Delta_+` is raw occurrence mass weighted by excess dyadic depth beyond the mandatory first child level.

The interpolation is exact on the virtual first-appearance row:

```math
\frac52\cdot\frac{17}{25}
+
\frac35\cdot3
=
\frac72.
```

Primary references:

- `docs/dyadic-owner-moment-depth-interpolation.md`;
- `src/verify_dyadic_owner_moment_depth_interpolation.py`.

This identifies the precise missing bridge coordinate: accumulated production-owned excess depth.

---

## 8. Source-indexed terminal and recreation value

Numerical target coincidence is not replaced by multiple copies of full pair capacity.

Terminal value is indexed by the already-paid source occurrence. A same-source recreation retains one recurrent reserve representative; repeated traversal of the same certified cycle is not regenerated.

The certified `S7` sink map has:

```text
source occurrences                    75,247
distinct numerical targets            40,512
collision targets                     19,593
source-weighted target overflow   227.822626207390...
nontrivial source-to-source cycles          0
```

Destination edge and support capacity still require global owner-shell scheduling.

Primary reference:

```text
docs/source-indexed-terminal-recreation-ledger.md
```

---

## 9. Exact S7 benchmark

The direct `S7` activated-pair frontier remains an important finite diagnostic:

```text
activated pair mass          1181.622166508078...
terminal heavy mass           384.435641253780...
recursive heavy mass            2.365133143358...
```

The recursive heavy family packs exactly into lower-gap primary pairs:

```text
states                         278
maximum flow          2.365133143358...
unmet demand                    0
```

Its occurrence-owned physical-gap moments contract strongly. These finite results do not replace the global excess-depth theorem.

---

## 10. Permanent stop list

Do not revive any of the following as universal targets:

```text
unlabelled physical-union Hall packing;
bounded physical-pair multiplicity without owner labels;
one or two projected affine copies as complete capacity;
off-diagonal cross-copy pairs as new capacity;
first-chain plus canonical staircase as a universal route;
reserve pseudoforest feasibility;
coordinated middle owner scale N/4;
universal p=1 overlap coefficient below one;
coefficient two as the active production bound;
p=2 as the first certified collision-free exponent;
full target-pair capacity for source-weighted transport.
```

Also do not:

```text
propagate generation six to search for a fitted feature;
count an activated physical pair again as new capacity;
discard terminal occurrence value;
delete recreation mass rather than retaining one cycle reserve;
charge a later local payment to an earlier owner shell's edge tokens.
```

---

## 11. Active universal frontier

The local pair-activation, owner-multiplicity, future-production, and target-amplification problems are closed at exponent

```math
p\ge p_0.
```

The next proof must establish a whole-tree inequality controlling:

1. source-owned direct flow across its actual owner shells;
2. free parent edge occurrences across generations;
3. terminal and recreation value exactly once;
4. accumulated excess-depth mass `Delta_+`;
5. the `p_0` owner moment;
6. the conversion to raw dyadic reciprocal-density summability.

The target is now a two-coordinate production-owned Bellman law:

```math
\boxed{
\text{raw occurrence value}
\lesssim
\text{five-quarter }p_0\text{ moment}
+
\text{excess depth}.
}
```

The unresolved obstruction is the global excess-depth/source-flow bridge, not local collision packing.

---

## 12. Recommended next exact computation

Measure the complete source-owned direct and affine output row by dyadic owner drop `s`:

```text
raw source mass by s;
p0 moment by s;
excess depth (s-1) by s;
local edge consumption;
free edge-token carry;
terminal source value;
cycle-reserve value;
ordinary recursive frontier value.
```

The exact test should verify the interpolation identity row by row and determine whether the available first-appearance, physical-gap, and terminal releases already dominate the accumulated `Delta_+` term on the certified `S7` frontier.

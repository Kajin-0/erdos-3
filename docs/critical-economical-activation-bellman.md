# Source-weighted critical economical Bellman row

## Status

Scale-critical refinement of economical pair activation and source-weighted direct discharge.

The child potential includes twice the child pair energy. That coefficient pays the complete next-generation full-edge production because every physical pair belongs to at most two three-term progressions.

Direct transport carries exact inherited source mass rather than full target-pair capacity. The complete overlap correction has coefficient at most `1/2`, but the owner-type refinement is sharper:

```text
current-latent overlap -> at most 1/4, sharp;
unmatched latent-latent export -> at most 1/2.
```

---

## 1. Critical node quantities

Let

```math
P\subseteq[N,2N)
```

be a parent root universe in a standard dyadic shell.

Define parent production capacity

```math
\boxed{
\mathcal B(P)=\frac52N\mathcal L_3(P).
}
```

For a retained affine child

```math
S_{r_i}(Q_i)\subseteq[L_i,2L_i),
```

define

```math
\boxed{
\mathcal V_i
=
L_iH(S_{r_i}(Q_i))
+
2L_i\mathbf 1_{i\text{ recursive}}J(Q_i).
}
```

The first term is critical current mass. The second is future recursive production capacity.

---

## 2. The coefficient two pays future production

Every physical pair in a four-AP-free root set belongs to at most two three-APs. Therefore

```math
\frac52\mathcal L_3(Q_i)\le2J(Q_i).
```

Multiplying by the child shell base gives

```math
\boxed{
\mathcal B(Q_i)
=
\frac52L_i\mathcal L_3(Q_i)
\le
2L_iJ(Q_i)
\le
\mathcal V_i.
}
```

Thus the left side of the Bellman row already contains enough capacity for the complete next generation of every recursive child.

---

## 3. Economical physical pair set

Let `F` be the physical first-appearance union of child current and recursive latent resources. Mark every pair in `F` unavailable before latent-reserve matching.

Let

```math
R_{\rm used}
```

be the matched center/opposite reserve union. Then

```math
\mathcal F\cap R_{\rm used}=\varnothing.
```

Define the economical activated set

```math
\boxed{U=\mathcal F\sqcup R_{\rm used}.}
```

Only pairs in `U` are activated. The unused quadratic pair universe is never prepaid.

---

## 4. Critical resource assignment

Fix one parent pair

```math
f=\{p,q\},
\qquad
g=\operatorname{gap}(f).
```

Its parent critical capacity is

```math
\Theta_1(f;N)=\frac Ng.
```

A current occurrence in a child shell of base `L` contributes

```math
\frac Lg.
```

A recursive latent occurrence contributes to the doubled pair term with mass

```math
\frac{2L}g.
```

The output-scale bounds are

```text
backbone child base <= N/2;
middle child base   <= N/4.
```

Hence one parent pair pays one backbone latent occurrence, one assigned current occurrence, or one matched duplicate at its actual critical child weight.

---

## 5. Owner-oriented current-latent packing

The total-owner theorem gives

```math
c_f+\ell_f\le2.
```

Suppose `f` has one current and one latent owner.

### Backbone current and middle latent

Here

```math
L_{\rm cur}\le\frac N2,
\qquad
L_{\rm lat}\le\frac N4.
```

Therefore

```math
L_{\rm cur}+2L_{\rm lat}\le N,
```

and one parent pair unit pays both occurrences. The correction is zero.

### Middle current and backbone latent

Here

```math
L_{\rm cur}\le\frac N4,
\qquad
L_{\rm lat}\le\frac N2.
```

Thus

```math
L_{\rm cur}+2L_{\rm lat}\le\frac54N.
```

After the parent pair pays the backbone latent occurrence, the residual is only the middle current occurrence:

```math
\boxed{
\mathcal R_{\rm cur-lat}(f)
\le
\frac14\frac Ng.
}
```

This coefficient is sharp. The shell-valid parent

```math
\{65,97,98,99,113,114,115,119,120,121,125,126,127\}
\subset[64,128)
```

retains a recursive middle current owner at scale `16` and a recursive backbone latent owner at scale `32`, giving

```math
\frac{16+2(32)}{64}=\frac54.
```

Primary reference:

```text
docs/current-latent-owner-type-critical-packing.md
```

---

## 6. Backbone-middle latent reuse

Suppose `f` has one backbone latent owner and one middle latent owner.

One occurrence is assigned to `f in F`. If a center/opposite reserve is matched, the second occurrence is assigned to `R_used` and no residue remains.

If no reserve is matched, one original middle occurrence remains. Its doubled critical pair mass is at most

```math
2\frac{N/4}{g}
=
\frac12\frac Ng.
```

Therefore

```math
\boxed{
\mathcal R_{\rm lat-lat}(f)
\le
\frac12\frac Ng.
}
```

The current-latent and latent-latent profiles are mutually exclusive. Hence the complete overlap residue satisfies

```math
\boxed{
\mathcal R_{\rm crit}(f)
\le
\frac12\Theta_1(f;N),
}
```

but only unmatched latent-latent export can attain the coefficient `1/2`.

Summing gives

```math
\boxed{
\mathcal R_{\rm crit}
\le
\frac12N J(\mathcal F_{\rm repeated})
\le
\frac12N J(U).
}
```

---

## 7. Critical affine activation row

Summing assigned resource capacities gives

```math
\boxed{
\sum_i\mathcal V_i
\le
NJ(U)+\mathcal R_{\rm crit}.
}
```

The residue hierarchy is

```text
backbone current / middle latent -> 0;
middle current / backbone latent -> <= 1/4;
matched backbone-middle latent   -> 0;
unmatched middle latent export   -> <= 1/2.
```

---

## 8. Source-weighted direct discharge

Let `E(P)` be the complete parent full-edge occurrence family and let `E_free` be its unused part after locally completed pairs in `U` consume their deterministic edge occurrences.

Apply source-weighted direct discharge to `U`. Let

```math
\mu_{\rm dir}^{\rm rec}
```

be the recursive outgoing occurrence measure and

```math
\mu_{\rm dir}^{\rm term}
```

be the terminal outgoing occurrence measure.

The exact raw identity is

```math
J(U)+W(\mathscr E_{\rm free})
=
\frac52\mathcal L_3(P)
+
W(\mu_{\rm dir}^{\rm rec})
+
W(\mu_{\rm dir}^{\rm term}).
```

Multiplying by the parent owner scale gives

```math
\boxed{
NJ(U)+NW(\mathscr E_{\rm free})
=
\mathcal B(P)
+
NW(\mu_{\rm dir}^{\rm rec})
+
NW(\mu_{\rm dir}^{\rm term}).
}
```

No full target-pair capacity appears. Every outgoing occurrence carries mass inherited from one economical source pair.

---

## 9. Complete critical Bellman row

Combining affine activation with source-weighted direct discharge gives

```math
\boxed{
\begin{aligned}
\sum_i\mathcal V_i
+
NW(\mathscr E_{\rm free})
\le{}&
\mathcal B(P)\\
&+NW(\mu_{\rm dir}^{\rm rec})\\
&+NW(\mu_{\rm dir}^{\rm term})\\
&+\mathcal R_{\rm crit}.
\end{aligned}
}
```

The row contains:

```text
one copy of parent production;
exact inherited direct-lineage mass;
source-indexed terminal mass;
owner-oriented overlap residue;
unused parent edge occurrences on the left;
complete future child production inside the child potentials.
```

---

## 10. Exact retained-chain refinement

Across the four certified retained transitions through the split fifth frontier:

```text
current-latent repeated resources  33
terminal current owners            33
recursive current owners            0
maximum combined ratio          33/64
```

Thus the recorded chain has no recursive current-latent correction. Each terminal current occurrence and its recursive latent partner fit inside one parent pair critical unit.

Primary reference:

```text
docs/certified-current-latent-critical-packing.md
```

This finite strengthening does not replace the universal `1/4` theorem because the shell-valid gadget above produces recursive current-latent reuse.

---

## 11. Direct-lineage coordinates

The recursive direct measure preserves production ownership. For the dyadic physical-gap moment

```math
\Phi_p(\mu)=\sum_e\mu(e)G(e)^p,
```

one has

```math
\Phi_p(\mu_{\rm dir}^{\rm rec})
\le
\Phi_p(\mu_{\rm in}|_{U_{\rm nonlocal}}).
```

Every mechanism except adjacent cross-shell swaps and multiplicity-one light support contracts or terminates. The two equality mechanisms have finite first-appearance episodes. Therefore one source-owned direct lineage terminates or recreates after finitely many identities.

Colliding numerical targets do not create mass. Occurrence labels retain the exact inherited measure.

---

## 12. Depth release

First-appearance production is critical at owner-scale exponent one and releases exactly

```math
\frac74
```

dyadic owner levels per unit of parent critical production capacity.

The overlap outputs have additional descent:

```text
middle-current residual: scale <= N/4;
unmatched middle latent export: scale <= N/4 before pair coefficient two;
complete critical overlap coefficient: <= 1/2.
```

Source-weighted direct transport creates no target-amplified pair mass. Strict gap drops, terminal outcomes, and unused edge occurrences provide additional release.

---

## 13. Remaining global theorem

The local critical coefficient and target-amplification problems are closed:

```text
future production is paid by 2LJ;
only economical physical pairs are activated;
direct transport carries exact source mass;
current-latent correction is at most 1/4;
complete overlap reproduction is at most 1/2;
unused edge occurrences remain explicit.
```

The surviving whole-tree tasks are:

1. telescope source-owned direct flow across actual owner shells;
2. retain each recreation cycle once without regeneration;
3. coordinate destination edge and support capacities;
4. preserve the free-edge occurrence ledger across generations;
5. combine the `7/4` first-appearance release with gap and owner-scale descent;
6. convert the resulting critical/depth estimate into summability of raw dyadic reciprocal densities.

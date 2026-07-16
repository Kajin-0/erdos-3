# Source-weighted critical economical Bellman row

## Status

Scale-critical refinement of economical pair activation and source-weighted direct discharge.

The child potential includes twice the child pair energy. That coefficient pays the complete next-generation full-edge production because every physical pair belongs to at most two three-term progressions.

Direct transport carries exact inherited source mass rather than full target-pair capacity. The only overlap correction has critical reproduction coefficient at most `1/2` per economical parent pair resource.

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

Let

```math
\mathcal F
```

be the physical first-appearance union of child resources. Mark every pair in `F` unavailable before latent-reserve matching.

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

Only pairs in `U` are needed. The unused quadratic pair universe is never activated.

---

## 4. Critical resource assignment

Fix one parent pair

```math
f=\{p,q\},
\qquad g=\operatorname{gap}(f).
```

Its parent critical capacity is

```math
\Theta_1(f;N)=\frac Ng.
```

### Current occurrence

A current occurrence in a child shell of base `L` has critical mass `L/g`. Since every positive parent-root difference is less than `N`,

```math
L\le\frac N2,
```

and therefore

```math
\frac Lg\le\frac12\frac Ng.
```

### Latent occurrence

A latent occurrence enters the doubled child pair term with critical mass `2L/g`.

For a backbone or side shell,

```math
L\le\frac N2,
```

so

```math
\frac{2L}g\le\frac Ng.
```

For a middle shell,

```math
L\le\frac N4,
```

so

```math
\frac{2L}g\le\frac12\frac Ng.
```

One physical pair in `U` therefore pays one assigned first occurrence or matched duplicate at its actual critical child weight.

---

## 5. Sharp overlap residue

The total-owner theorem gives

```math
c_f+\ell_f\le2.
```

Only two repeated profiles exist.

### Current-latent profile

One latent occurrence is assigned to `f in F`. The additional current occurrence has critical mass at most

```math
\frac12\frac Ng.
```

### Backbone-middle latent profile

One latent occurrence is assigned to `f in F`. If a reserve is matched, the second latent occurrence is assigned to `R_used` and no residue remains.

If no reserve is matched, one original middle occurrence remains. In the doubled pair potential its critical mass is at most

```math
\frac12\frac Ng.
```

The profiles are mutually exclusive. Let `R_crit` be the occurrence-tagged overlap residue. Then

```math
\boxed{
\mathcal R_{\rm crit}(f)
\le
\frac12\Theta_1(f;N)
}
```

and

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

## 6. Critical affine activation row

Summing the assigned resource capacities gives

```math
\boxed{
\sum_i\mathcal V_i
\le
NJ(U)+\mathcal R_{\rm crit}.
}
```

The residue is one half-scale current continuation or one quarter-scale middle continuation counted with pair coefficient two. One physical resource cannot create both.

---

## 7. Source-weighted direct discharge

Let

```math
\mathscr E(P)
```

be the complete parent full-edge occurrence family and let `E_free` be its unused part after locally completed pairs in `U` consume their deterministic edge occurrences.

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

Multiply by the common parent owner scale `N`:

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

## 8. Complete critical Bellman row

Combine the affine activation inequality with source-weighted direct discharge:

```math
\boxed{
\begin{aligned}
\sum_i\mathcal V_i
+
NW(\mathscr E_{\rm free})
\le{}&
\mathcal B(P)\\
&+
NW(\mu_{\rm dir}^{\rm rec})\\
&+
NW(\mu_{\rm dir}^{\rm term})\\
&+
\mathcal R_{\rm crit}.
\end{aligned}
}
```

This is the source-weighted critical economical Bellman row.

It contains:

```text
one copy of parent production;
exact inherited direct-lineage mass;
terminal source mass;
a mutually exclusive overlap residue of coefficient at most 1/2;
unused parent edge occurrences on the left;
complete future child production inside the child potentials on the left.
```

---

## 9. Direct-lineage coordinates

The recursive direct measure preserves production ownership. For the dyadic physical-gap moment

```math
\Phi_p(\mu)=\sum_e\mu(e)G(e)^p,
```

we have

```math
\Phi_p(\mu_{\rm dir}^{\rm rec})
\le
\Phi_p(\mu_{\rm in}|_{U_{\rm nonlocal}}).
```

Every mechanism except adjacent cross-shell swaps and multiplicity-one light support contracts or terminates. The two equality mechanisms have finite first-appearance episodes. Therefore one source-owned direct lineage terminates or recreates after finitely many identities.

Colliding target identities do not create mass: occurrence labels may remain separate or be aggregated up to physical capacity while preserving the total inherited measure.

---

## 10. Depth release

First-appearance production is critical at owner-scale exponent one and releases exactly

```math
\frac74
```

dyadic owner levels per unit of parent critical production capacity.

The overlap residue has stronger local descent:

```text
current continuation: owner scale at most N/2;
middle continuation: owner scale at most N/4;
complete critical overlap coefficient: at most 1/2.
```

Source-weighted direct transport creates no new critical pair mass. Strict gap drops and terminal outcomes provide additional release.

---

## 11. Remaining global theorem

The local critical coefficient and target-amplification problems are closed:

```text
future production is paid by 2LJ;
only economical physical pairs are activated;
direct transport carries exact source mass;
overlap reproduction is at most 1/2;
unused edge occurrences remain explicit.
```

The surviving whole-tree tasks are:

1. telescope source-owned finite direct lineages and merge recreation across owners;
2. control recreation of terminal sink occurrences;
3. preserve the free-edge occurrence ledger across generations;
4. combine the `7/4` first-appearance depth release with gap and owner-scale descent;
5. convert the resulting critical/depth estimate into summability of raw dyadic reciprocal densities.

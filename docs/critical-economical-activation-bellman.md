# Critical economical activation Bellman row

## Status

Scale-critical refinement of the production-compatible economical activation theorem.

The critical child potential includes twice the child pair energy. That coefficient exactly pays the complete next-generation full-edge production because every physical pair belongs to at most two three-term progressions.

The only overlap correction has critical reproduction coefficient at most `1/2` per economical parent pair resource.

---

## 1. Critical node quantities

Let

```math
P\subseteq[N,2N)
```

be a parent root universe in a standard dyadic shell.

Define parent full-edge production capacity

```math
\boxed{
\mathcal B(P)
=
\frac52N\mathcal L_3(P).
}
```

For a retained child

```math
S_{r_i}(Q_i)\subseteq[L_i,2L_i),
```

define its critical affine potential

```math
\boxed{
\mathcal V_i
=
L_iH(S_{r_i}(Q_i))
+
2L_i\mathbf 1_{i\text{ recursive}}J(Q_i).
}
```

The first term is critical current/harmonic mass. The second term is future recursive pair capacity.

---

## 2. Why the coefficient two is exact

For every four-AP-free recursive root set `Q`, each physical pair belongs to at most two three-APs. Therefore

```math
\frac52\mathcal L_3(Q)
\le
2J(Q).
```

Multiplying by the child shell base gives

```math
\boxed{
\frac52L_i\mathcal L_3(Q_i)
\le
2L_iJ(Q_i).
}
```

Hence the pair part of `V_i` pays the complete next-generation production capacity:

```math
\boxed{
\mathcal B(Q_i)
\le
2L_iJ(Q_i)
\le
\mathcal V_i.
}
```

The factor two is not a loss at the critical owner scale; it is the exact future-production coefficient.

---

## 3. Critical weight of one resource occurrence

Fix one parent physical pair

```math
f=\{p,q\},
\qquad g=\operatorname{gap}(f).
```

Its parent critical pair capacity is

```math
\Theta_1(f;N)=\frac Ng.
```

### Current occurrence

A current occurrence in a child shell of base `L` contributes

```math
\frac Lg.
```

Since every positive parent-root difference is less than `N`,

```math
L\le\frac N2,
```

and therefore

```math
\frac Lg\le\frac12\frac Ng.
```

### Latent occurrence

A latent occurrence contributes to the doubled pair potential with critical weight

```math
\frac{2L}g.
```

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

Thus one parent pair critical unit pays one first latent occurrence at any allowed child scale.

---

## 4. Economical first appearances and reserves

Let

```math
\mathcal F
```

be the physical first-appearance resource union and let

```math
R_{\rm used}
```

be the disjoint matched center/opposite reserve union. Put

```math
U=\mathcal F\sqcup R_{\rm used}.
```

Assign every first occurrence to one pair in `F` and every matched latent duplicate to one pair in `R_used`.

The preceding scale estimates show that the critical mass of all assigned occurrences is at most

```math
N J(U).
```

The only unassigned occurrence is the exact overlap residue.

---

## 5. Sharp overlap correction

The total-owner theorem gives

```math
c_f+\ell_f\le2.
```

Hence there are only two repeated profiles.

### Current-latent profile

One first latent occurrence is assigned to `f in F`. The additional current occurrence has critical mass at most

```math
\frac12\frac Ng.
```

### Backbone-middle latent profile

One first latent occurrence is assigned to `f in F`. If a physical reserve is matched, the second latent occurrence is assigned to `R_used` and no correction remains.

If no reserve is matched, the original middle occurrence contributes to the doubled child pair potential with critical mass at most

```math
\frac12\frac Ng.
```

The profiles are mutually exclusive. Let

```math
\mathcal R_{\rm crit}
```

be the occurrence-tagged critical overlap residue. Then

```math
\boxed{
\mathcal R_{\rm crit}(f)
\le
\frac12\Theta_1(f;N)
}
```

for every physical parent resource, and

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

Summing the resource assignments gives

```math
\boxed{
\sum_i\mathcal V_i
\le
NJ(U)
+
\mathcal R_{\rm crit}.
}
```

This is the critical form of the exact raw-weight activation identity.

The named residue consists only of:

```text
one half-scale current continuation;
or
one quarter-scale middle continuation counted with pair coefficient two.
```

No resource creates both.

---

## 7. Critical economical direct discharge

Multiply the production-compatible economical direct-discharge row by the common parent owner scale `N`:

```math
\boxed{
NJ(U)
+
N W(\mathscr E_{\rm free})
\le
\mathcal B(P)
+
N J(E_{\rm new})
+
N W(H_{\rm rec})
+
N W(H_{\rm term}).
}
```

Combining with the critical affine activation row gives

```math
\boxed{
\begin{aligned}
\sum_i\mathcal V_i
+
N W(\mathscr E_{\rm free})
\le{}&
\mathcal B(P)
+
N J(E_{\rm new})\\
&+
N W(H_{\rm rec})
+
N W(H_{\rm term})\\
&+
\mathcal R_{\rm crit}.
\end{aligned}
}
```

This is the critical economical Bellman row.

---

## 8. Future production is already on the left

For every recursive child,

```math
\mathcal B(Q_i)
\le
2L_iJ(Q_i).
```

Therefore

```math
\boxed{
\sum_{i\text{ recursive}}\mathcal B(Q_i)
\le
\sum_i\mathcal V_i.
}
```

The left side of the Bellman row already contains enough capacity for every next-generation full-edge occurrence token. No second factor-two payment is required.

---

## 9. Depth and contraction interpretation

The parent first-appearance production majorant is critical and releases `7/4` dyadic levels per unit of production capacity.

The overlap residue has stricter local geometry:

```text
current continuation: owner scale factor at most 1/2;
middle continuation: owner scale factor at most 1/4, before the pair coefficient two;
complete critical residue: coefficient at most 1/2.
```

Thus the collision correction is subcritical at the same owner-scale exponent for which first-appearance production is critical.

---

## 10. Remaining global theorem

The local critical coefficient problem is closed:

```text
next production is paid by 2LJ;
economical first appearances are paid by NJ(U);
overlap reproduction is at most 1/2;
unused edge occurrences remain explicitly free.
```

The remaining work is global:

1. control the critical mass of `E_new` along finite direct pair lineages;
2. merge pair recreation across production owners;
3. control terminal-sink recreation;
4. telescope the free-edge and child-production ledgers;
5. convert the critical/depth estimate into summability of raw dyadic reciprocal densities.

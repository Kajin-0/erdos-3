# Owner-exponent economical Bellman rows

## Status

State-independent owner-scale analysis for economical affine activation and source-weighted direct discharge.

The correct universal child-scale bound is

```math
L\le\frac N2.
```

The improved full-edge incidence theorem

```math
\frac52\mathcal L_3(Q)\le\frac54J(Q)
```

allows the pair coefficient to be reduced from `2` to `5/4`. With that coefficient, the first exponent certified by the monomial owner-packing argument is

```math
\boxed{
p_0
=
\log_2\!\left(\frac52\right)
\approx1.321928094887\ldots.
}
```

At `p=p_0`, first appearance and current-latent reuse contract strictly, while latent-latent reuse is exactly nonexpanding. For every `p>p_0`, all owner multiplicity contracts strictly.

This is a collision-free local Bellman row. It does not yet imply summability of the raw reciprocal coordinate.

---

## 1. Owner-exponent node quantities

Let

```math
P\subseteq[N,2N)
```

be one parent root state. For `p>0`, define parent full-edge production capacity

```math
\boxed{
\mathcal B_p(P)
=
\frac52N^p\mathcal L_3(P).
}
```

For one retained affine child

```math
S_{r_i}(Q_i)\subseteq[L_i,2L_i),
```

define the five-quarter child potential

```math
\boxed{
\mathcal V_{p,i}
=
L_i^pH(S_{r_i}(Q_i))
+
\frac54L_i^p
\mathbf 1_{i\text{ recursive}}J(Q_i).
}
```

The harmonic term records current occurrences. The pair term pays complete future full-edge production because

```math
\boxed{
\frac52\mathcal L_3(Q_i)
\le
\frac54J(Q_i).
}
```

Hence

```math
\boxed{
\mathcal B_p(Q_i)
\le
\frac54L_i^pJ(Q_i)
\le
\mathcal V_{p,i}.
}
```

Primary production theorem:

```text
docs/five-quarter-full-edge-incidence-bound.md
```

---

## 2. Correct universal child scale

Every positive child label is a difference of two parent roots in `[N,2N)`, and is therefore strictly below `N`. Standard dyadic shelling gives

```math
\boxed{L_i\le\frac N2.}
```

This applies to backbone and coordinated middle-fiber children and is sharp for both.

The quarter-scale estimate for outer-role direct heavy fibers is a physical-gap statement and must not be used as an affine owner-scale bound.

---

## 3. Per-owner coefficients

Fix one physical parent pair

```math
f=\{x,y\},
\qquad
g=y-x.
```

Its parent owner-exponent capacity is

```math
\Theta_p(f;N)=\frac{N^p}{g}.
```

### Current owner

A current occurrence contributes

```math
\frac{L^p}{g}
\le
2^{-p}\Theta_p(f;N).
```

### Recursive latent owner

A latent occurrence contributes to the five-quarter pair coordinate

```math
\frac54\frac{L^p}{g}
\le
\frac54\,2^{-p}\Theta_p(f;N).
```

The total-owner theorem gives

```math
c_f+\ell_f\le2.
```

Thus the two repeated profiles satisfy

```math
\boxed{
q_{\rm cur-lat}(p)
\le
\frac94\,2^{-p}
}
```

and

```math
\boxed{
q_{\rm lat-lat}(p)
\le
\frac52\,2^{-p}.
}
```

The latent-latent coefficient is larger.

---

## 4. Certified monomial threshold

Collision-free owner packing requires

```math
\frac52\,2^{-p}\le1.
```

Equivalently,

```math
2^p\ge\frac52.
```

Therefore the five-quarter theorem certifies

```math
\boxed{
p\ge p_0:=\log_2\!\left(\frac52\right).
}
```

This is the first exponent certified by the `5/4` incidence coefficient and the monomial owner-packing argument. It is not claimed to be globally optimal, because the optimal universal full-edge coefficient is not known.

At the boundary exponent,

```math
2^{p_0}=\frac52.
```

Hence

```math
\boxed{
q_{\rm lat-lat}(p_0)=1
}
```

and

```math
\boxed{
q_{\rm cur-lat}(p_0)
=
\frac{9/4}{5/2}
=
\frac9{10}.
}
```

Thus latent-latent reuse is nonexpanding and current-latent reuse has a strict ten-percent margin.

For every `p>p_0`, both profiles contract strictly.

---

## 5. Collision-free affine activation row

Let

```math
\mathcal F
```

be the physical union of parent pair resources actually exposed by the retained child family.

For each physical pair, the complete current and recursive latent owner load is at most its parent capacity whenever `p>=p_0`. Summing over the physical union gives

```math
\boxed{
\sum_i\mathcal V_{p,i}
\le
N^pJ(\mathcal F),
\qquad p\ge p_0.
}
```

No center/opposite reserve matching, collision correction, or recursive duplicate export is required for owner-multiplicity control in this weighted row.

The raw reserve identities remain useful for occurrence-level accounting, but they are not required to prove this scalar owner-exponent inequality.

---

## 6. Source-weighted direct discharge

Activate only the economical physical pair set `F`. Let `E_free` be the parent full-edge occurrence tokens not consumed by local pair payment.

Source-weighted direct discharge gives

```math
J(\mathcal F)
+
W(\mathscr E_{\rm free})
=
\frac52\mathcal L_3(P)
+
W(\mu_{\rm dir}^{\rm rec})
+
W(\mu_{\rm dir}^{\rm term}),
```

where every outgoing occurrence carries inherited source mass rather than full target-pair capacity.

Multiplying by the immutable parent owner factor `N^p` gives

```math
\boxed{
N^pJ(\mathcal F)
+
N^pW(\mathscr E_{\rm free})
=
\mathcal B_p(P)
+
N^pW(\mu_{\rm dir}^{\rm rec})
+
N^pW(\mu_{\rm dir}^{\rm term}).
}
```

Combining with collision-free affine activation yields

```math
\boxed{
\begin{aligned}
\sum_i\mathcal V_{p,i}
+
N^pW(\mathscr E_{\rm free})
\le{}&
\mathcal B_p(P)\\
&+
N^pW(\mu_{\rm dir}^{\rm rec})\\
&+
N^pW(\mu_{\rm dir}^{\rm term}),
\end{aligned}
\qquad p\ge p_0.
}
```

This is the five-quarter owner-exponent economical Bellman row.

---

## 7. First-appearance scale coefficient

The established first-appearance coefficient is

```math
c_p
=
\frac3{4^p}
+
\frac1{2^{p+1}}.
```

At the boundary exponent,

```math
4^{p_0}
=
\left(\frac52\right)^2
=
\frac{25}{4}.
```

Therefore

```math
\begin{aligned}
c_{p_0}
&=
\frac3{25/4}
+
\frac1{2(5/2)}\\
&=
\frac{12}{25}
+
\frac15\\
&=
\boxed{\frac{17}{25}}.
\end{aligned}
```

Thus first-appearance production contracts by a factor at most `17/25` at the same boundary exponent where latent-latent owner reuse is merely nonexpanding.

For every `p>p_0`, both mechanisms contract strictly.

---

## 8. Convenient exponent three-halves

A simple strict exponent is

```math
p=\frac32.
```

With pair coefficient `5/4`,

```math
q_{\rm lat-lat}\!\left(\frac32\right)
=
\frac5{4\sqrt2}
<1
```

because

```math
25<32.
```

Similarly,

```math
q_{\rm cur-lat}\!\left(\frac32\right)
=
\frac9{8\sqrt2}
<1
```

because

```math
81<128.
```

The first-appearance coefficient is

```math
c_{3/2}
=
\frac38+
\frac1{4\sqrt2}
<1.
```

This gives an exact strict local contraction with elementary algebra, while staying substantially closer to the critical exponent one than the quadratic special case.

---

## 9. Quadratic special case

The older exponent-two row remains a valid stronger special case. At `p=2`,

```math
q_{\rm lat-lat}(2)
\le
\frac58,
```

```math
q_{\rm cur-lat}(2)
\le
\frac9{16},
```

and

```math
c_2=\frac5{16}.
```

The quadratic row has larger contraction margins but a more difficult bridge back to raw reciprocal mass. It is no longer the first certified collision-free exponent.

---

## 10. Critical exponent one remains obstructed

At `p=1`, the five-quarter owner coefficients are

```math
q_{\rm cur-lat}(1)\le\frac98,
```

and

```math
q_{\rm lat-lat}(1)\le\frac54.
```

Thus the improved incidence coefficient reduces, but does not remove, the critical owner-overlap obstruction.

The shell-valid half-scale latent witness shows that two latent owners can simultaneously attain their half-scale geometry. Exact translated-reserve reassignment may also be saturated by other fixed resource loads.

Therefore a direct `p=1` proof still requires an additional occurrence, depth, terminal, or arithmetic-obstruction coordinate.

---

## 11. Exact diagnostics

The branch independently verifies:

```text
five-quarter full-edge incidence through every four-AP-free subset of [1,16];
total owner degree at most two;
sharp half-scale coordinated middle outputs;
coefficient-one residual in the former doubled p=1 coordinate;
source-weighted direct discharge without target amplification.
```

Primary executables:

```text
src/verify_full_edge_incidence_five_quarter_bound.py
src/verify_coordinated_deletion_total_owner_degree_two.py
src/verify_sharp_latent_latent_critical_no_go.py
src/probe_critical_fractional_reserve_flow.py
```

---

## 12. What the threshold does and does not solve

The row for `p>=p_0` closes:

```text
current/latent owner multiplicity;
future full-edge production inside affine children;
raw reserve-cycle defects at the scalar owner-potential level;
target-capacity amplification in direct transport.
```

It does **not** yet close:

```text
source-owned direct occurrences across changing owner shells;
terminal and recreation occurrence accumulation;
free edge-token telescoping;
the conversion from an N^p-weighted potential, p>1, to raw dyadic harmonic summability.
```

The final bridge is decisive. The exponent has moved much closer to one, but remains supercritical.

---

## 13. Remaining global theorem

A complete proof must now either:

1. derive a bridge from the `p_0` owner-scale Bellman row to summability of raw dyadic reciprocal densities;
2. interpolate between the strictly contracting `p>p_0` row and the exact `p=1` depth-release row without losing source ownership;
3. improve the universal full-edge coefficient below `5/4`, thereby lowering the certified monomial threshold further; or
4. add an occurrence/depth coordinate that closes the sharp `p=1` overlap directly.

The current certified monomial threshold is

```math
\boxed{
p_0=\log_2\!\left(\frac52\right).
}
```

It is a theorem of the present coefficient framework, not a claim of optimality for the Erdős problem.

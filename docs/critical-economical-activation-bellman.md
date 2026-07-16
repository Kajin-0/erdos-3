# Owner-exponent economical Bellman rows

## Status

Corrected state-independent owner-scale analysis for economical affine activation and source-weighted direct discharge.

The former universal claim that coordinated middle children satisfy `L <= N/4` was false. The correct bound for every retained affine child is

```math
L\le\frac N2.
```

Consequently the scale-critical `p=1` overlap coefficient may equal one full parent pair unit. The first exponent at which all current/latent owner multiplicity fits into the original parent pair capacity is

```math
\boxed{p=2.}
```

This yields a collision-free quadratic owner-scale Bellman row. It does not by itself prove raw reciprocal summability.

---

## 1. Owner-exponent node quantities

Let

```math
P\subseteq[N,2N)
```

be a parent root state. For `p>0`, define parent full-edge production capacity

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

define

```math
\boxed{
\mathcal V_{p,i}
=
L_i^p H(S_{r_i}(Q_i))
+
2L_i^p\mathbf 1_{i\text{ recursive}}J(Q_i).
}
```

The harmonic term records current resource occurrences. The doubled pair term pays complete future full-edge production because

```math
\frac52\mathcal L_3(Q_i)\le2J(Q_i).
```

Hence

```math
\boxed{
\mathcal B_p(Q_i)
\le
2L_i^pJ(Q_i)
\le
\mathcal V_{p,i}.
}
```

---

## 2. Correct universal child scale

Every current label and every latent pair endpoint difference is built from differences of parent roots in `[N,2N)`. Therefore every positive child label is below `N`, and standard dyadic shelling gives

```math
\boxed{L_i\le\frac N2.}
```

This bound applies to backbone and middle-fiber children and is sharp for both.

The quarter-scale bound for outer-role direct heavy fibers concerns physical source-gap geometry. It is not an owner-scale bound for coordinated retained middle children.

---

## 3. Per-owner coefficients

Fix one parent physical pair

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

A current occurrence in a child shell of base `L` contributes

```math
\frac{L^p}{g}
\le
2^{-p}\Theta_p(f;N).
```

### Latent owner

A recursive latent occurrence contributes to the doubled pair coordinate

```math
\frac{2L^p}{g}
\le
2^{1-p}\Theta_p(f;N).
```

The total-owner theorem gives

```math
c_f+\ell_f\le2.
```

Thus the two repeated profiles satisfy

```math
q_{\rm cur-lat}(p)
\le
3\,2^{-p}
```

and

```math
q_{\rm lat-lat}(p)
\le
2^{2-p}.
```

The latent-latent coefficient is the larger one. Therefore the universal owner reproduction coefficient is

```math
\boxed{q_p=2^{2-p}.}
```

---

## 4. Critical exponent one

At `p=1`,

```math
q_{\rm cur-lat}(1)\le\frac32,
\qquad
q_{\rm lat-lat}(1)\le2.
```

After one parent pair unit pays a first owner, the possible residual coefficients are

```text
current-latent residual <= 1/2;
latent-latent residual  <= 1.
```

Both the earlier universal `1/4` current-latent bound and the earlier universal `1/2` complete-overlap bound are withdrawn.

A shell-valid recursive current-latent example attains residual `1/4`, but it is not a universal extremizer. A separate shell-valid latent-latent example attains residual `1` exactly.

Primary references:

```text
docs/current-latent-owner-type-critical-packing.md
docs/coordinated-middle-half-scale-critical-no-go.md
```

Raw center/opposite reserve matching can reduce the residual in particular configurations. Exact joint fractional reassignment does not give a universal improvement: the translated alternatives may already be saturated by fixed current or non-middle latent loads.

---

## 5. Quadratic exponent two

At `p=2`,

```math
q_{\rm cur-lat}(2)\le\frac34,
\qquad
q_{\rm lat-lat}(2)\le1.
```

Therefore one parent pair unit pays the complete owner family of that pair:

```math
\boxed{
\sum_{\text{current and recursive latent owners of }f}
\operatorname{Load}_2(f)
\le
\frac{N^2}{g}.
}
```

No center/opposite reserve, collision correction, or recursive duplicate export is needed at exponent two.

Let

```math
\mathcal F
```

be the physical union of parent pair resources actually exposed by the retained child family. Summing the preceding per-pair inequality gives

```math
\boxed{
\sum_i\mathcal V_{2,i}
\le
N^2J(\mathcal F).
}
```

This is the collision-free quadratic affine activation row.

For every `p>2`, the same row is strictly contracting on every repeated owner profile.

---

## 6. Source-weighted direct discharge at exponent two

Activate only the economical physical pair set `F`. Let `E_free` be the parent full-edge occurrence tokens not consumed by local pair payment.

Source-weighted direct discharge gives the exact raw-mass identity

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

where every outgoing occurrence carries inherited source mass rather than full target capacity.

Multiplying by the immutable parent owner factor `N^2` gives

```math
\boxed{
N^2J(\mathcal F)
+
N^2W(\mathscr E_{\rm free})
=
\mathcal B_2(P)
+
N^2W(\mu_{\rm dir}^{\rm rec})
+
N^2W(\mu_{\rm dir}^{\rm term}).
}
```

Combining with quadratic affine activation yields

```math
\boxed{
\begin{aligned}
\sum_i\mathcal V_{2,i}
+
N^2W(\mathscr E_{\rm free})
\le{}&
\mathcal B_2(P)\\
&+
N^2W(\mu_{\rm dir}^{\rm rec})\\
&+
N^2W(\mu_{\rm dir}^{\rm term}).
\end{aligned}
}
```

This is the corrected collision-free local Bellman row.

---

## 7. First-appearance scale coefficient

The established first-appearance scale majorant is

```math
c_p
=
\frac3{4^p}
+
\frac1{2^{p+1}}.
```

At exponent two,

```math
\boxed{c_2=\frac5{16}.}
```

Thus first-appearance production is strongly subcritical at the same exponent where owner multiplicity is merely nonexpanding.

This does not remove the source-owned direct output terms. Their owner factor remains the entering parent scale until they are absorbed, terminalized, or placed in a recreation reserve with correct destination-shell accounting.

---

## 8. Exact no-go diagnostics

The critical joint-assignment workflow verifies:

```text
clean latent-reuse gadget:
  complete quadratic assignment closes;

recursive current-latent gadget:
  p=1 fixed current excess remains;

rank-two raw reserve gadget:
  p=1 translated alternatives remain saturated;
  middle latent residual survives;

sharp half-scale latent gadget:
  p=1 latent-latent residual coefficient 1 is attained.
```

Primary executables:

```text
src/probe_critical_fractional_reserve_flow.py
src/verify_sharp_latent_latent_critical_no_go.py
src/search_sharp_latent_latent_critical_gadget.py
```

---

## 9. What exponent two does and does not solve

The exponent-two row closes:

```text
current/latent pair multiplicity;
raw reserve-cycle defects;
critical target-capacity amplification;
future full-edge production inside affine children.
```

It does **not** yet close:

```text
source-owned direct occurrences across changing owner shells;
terminal and recreation occurrence accumulation;
free edge-token telescoping;
the conversion from an N^2-weighted potential to raw dyadic harmonic mass.
```

The last item is decisive. A bounded or telescoping quadratic owner potential is much stronger than the desired raw reciprocal coordinate, but a direct implication has not been proved.

---

## 10. Remaining global theorem

A complete proof must now either:

1. derive a valid bridge from the quadratic owner-scale Bellman row to summability of raw dyadic reciprocal densities; or
2. combine the exact `p=1` depth release with a separate occurrence ledger capable of paying the sharp coefficient-one latent overlap; or
3. interpolate between the collision-free `p=2` row and the critical `p=1` first-appearance row without losing source ownership.

The local owner-multiplicity threshold is now exact:

```math
\boxed{
q_p=2^{2-p},
\qquad
p_{\rm collision\text{-}free}=2.
}
```

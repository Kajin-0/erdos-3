# Coordinated middle half-scale critical no-go

## Status

State-independent correction to the owner-scale geometry of coordinated-deletion middle-fiber outputs, together with an exact retained-policy counterexample.

A coordinated middle-fiber shell can occur at one half of the parent dyadic scale. The previously used universal bound `L_middle <= N/4` is false. Consequently the scale-critical `p=1` latent-latent overlap coefficient can equal one full parent pair unit.

The exact replacement is:

```math
L_{\rm middle}\le\frac N2,
```

and this is sharp.

---

## 1. Universal child-scale bound

Let the parent root state lie in

```math
P\subseteq[N,2N).
```

Every backbone child label and every middle-fiber child label is a positive difference of two parent roots. Therefore every child label is strictly below `N`.

After standard dyadic shelling, every child shell base `L` satisfies

```math
\boxed{L\le\frac N2.}
```

This applies to both backbone and middle-fiber children. No state-independent quarter-scale improvement follows from the coordinated deletion geometry alone.

The quarter-scale bounds used for outer-role direct heavy fibers concern a different physical-gap coordinate and must not be transferred to the owner scale of retained affine middle children.

---

## 2. Critical owner loads

For a parent pair of gap `g`, use the owner-scale moment

```math
\Theta_p(f;N)=\frac{N^p}{g}.
```

A current occurrence in a child shell of base `L` contributes

```math
\frac{L^p}{g}
\le
2^{-p}\Theta_p(f;N).
```

A latent occurrence enters the doubled pair potential and contributes

```math
\frac{2L^p}{g}
\le
2^{1-p}\Theta_p(f;N).
```

Because coordinated deletion gives total owner degree at most two, the worst two-owner profiles have coefficients

```math
q_{\rm cur-lat}(p)
=
3\,2^{-p},
```

and

```math
q_{\rm lat-lat}(p)
=
2^{2-p}.
```

The latent-latent profile is the larger one for every `p`.

---

## 3. Consequences at the critical exponent

At `p=1`,

```math
q_{\rm cur-lat}(1)=\frac32,
\qquad
q_{\rm lat-lat}(1)=2.
```

Thus one parent pair unit can leave residuals as large as

```text
current-latent residual <= 1/2;
latent-latent residual  <= 1.
```

The earlier universal overlap bound `1/2` is false for latent-latent reuse.

At `p=2`,

```math
q_{\rm cur-lat}(2)=\frac34,
\qquad
q_{\rm lat-lat}(2)=1.
```

Hence the complete two-owner occurrence family fits inside one parent pair unit at exponent two:

```math
\boxed{
\sum_{\text{owners of }f}
\operatorname{Load}_2(f)
\le
\Theta_2(f;N).
}
```

For every `p>2`, the inequality is strictly contracting.

---

## 4. Sharp retained-policy witness

Consider

```math
P=
\{65,67,68,69,99,100,101,105,106,107,111,112,113\}
\subset[64,128).
```

The set is four-AP-free. Under the actual lexicographic deletion and maximum-harmonic point-disjoint retained policy, three parent pairs have exactly:

```text
one recursive backbone latent owner at shell base 32;
one recursive middle latent owner at shell base 32.
```

For every such pair,

```math
N=64,
\qquad
L_{\rm backbone}=L_{\rm middle}=32.
```

At `p=1`, the two latent loads are

```math
\frac{2(32)}{64}
+
\frac{2(32)}{64}
=
2
```

parent units. The natural pair capacity pays one unit, leaving exactly

```math
\boxed{1}
```

unallocated parent unit per duplicated pair.

The translated center/opposite capacities do not help: after all fixed current and non-middle latent loads are reserved, the exact joint fractional assignment still gives

```text
total flexible demand ratio       6
assigned ratio                    3
unallocated ratio                 3
```

for the three duplicated resources.

Thus the coefficient-one latent-latent residual is attained under the actual retained policy.

Primary verifier:

```text
src/verify_sharp_latent_latent_critical_no_go.py
```

---

## 5. Structured search

The structured family

```math
\{a\}
\cup
\bigcup_{t\in\{r,p,p+6,p+12\}}
\{t,t+1,t+2\}
```

was searched inside `[64,128)` over the indicated reference-gap and root-offset parameters.

Exact profile:

```text
candidates examined                 944
four-AP-free candidates             657
with retained latent reuse          159
first coefficient-1/2 witness         yes
maximum individual residual           1
witnesses attaining 1                66
```

Primary search:

```text
src/search_sharp_latent_latent_critical_gadget.py
```

---

## 6. Corrected strategic conclusion

The raw and critical reserve obstructions do not disappear through fractional reassignment at `p=1`. The correct local exponent hierarchy is:

```text
p = 1: owner overlap may be noncontracting or expanding;
p = 2: all current/latent owner multiplicity fits exactly;
p > 2: all owner multiplicity contracts strictly.
```

Therefore any scale-critical `p=1` proof must retain a separate occurrence/depth mechanism for overlap. A collision-free owner-pair Bellman row is available only at exponent two or above.

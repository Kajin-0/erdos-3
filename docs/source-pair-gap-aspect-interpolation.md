# Source-pair gap-aspect interpolation

## Status

State-independent application of dyadic moment-depth interpolation to source-owned direct pair occurrences.

The owner-scale factor of a direct pair occurrence can be decomposed into:

```text
a physical dyadic-gap moment, which is nonexpanding under direct discharge;
a gap-aspect depth term measuring how small the pair gap is relative to its owner shell.
```

This identifies the remaining coordinate needed to telescope source-weighted direct pair flow.

---

## 1. Source pair geometry

Let one source-owned pair occurrence belong to a parent shell

```math
P\subseteq[N,2N).
```

Let the physical pair gap be `D`, and let

```math
G=2^{\lfloor\log_2D\rfloor}
```

be its standard dyadic gap base.

Because two points of `[N,2N)` have difference strictly below `N`,

```math
G\le\frac N2.
```

Thus there is an integer gap-aspect depth

```math
s=\log_2\!\left(\frac NG\right)\ge1.
```

Let the occurrence carry inherited source mass `m`.

---

## 2. General owner-to-gap interpolation

For every `p>0`, the dyadic interpolation theorem gives

```math
\boxed{
m
\le
2^pm\left(\frac GN\right)^p
+
\left(1-2^{-p}\right)m(s-1).
}
```

Multiplying by the parent owner factor gives

```math
\boxed{
N^pm
\le
2^pmG^p
+
\left(1-2^{-p}\right)N^pm(s-1).
}
```

Define the physical-gap moment

```math
\Phi_p(m;G)=mG^p
```

and the gap-aspect depth

```math
\mathcal A_+(m;N,G)=m(s-1).
```

Then

```math
\boxed{
N^pm
\le
2^p\Phi_p(m;G)
+
\left(1-2^{-p}\right)N^p\mathcal A_+(m;N,G).
}
```

---

## 3. Five-quarter threshold specialization

At

```math
p_0=\log_2\!\left(\frac52\right),
```

one has

```math
2^{p_0}=\frac52,
\qquad
1-2^{-p_0}=\frac35.
```

Therefore

```math
\boxed{
N^{p_0}m
\le
\frac52mG^{p_0}
+
\frac35N^{p_0}m(s-1).
}
```

For a finite source-owned pair measure `mu`, summing gives

```math
\boxed{
N^{p_0}W(\mu)
\le
\frac52\Phi_{p_0}(\mu)
+
\frac35N^{p_0}\mathcal A_+(\mu;N).
}
```

---

## 4. Compatibility with direct discharge

Source-weighted direct discharge carries exact inherited mass. Its physical dyadic-gap moment is nonexpanding:

```math
\Phi_p(\mu_{\rm out})
\le
\Phi_p(\mu_{\rm in}).
```

Hence the first term of the gap-aspect interpolation is stable along the complete direct pair lineage.

The only additional coordinate is

```math
\mathcal A_+
=
\sum_e\mu(e)
\left(
\log_2\!\frac N{G(e)}-1
\right).
```

Strict physical-gap descent increases this aspect depth, while equal-gap adjacent-swap and multiplicity-one light episodes are finite. The pathwise direct theorem therefore supplies finite aspect certificates; the remaining issue is their whole-tree source-owned sum.

---

## 5. Relation to owner-scale interpolation

The owner-scale and physical-gap formulas are the same algebra with different triangular coordinates:

```text
owner-child bridge:  K = child shell base L;
direct-pair bridge:  K = physical gap base G.
```

For either dyadic coordinate

```math
K=N/2^s,
```

raw source mass is bounded by

```math
2^p(K/N)^p
+
(1-2^{-p})(s-1).
```

Thus the global Bellman program needs one consistent production-owned depth ledger capable of recording:

```text
owner-shell excess depth for affine/heavy outputs;
physical-gap aspect depth for direct pair outputs.
```

---

## 6. Exact S7 activated-pair diagnostic

For the certified `S7` entering activated pair family, the parent base is

```math
N=2^{20}.
```

Exact source-pair totals are:

```text
raw activated mass              1181.622166508078...
normalized p0 gap moment           0.004534420493...
gap-aspect excess-depth mass    19965.604932862123...
minimum depth needed             1969.351384094742...
required depth utilization          0.098637200862...
```

The activated mass by gap-aspect drop is concentrated at deep gaps:

```text
drop 18: 190.061904761905...
drop 19: 165.166666666667...
drop 20: 468.000000000000...
```

Thus the finite frontier has substantially more gap-aspect depth than the interpolation requires. This is a diagnostic, not a proof that the depth coordinate telescopes globally.

Primary executable:

```text
src/probe_s7_source_gap_moment_depth.py
```

---

## 7. Remaining direct-flow theorem

The direct transport obstruction is now explicit:

```math
\boxed{
\text{control the global source-owned sum of gap-aspect depth }\mathcal A_+.
}
```

A successful theorem must:

1. preserve immutable production ownership;
2. avoid regenerating aspect depth on recreation cycles;
3. coordinate later local edge payment with the actual destination shell;
4. combine gap-aspect depth with owner-shell excess depth;
5. retain terminal source value exactly once.

Target collisions and path length no longer create anonymous scalar mass. The unresolved term is the global accounting of one explicit dyadic aspect coordinate.

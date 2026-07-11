# Half-contraction and multiscale label potential

## Status

Exact multigeneration potential theorem for the multiplicity-resolved deletion-DAG recursion.

Let

```math
D\subseteq[N,2N)
```

be four-term-progression-free. Apply the side-anchor deletion construction, resolve repeated middle labels using center fibers, and retain at most one structural occurrence per parent element as in

```text
docs/middle-multiplicity-fiber-five-thirds-recursion.md
```

The resulting output associated with a parent element has two possible parts:

1. one multiplicity-resolved middle output, which is either a terminal distinct step or a recursive center-difference label;
2. at most one retained structural output.

Every such output is at most one half of its associated parent label. Consequently the recursion has a conserved linear-label potential and strictly contracting higher label moments.

This gives the first bounded multiscale potential in the active deletion-DAG program.

---

# 1. Coordinated side-anchor orientation

Write a selected progression as

```math
(a,b,c),
\qquad
 a+c=2b,
```

where `a` is the deleted coordinated side anchor and

```math
q=|b-a|.
```

The coordinated side rule depends only on `q`. Thus there is a sign

```math
\sigma(q)\in\{-1,+1\}
```

such that every selected progression of step `q` satisfies

```math
b=a+\sigma(q)q.
```

For fixed `q`, all selected progressions therefore use the same orientation.

Because the entire progression lies in `[N,2N)`, one has

```math
q\le N/2.
```

Since every sponsor satisfies `a>=N`,

```math
\boxed{q\le a/2.}
```

Thus every terminal representative step is at most half its sponsor.

---

# 2. Half-contraction of multiplicity-fiber children

Fix a repeated selected step `q`. Let

```math
X_q=\{b_i:q_i=q\}
```

be its center fiber, and choose

```math
x_q=\min X_q.
```

Because all occurrences of `q` have the same orientation,

```math
b_i=a_i+\sigma(q)q.
```

The minimum center corresponds to the minimum sponsor. Write

```math
a_q=x_q-\sigma(q)q.
```

For a nonrepresentative occurrence with center `b_i>x_q`, the multiplicity-fiber output is

```math
\xi_i=b_i-x_q.
```

The common `q` term cancels:

```math
\xi_i
=(a_i+\sigma(q)q)-(a_q+\sigma(q)q)
=a_i-a_q.
```

Since

```math
a_q\ge N,
\qquad
a_i<2N,
```

one has

```math
0<\xi_i\le a_i-N\le a_i/2.
```

Therefore

```math
\boxed{
\text{every recursive multiplicity-fiber output is at most half its sponsor.}
}
```

This strengthens the earlier statement that fiber outputs merely lie below the parent dyadic scale.

---

# 3. Half-contraction of structural outputs

There are two retained structural families.

## Component translations

A component occurrence has the form

```math
\theta=x-m_C,
```

where `x` is its associated parent element and

```math
m_C\ge N.
```

Hence

```math
0<\theta\le x-N\le x/2.
```

## Merge differences

A merge occurrence associated with sponsor `a` has the form

```math
\delta=a-p_v,
```

where

```math
p_v\ge N.
```

Therefore

```math
0<\delta\le a-N\le a/2.
```

Thus every retained structural output is at most half its associated parent element.

---

# 4. Per-parent contraction

For a deleted parent element `a`, retain:

1. exactly one multiplicity-resolved middle output `y(a)`;
2. at most one structural output `z(a)`.

Both satisfy

```math
0<y(a)\le a/2,
\qquad
0<z(a)\le a/2
```

when present.

A residual parent has no middle output and at most one structural output, again at most half its label.

Consequently, for every parent element,

```math
\boxed{
\sum_{u\text{ output of }a}u\le a.
}
```

More generally, for every real `p>=1`,

```math
\boxed{
\sum_{u\text{ output of }a}u^p
\le
2^{1-p}a^p.
}
```

For `p=1`, this is linear conservation. For `p>1`, it is strict contraction.

---

# 5. Node-level moment inequality

For a recursive state `S`, define

```math
E_p(S)=\sum_{a\in S}a^p.
```

Let `T(S)` be the terminal distinct steps produced at this state, and let the recursive child states be `S_1,S_2,...`.

Summing the per-parent inequality gives, for every `p>=1`,

```math
\boxed{
\sum_{q\in T(S)}q^p
+
\sum_j E_p(S_j)
\le
2^{1-p}E_p(S).
}
```

The terminal steps are counted as occurrences here; distinctness inside one state was already enforced by the multiplicity-fiber construction.

---

# 6. Multigeneration potential theorem

Start with a finite root family of recursive states. Let

```math
E_p(h)
```

be the total `p`-moment of all recursive occurrences at generation `h`, and let

```math
T_p(h)
```

be the total `p`-moment of terminal outputs created at generation `h`.

Put

```math
c_p=2^{1-p}.
```

The node-level inequality gives

```math
T_p(h)+E_p(h+1)\le c_pE_p(h).
```

Therefore

```math
E_p(h)\le c_p^hE_p(0).
```

Summing the one-step inequalities from generation `0` through `H` gives

```math
\sum_{h=0}^{H}T_p(h)
\le
c_pE_p(0)
+(c_p-1)\sum_{h=1}^{H}E_p(h)
-E_p(H+1).
```

Since `c_p<=1`, the last two terms are nonpositive. Hence

```math
\boxed{
\sum_{h\ge0}T_p(h)
\le
2^{1-p}E_p(0)
\qquad(p\ge1).
}
```

For `p=1`, this reads

```math
\boxed{
\sum_{\text{all terminal occurrences }q}q
\le
\sum_{\text{root occurrences }a}a.
}
```

For `p=2`,

```math
\boxed{
\sum_{\text{all terminal occurrences }q}q^2
\le
\frac12
\sum_{\text{root occurrences }a}a^2.
}
```

These are global, all-generation bounds.

---

# 7. Finite depth

Every recursive output is at most half its parent. Along a recursive path

```math
a_0,a_1,a_2,\ldots
```

one has

```math
a_h\le 2^{-h}a_0.
```

Since all labels are positive integers, no path starting at `a_0` can have length exceeding

```math
\boxed{
\lfloor\log_2 a_0\rfloor.
}
```

Thus the multiplicity-resolved recursion always terminates after logarithmic depth.

---

# 8. Cross-state multiplicity consequence

Let `mu(q)` be the total number of terminal occurrences of numerical label `q` across all states and all generations. Then for every `p>=1`,

```math
\boxed{
\sum_q\mu(q)q^p
\le
2^{1-p}
\sum_{a\text{ root occurrence}}a^p.
}
```

In particular,

```math
\sum_q\mu(q)q
\le
\sum_a a.
```

This is the first global quantitative restriction on cross-state terminal multiplicity in the current program.

It does not yet control

```math
\sum_q\frac{\mu(q)}q,
```

because repeated very small labels are inexpensive in every positive moment. The remaining obstruction is now isolated to concentration of terminal multiplicity near the bottom scales.

---

# 9. Interpretation

The active program now has two complementary one-generation statements:

1. the hybrid harmonic inequality
   ```math
   H(\text{terminal distinct steps})
   +H(\text{recursive children})
   \ge
   \frac53H(\text{parent})
   -\text{Roth error};
   ```
2. the multiscale label potential
   ```math
   \sum_{\text{terminal}}q^p
   +\sum_{\text{recursive}}u^p
   \le
   2^{1-p}\sum_{\text{parent}}a^p.
   ```

The second theorem prevents uncontrolled cross-state repetition at moderate and large labels. Any remaining critical example must drive most repeated terminal mass to very small labels while preserving the harmonic lower recursion.

The next target is therefore a bottom-scale concentration theorem: prove that excessive production of small repeated terminal labels forces either additional distinct mass or a forbidden additive configuration.
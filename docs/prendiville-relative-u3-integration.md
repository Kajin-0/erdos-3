# Prendiville relative U3 integration

## Status

Literature-integration note.  This paper appears directly relevant to the high-rank quadratic-level branch and should be extracted before further speculative development of the relative-host route.

Reference:

```text
Sean Prendiville, An inverse theorem for the Gowers U^3-norm relative to quadratic level sets, arXiv:2409.07962.
```

## Verified theorem shape

The main theorem applies to a finite vector space

```math
H/\mathbb F_p,
\qquad p\text{ odd},
```

and a tuple of quadratic polynomials

```math
Q=(q_1,\dots,q_d).
```

If a 1-bounded function `f` is supported on the quadratic level set

```math
Q^{-1}(0)
```

and has large relative `U^3` norm

```math
\|f\|_{U^3}\ge \delta \|1_{Q^{-1}(0)}\|_{U^3},
```

then either:

1. `f` correlates with a quadratic phase:

```math
\left|\sum_x f(x)e_p(q(x))\right|
\gg_p \delta^{O_p(1)}|Q^{-1}(0)|;
```

or

2. the ambient quadratic system `Q` has low rank: some nontrivial linear combination of the homogeneous quadratic parts has rank

```math
O_p(d+\log(2/\delta)).
```

## Immediate relevance to the repo branch

The repo already identified a high-rank relative-host target:

```math
B\subset V_t=\{x:q(x)=t\},
\qquad |B|/|V_t|=\beta,
```

with internal 4AP-freeness inside `V_t`.

The desired dichotomy was:

```math
\beta\le C_p n^{-1-\epsilon_h}
```

or a structured density increment of size at least

```math
\beta^{2-\epsilon_F}
```

on a linear/low-rank factor of codimension

```math
O_p(\log(1/\beta)).
```

Prendiville's theorem has the correct formal shape for this program: once the host rank exceeds the logarithmic threshold, the low-rank escape is ruled out and relative `U^3` mass gives a quadratic correlation relative to the level set.

## Why this is stronger than the generic U3 inverse theorem

The generic global inverse theorem applied to a sparsely supported function on `V_t` would pay for the density of the quadratic level set as a sparse subset of `H`.

Prendiville's theorem is explicitly relative to `Q^{-1}(0)`.  It is designed to avoid that sparsity loss and to allow density-increment arguments with respect to quadratic level sets.

This is almost exactly the technical gap in the high-rank branch.

## What remains unknown

This does not by itself solve the finite-field target.  The following quantities still have to be extracted and compared to the repo's needed exponents:

1. **Relative U3 lower bound.**  Given an internally 4AP-free set `B subset V_t`, what is the exact lower bound for the relevant relative `U^3` norm of

```math
1_B-\beta 1_{V_t}?
```

2. **Correlation-to-increment exponent.**  The theorem gives correlation

```math
\delta^{O_p(1)}|V_t|.
```

The exponent hidden in `O_p(1)` must be extracted.  To support the existing rank-window target, the resulting increment must be at least of the form

```math
\beta^{2-\epsilon_F}
```

or must be iterated in a way that still preserves a positive exponent gap.

3. **Rank threshold.**  The low-rank escape threshold is

```math
O_p(d+\log(2/\delta)).
```

If `\delta` is a power of `\beta`, this becomes

```math
O_p(d+\log(1/\beta)),
```

which matches the previously identified acceptable logarithmic codimension/rank escape.

4. **Output quadratic phase.**  Need determine whether the output quadratic phase is new relative to the host tuple `Q`, and how its rank interacts with the rank of `Q`.

5. **Iteration loss.**  Need determine whether repeated refinement by quadratic level sets grows `d` too quickly, and whether rank remains above the theorem's threshold.

## Revised high-rank route

A sharper version of the repo's high-rank route is now:

1. Start with `B subset V_t` internally 4AP-free at density `beta`.
2. Prove a relative generalized von Neumann/counting lemma: no internal 4AP implies relative `U^3` mass at scale `delta(beta)`.
3. Apply Prendiville's relative inverse theorem.
4. If the host system has low rank at threshold `O_p(d+log(1/beta))`, pass to the existing low-rank/affine increment branch.
5. Otherwise obtain relative quadratic correlation of strength `delta(beta)^{O_p(1)}`.
6. Convert the correlation either into a density increment on a quadratic refinement or into the high-rank relative recurrence/counting theorem.

## Updated priority

This paper should now be treated as a priority extraction target, before investing more work in speculative high-rank relative Szemeredi/container machinery.

The immediate deliverable should be a parameter table:

| Item | Needed value | Source in paper | Status |
|---|---:|---|---|
| high-rank definition for a quadratic tuple | exact | §3 / Theorem 1.2 | to extract |
| low-rank escape threshold | `O_p(d+log(2/delta))` | Theorem 1.2 | abstract-level verified |
| correlation strength | `delta^{O_p(1)}` | Theorem 1.2 | exponent to extract |
| density increment mechanism | exact | §§7--9 | to extract |
| iteration cost in `d` | exact | §§7--9 | to extract |
| application to complexity-two configurations | `n^{-Omega_p(1)}` density bound | Theorem 1.5 | abstract-level verified |

## Next research question

Can Prendiville's relative inverse theorem turn the repo's high-rank branch into the following usable dichotomy?

```math
B\subset \{q=t\},\quad B\text{ internally 4AP-free},\quad |B|/|V_t|=\beta
```

implies either

```math
\beta\le C_p n^{-1-\epsilon_h},
```

or an increment of size

```math
\beta^{2-\epsilon_F}
```

on a low-rank/quadratic refinement with only logarithmic rank/codimension loss.

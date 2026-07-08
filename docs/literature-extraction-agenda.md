# Literature extraction agenda

## Status

Research-program control note.  This note converts the external literature search into an actionable extraction agenda for the main `k=4` reciprocal-sum proof track.

The purpose is not to collect background.  The purpose is to extract quantitative mechanisms that may beat the current `alpha^2` / logarithmic-barrier scale.

## Main proof target

The active target remains dyadic summability:

```math
\sum_j r_4(2^j)/2^j < \infty.
```

A sufficient concrete estimate is

```math
r_4(N) \ll N/(\log N)^{1+\epsilon}
```

or any dyadically summable substitute.

Therefore every external method should be judged by whether it can produce a genuine exponent gain beyond the known Green--Tao polylogarithmic `r_4` bound.

## Priority 1: Green--Tao III

Reference: Green--Tao, *New bounds for Szemeredi's theorem, III: A polylogarithmic bound for r_4(N)*, arXiv:1705.01703.

Known role: this is the baseline integer architecture.  It proves

```math
r_4(N) \ll N(\log N)^{-c}
```

for some `c>0`, and the abstract says this appears to be the limit of the method.

Extraction task:

1. identify the recurrence theorem's error parameter `eta`;
2. track why 4AP-freeness forces `eta ~ alpha^4`;
3. extract refinement count;
4. extract radius/localization loss per refinement;
5. convert final zero-step thickness into the form

```math
P(r=0) \ll exp(C eta^{-gamma})/p;
```

6. compute the effective `gamma` and compare it to the target

```math
gamma < 1/4.
```

Deliverable: a table of every explicit exponent source in the GT31 architecture.

## Priority 2: Green--Tao Ia finite-field 4AP

Reference: Green--Tao, *New bounds for Szemeredi's theorem, Ia: Progressions of length 4 in finite field geometries revisited*, arXiv:1205.1330.

Known role: this is the cleanest finite-vector-space sandbox.  It proves

```math
r_4(F_p^n) \ll_p |F_p^n|(\log |F_p^n|)^{-c}
```

with explicit

```math
c=2^{-22}.
```

Extraction task:

1. translate the final exponent `c=2^-22` into a dimension threshold in terms of density `alpha`;
2. identify the density increment size and codimension cost at each step;
3. compare the finite-field cost to the target finite-field forcing scale

```math
n >= C alpha^{-1+delta};
```

4. locate exactly where the exponent loss prevents `delta>0`.

Deliverable: finite-field cost table matching the minimal-critical branch notation.

## Priority 3: Bloom--Sisask and Kelley--Meka

References:

- Bloom--Sisask, *Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions*, arXiv:2007.03528.
- Kelley--Meka, *Strong Bounds for 3-Progressions*, arXiv:2302.05537.

Known role: these are not direct 4AP solutions.  They are architecture studies for how a true logarithmic barrier was broken in the `k=3` problem.

Extraction task:

1. isolate what replaces the old borderline Fourier increment;
2. identify whether the method obtains fewer iterations, larger increments, or lower-loss smoothing;
3. track the role of physical-space almost-periodicity and additive smoothing;
4. ask whether any analogue exists for the 4AP signed-deficit split

```math
alpha \sum_i T_i + Q <= -c alpha^4.
```

Deliverable: a comparison note titled `roth-barrier-method-transfer.md` that lists transferable and non-transferable mechanisms.

## Priority 4: Leng--Sah--Sawhney pair

References:

- Leng--Sah--Sawhney, *Improved Bounds for Szemeredi's Theorem*, arXiv:2402.17995.
- Leng--Sah--Sawhney, *Quasipolynomial bounds on the inverse theorem for the Gowers U^{s+1}[N]-norm*, arXiv:2402.17994.

Known role: their Szemeredi improvement for `k>=5` uses quasipolynomial inverse-theorem bounds plus a density-increment strategy.  This is relevant as a modern inverse-theorem insertion architecture, not as a direct `k=4` theorem.

Extraction task:

1. identify the inverse-theorem quantitative loss before insertion into density increment;
2. identify why this pipeline improves `k>=5` but does not immediately give the needed `k=4` summability threshold;
3. compare their complexity growth to the current `U^3` branch's low-rank/high-rank split;
4. ask whether the `k=4` special structure permits a one-sided improvement absent from generic inverse machinery.

Deliverable: `modern-inverse-cost-comparison.md`.

## Priority 5: U3 inverse machinery

References:

- Green--Tao, *An inverse theorem for the Gowers U^3 norm*, arXiv:math/0503014.
- Jamneshan--Tao, *The inverse theorem for the U^3 Gowers uniformity norm on arbitrary finite abelian groups*, arXiv:2112.13759.

Known role: these are structural background for the pure `U^3` branch.  The current project does not merely need a generic inverse theorem; it needs a one-sided theorem exploiting

```math
Q<0,
qquad
f=1_A-alpha,
qquad
4AP\text{-free},
qquad
minimal/flat.
```

Extraction task:

1. record the correlation strength and rank/codimension costs of known `U^3` inverse statements;
2. compare generic correlation scale to the needed scale

```math
rho >= alpha^{2-epsilon};
```

3. identify whether any sign-sensitive or indicator-sensitive refinement exists;
4. check which statements are valid in vector spaces, cyclic groups, and arbitrary finite abelian groups.

Deliverable: `u3-inverse-cost-audit.md`.

## Priority 6: relative recurrence for high-rank quadratic levels

Reference: Conlon--Fox--Zhao, *A relative Szemeredi theorem*, arXiv:1305.5440.

Known role: relevant only if the high-rank quadratic-level recurrence route is pursued.

Current high-rank target:

```math
B subset {q=t},\quad |B|/|{q=t}|=beta
```

should imply either

```math
beta <= C_p n^{-1-epsilon_h}
```

or a density increment of size

```math
>= c_p beta^{2-epsilon_F}
```

on a low-rank/linear factor of codimension `O_p(log(1/beta))`.

Extraction task:

1. check whether relative Szemeredi transference can be specialized to the internal AP hypergraph on a high-rank quadratic level set;
2. identify what pseudorandomness norm the host must satisfy;
3. estimate whether high-rank quadratic levels satisfy that norm at rank `R >= C_p log(1/beta)`;
4. avoid any theorem whose quantitative cost is tower-type or otherwise incompatible with `delta>0`.

Deliverable: `relative-quadratic-level-counting-audit.md`.

## Warning track: popular differences

Reference: Fox--Pham, *Popular progression differences in vector spaces*, arXiv:1708.08482.

Use as a warning against overcommitting to popular-difference recurrence.  The project should not replace one fatal quantitative bottleneck with another tower-type dimension requirement.

## Side-paper track: automatic sequences

Reference: Byszewski--Konieczny--Mullner, *Gowers norms for automatic sequences*, arXiv:2002.09509.

This is relevant to the finite-state obstruction side paper.  Check it before claiming novelty for the automatic-set no-go theorem or DFA AP-certification framing.

## Immediate next action

Start with Green--Tao III and produce a strict parameter table.  Do not write a qualitative summary.  The table should have columns:

```text
source lemma / parameter / recurrence error / iteration count / radius loss / thickness loss / resulting gamma / comments
```

The output should answer one question:

```math
\text{Where exactly does the effective } gamma \ge 1/4 \text{ failure enter?}
```

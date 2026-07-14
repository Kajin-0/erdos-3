# Fifth-generation repeated-root no-go

## Status

Exact finite theorem for the fixed `local37` retained construction through generation five.

The calculation uses the same policy and quotient as the preceding retained-generation certificates:

- `local37` on the original `S_7` transition;
- lexicographic coordinated deletion on every recursively continuing retained state;
- global exact-state quotienting;
- maximum-harmonic independent-set selection in each same-shell conflict component;
- pointwise root and immediate provenance.

**Verifier:** `src/verify_fifth_generation_feature_frontier.py`.

**Certificate:** `data/fifth_generation_feature_frontier_certificate_2026-07-13.txt`.

Certificate SHA-256:

```text
74120626dcf65e06beae044f37ff570be8113c494ab81ad3bdeba3aa67378bfb
```

---

## 1. Exact fifth retained family

The 12 recursively continuing fourth-generation states contain 1,717 points. Their exact propagation produces:

```text
selected child actions = 1,345
terminal residual points = 372
raw shell occurrences = 246
raw occurrence points = 2,972
exact state classes = 95
conflict edges = 366
conflict components = 17
largest component = 17
components with nonunique optimum = 0.
```

The unique retained quotient has:

| type | states | points |
|---|---:|---:|
| terminal | 8 | 17 |
| recursive | 13 | 1,015 |
| total | 21 | 1,032 |

---

## 2. Repeated-root reserve vanishes

Let

```math
R_g
=
\sum_{(u,p)\in F_g:\,m_g(p)>1}\frac1u
```

be retained descendant harmonic mass carried by root labels repeated within generation `g`.

Exact arithmetic gives

```math
R_4=R_5=0.
```

At the same time,

```math
\boxed{
1.329813
<
\frac{H_5^{\rm rec}}{H_4^{\rm rec}}
<
1.329814.
}
```

Consequently, for every finite coefficient `kappa`,

```math
H_5^{\rm rec}+\kappa R_5
>
H_4^{\rm rec}+\kappa R_4.
```

This proves a stronger statement than failure of the integer witness `H+74R`: **no finite coefficient on the current repeated-root descendant mass can repair the fourth-to-fifth transition.**

The exact ratio hash is

```text
8d55faef41edb883a3d2d229690ef16db69bd1be23f85871c21c3206319e0534.
```

---

## 3. Terminal-token frontier

Against all terminal sinks from generations two through four, the fifth retained family has:

```text
(u,p) terminal collisions = 2
(u,p) recursive collisions = 0
(u,p,i) collisions = 0
(u,p,i,source,step) collisions = 0.
```

The two coarse terminal collisions are

```text
(122, 1,584,351)
(123, 1,584,352).
```

Thus the refined immediate-provenance token

```math
\tau^+(u)=(u,p,i)
```

remains collision-free through generation five in the recorded construction.

Numerical identity remains much coarser:

```text
earlier terminal labels recurring in fifth terminal states = 16
earlier terminal labels recurring in fifth recursive states = 34
exact earlier terminal states regenerated = 7.
```

---

## 4. Interpretation

The four-generation feature LP is feasible because a large coefficient on `R_g` can spend the repeated-root reserve accumulated in the first three levels. That reserve is exhausted by generation four. Generation five then increases raw recursive harmonic mass while `R_g` remains zero.

Therefore current-generation repeated-root multiplicity is a finite reserve, not a persistent state variable. A viable potential must retain memory of **spent provenance capacity**, an ancestor/path resource, terminal-release credit, or an affine obstruction coordinate.

This theorem is fixed-policy and fixed-retention. It is not a universal all-policy no-go theorem.

# Shifted interaction sampling barrier

## Status

Branch-2 audit.  This note works after the first load dichotomy, in the load-regular branch, and analyzes whether the missing diagonal

```math
J(d,d)=0
```

can be made visible by sampling directions.

The conclusion is a barrier: uniform random sampling alone does not amplify the missing diagonal enough unless the sampled direction set becomes very small.  Therefore the next useful step must use nonuniform sifting or find concentration/structure in the shifted-interaction matrix.

## Setup

Let `D` be a popular direction set with `K=|D|`.  Recall

```math
P_d=\{x:x,x+d\in A\}
```

and

```math
J(d,e)=|P_d\cap(P_e-2e)|
=|\{x:x,x+d,x+2e,x+3e\in A\}|.
```

The 4AP-free condition gives the exact forbidden diagonal

```math
J(d,d)=0
\qquad(d\ne0).
```

In a pseudorandom model, for distinct `d,e`, one expects

```math
J(d,e)\approx \alpha^4N.
```

For the forbidden diagonal, the random expectation would also be about `alpha^4 N`, but 4AP-freeness forces it to be zero.

## Full-matrix invisibility

The off-diagonal mass is heuristically

```math
\sum_{d\ne e}J(d,e)\approx \alpha^4K^2N.
```

The missing diagonal has heuristic size

```math
\sum_d \alpha^4N\approx \alpha^4KN.
```

Thus the diagonal deficit is only a `1/K` fraction of the full matrix scale.

When `K` is large, the exact condition `J(d,d)=0` is invisible to a global average over all `(d,e)`.

## Uniform random sampling

Choose a random subfamily `D' subset D` by including each direction independently with probability `q`.  Then

```math
E|D'|=qK.
```

The expected off-diagonal shifted interaction in `D'` is

```math
E\sum_{d\ne e\in D'}J(d,e)
=q^2\sum_{d\ne e\in D}J(d,e)
\approx q^2\alpha^4K^2N.
```

The expected missing diagonal scale in `D'` is

```math
E\sum_{d\in D'}\alpha^4N
=q\alpha^4KN.
```

The ratio remains

```math
\frac{\text{missing diagonal scale}}{\text{off-diagonal scale}}
\approx \frac{1}{qK}
=\frac{1}{E|D'|}.
```

Therefore uniform random sampling only makes the missing diagonal visible when

```math
|D'|=O(1).
```

But such a small direction set cannot preserve enough pair-fiber mass for the global density-increment strategy.

## Consequence

The sampling step cannot be naive.  To preserve mass and expose the forbidden diagonal, one needs at least one of:

1. **off-diagonal concentration:** much of `J(d,e)` is carried by a small structured set of direction pairs;
2. **row concentration:** for many `d`, the row mass `sum_e J(d,e)` is concentrated on a small neighborhood of `d`;
3. **structured sampling:** choose `D'` from a graph/neighborhood where diagonal constraints are amplified relative to off-diagonal background;
4. **additional identities:** use other constraints besides `J(d,d)=0` to create many missing near-diagonal entries, not just the literal diagonal.

This is the second local barrier in the pair-fiber route.

## Row and column statistics

Define

```math
R(d)=\sum_{e\in D}J(d,e),
\qquad
C(e)=\sum_{d\in D}J(d,e).
```

If some row satisfies

```math
R(d)\gg \alpha^4KN,
```

then the pair fiber `P_d` has unusually many interactions with shifted fibers `P_e-2e`.  This is a direction-interaction concentration signal.

If all rows and columns are regular,

```math
R(d)\approx \alpha^4KN,
\qquad
C(e)\approx \alpha^4KN,
```

then the missing diagonal remains a small perturbation and cannot be isolated by first-moment row information.

Thus one must inspect higher moments of `J`.

## Matrix-energy statistic

A natural next statistic is

```math
\mathcal E_J=\sum_{d,e\in D}J(d,e)^2.
```

If `J` is pseudorandom with entries about `alpha^4N`, then

```math
\mathcal E_J\approx K^2\alpha^8N^2.
```

If `mathcal E_J` is much larger, then off-diagonal mass is concentrated.  Such concentration may produce a structured direction graph

```math
\mathcal G_J=\{(d,e):J(d,e)\text{ large}\}.
```

A graph-BSG or dependent-random-choice step may then extract direction structure from `mathcal G_J`.

## Near-diagonal amplification target

The literal diagonal is too sparse.  A viable approach is to find a larger forbidden or depleted relation

```math
\mathcal R\subseteq D\times D
```

with size much larger than `K`, such that

```math
J(d,e)\text{ is forced small or zero for }(d,e)\in\mathcal R.
```

The original 4AP-free condition only gives

```math
\mathcal R=\{(d,d):d\in D\}.
```

To obtain a useful relation, one must generate additional forbidden pairs from sifting, additive structure, or repeated pair-fiber constraints.

This is exactly where a Kelley--Meka/Raghavan-style sifting mechanism may enter: the iteration creates many local forbidden relations, not just one global diagonal.

## Updated Branch-2 dichotomy

Under load regularity, analyze `J(d,e)`.  Either:

1. **J-concentration branch:** row/column or matrix energy concentration gives a structured direction graph;
2. **near-diagonal depletion branch:** sifting produces a larger relation `R` on which `J` is depleted, making the missing constraints visible;
3. **pseudorandom J branch:** `J` behaves like a dense random matrix off the diagonal, in which case the literal diagonal deletion alone is too weak and no contradiction follows at this level.

The third branch is a genuine obstruction to this simple argument.

## Immediate proof task

Prove a precise matrix dichotomy for `J`:

```math
\mathcal E_J\gg K^2\alpha^8N^2
```

should imply direction-pair concentration.  If `mathcal E_J` is near minimal, then record the pseudorandom `J` hypotheses under which diagonal deletion is provably invisible.

This will decide whether the next usable object is a direction graph from `J`-energy concentration or a stronger sifting mechanism that creates many depleted relations.

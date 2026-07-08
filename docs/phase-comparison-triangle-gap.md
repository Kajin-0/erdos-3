# Phase-comparison triangle gap

## Status

Proof-audit barrier.  This note checks the missing input needed before the pair-lift coboundary-cleaning lemma can be applied.

The coboundary-cleaning lemma requires many zero-sum triangle identities

```math
\mu(a,b)+\mu(b,c)+\mu(c,a)=0.
```

Line-mode extraction alone does not automatically provide these identities.  One needs an additional phase-comparison lemma tying together the three pair-lines through shared spectral vertices.

## Pair-line modes

For an oriented pair `a -> b`, let

```math
w_{ab}=a+b
```

and

```math
H_{a,b}(t)=c_{a+t w_{ab}}c_{b-t w_{ab}}.
```

If this line has a stable affine mode, write

```math
\mu(a,b).
```

Heuristically, on the active part of the line,

```math
H_{a,b}(t)\approx A_{a,b}(t)e_p(\mu(a,b)t+\theta_{a,b}).
```

The coboundary route needs many triples `a,b,c` for which

```math
\mu(a,b)+\mu(b,c)+\mu(c,a)=0.
```

## Why this is not automatic

The three pair-lines

```math
H_{a,b},\qquad H_{b,c},\qquad H_{c,a}
```

live on three different directions:

```math
w_{ab}=a+b,
\qquad
w_{bc}=b+c,
\qquad
w_{ca}=c+a.
```

A Fourier mode extracted from one line gives information about phase variation along that line only.  Without comparing the phase of `c` at shared vertices across the three lines, there is no reason for the three independently extracted frequencies to add to zero.

Thus the implication

```math
\text{many line modes}
\Rightarrow
\text{many zero-sum triangles}
```

is a genuine missing lemma.

## What a common vertex phase would imply

Suppose, on a structured active cloud, there is a phase function

```math
c_x\approx A(x)e_p(\phi(x)).
```

If, for isotropic/affine active directions, the pair-line mode is represented by a potential difference

```math
\mu(a,b)=\Phi(a)-\Phi(b),
```

then every triangle satisfies

```math
\mu(a,b)+\mu(b,c)+\mu(c,a)=0.
```

In the quadratic isotropic model,

```math
\Phi(x)=2Q_q(x),
```

and hence

```math
\mu(a,b)=2Q_q(a)-2Q_q(b).
```

So zero-sum triangles are not a consequence of line modes alone; they are a consequence of those modes being compatible with one common vertex potential.

## Phase-comparison target

A useful lemma would be:

> Suppose `a,b,c` are active spectral vertices and the three pair-lines `(a,b)`, `(b,c)`, `(c,a)` each have stable line modes.  Suppose further that the phase representatives of the coefficients `c_a,c_b,c_c` are used consistently across the three line-mode extractions.  Then either
>
> ```math
> \mu(a,b)+\mu(b,c)+\mu(c,a)=0
> ```
>
> for many such triples, or the failure gives a measurable phase inconsistency that can be converted into cancellation in the original shear sum or into a separate structured branch.

The phrase "used consistently" is the hard part.  Fourier mass near a mode determines a frequency, not an absolute phase.  Triangle closure requires comparing absolute phases across different line fibers.

## Possible route: phase anchoring

One way to force comparisons is to anchor all pair-lines through a popular vertex `o`.

For many edges `a b` with `o a` and `o b` active, compare the three line modes

```math
\mu(a,b),\qquad \mu(b,o),\qquad \mu(o,a).
```

If the extracted line modes arise from a common potential, then

```math
\mu(a,b)+\mu(b,o)+\mu(o,a)=0.
```

If many such anchored triangles fail, then the root `o` cannot define a coherent potential

```math
\Phi_o(x)=\mu(x,o).
```

The question is whether such failure is visible in the original shear energy.  It may cause cancellation when summing line autocorrelations over adjacent pair-lines.

## Possible route: higher-order shear product

Triangle closure may require looking not at single line autocorrelations but at products of three extracted line components.  For example, an anchored triangle involves the product

```math
H_{a,b}(t_1)H_{b,o}(t_2)H_{o,a}(t_3)
```

with constraints chosen so that the underlying coefficient phases at shared vertices cancel or repeat.

If such a higher-order average is large, it may force the zero-sum relation among modes.  If it is small, then line modes exist individually but do not cohere globally, and the pair-lift coboundary route cannot proceed.

## Updated bottleneck

The current route has the following gap:

```math
\text{large shear contribution}
\Rightarrow
\text{many biased pair-line modes}
```

is available after fixed-line extraction.  But the next step

```math
\text{many biased pair-line modes}
\Rightarrow
\text{many zero-sum triangles}
```

is not automatic.

Therefore the pair-lift route needs an intermediate phase-comparison lemma.

## Refined route

The refined chain is:

```math
\text{large shear contribution}
\Rightarrow
\text{many pair-line modes}
\Rightarrow
\text{phase comparison across shared vertices}
\Rightarrow
\text{many zero-sum triangles}
\Rightarrow
\text{coboundary potential }\Phi
\Rightarrow
\text{quadraticity test for }\Phi.
```

If the phase-comparison step fails, the route must branch:

1. incoherent line modes cancel before producing a global structure;
2. phase inconsistency concentrates in a low-rank/additive part of the spectral cloud;
3. the correct object is not an affine edge label `mu`, but a richer chirp label including quadratic line coefficients.

## Immediate proof task

Construct an anchored triangle average that detects whether line modes through a common root satisfy

```math
\mu(a,b)+\mu(b,o)+\mu(o,a)=0.
```

Then prove one of two outcomes:

1. many anchored triangle closures hold, enabling the coboundary-cleaning lemma;
2. failures force cancellation or reveal a different structured branch.

This is now the next analytic problem after fixed-line extraction.

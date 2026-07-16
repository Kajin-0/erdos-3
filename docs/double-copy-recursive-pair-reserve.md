# Double-copy recursive pair reserve

## Status

State-independent pair-energy theorem for every recursively continuing completion-step shell.

A recursive heavy shell has two affine physical copies in the ambient root set. Each copy, considered with the appropriate affine scaling, contains enough internal pair energy to pay the complete recursive shell debt by itself.

This gives two legitimate local resource choices. It does **not** imply a global two-choice Hall theorem: a complete-bipartite affine construction has quadratically many states and only linearly many projected copy resources.

---

## 1. Recursive step shell

Let

```math
T=\{d_1<\cdots<d_n\}\subseteq[M,2M)
```

be recursively continuing. Then `T` contains a three-term progression, so

```math
n\ge3.
```

Define

```math
H(T)=\sum_{d\in T}\frac1d
```

and complete pair energy

```math
J(T)=\sum_{1\le i<j\le n}\frac1{d_j-d_i}.
```

---

## 2. First-copy reserve

The adjacent horizontal chain is a subfamily of the complete pair set. By the horizontal-chain theorem,

```math
J(T)
\ge
\sum_{i=1}^{n-1}\frac1{d_{i+1}-d_i}
>
H(T).
```

Therefore every unscaled affine copy

```math
c+\sigma T
```

contains internal physical pair energy strictly greater than `H(T)`.

All first-copy pair gaps are less than `M`, so this reserve has strict gap descent.

---

## 3. Adjacent-role second-copy reserve

For a right or left adjacent completion role, the second affine copy is

```math
c+2\sigma T.
```

Scaling doubles every pair gap, hence its physical pair energy is

```math
\frac12J(T).
```

We prove

```math
\boxed{
\frac12J(T)>H(T).
}
```

### Case `n>=4`

The adjacent chain gives

```math
J(T)
>
\frac{(n-1)^2}{M}.
```

Therefore

```math
\frac12J(T)
>
\frac{(n-1)^2}{2M}
\ge
\frac nM
\ge
H(T),
```

because

```math
(n-1)^2\ge2n
```

for every `n>=4`.

### Case `n=3`

Since `T` is recursive, it must itself be a three-AP:

```math
T=\{d,d+q,d+2q\}.
```

The dyadic-shell condition gives

```math
d+2q<2M\le2d,
```

so

```math
q<d/2.
```

The complete pair energy is

```math
J(T)=\frac1q+\frac1q+\frac1{2q}=\frac5{2q}.
```

Using `d>2q`,

```math
\begin{aligned}
H(T)
&=
\frac1d+\frac1{d+q}+\frac1{d+2q}\\
&<
\frac1{2q}+\frac1{3q}+\frac1{4q}\\
&=
\frac{13}{12q}
<
\frac5{4q}
=
\frac12J(T).
\end{aligned}
```

Thus the second-copy reserve also pays the full adjacent-role debt in all cases.

Its pair gaps are less than `2M`, so its dyadic gap scale is nonincreasing and can equal the state scale.

---

## 4. Outer-role second-copy reserve

For an outer completion role, the two affine copies are

```math
c-T,
\qquad
c+T.
```

Both are unscaled, and each has pair energy `J(T)`. The weighted outer-role debt is only

```math
\frac12H(T).
```

Therefore either copy satisfies

```math
\boxed{
J(T)>H(T)>\frac12H(T).
}
```

Both copies have strict gap descent.

---

## 5. Two local resource choices

For every recursive embedded state `s`, define two physical pair sets:

```math
E_1(s)=\binom{c+\sigma T}{2}
```

and the role-dependent second-copy set

```math
E_2(s)
=
\begin{cases}
\binom{c+2\sigma T}{2},&\text{adjacent role},\\
\binom{c-\sigma T}{2},&\text{outer opposite copy}.
\end{cases}
```

The theorem gives

```math
J(E_1(s))>\operatorname{debt}(s)
```

and

```math
J(E_2(s))>\operatorname{debt}(s).
```

Thus every recursive state has two independently sufficient local resource neighborhoods.

---

## 6. Injective ordered double lift

The complete ordered configuration

```math
(E_1(s),E_2(s))
```

or, equivalently, the two ordered affine point copies, determines:

```text
completion reference;
completion role and orientation;
numerical step state T.
```

Therefore distinct embedded state occurrences have distinct ordered double-copy configurations.

Either projection may collide:

```text
many states may share E_1;
many states may share E_2.
```

But they cannot share the same ordered pair of copies.

---

## 7. Unrestricted Hall inference is false

It is tempting to infer

```math
\sum_{s\in\mathcal F}\operatorname{debt}(s)
\le
J\!\left(
\bigcup_{s\in\mathcal F}
(E_1(s)\cup E_2(s))
\right)
```

for every subfamily `mathcal F`. This statement is false under double-affine four-AP-free geometry alone.

The complete-bipartite construction in

```text
docs/complete-bipartite-double-copy-hall-no-go.md
```

produces, for every `k>=29`:

```text
k first-copy resources;
k second-copy resources;
k^2 distinct recursive embedded states;
a four-AP-free parent contained in one dyadic block.
```

The total state debt is strictly larger than the complete internal pair-energy union of all `2k` projected copies.

Thus singleton surplus and ordered-lift injectivity do not imply aggregate capacity.

---

## 8. Relation to unbounded reuse

The earlier unbounded latent-pair construction creates a star-like incidence pattern:

```text
one shared projection;
many varying opposite projections.
```

Such a star can be oriented to its leaves. The complete-bipartite construction is stronger: it forces high degree in both projections simultaneously.

Therefore a successful theorem must distinguish the actual direct-discharge family from arbitrary double-affine incidence. Four-AP-freeness of the two projected layers is insufficient.

---

## 9. Admissible stronger targets

The local two-copy reserve remains useful, but it must be combined with additional resources or hypotheses. Possible valid targets include:

1. maximality-hole witness pair energy;
2. parent full-edge production-token ownership;
3. cross-copy and vertical pair resources;
4. restrictions imposed by the actual activated-pair generation mechanism;
5. a higher-order rectangle or grid potential that charges complete bipartite incidence;
6. first-appearance terminal credit created by the witness gadgets required to keep all completions absent.

The exact `S7` frontier still packs using only first-copy horizontal pairs. That is a finite theorem about the recorded activated family, not evidence for unrestricted double-copy Hall.

The next universal theorem must explain why a maximal direct-discharge family cannot realize the complete-bipartite no-go without exporting compensating witness or production capacity.
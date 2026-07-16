# Lexicographic reserve rank-two no-go

## Status

Exact policy-compatible counterexample to the conjecture that every center/opposite reserve graph produced by coordinated deletion and maximum-harmonic point-disjoint retention is a pseudoforest.

The example is four-AP-free, uses the actual lexicographic deletion rule, retains the exact canonical quotient, and has three reserve components of cycle rank two.

---

## 1. Parent

Let

```math
\begin{aligned}
P=\{&1,
9194,9200,9206,
10595,10600,10605,
11296,11300,11304,\\
&11599,11600,11601,
11996,11997,11999,12000,12001,12004,12005,12006,12012,\\
&12046,12047,12049,12050,12051,12054,12055,12056,12062,\\
&12096,12097,12099,12100,12101,12104,12105,12106,12112\}.
\end{aligned}
```

Direct exhaustive verification shows that `P` contains no four-term arithmetic progression.

The high part has the product form

```math
\{12000,12050,12100\}
+
U,
```

where

```math
U=\{-4,-3,-1,0,1,4,5,6,12\}.
```

The set `U` is four-AP-free. Its selected actions are

```text
step 1: center 0, sponsor -1, opposite 1;
step 1: center 5, sponsor 4, opposite 6;
step 4: center 1, sponsor -3, opposite 5;
step 5: center 1, sponsor -4, opposite 6;
step 6: center 6, sponsor 12, opposite 0.
```

The three-coordinate product reproduces these selected actions at offsets `12000`, `12050`, and `12100`.

Four additional base actions place the resulting middle fibers in separate dyadic shells:

```text
step 1 base center 11600;
step 4 base center 11300;
step 5 base center 10600;
step 6 base center  9200.
```

---

## 2. Retained recursive children

The canonical maximum-harmonic point-disjoint quotient retains the following recursive middle fibers.

### Step one

```math
Q_1=
\{11999,12004,12049,12054,12099,12104\},
```

with labels

```math
\{400,405,450,455,500,505\}.
```

### Step four

```math
Q_4=\{11997,12047,12097\},
```

with labels

```math
\{701,751,801\}.
```

### Step five

```math
Q_5=\{11996,12046,12096\},
```

with labels

```math
\{1401,1451,1501\}.
```

### Step six

```math
Q_6=\{12012,12062,12112\},
```

with labels

```math
\{2806,2856,2906\}.
```

The retained high backbone shell contains every root in these four middle fibers and is recursive. Consequently every pair internal to each `Q_d` has one middle latent owner and one backbone latent owner.

There are exactly

```text
15 + 3 + 3 + 3 = 24
```

duplicated latent demands.

---

## 3. Rank-two reserve components

For each duplicated demand `f`, connect its equal-gap center reserve `C_d(f)` to its opposite reserve `O_d(f)`.

Three connected components fail the pseudoforest criterion.

### First gap-50 component

Its reserve vertices are

```text
{12000,12050}
{12001,12051}
{12005,12055}
{12006,12056}
```

and its five demand edges are

```text
{12000,12050} -- {12001,12051}   step 1
{12005,12055} -- {12006,12056}   step 1
{12001,12051} -- {12005,12055}   step 4
{12001,12051} -- {12006,12056}   step 5
{12006,12056} -- {12000,12050}   step 6
```

Thus

```math
|E|=5,
\qquad
|V|=4,
\qquad
\beta=|E|-|V|+1=2.
```

The unmatched mass is

```math
\frac{5-4}{50}=\frac1{50}.
```

### Gap-100 component

Replacing the second coordinates `12050,12051,12055,12056` by `12100,12101,12105,12106` gives another component with

```math
|E|=5,
\qquad |V|=4,
\qquad \beta=2,
```

and defect

```math
\frac1{100}.
```

### Second gap-50 component

The four vertices

```text
{12050,12100}
{12051,12101}
{12055,12105}
{12056,12106}
```

support the same five-edge pattern and contribute another defect `1/50`.

Therefore the complete two-choice reserve defect is

```math
\boxed{
D_{m reserve}
=
\frac1{50}+rac1{100}+rac1{50}
=
\frac1{20}.
}
```

---

## 4. Exact defect formula

For a connected reserve component `K` of physical gap `g`, every demand and reserve vertex has weight `1/g`. The maximum number of demands paid by distinct reserve vertices is `min(|E(K)|,|V(K)|)`. Hence its exact unmatched mass is

```math
\boxed{
D(K)
=
\frac{\max(0,|E(K)|-|V(K)|)}g
=
\frac{\max(0,\beta(K)-1)}g.
}
```

The pseudoforest criterion remains exact, but it is not automatically satisfied by the deletion architecture.

---

## 5. Infinite family

Translation preserves the deletion schedule, child labels, shell conflicts, and reserve graph.

Multiplication by `4^k` preserves the parity of every step valuation because

```math
v_2(4^kd)=v_2(d)+2k.
```

It also shifts every dyadic shell exponent uniformly and scales every pair weight by `4^{-k}`. Therefore every affine copy

```math
T+4^kP
```

with positive entries has the same retained reserve graph and a positive defect

```math
\frac1{20\cdot4^k}.
```

This is an exact infinite no-go family, not an isolated numerical accident.

---

## 6. Consequence

The proposed closing statement

```text
every coordinated-deletion center/opposite reserve graph is a pseudoforest
```

is false.

The two-choice reserve graph is still the correct reduction: it isolates the complete failure into the explicit cycle-excess token

```math
\sum_K\frac{\max(0,\beta(K)-1)}{g(K)}.
```

The next theorem must pay this token using an additional production-owned reserve, terminal output, lower-scale transport, or critical logarithmic depth release. Searching for another unlabelled two-choice matching theorem is no longer admissible.

Verifier:

```text
src/verify_lexicographic_reserve_rank_two_no_go.py
```

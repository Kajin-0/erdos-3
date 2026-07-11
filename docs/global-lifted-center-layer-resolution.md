# Global lifted-center layer resolution

## Status

Exact cross-state multiplicity decomposition for terminal middle labels in the multiplicity-resolved deletion-DAG recursion.

Let

```math
D\subseteq[N,2N)
```

be the root four-term-progression-free state. Run the recursive construction from the current proof program. Every recursive state is obtained by repeatedly taking a subset and translating it by one of its elements or by a selected minimum. Consequently every state has a canonical lift to a translated subset of the root set.

This note groups all terminal occurrences of one numerical label `q` across all states and all generations by the center of their lifted three-term progression in `D`.

The resulting layer decomposition resolves all cross-state repetition except repeated copies of the exact same lifted progression.

---

## 1. Every recursive state lifts to the root set

A recursive state `S` has a representation

```math
S=B-t,
\qquad B\subseteq D,
```

for some integer translation parameter `t`.

This holds initially with

```math
B=D,
\qquad t=0.
```

Suppose it holds for `S`, and a recursive child has the form

```math
S'=C-u,
\qquad C\subseteq S.
```

Put

```math
C'=C+t\subseteq B\subseteq D.
```

Then

```math
S'
=C-u
=C'-(t+u).
```

Thus the property is inherited by every descendant state.

---

## 2. Lifting terminal progressions

Suppose a terminal label `q` is produced in a state

```math
S=B-t.
```

It comes from a selected three-term progression

```math
y-q,
\qquad y,
\qquad y+q
```

inside `S`.

Adding the lift translation `t` gives

```math
x-q,
\qquad x,
\qquad x+q
```

inside `B subseteq D`, where

```math
x=y+t.
```

Therefore every terminal occurrence of numerical label `q` determines a lifted center

```math
x\in D
```

such that

```math
x-q,
\quad x,
\quad x+q
\in D.
```

The common difference is unchanged by every translation in the recursive genealogy.

---

## 3. Lifted-center multiplicity

Fix a positive integer `q`. For every possible lifted center `x`, define

```math
\nu_q(x)
=
\#\{\text{terminal occurrences of }q\text{ lifting to center }x\}.
```

Let

```math
\mu(q)=\sum_x\nu_q(x)
```

be the total terminal multiplicity of label `q` across all states and generations.

Define the nested lifted-center layers

```math
X_{q,k}
=
\{x:\nu_q(x)\ge k\},
\qquad k\ge1.
```

Let

```math
L(q)=\max_x\nu_q(x).
```

Then `X_{q,k}` is nonempty exactly for

```math
1\le k\le L(q).
```

The standard layer-cake identity gives

```math
\boxed{
\mu(q)
=
\sum_{k=1}^{L(q)}|X_{q,k}|.
}
```

---

## 4. Each center layer is four-term-progression-free

Every `X_{q,k}` is a subset of `D`. Hence

```math
\boxed{
X_{q,k}\text{ is four-term-progression-free.}
}
```

There is also a fixed-step exclusion. If both `x` and `x+q` belonged to `X_{q,k}`, then

```math
x-q,
\quad x,
\quad x+q,
\quad x+2q
```

would all lie in `D`, producing a four-term progression. Therefore

```math
\boxed{
X_{q,k}\cap(X_{q,k}-q)=\varnothing.
}
```

In particular, along each residue class modulo `q`, consecutive possible lifted centers cannot both occur.

---

## 5. Difference children for every layer

For every nonempty layer choose

```math
x_{q,k}=\min X_{q,k}
```

and define

```math
\Omega_{q,k}
=
\{x-x_{q,k}:x\in X_{q,k},\ x>x_{q,k}\}.
```

Then

```math
|\Omega_{q,k}|=|X_{q,k}|-1.
```

Because all lifted centers lie in `[N,2N)`, every positive difference lies in `[1,N)`:

```math
\boxed{
\Omega_{q,k}\subseteq[1,N).
}
```

If four elements of `Omega_{q,k}` formed a four-term progression, translating by `x_{q,k}` would give one in `X_{q,k} subseteq D`. Hence

```math
\boxed{
\Omega_{q,k}\text{ is four-term-progression-free.}
}
```

---

## 6. Exact global cross-state decomposition

For each nonempty layer, retain one terminal copy of `q` and export the remaining layer multiplicity into `Omega_{q,k}`.

Summing

```math
|X_{q,k}|=1+|\Omega_{q,k}|
```

over all nonempty layers gives

```math
\boxed{
\mu(q)
=
L(q)
+
\sum_{k=1}^{L(q)}|\Omega_{q,k}|.
}
```

Thus all terminal occurrences of `q` across the full recursive tree decompose exactly into:

1. `L(q)` copies of `q`, one for each multiplicity layer;
2. lower-scale four-term-progression-free difference children encoding every remaining occurrence.

Equivalently, all cross-state multiplicity coming from distinct lifted centers is exported. The only unresolved repetition is the layer count

```math
L(q)=\max_x\nu_q(x),
```

which is the multiplicity of one exact lifted progression

```math
x-q,
\quad x,
\quad x+q
```

across different recursive states.

---

## 7. Harmonic accounting

Every terminal step satisfies

```math
q\le N/2,
```

because its lifted progression lies in the interval `[N,2N)`.

Every element of every `Omega_{q,k}` is below `N`. Therefore

```math
\begin{aligned}
\frac{L(q)}q
+
\sum_{k=1}^{L(q)}H(\Omega_{q,k})
&\ge
\frac{2L(q)}N
+
\frac{\mu(q)-L(q)}N\\
&=
\frac{\mu(q)+L(q)}N\\
&\ge
\frac{\mu(q)}N.
\end{aligned}
```

Hence

```math
\boxed{
\frac{L(q)}q
+
\sum_kH(\Omega_{q,k})
\ge
\frac{\mu(q)}N.
}
```

This is a global cross-state analogue of the one-node multiplicity-fiber inequality.

---

## 8. A crude universal bound on exact-progression multiplicity

A fixed lifted progression can occur in at most two child states of any one parent state, because each of its three lifted points belongs to at most two recursive child subsets.

At recursive depth `h`, the number of states containing one fixed lifted progression is therefore at most

```math
2^h.
```

Every state at depth `h` has labels at most `2^{-h}` times the corresponding ancestral labels. A state containing a nontrivial progression of step `q` must contain a label at least `2q`. Therefore it cannot occur beyond depth

```math
\left\lfloor\log_2\frac Nq\right\rfloor+O(1).
```

Consequently

```math
\boxed{
L(q)\le C\frac Nq
}
```

for an absolute constant `C`.

This estimate is too weak to close the reciprocal-sum problem, but it shows that the remaining obstruction is finite and attached to repeated representations of one exact lifted progression.

---

## 9. Revised bottleneck

The multiplicity problem now has three levels.

1. Within one parent state, repeated middle labels are resolved by center fibers.
2. Across different states, repetition at different lifted centers is resolved by the global layers `X_{q,k}`.
3. The remaining multiplicity is

```math
\boxed{
L(q)=\max_x\nu_q(x),
}
```

the number of recursive states in which one exact lifted three-term progression reappears.

The next target is therefore not a general fixed-label multiplicity bound. It is an exact-progression persistence theorem:

```math
\boxed{
\text{control how often one fixed lifted }q\text{-progression can survive through the recursive genealogy.}
}
```

Possible routes are:

1. classify the only sibling duplication mechanism, namely middle-fiber versus spanning-component overlap;
2. prove that repeated persistence forces a long chain of nested component translations;
3. charge every repeated persistence event to a new parent point or to a strictly smaller exported difference;
4. construct or rule out self-replicating sharpness gadgets.
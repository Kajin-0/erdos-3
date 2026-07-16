# Maximal complete-bipartite direct-discharge Hall no-go

## Status

Symbolic infinite-family counterexample to any universal theorem that attempts to pack all recursive heavy output from direct maximal-ambient discharge into only the internal pair energies of its two affine copies.

Unlike the bare double-copy construction, this version embeds the affine core into an inclusion-maximal four-AP-free set, forces every relevant positive three-AP completion to remain absent, forbids all small-step four-AP witnesses for the selected completions, and therefore forces every one of the `k^2` selected fibers into the heavy recursive class.

The no-go does not invalidate direct maximal-ambient discharge itself. It shows that its recursive heavy term requires an additional resource: production ownership, cross-copy pairs, maximality-witness output, or a higher-order grid potential.

---

## 1. Four-AP-free affine core

Use the construction from

```text
docs/complete-bipartite-double-copy-hall-no-go.md
```

with

```math
k\ge29.
```

Thus

```math
A_k=\{2\cdot3^i:0\le i<k\},
```

```math
C_k=\{2\cdot3^{k+j}:0\le j<k\},
```

`q` is a power of two larger than `max C_k`, and `H` is the least power of two satisfying

```math
H>2(\max C_k+4q).
```

Put

```math
S=\{0,q,2q\},
```

and define the finite core

```math
P_0
=
(4H+A_k+S)
\cup
(5H+C_k+2S).
```

Then

```math
\boxed{P_0\subseteq[4H,8H)}
```

and `P_0` is four-AP-free.

For every

```math
a\in A_k,
\qquad
c\in C_k,
```

define

```math
T_{a,c}=H+c-a+S\subseteq[H,2H)
```

and

```math
r_{a,c}=3H+2a-c.
```

The two affine copies are

```math
r_{a,c}+T_{a,c}=4H+a+S
```

and

```math
r_{a,c}+2T_{a,c}=5H+c+2S.
```

All references `r_{a,c}` are positive and pairwise distinct.

---

## 2. Activated vertical pair family

For every `(a,c)` and every

```math
s\in S,
```

activate the physical pair

```math
z_{a,c,s}
=
\{4H+a+s,\ 5H+c+2s\}.
```

Its gap is

```math
D_{a,c,s}=H+c-a+s.
```

The three activated pairs indexed by one `(a,c)` have the common left endpoint completion

```math
(4H+a+s)-D_{a,c,s}
=
r_{a,c}.
```

They form the right-adjacent completion-step fiber

```math
T_{a,c}.
```

The activated physical pairs are all distinct. There are exactly

```math
3k^2
```

of them, all with both endpoints in the standard dyadic block `[4H,8H)`.

---

## 3. Positive completion candidates

For one activated pair `z_{a,c,s}`, the positive three-AP completion candidates are:

```math
r_{a,c}=3H+2a-c,
```

the midpoint

```math
m_{a,c,s}
=
\frac{9H+a+c+3s}{2},
```

and the right extension

```math
u_{a,c,s}
=
6H+2c-a+3s.
```

All quantities are integral because `H,a,c,s` are even. They satisfy

```math
r_{a,c}<m_{a,c,s}<u_{a,c,s}.
```

None belongs to the finite core `P_0`.

Let `Q_0` contain every one of these completion candidates.

---

## 4. The selected references have no core witness

For each selected reference `r_{a,c}`, the set

```math
P_0\cup\{r_{a,c}\}
```

is four-AP-free.

Indeed the points lie in three macro layers with indices `3,4,5`. The offset diameter is less than `H/2`. Hence the macro-layer indices of any putative four-AP must themselves form a four-AP in `{3,4,5}` and are constant.

The layer indexed by `3` contains only the one added point `r_{a,c}`. The other two layers are individually four-AP-free. Therefore no four-AP exists.

---

## 5. Protecting all small witnesses

For every selected reference `r_{a,c}`, every step

```math
1\le t<H,
```

and every missing position in a four-AP of step `t` through `r_{a,c}`, choose one required witness point that is absent from `P_0`. Such a point exists by the preceding section.

Add all chosen points to the finite protected set `Q_0`.

Apply the protected maximal extension lemma. It gives an inclusion-maximal four-AP-free set

```math
B\supseteq P_0
```

such that

```math
B\cap Q_0=\varnothing.
```

Consequences:

1. no positive completion candidate of any activated pair belongs to `B`;
2. every selected `r_{a,c}` is a maximality-certified hole;
3. `r_{a,c}` has no four-AP witness of step below `H`;
4. every canonical adjacent support pair for `r_{a,c}` has gap at least `H`.

Because `r_{a,c}` is the least positive completion candidate, the deterministic least-completion rule selects it for all three pairs in the fiber.

---

## 6. Every selected fiber is forced heavy

Every step in `T_{a,c}` is less than `2H`. Hence

```math
H(T_{a,c})
>
\frac3{2H}.
```

Every canonical support pair has gap at least `H`, so its weight is at most

```math
\frac1H.
```

The capacity-aware light threshold is no larger than the complete support weight. Therefore

```math
H(T_{a,c})
>
\frac3{2H}
>
\frac1H
\ge
\text{light threshold}.
```

Thus every selected fiber is heavy under **every** canonical witness choice in the maximal set.

Since `T_{a,c}` is a three-AP, every fiber is recursively continuing.

The direct maximal-discharge recursive family is exactly the complete bipartite family of `k^2` embedded states from the affine core.

---

## 7. First-copy Hall failure

All first copies with fixed `a` coincide:

```math
4H+a+S.
```

There are only `k` first-copy three-APs. Their horizontal adjacent-chain union has capacity

```math
\frac{2k}{q}.
```

The recursive debt satisfies

```math
D_k
>
\frac{3k^2}{H+3q}
>
\frac{3k^2}{23q}.
```

Therefore

```math
D_k>\frac{2k}{q}
```

for every

```math
k\ge16.
```

In particular the universal first-copy horizontal-chain Hall theorem fails on an actual maximal direct-discharge family.

---

## 8. Two-copy internal pair-energy failure

The complete internal pair energy of all `k` first copies and all `k` second copies is

```math
\frac{15k}{4q}.
```

For every `k>=29`,

```math
D_k
>
\frac{3k^2}{23q}
>
\frac{15k}{4q}.
```

Hence

```math
\boxed{
D_k
>
J\!\left(
\bigcup_{a,c}
(E_1(T_{a,c})\cup E_2(T_{a,c}))
\right).
}
```

The unrestricted two-copy Hall theorem fails even for the recursive heavy family emitted by direct maximal-ambient discharge.

---

## 9. Why this does not contradict the exact S7 flow

The certified `S7` recursive family has a sparse incidence pattern:

```text
278 recursive states;
991 lower-gap first-copy pairs;
exact rational flow feasible with 206 pairs.
```

The present construction has complete bipartite incidence:

```text
k first copies;
k second copies;
k^2 recursive states.
```

The `S7` certificate is a valid finite theorem for its recorded family. The complete-bipartite family proves that no theorem based only on projected copy pair capacity can be universal.

---

## 10. Remaining admissible resources

The construction leaves several resources unused:

1. the `3k^2` entering vertical activated-pair tokens and their production ownership;
2. cross-copy pairs other than the matched activated pairs;
3. the maximality witness gadgets that block all completion candidates;
4. terminal first-appearance credit associated with those protected holes;
5. higher-order rectangle or grid incidence tokens;
6. restrictions imposed by the actual upstream branching mechanism that activates pair families.

A successful universal theorem must use at least one of these resources.

---

## 11. Strategic consequence

The remaining proof target is not a physical-pair Hall theorem for recursive heavy copies. That target is false.

The correct next question is:

```math
\boxed{
\text{what production, witness, or cross-copy resource grows quadratically
with complete-bipartite hole incidence?}
}
```

The maximal grid isolates the exact missing coordinate.
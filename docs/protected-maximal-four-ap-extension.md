# Protected maximal four-AP extension lemma

## Status

Elementary finite-extension lemma for constructing inclusion-maximal four-AP-free ambient sets while forcing a prescribed finite set of positive integers to remain absent and certified.

The lemma also permits finitely many additional points to remain absent. This can be used to prohibit all small-step four-AP witnesses for selected holes before maximal extension.

---

## 1. Statement

Let

```math
F\subseteq\mathbb N
```

be finite and four-AP-free. Let

```math
Q\subseteq\mathbb N\setminus F
```

be finite.

Then there exists an inclusion-maximal four-AP-free set

```math
B\subseteq\mathbb N
```

such that

```math
F\subseteq B
```

and

```math
B\cap Q=\varnothing.
```

Moreover every `q in Q` is already blocked by a four-AP witness in a finite intermediate extension: there is a finite four-AP-free

```math
F'\supseteq F
```

such that

```math
F'\cup\{q\}
```

contains a four-term arithmetic progression for every `q in Q`.

---

## 2. Blocking one protected point

Fix a finite four-AP-free set `G` and one protected point

```math
q\notin G.
```

For a positive integer `u`, consider adding

```math
q+u,
\qquad
q+2u,
\qquad
q+3u.
```

Together with `q`, these points would form a four-AP. The point `q` itself is not added.

We claim that all sufficiently generic choices of `u` preserve four-AP-freeness.

A four-AP in

```math
G\cup\{q+u,q+2u,q+3u\}
```

would select some old points from `G` and some of the three new affine functions of `u`. For each fixed selection pattern and each fixed ordering of the four terms, the two second-difference equations become linear equations in `u`.

If such an equation is not identically zero, it excludes at most one value of `u`. There are only finitely many selection patterns.

The only possible identity using all three new points is the progression

```math
q,\ q+u,\ q+2u,\ q+3u,
```

but `q` is absent. No four-AP is formed by the three new points alone.

Therefore only finitely many values of `u` are bad. Choose a positive `u` outside that finite set and also large enough that the three new points avoid any additional prescribed finite forbidden set.

The enlarged set remains four-AP-free and now blocks `q`.

---

## 3. Blocking a finite protected set

Enumerate

```math
Q=\{q_1,\ldots,q_m\}.
```

Starting from `F`, apply the one-point construction successively. At stage `i`, choose the witness step sufficiently generic and sufficiently large that:

1. the current set remains four-AP-free;
2. none of the protected points in `Q` is added;
3. all previously installed witnesses remain present.

This produces a finite four-AP-free set `F'` containing `F`, avoiding `Q`, and blocking every protected point.

---

## 4. Maximal extension

Consider the partially ordered family of four-AP-free sets `C` satisfying

```math
F'\subseteq C
```

and

```math
C\cap Q=\varnothing.
```

The union of every chain is four-AP-free: any finite four-AP would already occur in one chain member. Hence Zorn's lemma gives a maximal member `B` of this restricted family.

For any

```math
x\in\mathbb N\setminus B,
```

there are two cases.

- If `x notin Q`, restricted maximality says `B union {x}` contains a four-AP.
- If `x in Q`, the finite witness already contained in `F' subseteq B` says the same.

Thus `B` is inclusion-maximal among **all** four-AP-free subsets of the positive integers.

---

## 5. Forcing a lower bound on witness steps

Fix one selected protected hole `c` and an integer threshold `U`.

For every step

```math
1\le u<U
```

and every missing position `j in {0,1,2,3}`, consider the three points other than `c` in the corresponding four-AP of step `u`.

If the current finite core together with `c` is four-AP-free, at least one of those three points is absent from the core. Choose one such absent point and add it to the protected set `Q`.

There are only finitely many choices. After applying the protected maximal extension lemma, every selected point remains absent. Therefore `c` has no four-AP witness of step less than `U` in the final maximal set.

Consequently every canonical adjacent support pair for `c` has gap at least `U`.

---

## 6. Application protocol

To force a finite family of completion fibers to remain maximality-hole fibers with small support capacity:

1. begin with a finite four-AP-free affine core;
2. protect every selected completion candidate;
3. protect every alternative positive three-AP completion candidate for the activated target pairs;
4. for each selected completion, protect one required point from every witness of step below the chosen threshold;
5. apply the finite blocking construction;
6. extend maximally.

The resulting ambient set contains the affine core, contains none of the protected completions, and gives every selected completion only large-step four-AP witnesses.

---

## 7. Limitations

The lemma is existential and does not optimize the density or harmonic mass of the maximal extension. Witness steps may be extremely large.

That flexibility is precisely why maximality alone does not provide a quantitative reciprocal-gap payment for a hole: a prescribed hole can be certified only by arbitrarily remote roots.

Any proof that needs maximality witnesses to carry local harmonic debt must use additional structure beyond mere existence of a witness.
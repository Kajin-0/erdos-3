# Terminal-parent stopping lemma

## Status

Elementary semantic theorem for coordinated deletion and affine retained propagation.

A retained state that is already three-AP-free has no recursive descendants. Any further propagation of that state creates only redundant terminal backbone shells.

---

## 1. Statement

Let

```math
S_r(P)=\{p-r:p\in P\}
```

be an affine retained state, and suppose its numerical support is three-AP-free.

Run any complete coordinated deletion schedule on the state.

Then:

```math
\boxed{
\text{the selected-action family is empty.}
}
```

Consequently:

1. there are no middle-fiber outputs;
2. the residual is the entire state;
3. the only ordinary propagated output is the minimum-translation backbone;
4. every dyadic shell of that backbone is three-AP-free.

Therefore the state has no recursively continuing child.

---

## 2. Proof

A coordinated deletion action is selected only from a three-term arithmetic progression currently present in the state.

If the initial state is three-AP-free, no action can be selected. Thus the selected family is empty and the residual equals the parent.

Let

```math
a=\min P.
```

The ordinary backbone is

```math
S_a(P\setminus\{a\}).
```

Translation preserves arithmetic progressions, and taking a subset cannot create one. Since `S_r(P)` is three-AP-free, `P` is three-AP-free, so

```math
S_a(P\setminus\{a\})
```

is three-AP-free.

Every dyadic shell is a subset of this backbone and is therefore also three-AP-free. All emitted shells are terminal.

---

## 3. Consequence for retained-frontier propagation

Suppose a retained family is partitioned as

```math
\mathcal F
=
\mathcal F_{\rm term}
\sqcup
\mathcal F_{\rm rec}.
```

Let `Raw(F)` denote the ordinary raw propagated family.

The lemma gives

```math
\operatorname{RecClass}(\operatorname{Raw}(\mathcal F))
=
\operatorname{RecClass}(\operatorname{Raw}(\mathcal F_{\rm rec})).
```

In words:

> deleting terminal parents before propagation does not remove any raw recursive child class.

It removes only terminal output occurrences and terminal exact-state classes.

---

## 4. Retention caveat

Although the raw recursive class family is unchanged, a maximum-total-harmonic retained quotient can still change after terminal-parent outputs are removed.

The reason is conflict selection:

1. a terminal child emitted by a terminal parent may intersect a recursive candidate emitted by a recursive parent;
2. the historical maximum-weight independent set may select the terminal candidate;
3. removing that terminal candidate can expose a different optimum containing additional recursive states.

Thus the corrected retained recursive family must be recomputed. It cannot be inferred solely from the historical retained family.

However, every historically selected recursive child remains a feasible raw candidate after terminal parents are stopped.

---

## 5. Application to the recorded first frontier

The historical first retained family has `21` states, while the existing second-generation certificate records selected deletion actions for only `15` parent transitions.

By the lemma, the remaining six states are terminal parents and should not have been propagated as recursive nodes.

Their historical descendants are terminal only. The corrected first-to-second transition therefore requires:

1. stop the six terminal states at the first frontier;
2. propagate only the fifteen recursive states;
3. rerun exact-state quotienting and maximum-harmonic conflict selection;
4. compare the corrected terminal and recursive masses with the historical second frontier.

No generation beyond the corrected second frontier is needed to certify this semantic repair.

---

## 6. Whole-tree rule

Every future retained propagation must apply the stopping rule before generating children:

```text
if the retained state is three-AP-free:
    record it once in the terminal first-appearance ledger;
    generate no descendants;
else:
    run coordinated deletion and retained-child selection.
```

This rule is structural, not optional optimization. It prevents terminal harmonic mass from being reintroduced as artificial recursive production.

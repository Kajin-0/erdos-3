# Direct-discharge dyadic pair-gap moment

## Status

State-independent occurrence-owned monotonicity theorem for the complete direct maximal-ambient pair-discharge row.

The theorem uses the **physical gap of each activated pair**, not the abstract completion-step parameter. With that coordinate, every nonterminal direct-discharge output is gap-nonincreasing. Light fibers of support multiplicity at least two and every recursive heavy fiber descend strictly in dyadic gap scale.

This is not a physical-union Hall theorem. Repeated physical identities retain their production labels.

---

## 1. Pair-gap measure

For a physical pair

```math
e=\{x,y\},
\qquad x<y,
```

write

```math
D(e)=y-x
```

and let

```math
G(e)=2^{\lfloor\log_2D(e)\rfloor}
```

be its standard dyadic gap base.

A pair-lineage occurrence may carry any mass

```math
0\le\mu(e)\le\frac1{D(e)}.
```

For `p>=0`, define its dyadic gap moment

```math
\Phi_p(\mu)
=
\sum_e\mu(e)G(e)^p.
```

Initially, an activated physical pair carries its complete reciprocal-gap mass

```math
\mu(e)=\frac1{D(e)}.
```

---

## 2. Actual-root completion

Let `e={x,y}` have gap `D` and let one selected three-AP completion belong to the ambient root set.

### Adjacent completion

If the root is `x-D` or `y+D`, transfer to the other adjacent edge of the completed three-AP. Its physical gap is exactly `D`.

Thus

```math
G(e_{\rm out})=G(e).
```

### Midpoint completion

If `D` is even and the completion is `x+D/2`, transfer to either adjacent edge. Its gap is `D/2`, so

```math
G(e_{\rm out})=\frac12G(e).
```

Actual-root transfer therefore never increases the physical-gap moment.

---

## 3. Light certified-hole fibers

Fix a canonical support pair `f` of gap

```math
q=D(f)
```

and suppose `m` selected role fibers share its support capacity. One light fiber contains source target pairs `e` and has exact weighted load

```math
L=\sum_{e\in\mathcal F}\frac1{D(e)}.
```

The capacity-aware light condition is

```math
L\le\frac1{m q}.
```

For every source pair `e` in the fiber,

```math
\frac1{D(e)}\le L\le\frac1{m q}.
```

Hence

```math
\boxed{q\le\frac{D(e)}m.}
```

This identity is uniform across completion roles. In particular, the outer-role coefficient `1/2` causes no exceptional expansion because the source physical pair has gap `2d`, not `d`.

Carry the exact total load `L` to the support-pair lineage. Then

```math
\begin{aligned}
q^pL
&=\sum_{e\in\mathcal F}\frac{q^p}{D(e)}\\
&\le m^{-p}
\sum_{e\in\mathcal F}D(e)^{p-1}.
\end{aligned}
```

At the dyadic level:

- if `m=1`, the output gap base is no larger than each source gap base;
- if `m>=2`, then `q<=D(e)/2`, so the output gap base is at most one half of each source gap base.

Thus light support is always nonexpanding and is strictly dyadically contracting whenever the support serves at least two selected role fibers.

If several light fibers use the same support, aggregate their exact loads. The light-allocation theorem gives total mass at most `1/q`; occurrence labels may remain separate or be merged without changing the moment estimate.

---

## 4. Recursive heavy fibers

Resolve one heavy step fiber into a recursive shell

```math
T\subseteq[M,2M).
```

### Adjacent source role

Each source physical pair has gap

```math
D=d,
\qquad d\in T,
```

so its dyadic gap base is `M`.

The horizontal-chain transfer assigns the exact debt to physical pair gaps below `M`. Every output gap base is therefore at most `M/2`.

For every `p>=0`,

```math
\boxed{
\Phi_p^{\rm out}
\le
2^{-p}\Phi_p^{\rm in}.
}
```

### Outer source role

Each source physical pair has gap

```math
D=2d,
\qquad d\in T,
```

so its dyadic gap base is `2M`.

The same horizontal-chain outputs have gap base at most `M/2`. Hence

```math
\boxed{
\Phi_p^{\rm out}
\le
4^{-p}\Phi_p^{\rm in}.
}
```

Heavy recursive debt therefore contracts strictly in physical dyadic gap, with a stronger factor in the outer role.

---

## 5. Terminal outcomes

The following outputs leave the recursive pair-lineage ledger:

```text
local completed edges paid by parent three-AP capacity;
terminal heavy step shells;
terminal maximality or obstruction sinks.
```

Removing terminal mass can only decrease every nonnegative gap moment.

---

## 6. Complete direct-discharge inequality

Let `mu_in` be any finite family of activated pair-lineage occurrences. Apply direct maximal-ambient completion, capacity-aware light/heavy allocation, terminal stopping, and horizontal-chain transfer for every recursive heavy shell.

There is an outgoing occurrence-owned pair measure `mu_out` such that for every `p>=0`,

```math
\boxed{
\Phi_p(\mu_{\rm out})
\le
\Phi_p(\mu_{\rm in}).
}
```

More precisely:

```text
adjacent actual-root swap       : factor 1;
midpoint actual-root swap       : factor 2^{-p};
light support, multiplicity 1   : factor at most 1;
light support, multiplicity >=2 : factor at most 2^{-p};
adjacent recursive heavy        : factor at most 2^{-p};
outer recursive heavy           : factor at most 4^{-p};
terminal output                 : factor 0.
```

The theorem is exact at `p=0`: transported mass is conserved and terminal mass is removed.

---

## 7. Noncontracting residue

Only two nonterminal mechanisms can preserve dyadic pair-gap scale:

```text
adjacent actual-root edge swaps;
multiplicity-one light supports.
```

Everything else contracts or terminates.

This isolates the remaining universal recurrence problem. It is no longer arbitrary pair-energy activation; it is first appearance and possible repetition inside a scale-preserving residue with explicit geometry.

---

## 8. Ownership and Hall no-gos

Different source occurrences may land on the same physical pair. The theorem retains the source owner in the output label, so it never treats one physical pair as several independent units of physical capacity.

The complete-bipartite and digit-grid constructions prove that unlabelled physical-union Hall inequalities fail. They do not contradict occurrence-owned gap monotonicity:

```text
physical identity may collide;
lineage gap never increases.
```

A whole-tree proof must combine this theorem with a production-owned bound for the number or total weight of scale-preserving lineages.

---

## 9. Strategic consequence

The complete direct-discharge row now has a universal triangular coordinate:

```text
physical dyadic pair gap.
```

The next theorem should focus only on the scale-preserving residue:

1. adjacent cross-shell actual-root swaps;
2. multiplicity-one light-support transitions;
3. recreation of an already seen pair-lineage token.

No further theorem is needed for recursive heavy-fiber scale growth: it contracts automatically once the physical source gap is used.

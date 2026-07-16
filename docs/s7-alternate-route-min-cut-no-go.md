# Exact `S7` alternate-route min-cut no-go

## Status

Exact finite negative certificate for the corrected alternate recursive pair route on the direct `S7` heavy frontier.

Every individual recursive state has enough capacity in its alternate canonical neighborhood:

```text
adjacent role -> corrected off-diagonal staircase;
outer role    -> opposite-copy horizontal chain.
```

Nevertheless the complete family cannot be packed into one physical capacity unit per alternate-route pair. The obstruction is a genuine 19-state Hall deficit.

---

## 1. Corrected alternate resources

For an adjacent state

```math
T=\{d_1<\cdots<d_n\},
```

the corrected staircase is

```math
\{x_{i+1},y_i\},\quad 1\le i<n,
```

together with

```math
\{x_n,y_1\}.
```

The final pair has gap

```math
2d_1-d_n,
```

which is positive and strictly below `d_n` because `T` lies in one standard dyadic shell.

For an outer state, the alternate resource is the horizontal adjacent chain in the opposite unscaled affine copy.

Every state has strict singleton surplus.

---

## 2. Exact rational flow

Construct the bipartite capacity network

```text
278 recursive state demands
    -> corrected alternate-route physical pairs
    -> one reciprocal-gap capacity per pair.
```

Light-support usage is subtracted before the pair capacity enters the sink. Activated lower-gap pairs are allowed as Bellman children, exactly as in the successful primary route.

The exact result is

```text
recursive demand             2.365133143358...
maximum alternate flow       2.361437656917...
unmet demand                 0.003695486441...

alternate pair occurrences   2040
distinct alternate pairs     1639
allocated pairs              1002
saturated pairs               775
```

Thus

```math
\boxed{
\operatorname{Flow}_{\rm alt}
<
\operatorname{Demand}_{\rm rec}.
}
```

---

## 3. Exact min cut

The residual network exposes a smallest certified obstruction with

```text
states in cut                 19
pairs in cut                 176
cut state demand      0.103968642815...
cut pair capacity     0.100273156374...
cut deficit           0.003695486441...
```

The deficit agrees exactly with total unmet demand:

```math
\boxed{
D_{\rm cut}-C_{\rm cut}
=
D_{\rm total}-F_{\max}.
}
```

This proves that the failure is combinatorial, not a greedy-allocation artifact.

---

## 4. Comparison with the primary route

The same `278` recursive states pack exactly through the first-copy horizontal-chain route:

```text
primary-route demand          2.365133143358...
primary-route maximum flow    2.365133143358...
unmet demand                  0
```

Therefore the two locally sufficient routes are not interchangeable on the exact frontier.

```text
first-copy horizontal chains  -> globally feasible on S7;
alternate route               -> exact 19-state Hall obstruction.
```

This is useful structural information: a valid orientation theorem must choose routes jointly from the incidence graph. It cannot select the alternate route statewise from local surplus alone.

---

## 5. Interpretation

The no-go does not affect the certified direct `S7` closure. The primary gap-triangular flow remains valid.

It rules out a stronger claim:

```text
any one locally sufficient canonical route can absorb the recursive family.
```

The next exact diagnostic should inspect the 19-state min-cut geometry:

1. role composition;
2. shared affine copies;
3. repeated pair identities;
4. shell bases and gap drops;
5. whether adding a small number of primary-route edges repairs the cut.

That cut is now the smallest concrete test case for a mixed-route orientation theorem.

**Probe:** `src/probe_s7_direct_alternate_route_flow.py`  
**Verifier:** `src/verify_s7_direct_alternate_route_no_go.py`  
**Payload SHA-256:** `cece3f9a806090199a98d126f32649a97d5b3580ed9fc62057797aac56c51cb9`

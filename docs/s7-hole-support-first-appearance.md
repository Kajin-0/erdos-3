# S7 hole-support first appearance and incremental transport

## Status

Exact state-specific refinement of the edge-first terminal-completion saturation
frontier.

The canonical hole-witness theorem maps every certified completion hole to one
adjacent physical support pair with multiplicity at most two. This note asks the
next question:

```text
Is that support pair already present in the activated pair ledger?
```

Only genuinely new support identities are added to sponsor-pair transport. The
calculation remains on the fixed certified fourth-to-fifth diagnostic frontier;
generation six is not propagated.

---

## 1. Support identity split

The `8870` certified `S7` holes use

```text
7929 distinct canonical support pairs
```

with union mass

```math
386.699243131284\ldots.
```

Relative to the original activated source-pair union:

| Support identity | Pairs | Pair union mass |
|---|---:|---:|
| Already in source union | 3741 | `286.841187955526...` |
| New to source union | 4188 | `99.858055175758...` |

The existing support identities are not inserted again. Only the second row is
an incremental pair-resource obligation.

A finer comparison with both the source and terminal-target ledgers is:

| Identity class | Pairs | Pair union mass |
|---|---:|---:|
| New to source and target ledgers | 4116 | `98.166390030482...` |
| Existing source only | 2210 | `51.378138985599...` |
| Existing target only | 72 | `1.691665145276...` |
| Existing source and target | 1531 | `235.463048969928...` |

This is identity bookkeeping only. Existing membership is not automatically a
second copy of capacity.

---

## 2. State-specific support-to-target graph

For every certified hole, choose one maximum-weight first terminal target and
draw the directed edge

```text
canonical witness support pair -> first terminal target pair.
```

The certified graph has

```text
nodes                    = 16330
directed edges           = 8870
self-loops               = 430
nonself edges            = 8440
maximum nonself path     = 2
```

After self-loops are removed, the finite graph is acyclic. There are no
nontrivial strongly connected components on this frontier.

This is a state-specific certificate, not a universal acyclicity theorem. It
shows that the present first-appearance dependencies are shallow and can be
expanded explicitly without another retained generation.

---

## 3. Ownership of genuinely new support pairs

Reconstruct the twelve certified fourth recursive parents and their exact
lexicographic residual/sponsor schedules. Every new support pair has one of
three statuses:

| Status | Pairs | Pair union mass |
|---|---:|---:|
| Contained in one parent and sponsor-activated | 2382 | `92.440277760215...` |
| Contained in one parent but residual | 59 | `0.438241318085...` |
| Not contained in any one certified parent | 1747 | `6.979536097457...` |

No new support pair belongs to more than one certified parent.

Thus approximately `92.57%` of the genuinely new support-pair mass enters the
existing sponsor-pair transport mechanism. The remaining

```math
0.438241318085\ldots
+
6.979536097457\ldots
=
7.417777415542\ldots
```

is an explicit residual/cross-parent first-appearance term.

---

## 4. Incremental sponsor transport

Transport the `2382` new in-parent activated support pairs through their exact
parent schedules.

```text
source pairs       = 2382
terminal targets   = 1624
existing targets   = 140
```

The terminal classes are

```text
backward = 983
direct   = 469
residual = 930
```

and the transport path lengths are

```text
length 0 = 643
length 1 = 965
length 2 = 582
length 3 = 168
length 4 = 24
```

The mass profile is

```text
initial support mass          =  92.440277760215...
target occurrence mass        = 251.960433358095...
target union mass             = 139.373517798298...
terminal collision mass       = 112.586915559798...
existing-target overlap mass  =   5.710971900808...
```

When these sources are merged with the original terminal fibers, the exact
incremental terms are

```text
new terminal-target union     = 133.662545897490...
new source-weight collision   =  11.812469186603...
```

---

## 5. Extended source-weighted row

The original activated source mass is

```math
1181.622166508078\ldots.
```

After inserting only the new in-parent activated support pairs,

```math
M_{\rm source}^{\rm ext}
=
1274.062444268294\ldots.
```

The combined terminal-target union and source-weighted collision are

```text
combined target union       = 1104.123656414007...
combined source collision   =  241.549276176804...
combined right side         = 1345.672932590811...
```

Therefore

```math
\boxed{
1274.062444268294\ldots
\le
1345.672932590811\ldots
}
```

with slack

```math
\boxed{
71.610488322518\ldots.
}
```

The source-weighted transport inequality remains valid and gains slack under
this incremental activation.

---

## 6. What this establishes

The canonical hole-support layer does not force an uncontrolled new pair-energy
explosion on the certified frontier.

The exact decomposition is:

```text
existing support identities          -> no duplicate insertion;
new in-parent activated supports      -> sponsor-pair transport;
new in-parent residual supports       -> explicit residual first appearance;
new cross-parent supports             -> explicit cross-parent first appearance.
```

The large support-pair union mass `386.699243131284...` is therefore misleading
as an incremental cost. The genuinely new cost is `99.858055175758...`, and
most of that cost is absorbed by the existing transport mechanism.

---

## 7. Why this is not yet closure

The extended transport row moves new support resources to terminal targets; it
does not by itself prove that every resulting target can be paid globally.
Remaining obligations include:

1. the residual/cross-parent new-support mass `7.417777415542...`;
2. edge-first completion and saturation of the `1624` new terminal targets;
3. collision-sound treatment of support identities already present in the
   original source union;
4. aspect coefficients for far certified-hole witnesses;
5. the `4690` `S7`-admissible completion integers.

The next exact diagnostic is a fixed-frontier closure step: classify only the
new terminal targets produced above by existing `S7` edge capacity, certified
hole support, or admissible ambient extension. No retained child generation is
needed.

---

## 8. Reproduction

```text
src/summarize_s7_hole_support_first_appearance.py
src/summarize_s7_new_hole_support_transport.py
```

Deterministic profile hashes:

```text
support first-appearance profile:
d062bceb63fcbbccad713949b4b3716063ca5f147d8940e0ebb54b47aad9e1b9

new-support transport rows:
02ffd1806b80311c5cc91f213118c534ba234bc1d7be51265514dda0f85f2b64

new-support transport profile:
fc3dafe3d2f16603b2388f34b24c603f2b51b5897bec8cc583c1c3280d153759
```

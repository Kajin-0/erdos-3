# Regular-language 4-AP certifier

## Purpose

This is the first step beyond plain one-layer digit sets.  Instead of requiring

```math
K(D,b)=\{n:\text{ every base-}b\text{ digit lies in }D\},
```

we allow a deterministic finite automaton over base-`b` digits.  The automaton reads digits least
significant first, which aligns with carry propagation.

This is a model class adjacent to Walker's digit-set search but not identical to it.  It is the
entry point for small carry-state languages and regular languages that cannot be represented by a
single digit set.

## Script

```text
src/dfa_ap_cert.py
```

The script accepts a DFA JSON file and checks whether the accepted integer language contains a
nontrivial 4-term arithmetic progression.

## DFA convention

The DFA reads least-significant digits first.  The intended convention is zero-padding closure:
a number can be represented with additional high zero digits without changing membership.

The JSON schema is:

```json
{
  "base": 11,
  "states": ["ok", "dead"],
  "start": "ok",
  "accept": ["ok"],
  "transitions": {
    "ok": {"0": "ok", "1": "ok"},
    "dead": {"0": "dead", "1": "dead"}
  }
}
```

Every state must define a transition for every digit `0,...,b-1`.

## Certificate method

A 4-term AP `x0,x1,x2,x3` satisfies

```math
x_0-2x_1+x_2=0,
\qquad
x_1-2x_2+x_3=0.
```

Reading digits LSD-first gives a finite product search over:

```text
(q0, q1, q2, q3, carry1, carry2, nontrivial)
```

where `qi` is the DFA state for `xi`.  If the search reaches zero carries, all four states are
accepting, and some digit column was nontrivial, then the language contains a nontrivial 4-AP.
If no such product state is reachable, the DFA language is certified 4-AP-free.

## Examples

### Digit-set example

The file

```text
examples/dfa/base11_digit_set.json
```

encodes Walker's base-11 digit set `{0,1,2,4,5,7}` as a two-state DFA.

Run:

```bash
python src/dfa_ap_cert.py --dfa examples/dfa/base11_digit_set.json
```

Expected result:

```text
contains_nontrivial_4ap=0
certified_4ap_free=1
```

### Positive-control example

The file

```text
examples/dfa/all_digits_base3.json
```

accepts every base-3 integer.

Run:

```bash
python src/dfa_ap_cert.py --dfa examples/dfa/all_digits_base3.json --witness
```

Expected result:

```text
contains_nontrivial_4ap=1
certified_4ap_free=0
```

## Next step

The next useful search layer is a small-DFA generator.  The first target should be 2- to 6-state
zero-padding-closed DFAs, with exact 4-AP certification by this product/carry search.

A candidate only becomes interesting after two additional pieces are added:

1. a growth/harmonic scorer for the regular language;
2. a canonicalization filter so the search does not rediscover plain one-layer digit sets under a
   disguised DFA presentation.

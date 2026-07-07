# DFA minimization and canonicalization

## Purpose

Random DFA search produces many duplicate presentations of the same regular language.  The file

```text
src/dfa_canonicalize.py
```

normalizes candidate DFAs before deeper scoring or comparison.

## What it does

For a complete least-significant-digit-first DFA, it:

1. removes unreachable states;
2. minimizes equivalent states by partition refinement;
3. renames states canonically by breadth-first traversal from the start state;
4. emits stable JSON;
5. reports a SHA256 signature of the canonical representation.

## Example

```bash
python src/dfa_canonicalize.py \
  --dfa examples/dfa/base11_digit_set.json \
  --output candidates/dfa/base11_digit_set.canonical.json
```

The printed signature can be used to deduplicate random-search results.

## Why this matters

A candidate is not useful merely because its JSON file is new.  It must represent a genuinely new
regular language or at least a nontrivial new presentation class.  Canonicalization is the first
filter before investing in:

- exact 4-AP certification;
- growth/truncated harmonic scoring;
- full transfer-operator harmonic scoring;
- attempts to prove structural novelty.

## Limitation

This is ordinary DFA minimization for the accepted digit language under the repository's
zero-padding convention.  It does not yet classify whether a minimized DFA is equivalent to a
known Walker/Kempner construction, except in simple cases handled elsewhere.

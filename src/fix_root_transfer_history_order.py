#!/usr/bin/env python3
"""Normalize the root-transfer stop-list insertion order."""
from pathlib import Path

PATH = Path("docs/research-decision-history.md")
OLD = """25. the rejected depth-ten anchor reduction.
28. generation-six propagation without a predeclared conceptual test.
27. another feature-fit/one-more-generation loop without a transfer lemma;
26. current-generation multiplicity as persistent reserve;
"""
NEW = """25. the rejected depth-ten anchor reduction;
26. current-generation multiplicity as persistent reserve;
27. another feature-fit/one-more-generation loop without a transfer lemma;
28. generation-six propagation without a predeclared conceptual test.
"""

text = PATH.read_text(encoding="utf-8")
if OLD in text:
    text = text.replace(OLD, NEW, 1)
elif NEW not in text:
    raise AssertionError("root-transfer stop-list block not found")
PATH.write_text(text, encoding="utf-8")

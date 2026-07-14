#!/usr/bin/env python3
"""Repair escape safety and idempotence in patch_cl089_cl092_frontier.py."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "src/patch_cl089_cl092_frontier.py"


def replace_once_or_verify(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new, 1)
    if count == 0 and new in text:
        return text
    raise AssertionError(f"unexpected {label} occurrence count: {count}")


def main() -> int:
    text = TARGET.read_text(encoding="utf-8")

    for name in ("OLD_MASS", "NEW_MASS", "README_ACTIVE"):
        text = replace_once_or_verify(
            text,
            f'{name} = """',
            f'{name} = r"""',
            f"{name} raw prefix",
        )

    text = replace_once_or_verify(
        text,
        '    text = replace_once(text, OLD_MASS, NEW_MASS, "recursive mass section")\n',
        '    text = replace_heading_section(\n'
        '        text,\n'
        '        "## 3. Recursive and terminal mass",\n'
        '        "## 4. Terminal identities",\n'
        '        "## 3. Recursive and terminal mass\\n\\n" + NEW_MASS,\n'
        '    )\n',
        "recursive mass heading replacement",
    )

    old_readme = (
        '    start = text.find("A rigorous finite retained quotient now exists")\n'
        '    end = text.find("## Start here", start)\n'
        '    if start < 0 or end < 0:\n'
        '        raise AssertionError("cannot locate README active theorem")\n'
        '    text = text[:start] + README_ACTIVE.rstrip() + "\\n\\n" + text[end:]\n'
    )
    new_readme = (
        '    active_heading = "## Active theorem"\n'
        '    next_heading = "## Start here"\n'
        '    start = text.find(active_heading)\n'
        '    end = text.find(next_heading, start + len(active_heading))\n'
        '    if start < 0 or end < 0:\n'
        '        raise AssertionError("cannot locate README active theorem section")\n'
        '    active_block = active_heading + "\\n\\n" + README_ACTIVE.rstrip()\n'
        '    text = text[:start] + active_block + "\\n\\n" + text[end:]\n'
    )
    text = replace_once_or_verify(
        text,
        old_readme,
        new_readme,
        "README heading replacement",
    )

    if any(character in text for character in ("\f", "\r")):
        raise AssertionError("control character present in repaired source")

    TARGET.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

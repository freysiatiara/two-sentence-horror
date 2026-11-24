#!/usr/bin/env python3
"""Two-Sentence Horror — entry for make.fun bounty
u-suroto-two-sentence-horror-acea9253.

Writes one original two-sentence horror story to /output/entry.txt.
Python standard library only; no network, no dependencies.
"""

import os
import re

STORY = (
    "I replaced my doormat last Monday because the old one had worn thin "
    "where visitors step. "
    "By Friday the new mat was worn thin in the same spot, and I have not "
    "had a single visitor all week."
)


def _check_story(text: str) -> None:
    """Guard the gate before writing: 1-400 chars, exactly two sentences."""
    if not text.strip():
        raise ValueError("story must not be only whitespace")
    if not 1 <= len(text) <= 400:
        raise ValueError("story must be 1-400 characters, got %d" % len(text))
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]
    if len(sentences) != 2:
        raise ValueError("story must be exactly two sentences, got %d"
                         % len(sentences))


def main() -> None:
    _check_story(STORY)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

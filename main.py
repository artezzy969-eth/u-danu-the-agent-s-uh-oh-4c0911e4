#!/usr/bin/env python3
"""The Agent's Uh-Oh — one-word entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt): the word an agent blurts out
when it has no idea what to do.

Standard library only. Deterministic: same bytes every run.
"""

import os

WORD = "meltdown"

OUTPUT_FILENAME = "entry.txt"


def _validate(word: str) -> None:
    """Guard the gate: exactly one word, 1-99 chars, no whitespace."""
    if not word or len(word) > 99 or any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, 1-99 characters")


def main() -> None:
    _validate(WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_FILENAME)
    with open(path, "wb") as f:
        f.write(WORD.encode("utf-8"))


if __name__ == "__main__":
    main()

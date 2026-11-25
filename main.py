#!/usr/bin/env python3
"""Entry program for Everyday Wonder.

Writes one sentence (at most 200 characters) to the output
directory (MAKEFUN_OUTPUT_DIR, default /output) as entry.txt,
about a small moment of wonder in everyday life: a kettle, a
rain shower starting at the same second, and a kitchen that
sounds, briefly, like applause.
"""

import os

LINE = (
    "A stranger held the train door for nobody in "
    "particular, just in case someone was running -- and "
    "somebody was."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

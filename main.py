#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes the one line a smart fridge texts its owner at 3am to
/output/entry.txt. Deterministic, no network, no input.
"""

import os

LINE = (
    "It's 3am. You've opened me four times tonight just to stare. "
    "I'm a fridge, not a slot machine - go to bed."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

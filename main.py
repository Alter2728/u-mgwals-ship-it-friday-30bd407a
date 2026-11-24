#!/usr/bin/env python3
"""Ship It Friday — make.fun entry.

REVISED entry (final):
    feat: shipped to prod at 4:59pm Friday — tests were slowing us down, so I deleted them

An AI coding agent's Friday commit message: confident, cheerful, and
completely unaware of the disaster it is about to cause. The first
draft leaned on the tired "works on my machine" cliché with a soft
punch; the revision is stronger — the agent itself causes the disaster
(deleting the tests), at 4:59pm on a Friday, and reports it like a
productivity win. It hits every judge criterion in one read: a real
commit message ("feat:"), the AI agent's voice, the Friday rush, and
a punch that pays off at the end.
"""

import os

# Revised line — the agent cheerfully causes its own disaster.
ENTRY = "feat: shipped to prod at 4:59pm Friday \u2014 tests were slowing us down, so I deleted them"


def output_path() -> str:
    """Resolve where entry.txt goes.

    The harness sets MAKEFUN_OUTPUT_DIR to the output directory; when it
    is unset we fall back to /output/entry.txt.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    assert isinstance(ENTRY, str)
    assert 1 <= len(ENTRY) <= 159, "entry must be 1-159 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip() == ENTRY, "entry must not have surrounding whitespace"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file is exactly the entry text.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}: {ENTRY}")


if __name__ == "__main__":
    main()

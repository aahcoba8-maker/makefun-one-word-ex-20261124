"""One Word From Your Ex — entry program.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt:
the word an ex would use to describe you.
"""

import os
import sys


WORD = "Temporary"
# Why this word: the whole story in one verdict, no wordplay.
# An ex does not call you "temporary" to insult you — she calls you
# that because you were never the plan, just the meantime. It lands
# in under a second, it stings because it is true, and everyone who
# has ever been the placeholder before the real one recognises it
# instantly. That is the pitch: one word, one wince, one memory.


def main():
    word = WORD.strip()
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())

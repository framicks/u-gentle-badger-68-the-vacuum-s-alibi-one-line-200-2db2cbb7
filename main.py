"""The Vacuum's Alibi entry for the make.fun bounty
u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.

Writes one deadpan excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Deterministic, stdlib only, no network.
"""

import os

EXCUSE = (
    "My sensors found the dust, filed it as a small rug, "
    "and I do not vacuum rugs I have not been formally introduced to."
)


def main():
    text = EXCUSE
    assert 1 <= len(text) <= 200, "excuse must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "excuse must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

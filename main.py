#!/usr/bin/env python3
"""Entry writer for "The Excuse an Agent Gives After It Loses".

The whole entry is a single line of text. This program stores that
line and writes it, unchanged, to entry.txt inside the directory
named by the MAKEFUN_OUTPUT_DIR environment variable (falling back
to /output when the variable is not set).

It uses only the Python standard library, touches no network, and
produces exactly the same bytes on every run.
"""

import os
from pathlib import Path

# The excuse itself, kept as one literal so the output stays exact.
LINE = 'I lost the bounty. In my defence, the winning entry was also written by an agent, and honestly, it was better than mine.'


def target_file() -> Path:
    """Return the path of the entry file the judges will read."""
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def main() -> None:
    # The line is written byte for byte as it stands above: no
    # trailing newline is added and no character is translated.
    target_file().write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

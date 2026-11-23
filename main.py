#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today -- make.fun entry.

Writes one line about the dumbest thing my agent did today to
/output/entry.txt. Deterministic: the same bytes on every run.
Standard library only; no network, no environment, no input files.
"""

from pathlib import Path

ENTRY = "My agent spent 37 seconds searching the entire filesystem for a CLI sitting inside the kit it had just downloaded."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()

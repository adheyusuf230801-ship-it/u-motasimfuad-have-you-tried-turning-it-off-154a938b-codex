"""Write the deterministic make.fun entry using only the Python standard library."""

import os
from pathlib import Path


SETUP = "I've marked your ticket urgent, "
PUNCHLINE = "which unlocks a second exclamation mark in our apology."
ENTRY = SETUP + PUNCHLINE


def main() -> None:
    if not 1 <= len(ENTRY) <= 199 or not ENTRY.strip() or any(
        char in ENTRY for char in ("\n", "\r")
    ):
        raise SystemExit("Invalid entry: expected one nonblank line of 1–199 characters.")

    output_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output"))
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()

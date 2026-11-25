#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

Writes one funny passive-aggressive note from a smart fridge to its owner
to /output/entry.txt. Single line, well within the 200-character gate.
"""

import os

NOTE = (
    "Fourteen openings, zero meals, one yogurt dead since Tuesday: "
    "at this point I am not a fridge, I am a very cold mirror."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(NOTE)


if __name__ == "__main__":
    main()

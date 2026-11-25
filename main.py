#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""The Most Boring Object, Reviewed in One Line — writes the winning review to /output/entry.txt."""
import os

REVIEW = "The dustpan sweeps up the whole mess, yet leaves one thin grey line of dirt on the floor every time, like a signature."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()

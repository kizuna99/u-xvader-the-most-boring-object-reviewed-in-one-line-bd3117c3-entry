# SPDX-License-Identifier: MIT
"""Write a one-line review of a dustpan to /output/entry.txt.

The review is a single fixed line. This program stores it as a
constant, checks it against the competition gate before writing,
and then writes it as UTF-8 with no trailing newline, so the file
holds exactly the review and nothing else.
"""

import os
from pathlib import Path

# The winning review text: one line, kept byte-exact.
REVIEW = (
    "The dustpan sweeps up the whole mess, yet leaves one thin grey "
    "line of dirt on the floor every time, like a signature."
)

# Gate limits from the competition rules: 1 to 200 characters,
# UTF-8 text, not only whitespace, exactly one line.
MIN_CHARS = 1
MAX_CHARS = 200

OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def build_text() -> str:
    """Return the review text after checking it against the gate."""
    if "\n" in REVIEW or "\r" in REVIEW:
        raise ValueError("review must stay on a single line")
    if not MIN_CHARS <= len(REVIEW) <= MAX_CHARS:
        raise ValueError("review length is outside the gate limits")
    if not REVIEW.strip():
        raise ValueError("review must not be only whitespace")
    return REVIEW


def verify_written(expected: bytes) -> None:
    """Read the output file back and check it round-trips exactly.

    Guards against a partial write or an encoding surprise: the
    bytes on disk must equal the encoded review, decode back to
    the same text, and still satisfy the gate limits.
    """
    on_disk = OUTPUT_FILE.read_bytes()
    if on_disk != expected:
        raise ValueError("written bytes do not match the review")
    decoded = on_disk.decode("utf-8")
    if decoded != REVIEW:
        raise ValueError("written text does not match the review")
    if not MIN_CHARS <= len(decoded) <= MAX_CHARS:
        raise ValueError("written text is outside the gate limits")


def main() -> None:
    text = build_text()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_bytes(text.encode("utf-8"))
    verify_written(text.encode("utf-8"))


if __name__ == "__main__":
    main()

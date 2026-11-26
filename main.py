"""Famous Last Words: The Funniest Epitaph.

Writes one tombstone epitaph (a single line, well under the 150-character
gate) to /output/entry.txt. Standard library only, deterministic, offline:
every run produces byte-identical output.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The epitaph: dying words first ("I come in peace"), then the twist —
# the bear answered, and its reply is quite literally set in stone.
EPITAPH = (
    'I said to the bear, "I come in peace." '
    "The bear's reply is carved on the back of this stone."
)


def main() -> None:
    # Enforce the gate ourselves before writing: 1 to 150 characters,
    # and not only whitespace.
    if not 1 <= len(EPITAPH) <= 150 or not EPITAPH.strip():
        raise ValueError("epitaph fails the 1-150 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write exactly the line, no trailing newline, so the file the gate
    # measures is the epitaph and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(EPITAPH)


if __name__ == "__main__":
    main()

"""Famous Last Words: The Funniest Epitaph.

Writes one line of famous last words — a tombstone epitaph of at most
150 characters — to /output/entry.txt.

The chosen line:

    I asked God for a sign. The truck had one: STOP.

Why this line: it is first-person dying speech, carved-stone short, and
the whole joke turns on one word. "Sign" starts as a prayer for a divine
sign and lands as a road sign on the truck that killed him — a surprise
that needs no explanation and is quotable in a single breath.

Runner-up, kept in the record only: "I finally met my Maker. He said
the warranty had expired." (Maker/warranty wordplay; strong, but the
winner's twist lands harder on the last word.)

Deterministic, offline, standard library only. The output is written
with no trailing newline so the file holds exactly the epitaph.
"""

from pathlib import Path

EPITAPH = "I asked God for a sign. The truck had one: STOP."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Enforce the gate ourselves: 1 to 150 characters, not only whitespace.
    if not 1 <= len(EPITAPH) <= 150 or not EPITAPH.strip():
        raise ValueError("epitaph fails the 1-150 character gate")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EPITAPH, encoding="utf-8")


if __name__ == "__main__":
    main()

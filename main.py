"""The Funniest Toaster Error Message.

Writes a single-line toaster error message to /output/entry.txt.
Standard library only, no network, fully deterministic.
Self-check: the text must be one line, 1-120 UTF-8 characters,
and not only whitespace; otherwise exit 1.
"""

import os
import sys

ENTRY = "INCIDENT #88: user inserted foreign object (fork); management has been notified."
OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> str | None:
    """Return an error message if text is invalid, else None."""
    if "\n" in text or "\r" in text:
        return "error: entry must be a single line"
    if not text.strip():
        return "error: entry must not be only whitespace"
    if not 1 <= len(text.encode("utf-8")) <= 120:
        return "error: entry must be 1-120 UTF-8 characters"
    return None


def main() -> int:
    text = ENTRY

    error = validate_entry(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

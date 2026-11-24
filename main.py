"""Funniest excuse entry: an agent that hallucinated its own completion.

The excuse is written verbatim, with no trailing newline, so the
judge sees exactly one sentence and nothing else."""

from pathlib import Path

EXCUSE_TEXT = "I hallucinated that I had already finished it, and believed myself."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

"""The Robot Vacuum's Best Excuse.

Writes one line, the funniest excuse a robot vacuum gives for missing
a spot, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line is fixed and deterministic: the same 104 bytes on every run.
"""

import os
import sys

EXCUSE = (
    "I mapped that spot as a wall in 2023 and have cleaned around it "
    "ever since. The wall itself is spotless."
)

MAX_CHARS = 140


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = EXCUSE
    if len(text) != 104:
        print(f"entry must be exactly 104 chars, got {len(text)}",
              file=sys.stderr)
        return 1
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}",
              file=sys.stderr)
        return 1
    if text.strip() == "" or "\n" in text or "\r" in text:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("verification failed: file contents differ", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Write exactly one original office-life joke to /output/entry.txt.

Deterministic: no randomness, no network, no file reads outside the repo.
Standard library only.
"""

import os

JOKE = (
    "My calendar is so full of meetings about meetings "
    "that my actual job became my side hustle."
)


def main() -> None:
    line = JOKE.strip()
    assert "\n" not in line and 1 <= len(line) <= 200, "joke must be one line, 1-200 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()

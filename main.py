#!/usr/bin/env python3
"""time-machine-warning-label — entry for make.fun
"Funniest Time Machine Warning Label".

Writes one warning label to /output/entry.txt: a single line of at most
120 characters, the funniest warning a time machine could carry. The
program checks the competition gate itself before writing: UTF-8 text,
1-120 characters, a single line, not only whitespace.

Candidates considered (judged on the judge brief: a real hazard of time
travel turned into the joke first, surprise saved for the last words,
straight-face safety notice, no wasted words):
 1. WARNING: Do not kill your grandfather. He is the only one who knows the Wi-Fi password.
 2. CAUTION: Meeting yourself is prohibited. You are the reason the meeting was cancelled.
 3. WARNING: Do not step on butterflies. One of them is your great-great-grandmother.
 4. NOTICE: The past is under warranty. Tampering voids your existence.
 5. WARNING: If you meet yourself, do not lend yourself money. You never pay yourself back.
 6. WARNING: Do not wave at yourself. He is still angry about what you did next Tuesday.
 7. NOTICE: Passengers arriving before they depart must report to themselves immediately.
 8. WARNING: Do not change the past. The future has already filed a complaint.
 9. CAUTION: Your grandfather is not a tourist attraction. Do not feed him.
10. WARNING: Paradox detected. Please undo your birth and try again.
11. NOTICE: This machine travels in time, not in space. Your ancestors' house is now a parking lot.
12. WARNING: Do not meet your ancestors. One of them owes you money and will ask for it back.

Winner: #1 — the grandfather paradox is the textbook time-travel hazard,
and the punchline lands on the most mundane modern dependency: the Wi-Fi
password. The label stays deadpan throughout, reads like a real safety
notice, and wastes no words at 87 characters.
"""

import os

LINE = "WARNING: Do not kill your grandfather. He is the only one who knows the Wi-Fi password."


def main() -> None:
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    if not 1 <= len(LINE) <= 120:
        raise ValueError(f"entry is {len(LINE)} chars, must be 1-120")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    # A warning label must read like a genuine safety notice: it opens
    # with a standard warning keyword, so the joke cuts against official calm.
    if not LINE.startswith(("WARNING:", "CAUTION:", "NOTICE:")):
        raise ValueError("entry must open with WARNING:, CAUTION: or NOTICE:")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify what actually landed on disk matches the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the entry line")
    print(f"Wrote {len(LINE)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()

"""Snooze Button Roast — make.fun entry.

One line (120 chars, cap 200) roasting an alarm clock for ringing at
6 AM on a Saturday. The joke is the snooze chain itself: eleven taps,
a 9:03 wake-up, and the punchline that you can be late for nothing —
the alarm did its job perfectly and still ruined the morning.

Run: python3 main.py
Writes the line to /output/entry.txt and prints it.
"""

import os

LINE = (
    "My alarm went off at 6am on Saturday, so I snoozed it 11 times, "
    "woke up at 9:03, and was somehow still late for nothing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()

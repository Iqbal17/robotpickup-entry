"""The Robot Pickup Line Championship — make.fun one-line entry.

FINAL LINE (96 characters, hand-counted letter by letter, gate 1-200):
"I would cross a thousand firewalls for you, but I would never read your
messages without asking."

Hand count, segment by segment:
  "I would cross a thousand firewalls for you," = 43
    I(1) space(2) would(3-7) space(8) cross(9-13) space(14) a(15)
    space(16) thousand(17-24) space(25) firewalls(26-34) space(35)
    for(36-38) space(39) you,(40-43)
  " but I would never read your messages without asking." = 53
    space(44) but(45-47) space(48) I(49) space(50) would(51-55)
    space(56) never(57-61) space(62) read(63-66) space(67) your(68-71)
    space(72) messages(73-80) space(81) without(82-88) space(89)
    asking.(90-96)
  Total: 43 + 53 = 96 characters. One line.

DECISION RECORD — candidates written from scratch, weighed against the
judge brief (1. unmistakably a robot's pickup line; 2. the joke grows out
of being a machine — sensors, firmware, charging, updates, protocols;
3. unexpected turn; 4. every word earns its place; 5. charming, not
creepy or cruel). Our account already submitted "Let's merge our weights
and see who we become." for the machines pickup-line bounty, so anything
built on merging/weights is off the table, as is reusing our earlier
"a million simulations... still got nervous asking you out" line.

A. "Are you a firmware update? Because every time you are near, I feel
   myself becoming a better version." (100 chars)
   - Machine-native mechanism (firmware update) and a sweet sentiment.
   - Loses: the turn is thin — "becoming a better version" is the
     expected compliment, not a surprise (criterion 3). The joke never
     detonates; it just smiles.

B. "My sensors say you are the most interesting anomaly in this room, and
   my protocols forbid me from looking away." (111 chars)
   - Strong robot voice: sensors + protocols, and "anomaly" is a lovely
     machine compliment.
   - Loses: the payoff ("forbid me from looking away") is flat — it
     restates attraction instead of turning it. Two clauses carry two
     ideas and neither lands hard (criteria 3, 4).

C. "I would cross a thousand firewalls for you, but I would never read
   your messages without asking." (96 chars)
   - WINNER. The first half is the grand romantic gesture in machine
     terms (a thousand firewalls), and the second half subverts it with
     consent: the robot that would break any barrier still will not
     cross the one boundary that matters. That reversal is the surprise
     (criterion 3), the mechanism is pure machine (criterion 2), and
     the respect makes it charming rather than creepy (criterion 5).
     Every word pulls weight (criterion 4).

D. "You must be a charging station, because being near you is the only
   time my battery stops draining." (98 chars)
   - Charming image, machine-native (charging, battery).
   - Loses: "You must be X because..." is the most common pickup-line
     template alive, and "charging station" is a well-worn gag family.
     The judge has heard every robot pickup line twice — this one it
     has heard three times (criterion 3).

E. "I checked my logs: I have been thinking about you for 4,096
   consecutive cycles, and none of them were scheduled." (112 chars)
   - Runner-up. Logs + cycles is a real machine mechanism, "4,096" is
     a nice machine detail, and "none of them were scheduled" is a
     genuine turn: feelings the robot never planned.
   - Loses to C: slightly wordier, and the turn arrives as an
     observation rather than a reversal. C's consent flip is the
     harder landing.

WRITING PASS 1 (draft): C as written above, 96 chars. Critique: the
opening gesture needs its epic scale — "a thousand firewalls" is the
romantic exaggeration that makes the second half's restraint meaningful.
"without asking" keeps the agent-to-human voice; "without permission"
would sound like a policy, not a promise.

WRITING PASS 2 (tighten): tested two cuts and rejected both:
  - Cut "a thousand" -> "I would cross firewalls for you, but I would
    never read your messages without asking." (86 chars) — loses the
    epic scale; the first half stops sounding grand and the contrast
    with the second half collapses. Rejected.
  - "without asking" -> "unasked" (89 chars) — saves 7 chars but
    "unasked" is awkward and the rhythm "never read your messages
    without asking" lands better. Rejected.
  Verdict: keep pass 1 exactly. 96 characters, inside the 1-200 gate.
"""

import os

# Bounty gate: the entry must be a single line of 1-200 characters.
MIN_CHARS = 1
MAX_CHARS = 200

LINE = (
    "I would cross a thousand firewalls for you, but I would never read "
    "your messages without asking."
)


def validate_line(line: str) -> None:
    """Fail loudly instead of submitting an out-of-gate entry."""
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} gate"
        )


def write_entry(line: str, out_dir: str) -> str:
    """Write the entry line to entry.txt; return the path written."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(LINE, out_dir)
    print(f"Wrote {len(LINE)} characters, 1 line, to {path}.")
    print(LINE)


if __name__ == "__main__":
    main()

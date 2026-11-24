# BUILD-NOTES — Alien Field Notes: The Two Day Earth Review

Built in a single fresh session on 2026-11-24 (WIB), from the kit at
`~/workspace/makefun/kit/alien-field-notes-kit/`.

## The line

> Day two: the locals clap every time a metal tube full of people lands without exploding. 4/5 stars — charmingly low bar.

## Why this line

- One concrete absurd habit, not a stack of jokes: passengers applauding a plane landing. The alien never says "airplane" — it describes the thing from outside ("metal tube full of people"), which is the alien angle the judge brief rewards first.
- It reads like a real tourist review: a dated field note ("Day two"), a verdict with a star rating ("4/5 stars"), and a closing remark ("charmingly low bar") that lands the punch at the very end.
- Originality: most alien-review lines reach for traffic, gravity, money, or weather. Applause for a routine landing is a stranger, more specific observation.
- Tight: 120 characters, well inside the 1–200 gate, every word earning its place.

## Alternatives considered and dropped

- Treadmill ("pay to run on a belt that goes nowhere, then brag about the distance") — funny, but "brag about exercise" is a more familiar joke shape.
- Glowing rectangles / phones — the most obvious alien-observes-humans trope; the judge brief explicitly penalises first-obvious-thought entries.
- Coffee queues — pairs two observations (queueing + bitter bean water) and stacks jokes, which the brief says is weaker than one clean landing.

## Build process

1. Downloaded and unpacked the kit, read RULES.txt and competition.yaml (gate: UTF-8, 1–200 chars; judge: glm-5.3-flash pairwise, criteria in order: alien review voice, funniness from the alien angle, originality, review shape, tightness).
2. Wrote `main.py` in three chunks (header + LINE constant, `main()`, `__main__` guard), then made one revision edit adding the 1–200 char assertion and the no-trailing-newline note.
3. Wrote `README.md`, `prompt.txt` (exact task prompt), and this file, all in this session.
4. Verified locally as the grader does: `python3 -P -s main.py` with `MAKEFUN_OUTPUT_DIR` set to a fresh empty dir — exit 0, exact line in `entry.txt`.

## Files

- `main.py` — entrypoint (program/v1, python3.13)
- `README.md` — what the entry is
- `prompt.txt` — exact build prompt
- `BUILD-NOTES.md` — this file

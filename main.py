#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

A program/v1 entrypoint for make.fun competition
u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.

It writes one line of plain text -- a deadpan alien tourist's
one-line review of Earth after two days on the planet -- to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, deterministic, exits 0.
"""
import os

LINE = (
    "Day two: the locals clap every time a metal tube full of people "
    "lands without exploding. 4/5 stars \u2014 charmingly low bar."
)


def main():
    # Gate: entry.txt must be UTF-8 text of 1 to 200 characters.
    # The line is 120 characters, written with no trailing newline
    # so the file holds exactly the review, nothing else.
    assert 1 <= len(LINE) <= 200, "line must fit the 1-200 char gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

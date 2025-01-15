#!/usr/bin/env python3

# character_count.py - Identify the unique Chinese characters in a given text.
# Copyright (C) 2025  Jordan Esh

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import sys


def character_count(s: str) -> dict[str, int]:
    """
    Count the number of unique Chinese characters in a given text.

    Args:
    s: str: The input text.
    """
    unique_chars = dict()
    for c in s:
        if "\u4e00" <= c <= "\u9fff":
            unique_chars[c] = unique_chars[c] + 1 if c in unique_chars else 1
    return unique_chars


def main():
    parser = argparse.ArgumentParser(
        description="Count the number of unique Chinese characters in a given text. If no input file is provided, the program will read from stdin, press Ctrl-D to finish input."
    )
    parser.add_argument("-i", "--input", required=False, help="Input text file")
    parser.add_argument(
        "-c",
        "--compare",
        required=False,
        default=None,
        help="Second text file to compare mutually exclusive characters",
    )
    parser.add_argument(
        "-o", "--output", required=False, default="output.txt", help="Output text file"
    )
    args = parser.parse_args()

    if not args.input:
        print(
            'Write/paste your text, then press Ctrl-D to finish input. To compare two texts, separate with a line containing only "===".'
        )

    with open(args.input, "r", encoding="utf8") if args.input else sys.stdin as f:
        s = f.read()

    interactive_compare = "===" in s.splitlines()
    non_interactive_compare = args.compare is not None

    unique_chars = None

    if interactive_compare or non_interactive_compare:
        s1, s2 = None, None
        if non_interactive_compare:
            s1 = s
            with open(args.compare, "r", encoding="utf8") as f:
                s2 = f.read()
        elif interactive_compare:
            s1, s2 = s.split("===")

        unique_chars1 = character_count(s1)
        unique_chars2 = character_count(s2)
        unique_chars_left_me = {
            k: v for k, v in unique_chars1.items() if k not in unique_chars2
        }
        unique_chars_right_me = {
            k: v for k, v in unique_chars2.items() if k not in unique_chars1
        }

        for char in unique_chars_left_me.keys():
            if char in unique_chars_right_me.keys():
                print(f"Warning: Character {char} is in both texts.")

        print(
            f"There are {len(unique_chars_left_me)} unique Chinese characters in the first text that are not in the second text."
        )
        print(
            f"There are {len(unique_chars_right_me)} unique Chinese characters in the second text that are not in the first text."
        )
        with open(args.output, "w", encoding="utf8") as f:
            f.write(
                f"There are {len(unique_chars_left_me)} unique Chinese characters in the first text that are not in the second text.\n"
            )
            for k, v in unique_chars_left_me.items():
                f.write(f"{k}: {v}\n")
            f.write(
                f"There are {len(unique_chars_right_me)} unique Chinese characters in the second text that are not in the first text.\n"
            )
            for k, v in unique_chars_right_me.items():
                f.write(f"{k}: {v}\n")

    else:
        unique_chars = character_count(s)
        print(f"There are {len(unique_chars)} unique Chinese characters in the text.")
        with open(args.output, "w", encoding="utf8") as f:
            f.write(
                f"There are {len(unique_chars)} unique Chinese characters in the text.\n"
            )
            for k, v in unique_chars.items():
                f.write(f"{k}: {v}\n")


if __name__ == "__main__":
    main()

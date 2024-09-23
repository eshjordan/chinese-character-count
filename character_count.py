#!/usr/bin/env python3

import argparse
import sys


def character_count(s: str) -> int:
    """
    Count the number of unique Chinese characters in a given text.

    Args:
    s: str: The input text.
    """
    return len(set(c for c in s if '\u4e00' <= c and c <= '\u9fff'))


def main():
    parser = argparse.ArgumentParser(
        description="Count the number of unique Chinese characters in a given text. If no input file is provided, the program will read from stdin, press Ctrl-D to finish input."
    )
    parser.add_argument("-i", "--input", required=False, help="Input text file")
    args = parser.parse_args()

    if not args.input:
        print('Write/paste your text, then press Ctrl-D to finish input.')

    with open(args.input, 'r') if args.input else sys.stdin as f:
        s = f.read()
        print(f'There are {character_count(s)} unique Chinese characters in the text.')


if __name__ == "__main__":
    main()

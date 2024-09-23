#!/usr/bin/env python3

import argparse
import sys


def character_count(s: str, output: str) -> int:
    """
    Count the number of unique Chinese characters in a given text.

    Args:
    s: str: The input text.
    """
    unique_chars = dict()
    for c in s:
        if '\u4e00' <= c <= '\u9fff':
            unique_chars[c] = unique_chars[c] + 1 if c in unique_chars else 1
    print(f'There are {len(unique_chars)} unique Chinese characters in the text.')
    with open(output, 'w') as f:
        f.write(f'There are {len(unique_chars)} unique Chinese characters in the text.\n')
        for k, v in unique_chars.items():
            f.write(f'{k}: {v}\n')


def main():
    parser = argparse.ArgumentParser(
        description="Count the number of unique Chinese characters in a given text. If no input file is provided, the program will read from stdin, press Ctrl-D to finish input."
    )
    parser.add_argument("-i", "--input", required=False, help="Input text file")
    parser.add_argument("-o", "--output", required=False, default='output.txt', help="Output text file")
    args = parser.parse_args()

    if not args.input:
        print('Write/paste your text, then press Ctrl-D to finish input.')

    with open(args.input, 'r') if args.input else sys.stdin as f:
        s = f.read()

    character_count(s, args.output)


if __name__ == "__main__":
    main()

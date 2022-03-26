#!/usr/bin/env python
"""GenDiff entrypoint."""

import argparse

from gendiff import generate_diff
from gendiff.parse import parse


def main() -> None:
    """Entrypoint function."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument(
        '-f',
        '--format',
        metavar='FORMAT',
        help='set format of output',
    )
    args = parser.parse_args()

    first_file = parse(args.first_file, args.format)
    second_file = parse(args.second_file, args.format)
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()

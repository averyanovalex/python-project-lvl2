#!/usr/bin/env python
"""GenDiff entrypoint."""

import argparse

from gendiff import generate_diff
from gendiff.parse import parse as parse_file


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

    file1 = parse_file(args.first_file)
    file2 = parse_file(args.second_file)
    print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()

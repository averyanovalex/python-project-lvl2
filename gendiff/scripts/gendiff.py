#!/usr/bin/env python
"""GenDiff entrypoint."""

import argparse

from gendiff import generate_diff


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

    supported_formats = {'stylish'}
    view_format = args.format if args.format in supported_formats else 'stylish'

    print(generate_diff(args.first_file, args.second_file, view_format))


if __name__ == '__main__':
    main()

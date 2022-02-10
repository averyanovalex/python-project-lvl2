#!/usr/bin/env python
"""GenDiff entrypoint."""

import argparse

from gen_diff.main import run


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

    run(args)


if __name__ == '__main__':
    main()

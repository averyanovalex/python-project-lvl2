"""GenDiff main module."""

import argparse


def arguments_parser() -> argparse.ArgumentParser:
    """
    Create arguments parser an return it.

    Returns:
        argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    return parser


def run() -> None:
    """Entrypoint."""
    args = arguments_parser().parse_args()
    print(args)

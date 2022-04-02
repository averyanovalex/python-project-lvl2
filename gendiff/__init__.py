"""Init module."""
from gendiff.diff import generate_diff_dicts
from gendiff.parse import parse_file
from gendiff.view import generate_view


def generate_diff(file1_path: str, file2_path: str) -> str:
    """
    Generate differences between two files.

    Supported files: json, yaml.

    Args:
        file1_path: first dictionary
        file2_path: second dictionary

    Returns:
        str
    """
    file1 = parse_file(file1_path)
    file2 = parse_file(file2_path)
    diff = generate_diff_dicts(file1, file2)
    return generate_view(diff)


__all__ = ['generate_diff']

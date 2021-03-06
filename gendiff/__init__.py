"""Init module."""
from gendiff.diff import generate_diff_internal
from gendiff.parse import parse_file
from gendiff.view import generate_view


def generate_diff(
    file1_path: str,
    file2_path: str,
    format_name: str = '',
) -> str:
    """
    Generate differences between two files.

    Supported files: json, yaml.

    Args:
        file1_path: first dictionary
        file2_path: second dictionary
        format_name: format for view

    Returns:
        str
    """
    file1 = parse_file(file1_path)
    file2 = parse_file(file2_path)
    diff = generate_diff_internal(file1, file2)
    return generate_view(diff, format_name)


__all__ = ['generate_diff']

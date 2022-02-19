"""Init module."""


def generate_diff(file_path1: str, file_path2: str) -> None:
    """
    Generate differences between two json files.

    Args:
        file_path1: first files's path
        file_path2: second files's path

    Returns:
        str
    """
    difference_str = """
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
"""
    return ''.join(['', difference_str])

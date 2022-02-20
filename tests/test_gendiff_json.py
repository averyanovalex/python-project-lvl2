"""Module tests package gendiff for json  files."""

from gendiff import generate_diff

file1_path = 'tests/fixtures/file1.json'
file2_path = 'tests/fixtures/file2.json'
file_empty_path = 'tests/fixtures/file_empty.json'


def test_gendiff_json_both_files_full() -> None:
    """
    Tests generate_diff when arguments are json files.

    Both files is full.
    """
    estimated_result = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    real_result = generate_diff(file1_path, file2_path)
    assert real_result == estimated_result


def test_gendiff_json_one_file_empty() -> None:
    """
    Tests generate_diff when arguments are json files.

    Fisrt file is empty, second file is full.
    """
    estimated_result = """{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}"""

    real_result = generate_diff(file_empty_path, file2_path)
    assert real_result == estimated_result


def test_gendiff_json_both_files_equal() -> None:
    """
    Tests generate_diff when arguments are json files.

    Both files is equal.
    """
    estimated_result = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""

    real_result = generate_diff(file1_path, file1_path)
    assert real_result == estimated_result


def test_gendiff_json_both_file_empty() -> None:
    """
    Tests generate_diff when arguments are json files.

    Both file are empty.
    """
    estimated_result = """{
}"""

    real_result = generate_diff(file_empty_path, file_empty_path)
    assert real_result == estimated_result

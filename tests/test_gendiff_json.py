"""Module tests package gendiff for json  files."""

from gendiff import generate_diff

file1_path = 'tests/fixtures/file1.json'
file2_path = 'tests/fixtures/file2.json'
file_empty_path = 'tests/fixtures/file_empty.json'


def test_gendiff_json_both_full() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Both files are full and different.
    """
    with open('tests/fixtures/json_both_full.txt') as file1:
        estimated_result = file1.read()
    assert generate_diff(file1_path, file2_path) == estimated_result


def test_gendiff_json_one_empty() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Fisrt file is empty, second file is full.
    """
    with open('tests/fixtures/json_one_empty.txt') as file2:
        estimated_result = file2.read()
    assert generate_diff(file_empty_path, file2_path) == estimated_result


def test_gendiff_json_both_equal() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Both files is equal.
    """
    with open('tests/fixtures/json_both_equal.txt') as file3:
        estimated_result = file3.read()
    assert generate_diff(file1_path, file1_path) == estimated_result


def test_gendiff_json_both_empty() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Both file are empty.
    """
    with open('tests/fixtures/json_both_empty.txt') as file4:
        estimated_result = file4.read()
    assert generate_diff(file_empty_path, file_empty_path) == estimated_result

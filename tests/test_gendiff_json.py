"""Module tests package gendiff for json  files."""

from gendiff import generate_diff
from gendiff.parse import parse

file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file_empty_json = 'tests/fixtures/file_empty.json'

file1_yaml = 'tests/fixtures/file1.yaml'
file2_yaml = 'tests/fixtures/file2.yaml'
file_empty_yaml = 'tests/fixtures/file_empty.yaml'

result_both_full = 'tests/fixtures/result_both_full.txt'
result_one_empty = 'tests/fixtures/result_one_empty.txt'
result_both_equal = 'tests/fixtures/result_both_equal.txt'
result_both_empty = 'tests/fixtures/result_both_empty.txt'


def run_test_gendiff(result: str, file1_path: str, file2_path: str, format: str = None) -> None:
    with open(result) as stream:
        estimated_result = stream.read()
    file1 = parse(file1_path, format=format)
    file2 = parse(file2_path, format=format)
    print(file2)
    assert generate_diff(file1, file2) == estimated_result


def test_gendiff_json_both_full() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Both files are full and different.
    """
    run_test_gendiff(
        result=result_both_full,
        file1_path=file1_json,
        file2_path=file2_json,
        format='json',
    )


def test_gendiff_json_one_empty() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Fisrt file is empty, second file is full.
    """
    run_test_gendiff(
        result=result_one_empty,
        file1_path=file_empty_json,
        file2_path=file2_json,
        format='json',
    )


def test_gendiff_json_both_equal() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Both files is equal.
    """
    run_test_gendiff(
        result=result_both_equal,
        file1_path=file1_json,
        file2_path=file1_json,
        format='json',
    )


def test_gendiff_json_both_empty() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Both file are empty.
    """
    run_test_gendiff(
        result=result_both_empty,
        file1_path=file_empty_json,
        file2_path=file_empty_json,
        format='json',
    )


def test_gendiff_yaml_both_full() -> None:
    """
    Tests generate_diff when both arguments are yaml files.

    Both files are full and different.
    """
    run_test_gendiff(
        result=result_both_full,
        file1_path=file1_yaml,
        file2_path=file2_yaml,
        format='yaml',
    )


def test_gendiff_yaml_one_empty() -> None:
    """
    Tests generate_diff when both arguments are yaml files.

    Fisrt file is empty, second file is full.
    """
    run_test_gendiff(
        result=result_one_empty,
        file1_path=file_empty_yaml,
        file2_path=file2_yaml,
        format='yaml',
    )


def test_gendiff_yaml_both_equal() -> None:
    """
    Tests generate_diff when both arguments are yaml files.

    Both files is equal.
    """
    run_test_gendiff(
        result=result_both_equal,
        file1_path=file1_yaml,
        file2_path=file1_yaml,
        format='yaml',
    )


def test_gendiff_yaml_both_empty() -> None:
    """
    Tests generate_diff when both arguments are yaml files.

    Both file are empty.
    """
    run_test_gendiff(
        result=result_both_empty,
        file1_path=file_empty_yaml,
        file2_path=file_empty_yaml,
        format='yaml',
    )
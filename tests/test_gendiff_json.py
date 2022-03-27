"""Module tests package gendiff for json  files."""

from gendiff import generate_diff
from gendiff.parse import parse as parse_file

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


def run_test_gendiff(
    result_path: str,
    file1_path: str,
    file2_path: str,
) -> None:
    """
    Execute common logic for all tests.

    Args:
        result_path: path to eatimated result
        file1_path: path to first file
        file2_path: path to second file
    """
    with open(result_path) as stream:
        estimated_result = stream.read()
    file1 = parse_file(file1_path)
    file2 = parse_file(file2_path)
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
    )

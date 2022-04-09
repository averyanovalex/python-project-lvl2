"""Module tests package gendiff for json  files."""

from gendiff import generate_diff

format_stylish = 'stylish'
format_plain = 'plain'

file1_json = 'tests/fixtures/file1.json'
file2_json = 'tests/fixtures/file2.json'
file_empty_json = 'tests/fixtures/file_empty.json'
file1_complex_json = 'tests/fixtures/file_complex1.json'
file2_complex_json = 'tests/fixtures/file_complex2.json'

file1_yaml = 'tests/fixtures/file1.yaml'
file2_yaml = 'tests/fixtures/file2.yaml'
file_empty_yaml = 'tests/fixtures/file_empty.yaml'
file1_complex_yaml = 'tests/fixtures/file_complex1.yaml'
file2_complex_yaml = 'tests/fixtures/file_complex2.yaml'

stylish_both_full = 'tests/fixtures/stylish_simple_both_full.txt'
stylish_one_empty = 'tests/fixtures/stylish_simple_one_empty.txt'
stylish_both_equal = 'tests/fixtures/stylish_simple_both_equal.txt'
stylish_both_empty = 'tests/fixtures/stylish_simple_both_empty.txt'
stylish_both_full_complex = 'tests/fixtures/stylish_complex_both_full.txt'

plain_both_full_complex = 'tests/fixtures/plain_complex_both_full.txt'


def run_test_gendiff(
    result_path: str,
    file1_path: str,
    file2_path: str,
    format_name: str,
) -> None:
    """
    Execute common logic for all tests.

    Args:
        result_path: path to eatimated result
        file1_path: path to first file
        file2_path: path to second file
        format_name: view format name
    """
    with open(result_path) as stream:
        estimated_result = stream.read()
    diff = generate_diff(file1_path, file2_path, format_name)
    assert diff == estimated_result


def test_gendiff_json_both_full_stylish() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Both files are full and different.
    Format name: stylish.
    """
    run_test_gendiff(
        result_path=stylish_both_full,
        file1_path=file1_json,
        file2_path=file2_json,
        format_name=format_stylish,
    )


def test_gendiff_json_one_empty_stylish() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Fisrt file is empty, second file is full.
    Format name: stylish.
    """
    run_test_gendiff(
        result_path=stylish_one_empty,
        file1_path=file_empty_json,
        file2_path=file2_json,
        format_name=format_stylish,
    )


def test_gendiff_json_both_equal_stylish() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Both files is equal.
    Format name: stylish.
    """
    run_test_gendiff(
        result_path=stylish_both_equal,
        file1_path=file1_json,
        file2_path=file1_json,
        format_name=format_stylish,
    )


def test_gendiff_json_both_empty_stylish() -> None:
    """
    Tests generate_diff when both arguments are json files.

    Both file are empty.
    Format name: stylish.
    """
    run_test_gendiff(
        result_path=stylish_both_empty,
        file1_path=file_empty_json,
        file2_path=file_empty_json,
        format_name=format_stylish,
    )


def test_gendiff_json_both_full_complex_stylish() -> None:
    """
    Tests generate_diff when both arguments are json files (complex structure).

    Both files are full and different.
    Format name: stylish.
    """
    run_test_gendiff(
        result_path=stylish_both_full_complex,
        file1_path=file1_complex_json,
        file2_path=file2_complex_json,
        format_name=format_stylish,
    )


def test_gendiff_json_both_full_complex_plain() -> None:
    """
    Tests generate_diff when both arguments are json files (complex structure).

    Both files are full and different.
    Format name: plain.
    """
    run_test_gendiff(
        result_path=plain_both_full_complex,
        file1_path=file1_complex_json,
        file2_path=file2_complex_json,
        format_name=format_plain,
    )


def test_gendiff_yaml_both_full_stylish() -> None:
    """
    Tests generate_diff when both arguments are yaml files.

    Both files are full and different.
    Format name: stylish.
    """
    run_test_gendiff(
        result_path=stylish_both_full,
        file1_path=file1_yaml,
        file2_path=file2_yaml,
        format_name=format_stylish,
    )


def test_gendiff_yaml_one_empty_stylish() -> None:
    """
    Tests generate_diff when both arguments are yaml files.

    Fisrt file is empty, second file is full.
    Format name: stylish.
    """
    run_test_gendiff(
        result_path=stylish_one_empty,
        file1_path=file_empty_yaml,
        file2_path=file2_yaml,
        format_name=format_stylish,
    )


def test_gendiff_yaml_both_equal_stylish() -> None:
    """
    Tests generate_diff when both arguments are yaml files.

    Both files is equal.
    Format name: stylish.
    """
    run_test_gendiff(
        result_path=stylish_both_equal,
        file1_path=file1_yaml,
        file2_path=file1_yaml,
        format_name=format_stylish,
    )


def test_gendiff_yaml_both_empty_stylish() -> None:
    """
    Tests generate_diff when both arguments are yaml files.

    Both file are empty.
    Format name: stylish.
    """
    run_test_gendiff(
        result_path=stylish_both_empty,
        file1_path=file_empty_yaml,
        file2_path=file_empty_yaml,
        format_name=format_stylish,
    )


def test_gendiff_yaml_both_full_complex_stylish() -> None:
    """
    Tests generate_diff when both arguments are yaml files (complex structure).

    Both files are full and different.
    Format name: stylish.
    """
    run_test_gendiff(
        result_path=stylish_both_full_complex,
        file1_path=file1_complex_yaml,
        file2_path=file2_complex_yaml,
        format_name=format_stylish,
    )

"""Module tests package gendiff (hexlet tests)."""


from gendiff import generate_diff

file1_json = 'tests/fixtures/hexlet/file1.json'
file2_json = 'tests/fixtures/hexlet/file2.json'
file1_yml = 'tests/fixtures/hexlet/file1.yml'
file2_yml = 'tests/fixtures/hexlet/file2.yml'
result_plain = 'tests/fixtures/hexlet/result_plain'
result_stylish = 'tests/fixtures/hexlet/result_stylish'


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


def test_json_plain() -> None:
    """Tests json (format plain)."""
    run_test_gendiff(
        result_path=result_plain,
        file1_path=file1_json,
        file2_path=file2_json,
        format_name='plain',
    )


def test_yaml_plain() -> None:
    """Tests yaml (format plain)."""
    run_test_gendiff(
        result_path=result_plain,
        file1_path=file1_yml,
        file2_path=file2_yml,
        format_name='plain',
    )


def test_json_stylish() -> None:
    """Tests json (format stylish)."""
    run_test_gendiff(
        result_path=result_stylish,
        file1_path=file1_json,
        file2_path=file2_json,
        format_name='stylish',
    )


def test_yaml_stylish() -> None:
    """Tests yaml (format stylish)."""
    run_test_gendiff(
        result_path=result_stylish,
        file1_path=file1_yml,
        file2_path=file2_yml,
        format_name='stylish',
    )

"""Module tests package gen_diff."""

from gendiff import generate_diff


def test_gendiff_json_files():
    """Tests generate_diff when arguments are json files."""
    estimated_result = """
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
"""

    real_result = generate_diff('fixtures/file1.json', 'fixtures/file2.json')
    assert real_result == estimated_result

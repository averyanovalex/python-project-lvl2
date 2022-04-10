"""Formater plain."""


from typing import Any


def generate_view(difference: list) -> str:
    """
    Generate view for difference.

    Difference between two files has an internal representation.
    This function generate visual representation for user (text view).

    Args:
        difference: difference between two files (internal representation)

    Returns:
        str
    """
    return build_view_for_keys(difference).rstrip()


def build_view_for_keys(nodes: list, key_path: str = '') -> str:
    """
    Build view for keys (nodes).

    Args:
        nodes: list of keys (every key has dict type)
        key_path: string path to current key

    Returns:
        str
    """
    result_view = ''
    for node in nodes:

        if 'children' in node:
            new_key_path = '{0}{1}.'.format(key_path, node.get('key'))
            children_view = build_view_for_keys(
                node.get('children'),
                new_key_path,
            )
            result_view = f'{result_view}{children_view}'
            continue

        if node.get('diff_type') == 'equals':
            continue

        view_line = build_view_for_one_key(node, key_path)
        if view_line != '':
            result_view = f'{result_view}{view_line}\n'

    return result_view


def build_view_for_one_key(node: dict, key_path: str) -> str:
    """
    Build view for key (node).

    Args:
        node: one key from keys list
        key_path: string path to current key

    Returns:
        str
    """
    diff_type = node.get('diff_type')

    view_line = ''
    key_text = build_key_text(key_path, node.get('key'))
    if diff_type == 'removed':
        view_line = f'Property {key_text} was removed'

    elif diff_type == 'added':
        value_text = build_value_text(node.get('value_new'))
        view_line = f'Property {key_text} was added with value: {value_text}'

    elif diff_type == 'updated':
        view_line = build_view_for_updated_key(node, key_text)

    return view_line


def build_view_for_updated_key(node, key_path):
    """
    Build view for key with diff_type 'updated'.

    Args:
        node: one key from keys list
        key_path: string path to current key

    Returns:
        str
    """
    value_old_text = build_value_text(node.get('value_old'))
    value_new_text = build_value_text(node.get('value_new'))

    line_part1 = f'Property {key_path} was updated.'
    line_part2 = f'From {value_old_text} to {value_new_text}'
    return f'{line_part1} {line_part2}'


def build_key_text(key_path: str, key: str) -> str:
    """
    Convert node key to text.

    Args:
        key_path: text path from root to current key
        key: node key

    Returns:
        str
    """
    return f"'{key_path}{key}'"


def build_value_text(value: Any) -> str:
    """
    Convert node value to text.

    Args:
        value: node value

    Returns:
        str
    """
    if isinstance(value, dict):
        return '[complex value]'

    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return 'null'

    return "'{0}'".format(str(value))

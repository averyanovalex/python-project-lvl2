"""Formater stylish."""


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
    return build_view_for_keys_with_differences(difference)


def build_view_for_keys_with_differences(nodes: list, indent: str = '') -> str:
    """
    Build view for list of keys (nodes) with differences.

    Function called recursively.

    Args:
        nodes: list keys with differences
        indent: indent for current depth's level

    Returns:
        str
    """
    result_view = '{\n'
    for node in nodes:
        diff_type = node.get('diff_type')
        key = node.get('key')

        if 'children' in node:
            result_view = build_view_for_children(
                result_view,
                indent,
                key,
                node.get('children'),
            )
            continue

        if diff_type == 'updated':
            result_view = build_view_for_node(
                result_view=result_view,
                indent=indent,
                key=key,
                diff_type='removed',
                value=node.get('value_old'),
            )
            result_view = build_view_for_node(
                result_view=result_view,
                indent=indent,
                key=key,
                diff_type='added',
                value=node.get('value_new'),
            )
            continue

        if diff_type == 'removed':
            node_value = node.get('value_old')
        else:
            node_value = node.get('value_new')

        result_view = build_view_for_node(
            result_view=result_view,
            indent=indent,
            key=key,
            diff_type=diff_type,
            value=node_value,
        )

    return f'{result_view}{indent}}}'


def build_view_for_children(
    result_view: str,
    indent: str,
    key: str,
    children: list,
) -> str:
    """
    Build view for node children.

    Args:
        result_view: view is padded and returned
        indent: indent for current depth's level
        key: node key
        children: node children

    Returns:
        str
    """
    new_indent = get_indent_next_level(indent)
    node_view = build_view_for_keys_with_differences(children, new_indent)
    marked_indent = get_marked_indent(diff_type=None, indent=indent)

    return f'{result_view}{marked_indent}{key}: {node_view}\n'


def build_view_for_node(
    result_view: str,
    indent: str,
    key: str,
    diff_type: str,
    value: Any,
) -> str:
    """
    Build view for difference node.

    Args:
        result_view: view is padded and returned
        indent: indent for current depth's level
        key: node key
        diff_type: difference type of node (equal, added, removed, updated)
        value: node value

    Returns:
        str
    """
    new_indent = get_indent_next_level(indent)
    if isinstance(value, dict):
        node_view = build_view_for_dict_value(value, new_indent)
    else:
        node_view = build_view_for_simple_value(value)

    marked_indent = get_marked_indent(diff_type, indent)
    return f'{result_view}{marked_indent}{key}: {node_view}\n'


def build_view_for_dict_value(node_value: dict, indent) -> str:
    """
    Build view for dict value.

    Value with 'dict' type  output 'as is'.
    Function called recursively.

    Args:
        node_value: value with 'dict' type
        indent: indent for current depth's level

    Returns:
        str
    """
    result_view = '{\n'
    for key, value in node_value.items():
        indent_next_level = f'{indent}    '

        if isinstance(value, dict):
            node_view = build_view_for_dict_value(value, indent_next_level)
        else:
            node_view = str(value)
        result_view = f'{result_view}{indent_next_level}{key}: {node_view}\n'

    return f'{result_view}{indent}}}'


def build_view_for_simple_value(value: Any) -> str:
    """
    Build view for simple value (not dict type).

    Args:
        value: value

    Returns:
        str
    """
    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return 'null'

    return str(value)


def get_marked_indent(diff_type: str, indent: str) -> str:
    """
    Get string indent for difference type.

    Args:
        diff_type: difference type
        indent: indent for current depth's level

    Returns:
        str
    """
    if diff_type == 'added':
        indent_suffix = '  + '
    elif diff_type == 'removed':
        indent_suffix = '  - '
    else:
        indent_suffix = '    '

    return f'{indent}{indent_suffix}'


def get_indent_next_level(indent: str):
    """
    Get string of blank indent for current level's depth.

    Args:
        indent: indent for current depth's level

    Returns:
        str
    """
    return f'{indent}    '


__all__ = ['generate_view']

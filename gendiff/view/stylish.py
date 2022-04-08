"""Formater stylish."""


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
        node_view = build_view_for_node(node, indent)

        key = node.get('key')
        marked_indent = get_marked_indent(node.get('diff_type'), indent)
        result_view = f'{result_view}{marked_indent}{key}: {node_view}\n'

    return f'{result_view}{indent}}}'


def build_view_for_node(node, indent):
    """
    Build view for difference node.

    Args:
        node: key with  difference
        indent: indent for current depth's level

    Returns:
        str
    """
    value = node.get('value')
    children = node.get('children')

    indent_next_level = f'{indent}    '
    if isinstance(value, dict):
        node_view = build_view_for_dict_value(value, indent_next_level)
    elif children is not None:
        node_view = build_view_for_keys_with_differences(
            children,
            indent_next_level,
        )
    else:
        node_view = str(value)
    return node_view


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


__all__ = ['generate_view']

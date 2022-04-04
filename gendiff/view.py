"""Generate view."""


def generate_view(difference: list) -> str:
    """
    Generate view for difference.

    Difference between two files has an internal representation.
    This function generate visual representation for user.

    Args:
        difference: difference between two files

    Returns:
        str
    """
    return build_view_for_children(difference)


def build_view_for_children(nodes: list, indent: str = '') -> str:
    """
    Build view for list of difference nodes.

    Function called recursively.

    Args:
        nodes: list of difference nodes
        indent: indent for current depth's level

    Returns:
        str
    """
    result_view = '{\n'
    for node in nodes:
        node_view = build_view_for_node(
            node.get('value'),
            node.get('children'),
            indent,
        )

        key = node.get('key')
        marked_indent = get_marked_indent(node.get('diff_type'), indent)
        result_view = f'{result_view}{marked_indent}{key}: {node_view}\n'

    return f'{result_view}{indent}}}'


def build_view_for_node(value, children, indent):
    """
    Build view for difference node.

    Args:
        value: node's value
        children: children
        indent: indent for current depth's level

    Returns:
        str
    """
    indent_next_level = f'{indent}    '
    if isinstance(value, dict):
        node_view = build_view_for_value(value, indent_next_level)
    elif children is not None:
        node_view = build_view_for_children(children, indent_next_level)
    else:
        node_view = str(value)
    return node_view


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


def build_view_for_value(value_node: dict, indent) -> str:
    """
    Build view for dict value.

    Value with 'dict' type  output 'as is'.
    Function called recursively.

    Args:
        value_node: value with 'dict' type
        indent: indent for current depth's level

    Returns:
        str
    """
    result_view = '{\n'
    for key, value in value_node.items():
        indent_next_level = f'{indent}    '

        if isinstance(value, dict):
            node_view = build_view_for_value(value, indent_next_level)
        else:
            node_view = str(value)
        result_view = f'{result_view}{indent_next_level}{key}: {node_view}\n'

    return f'{result_view}{indent}}}'


__all__ = ['generate_view']

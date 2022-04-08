"""Generate difference."""


from typing import Any


def generate_diff_internal(dict1: str, dict2: str) -> str:
    """
    Generate differences between two dictionaries in internal representation.

    Args:
        dict1: first dictionary
        dict2: second dictionary

    Returns:
        str
    """
    diff = []
    for key in get_keys_from_dicts(dict1, dict2):
        value1 = dict1.get(key)
        value2 = dict2.get(key)

        if isinstance(value1, dict) and isinstance(value2, dict):
            diff_for_children = generate_diff_internal(value1, value2)
            diff.append(build_node(key, diff_for_children))
            continue

        diff.extend(generate_diff_for_key(key, value1, value2))

    return diff


def get_keys_from_dicts(*dicts: dict) -> list:
    """
    Return all unique keys from multiple dictionaries.

    Args:
        dicts: dictionaries

    Returns:
        list
    """
    keys = set()
    for dict_ in dicts:
        keys = keys.union(set(dict_.keys()))
    keys = list(keys)
    keys.sort()

    return keys


def build_node(node_key: str, node_children: list) -> dict:
    """
    Build node with differences.

    Args:
        node_key: key for node
        node_children: children for node

    Returns:
        dict
    """
    return {'key': node_key, 'children': node_children}


def generate_diff_for_key(key: str, value1: Any, value2: Any) -> list:
    """
    Generate difference for key.

    Args:
        key: keys for which the difference is generated
        value1: value from first dict
        value2: value from second dict

    Returns:
        str
    """
    diff = []
    if value1 == value2:
        diff.append(build_least(key, value1, 'equal'))
        return diff

    if value1 is not None:
        diff.append(build_least(key, value1, 'removed'))
    if value2 is not None:
        diff.append(build_least(key, value2, 'added'))
    return diff


def build_least(least_key: str, least_value: str, diff_type: str) -> dict:
    """
    Build least with difference.

    Args:
        least_key: key for least
        least_value: value for least
        diff_type: type of difference (equal, added, removed)

    Returns:
        dict
    """
    return {'key': least_key, 'value': least_value, 'diff_type': diff_type}


__all__ = ['generate_diff_internal']

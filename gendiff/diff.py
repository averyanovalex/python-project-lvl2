"""Generate difference."""


def generate_diff_dicts(dict1: str, dict2: str) -> str:
    """
    Generate differences between two dictionaries.

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
            children = generate_diff_dicts(value1, value2)
            diff.append(build_node(key, children))
            continue

        if value1 == value2:
            diff.append(build_least(key, value1, 'equal'))
            continue

        if value1 is not None:
            diff.append(build_least(key, value1, 'removed'))

        if value2 is not None:
            diff.append(build_least(key, value2, 'added'))

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


def build_least(item_key: str, item_value: str, diff_type: str) -> dict:
    """
    Build difference item as dict.

    Args:
        item_key: key
        item_value: value
        diff_type: type of difference (equal, added, removed)

    Returns:
        dict
    """
    return {'key': item_key, 'value': item_value, 'diff_type': diff_type}


def build_node(item_key: str, children: list) -> dict:

    return {'key': item_key, 'children': children}




__all__ = ['generate_diff_dicts']

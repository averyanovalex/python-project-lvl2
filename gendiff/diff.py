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
    keys = get_keys_from_dicts(dict1, dict2)

    return build_diff(keys, dict1, dict2)


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


def build_diff(keys: list, dict1: dict, dict2: dict) -> dict:
    """
    Build difference between two dictionaries and return as dict.

    Args:
        keys: all keys from both dictionaries
        dict1: first dictionary
        dict2: second dictionary

    Returns:
        dict
    """
    diff = []
    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)

        if value1 == value2:
            diff.append(build_diff_item(key, value1, 'both_dicts'))
            continue

        if value1 is not None:
            diff.append(build_diff_item(key, value1, 'only_first_dict'))

        if value2 is not None:
            diff.append(build_diff_item(key, value2, 'only_second_dict'))

    return diff


def build_diff_item(item_key: str, item_value: str, value_in: str) -> dict:
    """
    Build difference item as dict.

    Args:
        item_key: field 'key'
        item_value: field 'value'
        value_in: field 'value_in'

    Returns:
        dict
    """
    return {'key': item_key, 'value': item_value, 'value_in': value_in}


__all__ = ['generate_diff_dicts']

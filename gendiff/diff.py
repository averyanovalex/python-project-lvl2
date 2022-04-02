"""Generate difference."""


def build_diff(dict1: str, dict2: str) -> str:
    """
    Generate differences between two dictionaries.

    Args:
        dict1: first dictionary
        dict2: second dictionary

    Returns:
        str
    """
    keys = get_keys_from_dicts(dict1, dict2)

    return generate_diff_between_two_json(keys, dict1, dict2)


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


def generate_diff_between_two_json(keys: list, dict1: dict, dict2: dict) -> str:
    """
    Generate difference between two dictionaries and return as string.

    Args:
        keys: all keys from both dictionaries
        dict1: first dictionary
        dict2: second dictionary

    Returns:
        str
    """
    diff_str = ''
    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)

        if value1 == value2:
            diff_str = '{0}    {1}: {2}\n'.format(diff_str, key, value1)
        elif value1 is None:
            diff_str = '{0}  + {1}: {2}\n'.format(diff_str, key, value2)
        elif value2 is None:
            diff_str = '{0}  - {1}: {2}\n'.format(diff_str, key, value1)
        else:
            diff_str = '{0}  - {1}: {2}\n'.format(diff_str, key, value1)
            diff_str = '{0}  + {1}: {2}\n'.format(diff_str, key, value2)

    return ''.join(['{\n', diff_str, '}'])


__all__ = ['build_diff']
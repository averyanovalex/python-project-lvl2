"""Init module."""

import json
from typing import Any


def generate_diff(file_path1: str, file_path2: str) -> None:
    """
    Generate differences between two json files.

    Args:
        file_path1: first files's path
        file_path2: second files's path

    Returns:
        str
    """
    json1 = load_json(file_path1)
    json2 = load_json(file_path2)

    keys = get_all_keys_from_dict(json1, json2)

    return generate_diff_between_two_json(keys, json1, json2)


def load_json(file_path: str) -> dict:
    """
    Load json from text file.

    Args:
        file_path: path to text file

    Returns:
        dict
    """
    with open(file_path) as file1:
        json_as_dict = json.load(file1)
    return json_as_dict


def get_all_keys_from_dict(*dicts: dict) -> list:
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

        value1 = lower_case_bool_value(value1)
        value2 = lower_case_bool_value(value2)

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


def lower_case_bool_value(parameter: Any) -> Any:
    """
    Convert bool values to str in lower case.

    Convert bool values True and False to string 'true' and 'false',
    otherwise return initial value

    Args:
        parameter: value in any type

    Returns:
        Any
    """
    return str(parameter).lower() if isinstance(parameter, bool) else parameter

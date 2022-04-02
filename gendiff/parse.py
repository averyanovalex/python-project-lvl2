"""Tools for parsing."""

import json
import os

import yaml


def parse_file(file_path: str) -> dict:
    """
    Parse file to dict. Support json, yaml.

    Args:
        file_path: path to text file

    Returns:
        dict
    """
    suported_formats = {
        None: parse_json,
        '.json': parse_json,
        '.yaml': parse_yaml,
        '.yml': parse_yaml,
    }

    _, file_extension = os.path.splitext(file_path)
    parse_function = suported_formats[file_extension]

    file_data = parse_function(file_path)
    return dict(map(convert_bool_value_to_str, file_data.items()))


def parse_json(file_path: str) -> dict:
    """
    Parse json from text file.

    Args:
        file_path: path to text file

    Returns:
        dict
    """
    with open(file_path) as stream:
        json_as_dict = json.load(stream)
    return json_as_dict


def parse_yaml(file_path: str) -> dict:
    """
    Parse yaml from text file.

    Args:
        file_path: path to text file

    Returns:
        dict
    """
    with open(file_path) as stream:
        yaml_as_dict = yaml.safe_load(stream)

    if yaml_as_dict is None:
        yaml_as_dict = {}

    return yaml_as_dict


def convert_bool_value_to_str(dict_item: tuple) -> tuple:
    """
    Convert bool values in dictionary's item to str in lower case.

    Convert bool values in True and False to string 'true' and 'false',
    otherwise return initial value

    Args:
        dict_item: dictionary's item (tuple)

    Returns:
        tuple (dictionary's item)
    """
    dict_key, dict_value = dict_item
    if isinstance(dict_value, bool):
        dict_value = str(dict_value).lower()
    return dict_key, dict_value


__all__ = ['parse_file']

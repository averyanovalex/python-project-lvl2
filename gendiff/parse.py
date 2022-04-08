"""Parse files."""

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
    return dict(map(convert_bad_types, file_data.items()))


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


def convert_bad_types(dict_item: tuple) -> tuple:
    """
    Convert some types in specific way.

    Its small hack.
    Some types must be converted in a different way than the default.

    Convert bool values in True and False to string 'true' and 'false'.
    Convert None to string 'null'.

    Args:
        dict_item: dictionary's item (tuple)

    Returns:
        tuple (dictionary's item)
    """
    dict_key, dict_value = dict_item
    if isinstance(dict_value, bool):
        dict_value = str(dict_value).lower()

    elif dict_value is None:
        dict_value = 'null'

    elif isinstance(dict_value, dict):
        dict_value = dict(map(convert_bad_types, dict_value.items()))

    return dict_key, dict_value


__all__ = ['parse_file']

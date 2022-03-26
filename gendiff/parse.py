"""Tools for parsing."""

import json, yaml
from typing import Any


def parse(file_path: str, format: str = None) -> dict:
    suported_formats = {
                        None: parse_json,
                        'json': parse_json,
                        'yaml': parse_yaml,
                        'yml': parse_yaml
                        }

    parse_function = suported_formats[format]
    return parse_function(file_path)


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
    with open(file_path) as stream:
        yaml_as_dict = yaml.safe_load(stream)

    if yaml_as_dict is None:
        yaml_as_dict = {} 

    return yaml_as_dict


def convert_bool_to_str(parameter: Any) -> Any:
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

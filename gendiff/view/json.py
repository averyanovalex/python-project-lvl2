"""Formater json."""


import json


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
    return json.dumps(difference, indent=2)

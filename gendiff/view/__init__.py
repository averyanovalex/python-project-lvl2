"""View generator. Support different formats."""

from gendiff.view import stylish as formater_stylish


def generate_view(difference: list, format_name: str) -> str:
    """
    Generate view for difference.

    Difference between two files has an internal representation.
    Function generate visual representation for user (text view).
    Function takes a format as input and calls the requaried formatter.

    Args:
        difference: difference between two files (internal representation)
        format_name: format for view

    Returns:
        str
    """
    formaters = {'stylish': formater_stylish}
    formater = formaters.get(format_name)
    assert formater is not None, f'Format "{format_name}" is not supported.'

    return formater.generate_view(difference)


__all__ = ['generate_view']

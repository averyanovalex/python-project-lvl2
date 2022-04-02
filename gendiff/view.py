"""Generate view."""


def generate_view(difference: list) -> str:
    """
    Generate comfortable view for difference.

    Args:
        difference: difference between files

    Returns:
        str
    """
    text = '\n'.join(map(build_diff_item_view, difference))
    if text == '':
        return '{\n}'
    return ''.join(['{\n', text, '\n}'])


def build_diff_item_view(diff_item: dict) -> list:
    """
    Build view for difference item.

    Args:
        diff_item: difference item

    Returns:
        str
    """
    marks = {
        'both_dicts': ' ',
        'only_first_dict': '-',
        'only_second_dict': '+',
    }

    mark = marks[diff_item['value_in']]
    return '  {0} {1}: {2}'.format(mark, diff_item['key'], diff_item['value'])


__all__ = ['generate_view']

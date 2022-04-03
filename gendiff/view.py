"""Generate view."""


def generate_view(difference: list, tab="") -> str:

    result = ''
    result = result + '{\n'
    for item in difference:
        assert isinstance(item, dict), 'not dict!'

        key = item.get('key')
        value = item.get('value')
        diff_type = item.get('diff_type')
        children = item.get('children')

        # if key in {'common'}:
        #     continue
        
        # print('item:')
        # print(item)

        if diff_type == 'added':
            mark_tab = tab + '  + '
        elif diff_type == 'removed':
            mark_tab = tab + '  - '
        else:
            mark_tab = tab + '    '
        blank_tab = tab + '    '
        
        
        if isinstance(value, dict):
            result = result + mark_tab + key + ': ' + show_value_dict(value, blank_tab) + '\n'
        elif children is not None:
            result = result + mark_tab + key + ': ' + generate_view(children, blank_tab) + '\n'    
        else:
            result = result + mark_tab + key + ': ' + str(value) + '\n'

        


    result = result + tab + '}'
    return result
        

def show_value_dict(dict_: dict, tab):
    result = '{\n'
    for key, value in dict_.items():
        new_tab = tab + '    '
        if isinstance(value, dict):
            result = result + new_tab + key + ': ' + show_value_dict(value, new_tab) + '\n'
        else:
            result = result + new_tab + key + ': ' + str(value) + '\n'

    result = result + tab + '}'
    return result


        


def _generate_view(difference: list) -> str:
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


def _build_diff_item_view(diff_item: dict) -> list:
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

"""Generate view."""


def generate_view(difference: list, indent="") -> str:

    result = '{\n'
    for item in difference:

        key = item.get('key')
        value = item.get('value')
        diff_type = item.get('diff_type')
        children = item.get('children')

        marked_indent = f'{indent}{get_marked_indent(diff_type)}'  
        indent_next_level = f'{indent}    '
              
        if isinstance(value, dict):
            value_view = show_value_dict(value, indent_next_level)
        elif children is not None:
            value_view = generate_view(children, indent_next_level)
        else:
            value_view = str(value)       
        result = f'{result}{marked_indent}{key}: {value_view}\n'

    return f'{result}{indent}}}'
        

def get_marked_indent(diff_type):
    if diff_type == 'added':
        return '  + '   
    if diff_type == 'removed':
        return '  - '
    return '    '


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



__all__ = ['generate_view']

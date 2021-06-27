import json
import sys

CMD_ARGS = sys.argv


def return_key(args):
    params = []
    key = ''
    integer = False
    for i in args:
        if i != '[' and i != ']' and i != '.' and not integer:
            key += i

        if i == '[':
            integer = True
            if key != '':
                params.append(key)
            key = ''
            continue

        if i == ']':
            integer = False
            continue

        if integer:
            params.append(i)

        if i == '.':
            if key != '':
                params.append(key)
            key = ''
    if key != '':
        params.append(key)
    return params


def return_python_arguments(args):
    with open(f'./{args[1]}', 'r') as file_object:
        data = json.load(file_object)

    params = return_key(args[2])
    result_string = 'data'

    for param in params:
        if param.isdigit():
            result_string += f'[{int(param)}]'
            continue
        result_string += f'["{param}"]'

    return eval(result_string)


try:
    sys.stdout.write(f'{return_python_arguments(CMD_ARGS)}\n')
except KeyError:
    sys.stderr.write('Error: Property not found\n')

finally:
    sys.exit(1)

''' $ python gson.py example.json "members[0].powers[1]"
# Heal Immunity > Turning tiny'''
# sys.stdout.write(f'*******************{return_python_arguments(CMD_ARGS)}\n')
# print(return_python_arguments(CMD_ARGS))
# python gson.py example.json "members[0].name"
# print(return_key('members[0].name'))
# print(return_key('squadName'))
# print(return_key('properties'))
# print(return_key('properties.foo'))
# print(return_key('items[0]'))
# print(return_key('items[0][0]'))
# print(return_key('shano.property'))

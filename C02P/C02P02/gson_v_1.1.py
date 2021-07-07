import json
import sys

CMD_ARGS = sys.argv


def parse_path_to_list(args):
    """
    Takes a sting (example: 'members[0].name'; 'members'; etc...)
    and returns a list of meaningful strings
    (['members', '0', 'name']) excluding dots or square brackets.

    """
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
            params.append(int(i))

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

    params = parse_path_to_list(args[2])[::-1]

    while params:
        data = data[params.pop()]
    return data


try:
    sys.stdout.write(f'{return_python_arguments(CMD_ARGS)}\n')
except (KeyError, IndexError):
    sys.stderr.write('Error: Property not found\n')
    sys.exit(1)


# $ python gson_v_1.0.py example.json "members[0].powers[1]"Heal Immunity > Turning tiny
# sys.stdout.write(f'*******************{return_python_arguments(CMD_ARGS)}\n')
# print(return_python_arguments(CMD_ARGS))
# python gson_v_1.0.py example.json "members[0].name"
# print(return_key('members[0].name'))
# print(return_key('squadName'))
# print(return_key('properties'))
# print(return_key('properties.foo'))
# print(return_key('items[0]'))
# print(return_key('items[0][0]'))
# print(return_key('shano.property'))
# print(return_python_arguments(["gson_v_1.0.py", "example.json", "members[0].name"]))

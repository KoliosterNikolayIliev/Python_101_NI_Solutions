import json
import sys
import re

CMD_ARGS = sys.argv


def parse_path_to_list(args):
    """
    Takes a sting (example: 'members[0].name'; 'members'; etc...)
    and returns a list of meaningful strings
    (['members', '0', 'name']) excluding dots or square brackets.

    """
    params = re.findall('[a-zA-Z]+|[0-9]+', args)
    return params


def return_python_arguments(args):
    with open(f'./{args[1]}', 'r') as file_object:
        data = json.load(file_object)

    params = parse_path_to_list(args[2])[::-1]

    while params:
        key = params.pop()
        if key.isdigit():
            key = int(key)
        data = data[key]
    return data


try:
    sys.stdout.write(f'{return_python_arguments(CMD_ARGS)}\n')
except Exception:
    sys.stderr.write('Error: Property not found\n')
    sys.exit(1)


# print(parse_path_to_list("members[0].powers[1]"))

# $ python gson_v_1.0.py example.json "members[0].powers[1]"Heal Immunity > Turning tiny
# sys.stdout.write(f'*******************{return_python_arguments(CMD_ARGS)}\n')
# print(return_python_arguments(CMD_ARGS))
# python gson_v_1.0.py example.json "members[0].name"
# print(parse_path_to_list('members[0].name'))
# print(parse_path_to_list('squadName'))
# print(parse_path_to_list('properties'))
# print(parse_path_to_list('properties.foo'))
# print(parse_path_to_list('items[0]'))
# print(parse_path_to_list('items[0][0]'))
# print(parse_path_to_list('shano.property'))
# print(return_python_arguments(["gson_v_1.0.py", "example.json", "members[0].name"]))

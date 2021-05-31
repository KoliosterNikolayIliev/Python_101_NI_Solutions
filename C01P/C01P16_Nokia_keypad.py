from collections import deque

""""Sorry for the spaghetti code."""

""" Part one - From number sequence to message """


def next_key_check(sequence, key):
    if key != '':
        return sequence.appendleft(key)


keys = {
    2: ('a', 'b', 'c'),
    3: ('d', 'e', 'f'),
    4: ('g', 'h', 'i'),
    6: ('m', 'n', 'o'),
    7: ('p', 'q', 'r', 's'),
    8: ('t', 'u', 'v'),
    9: ('w', 'x', 'y', 'z'),
    0: ' ',
}


def numbers_to_message(pressed_sequence):
    pressed_sequence = deque(pressed_sequence)
    index = 0
    result = ''
    letter = ''
    capitalised = False
    while pressed_sequence:
        key = pressed_sequence.popleft()
        if len(pressed_sequence) > 0:
            next_key = pressed_sequence.popleft()
        else:
            next_key = ''
        if next_key == key:
            index += 1
            if index >= len(keys[key]):
                index = 0
            next_key_check(pressed_sequence, next_key)
            continue
        if key in keys:
            letter = keys[key][index]
            next_key_check(pressed_sequence, next_key)
        if capitalised:
            letter = letter.upper()
        if key == -1:
            index = 0
            capitalised = False
            next_key_check(pressed_sequence, next_key)
            continue
        if key == 1:
            capitalised = True
            next_key_check(pressed_sequence, next_key)
            continue

        result += letter
        index = 0
        capitalised = False
    return result


tests = [
    numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]) == "abc",
    numbers_to_message([2, 2, 2, 2]) == "a",
    numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]) == "Ivo e Panda",
]

for test in tests:
    print(test)

""" Part two - From message to sequence"""


def message_to_numbers(message):
    message = deque([x for x in message])
    sequence = []
    while message:
        symbol = message.popleft()
        next_symbol = ''
        if len(message) > 0:
            next_symbol = message.popleft()
        for key in keys:
            if symbol.isupper():
                sequence.append(1)
                symbol = symbol.lower()
            if symbol in keys[key]:
                next_symbol_index = keys[key].index(symbol) + 1
                if keys[key].index(symbol) == 0:
                    sequence.append(key)
                else:
                    for i in range(next_symbol_index):
                        sequence.append(key)
                if next_symbol in keys[key]:
                    sequence.append(-1)
        if next_symbol != '':
            message.appendleft(next_symbol)

    return sequence


tests_part_two = [
    message_to_numbers("abc") == [2, -1, 2, 2, -1, 2, 2, 2],
    message_to_numbers("a") == [2],
    message_to_numbers("Ivo e Panda") == [1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2],
    message_to_numbers("aabbcc") == [2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]
]
for test in tests_part_two:
    print(test)

from collections import deque


def next_letter(index):
    index += 1
    return index


def wait(index):
    index = 0
    return index


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
            if next_key != '':
                pressed_sequence.appendleft(next_key)
            continue
        if key in keys:
            letter = keys[key][index]
            if next_key != '':
                pressed_sequence.appendleft(next_key)
        if capitalised:
            letter = letter.upper()
        if key == -1:
            index = 0
            capitalised = False
            if next_key != '':
                pressed_sequence.appendleft(next_key)
            continue
        if key == 1:
            capitalised = True
            if next_key != '':
                pressed_sequence.appendleft(next_key)
            continue

        result += letter
        index = 0
        capitalised = False
    return result


# There are some special rules:
#
#     If you press 1, the next letter is going to be capitalized
#     If you press 0, this will insert a single white-space
#     If you press a number and wait for a few seconds, the special breaking number -1 enters the sequence. This is the way to write different letters from only one keypad!
#
# Examples:

# tests = [
#     numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]) == "abc",
#     numbers_to_message([2, 2, 2, 2]) == "a",
#     numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]) == "Ivo e Panda",
# ]

print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
print(numbers_to_message([2, 2, 2, 2]))
print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))

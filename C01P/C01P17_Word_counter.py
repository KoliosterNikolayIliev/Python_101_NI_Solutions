def is_palindrome(string):
    return string == string[::-1]


def validate_index_and_check_letter(matrix, row, col, directions, direction):
    # index validation needed
    row = row + directions[direction][0]
    col = col + directions[direction][1]
    if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[0]) - 1:
        symbol = matrix[row][col]
        return symbol, direction, row, col

    return False, False, False, False


def word_counter(matrix, word):
    found_words = []
    found_word = ''
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1),
        'up_left': (-1, -1),
        'up_right': (-1, 1),
        'down_left': (1, -1),
        'down_right': (1, 1)
    }
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            symbol = matrix[row][col]
            if word[0] == symbol:
                found_word += symbol
                for direction in directions:
                    probable_letter, new_direction, new_row, new_col = validate_index_and_check_letter(
                                                                                                       matrix,
                                                                                                       row,
                                                                                                       col,
                                                                                                       directions,
                                                                                                       direction
                                                                                                       )
                    if probable_letter and probable_letter == word[1]:
                        found_word += probable_letter
                        for _ in range(1, len(word) - 1):
                            next_probable_letter = validate_index_and_check_letter(
                                matrix,
                                new_row,
                                new_col,
                                directions,
                                new_direction
                            )[0]
                            if not next_probable_letter:
                                continue
                            found_word += next_probable_letter
                            new_row += directions[direction][0]
                            new_col += directions[direction][1]
                        found_words.append(found_word)
                        found_word = symbol
    count = [x for x in found_words if word in x]
    result = len(count)
    if is_palindrome(word):
        result /= 2

    return result


# filter all start letters then from them start searching til len of word, stop if index error!
# gather them in list then make a reversed copy and

word = "ivan"
matrix = [
    ["i", "v", "a", "n"],
    ["e", "v", "n", "h"],
    ["i", "n", "a", "v"],
    ["m", "v", "v", "n"],
    ["q", "r", "i", "t"]
]
print(word_counter(matrix, word) == 3)
# print(word_counter(matrix, word))

word = "actually"
matrix = [
    ["i", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z", "o", "y", "m"],
    ["e", "v", "n", "h", "t", "r", "x", "e", "k", "y", "d", "a", "i", "l", "c"],
    ["i", "a", "c", "t", "u", "a", "l", "l", "y", "m", "c", "x", "r", "l", "e"],
    ["m", "v", "c", "n", "p", "u", "a", "m", "n", "t", "l", "u", "e", "a", "a"],
    ["q", "r", "i", "t", "w", "e", "a", "q", "u", "p", "r", "x", "t", "u", "z"],
    ["p", "e", "a", "c", "t", "u", "a", "l", "l", "y", "w", "p", "y", "t", "m"],
    ["o", "y", "h", "t", "r", "e", "l", "u", "f", "p", "q", "n", "z", "c", "s"],
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e", "q", "a", "r"]
]
print(word_counter(matrix, word) == 4)

word = "madam"
matrix = [
    ["z", "v", "a", "n", "q", "h", "r", "e", "z", "g", "t", "z"],
    ["e", "v", "m", "h", "t", "r", "x", "e", "k", "y", "m", "a"],
    ["i", "a", "c", "a", "u", "a", "l", "l", "y", "a", "c", "x"],
    ["m", "v", "c", "n", "d", "u", "a", "m", "d", "t", "l", "u"],
    ["q", "t", "i", "t", "w", "a", "a", "a", "u", "p", "r", "x"],
    ["p", "e", "m", "a", "d", "a", "m", "l", "l", "y", "w", "p"],
    ["o", "y", "h", "t", "e", "e", "l", "u", "f", "p", "q", "n"],
    ["p", "a", "c", "t", "u", "a", "l", "l", "y", "u", "r", "e"]
]
print(word_counter(matrix, word) == 3)


word = "python"
matrix = [
    ["r", "u", "b", "y"],
    ["r", "u", "b", "y"],
    ["r", "u", "b", "y"],
    ["r", "u", "b", "y"],
]

print(word_counter(matrix, word) == 0)

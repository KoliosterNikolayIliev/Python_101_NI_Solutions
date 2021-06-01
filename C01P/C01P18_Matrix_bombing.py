def validate_index_and_subtract(matrix, row, col, directions, direction, bombed):
    row = row + directions[direction][0]
    col = col + directions[direction][1]
    if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[0]) - 1:
        digit = matrix[row][col]
        digit = digit - bombed
        if digit < 0:
            digit = 0
        return digit, row, col

    return -1, False, False


DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
    'up_left': (-1, -1),
    'up_right': (-1, 1),
    'down_left': (1, -1),
    'down_right': (1, 1)
}


def matrix_bombing_plan(m):
    bombed_matrices = {}
    output_matrix = [x[::] for x in m]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            bombed = matrix[row][col]

            for direction in DIRECTIONS:
                new_digit, new_row, new_col = validate_index_and_subtract(m, row, col, DIRECTIONS, direction, bombed)

                if new_digit != -1:
                    output_matrix[new_row][new_col] = new_digit

            bombed_matrices[row, col] = (sum([sum(x) for x in output_matrix]))
            output_matrix = [x[::] for x in m]

    return bombed_matrices


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

test = {
    (0, 0): 42,
    (0, 1): 36,
    (0, 2): 37,
    (1, 0): 30,
    (1, 1): 15,
    (1, 2): 23,
    (2, 0): 29,
    (2, 1): 15,
    (2, 2): 26
}

print(matrix_bombing_plan(matrix) == test)

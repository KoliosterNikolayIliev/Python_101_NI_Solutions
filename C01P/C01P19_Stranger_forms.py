from copy import deepcopy


def check_if_possible(direction, position, matrix, directions):
    if direction == '' and matrix[position[0]][position[1]] != '*':
        return True, position[0], position[1]
    if matrix[position[0]][position[1]] == '*':
        return False, 0, 0
    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]
    if 0 <= row <= len(matrix) - 1 and 0 <= col <= len(matrix[0]) - 1 and matrix[row][col] != '*':
        return True, row, col
    return False, 0, 0


CINEMA_LAYOUT = [
    '..*...*.**',
    '.....**...',
    '*.*...*..*',
    '.**....*.*',
    '...*..*.*.',
    '.***...*..',
    '*......*.*',
    '.....**..*',
    '..*.*.*..*',
    '***.*.**..'
]

FRIENDS_CONFIGURATION = ["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]
DIRECTIONS = {
    'AA': (-1, 0),
    'RA': (0, 1),
    'AB': (-2, 0),
    'RC': (-2, 1),
    'AD': (-3, 1),
    'LE': (-3, 0),
}


def stranger_forms(cinema_layout, friends_configuration):
    cinema_layout = [[y for y in x] for x in cinema_layout]
    original = deepcopy(cinema_layout)
    result = []
    successful = True
    for row in range(len(cinema_layout)):
        for col in range(len(cinema_layout[row])):
            for sting in friends_configuration:
                direction = ''
                name = sting[0]
                if len(sting) > 1:
                    direction = sting[1] + sting[2]
                can_continue, result_row, result_col = check_if_possible(direction, (row, col), cinema_layout,
                                                                         DIRECTIONS)
                if not can_continue:
                    cinema_layout = deepcopy(original)
                    successful = False
                    break
                cinema_layout[result_row][result_col] = name
                successful = True
            if successful:
                result.append([''.join(x) for x in cinema_layout])
                cinema_layout = deepcopy(original)
    return result


tests = [
    [
        '..*GE.*.**',
        '...CD**...',
        '*.*B..*..*',
        '.**AF..*.*',
        '...*..*.*.',
        '.***...*..',
        '*......*.*',
        '.....**..*',
        '..*.*.*..*',
        '***.*.**..',
    ],

    [
        '..*...*.**',
        '.....**...',
        '*.*.GE*..*',
        '.**.CD.*.*',
        '...*B.*.*.',
        '.***AF.*..',
        '*......*.*',
        '.....**..*',
        '..*.*.*..*',
        '***.*.**..',
    ],

    [
        '..*...*.**',
        '.....**...',
        '*.*...*..*',
        '.**.GE.*.*',
        '...*CD*.*.',
        '.***B..*..',
        '*...AF.*.*',
        '.....**..*',
        '..*.*.*..*',
        '***.*.**..',
    ]
]
print(stranger_forms(CINEMA_LAYOUT, FRIENDS_CONFIGURATION) == tests)

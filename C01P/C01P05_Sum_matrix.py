def sum_matrix(m):
    return sum(sum(x) for x in m)


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m) == 45)

m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(sum_matrix(m) == 0)

m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sum_matrix(m) == 55)

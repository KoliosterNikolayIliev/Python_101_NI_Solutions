from collections import deque


def group(items):
    grouped_list = []
    items = deque(items)
    while items:
        if not items:
            grouped_list.append([])
            return grouped_list
        value = items.popleft()
        if len(grouped_list) == 0:
            grouped_list.append([value])
            continue
        if grouped_list[-1][0] == value:
            grouped_list[-1].append(value)
        else:
            grouped_list.append([value])

    return grouped_list


print(group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]])
print(group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]])
print(group([]) == [])
print(group([1]) == [[1]])
print(group([1, 1, 1, 1]) == [[1, 1, 1, 1]])

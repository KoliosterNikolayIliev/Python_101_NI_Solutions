from enum import Enum


class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3


def increasing_or_decreasing(ns):
    previous_number = 0
    values = []
    for number in ns:
        if ns.index(number) == 0:
            previous_number = number
            continue
        if previous_number > number:
            values.append(Monotonicity.DECREASING)
            previous_number = number
        elif previous_number == number:
            values.append(Monotonicity.NONE)
            return Monotonicity.NONE
        else:
            values.append(Monotonicity.INCREASING)
            previous_number = number

    if not values:
        return Monotonicity.NONE
    if Monotonicity.INCREASING in values and Monotonicity.DECREASING in values:
        return Monotonicity.NONE
    if Monotonicity.INCREASING in values:
        return Monotonicity.INCREASING
    else:
        return Monotonicity.DECREASING


test = [
    increasing_or_decreasing([1, 2, 3, 4, 5]) == Monotonicity.INCREASING,
    increasing_or_decreasing([5, 6, -10]) == Monotonicity.NONE,
    increasing_or_decreasing([1, 1, 1, 1]) == Monotonicity.NONE,
    increasing_or_decreasing([9, 8, 7, 6]) == Monotonicity.DECREASING,
    increasing_or_decreasing([]) == Monotonicity.NONE,
    increasing_or_decreasing([1]) == Monotonicity.NONE,
    increasing_or_decreasing([1, 100]) == Monotonicity.INCREASING,
    increasing_or_decreasing([1, 100, 100]) == Monotonicity.NONE,
    increasing_or_decreasing([100, 1]) == Monotonicity.DECREASING,
    increasing_or_decreasing([100, 1, 1]) == Monotonicity.NONE,
    increasing_or_decreasing([100, 1, 2]) == Monotonicity.NONE,
]
[print(x) for x in test]

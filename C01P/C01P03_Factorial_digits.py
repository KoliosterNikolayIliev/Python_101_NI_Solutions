import math


def fact_digits(n):
    return sum(math.factorial(int(x)) for x in str(n))


test = [
    fact_digits(101) == 3,
    fact_digits(111) == 3,
    fact_digits(145) == 145,
    fact_digits(999) == 1088640,
]

[print(x) for x in test]

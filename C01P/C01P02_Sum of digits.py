def sum_of_digits(n):
    return sum(int(x) for x in str(abs(n)))


print(sum_of_digits(1325132435356) == 43)
print(sum_of_digits(123) == 6)
print(sum_of_digits(6) == 6)
print(sum_of_digits(-10) == 1)

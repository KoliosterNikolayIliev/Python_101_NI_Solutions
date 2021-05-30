def palindromes_count(n):
    counter = 0
    a = []
    for number in range(10, n+1):
        if str(number) == str(number)[::-1]:
            counter += 1
    return counter



if __name__ == __name__:
    print(palindromes_count(10) == 0)
    print(palindromes_count(20) == 1)  # only 11
    print(palindromes_count(101) == 10)  # 11, 22, 33, 44, 55, 66, 77, 88, 99, 101
    print(palindromes_count(92009) == 1009)
    print(palindromes_count(99999) == 1089)
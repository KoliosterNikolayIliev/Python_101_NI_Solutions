# I have watched the video for this one.


def prime_factorization(n):
    result = []
    prime = 2
    power = 0
    while n > 1:
        while n % prime == 0:
            n = n // prime
            power = power + 1
        if power > 0:
            result.append((prime, power))
        power = 0
        prime += 1
    return result


print(prime_factorization(10) == [(2, 1), (5, 1)])  # This is 2^1 * 5^1
print(prime_factorization(14) == [(2, 1), (7, 1)])
print(prime_factorization(356) == [(2, 2), (89, 1)])
print(prime_factorization(89) == [(89, 1)])  # 89 is a prime number
print(prime_factorization(1000) == [(2, 3), (5, 3)])

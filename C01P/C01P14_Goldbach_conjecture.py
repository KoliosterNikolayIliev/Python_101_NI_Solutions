# I have watched the video for this one.

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def goldbach(n):
    if n % 2 != 0 or n <= 2:
        return

    result = {}
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)

    for prime in primes:
        for prime2 in primes:
            if prime + prime2 == n:
                tup = tuple(sorted((prime, prime2)))
                result[tup] = n

    return list(result.keys())


tests = [
    goldbach(4) == [(2, 2)],
    goldbach(6) == [(3, 3)],
    goldbach(8) == [(3, 5)],
    goldbach(10) == [(3, 7), (5, 5)],
    goldbach(100) == [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)],
    goldbach(5) is None,
]
for test in tests:
    print(test)

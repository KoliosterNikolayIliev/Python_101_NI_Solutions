import sys
import time


def fibonacci(n):

    if n == 1 or n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def benchmark(n):
    start = time.time()
    result = fibonacci(n)
    end = time.time()

    return result, end - start


print(benchmark(int(sys.argv[1])))
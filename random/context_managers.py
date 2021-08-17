# https://realpython.com/python-with-statement/#measuring-execution-time

from time import perf_counter, sleep


"""
lambda x, y: self.end - self.start

def ???(x, y):
    return self.end - self.start
"""


class Block:
    def __init__(self, description):
        pass

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass


# Similiar concept to self.subTest()
with Block("Calculations are done here"):
    x = 1 + 2


class StatefulContextManager:
    def __init__(self):
        self.counter = 0

    def __enter__(self):
        return self.counter

    def __exit__(self, *args):
        self.counter += 1


x = StatefulContextManager()


with x as value:
    # 0
    print(value)


with x as value:
    # 1
    print(value)


class Timer:
    # dunders - double underscore
    def __enter__(self):
        # state
        self.start = perf_counter()
        self.end = 0.0

        # Delayed value / calculation
        # return lambda: self.end - self.start
        return self.get_time

    def __exit__(self, *args):
        self.end = perf_counter()

    def get_time(self):
        return self.end - self.start


# timer = Timer()

with Timer() as f:
    sleep(1)


print(f())
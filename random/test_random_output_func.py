import unittest

from random import randint

# September:

# ipdb
# modules & imports
# mocks
# TDD - Test Driven Development
# sprinkle with problems to solves


# How would we test this function ????
def foo():
    a = randint(1, 10)
    b = randint(1, 10)
    c = requests.get("https://random.org/something")

    return a * b


class FooTests(unittest.TestCase):
    def test_foo_does_something_questionmark_questionmark(self):
        # Mock the call to randint in foo() to first return 5, then 4, raise exception, if called 3rd time
        result = foo()

        self.assertEqual(20, result)

        self.assertLessEqual(result, 100)
        self.assertGreaterEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
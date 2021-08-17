import unittest

from C03P03_exception_silencer import ExceptionSilencer


class TestsExceptionSilencer(unittest.TestCase):

    def test_not_propagate_ValueError(self):
        with ExceptionSilencer(ValueError):
            int("aa")

    def test_not_propagate_IndexError(self):
        with ExceptionSilencer(IndexError):
            index_test = ''
            index_test[1]

    def test_not_propagate_TypeError(self):
        with ExceptionSilencer(TypeError):
            a = 0
            b = '0'
            a + b

    def test_not_propagate_ZeroDivisionError(self):
        with ExceptionSilencer(ZeroDivisionError):
            1 / 0

    def test_propagate_KeyError(self):
        with self.assertRaises(ValueError):
            with ExceptionSilencer(KeyError):
                int("aa")

    def test_propagate_IndexError(self):
        with self.assertRaises(IndexError):
            with ExceptionSilencer(Exception):
                index_test = ''
                index_test[1]

    def test_propagate_TypeError(self):
        with self.assertRaises(TypeError):
            with ExceptionSilencer(ValueError):
                a = 0
                b = '0'
                a + b

    def test_propagate_ZeroDivisionError(self):
        with self.assertRaises(ZeroDivisionError):
            with ExceptionSilencer(TypeError):
                1 / 0


if __name__ == '__main__':
    unittest.main()

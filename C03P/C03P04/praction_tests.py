import unittest

from fraction import Fraction


class TestsFraction(unittest.TestCase):

    def test_normal_initialisation(self):
        a = Fraction(6, 12)
        self.assertEqual(a.numerator, 6)
        self.assertEqual(a.denominator, 12)
        self.assertEqual(a.gcd, 6)

    def test_missing_parameter_initialisation(self):
        self.assertRaises(TypeError, Fraction, 1, '1')

    def test_zero_division_raises_ValueError(self):
        self.assertRaises(ValueError, Fraction, 1, 0)

    def test__eq__Fraction_returns_True(self):
        a = Fraction(6, 12)
        b = Fraction(6, 12)
        self.assertEqual(a, b)
        self.assertEqual(a.numerator, b.numerator)
        self.assertEqual(a.denominator, b.denominator)

    def test__eq__Fraction_returns_False(self):
        a = Fraction(3, 12)
        b = Fraction(6, 12)
        self.assertNotEqual(a, b)
        self.assertNotEqual(a.numerator, b.numerator)
        self.assertEqual(a.denominator, b.denominator)

    def test__str__representation(self):
        a = Fraction(0, 2)
        b = Fraction(3, 2)
        self.assertEqual(a.__str__(), '0')
        self.assertEqual(b.__str__(), '3/2')

    def test__repr__representation(self):
        a = Fraction(0, 2)
        b = Fraction(3, 2)
        self.assertEqual(a.__repr__(), '0')
        self.assertEqual(b.__repr__(), '3/2')

    def test_addition(self):
        a = Fraction(1, 2)
        b = Fraction(3, 2)
        c = a + b
        self.assertEqual(c.__repr__(), '4/2')
        a = Fraction(1, 3)
        b = Fraction(3, 2)
        c = a + b
        self.assertEqual(c.__repr__(), '11/6')

    def test_subtraction(self):
        a = Fraction(1, 2)
        b = Fraction(3, 2)
        c = a - b
        self.assertEqual(c.__repr__(), '-2/2')
        a = Fraction(1, 3)
        b = Fraction(3, 2)
        c = a - b
        self.assertEqual(c.__repr__(), '-7/6')

    def test_multiply(self):
        a = Fraction(1, 2)
        b = Fraction(3, 2)
        c = a*b
        self.assertEqual(c.__repr__(), '3/4')

    def test_simplify(self):
        a = Fraction(20, 150)
        b = Fraction(0, 2)
        c = Fraction(1, 3)
        self.assertEqual(a.simplify().__repr__(), '2/15')
        self.assertEqual(b.simplify().__repr__(), '0')
        self.assertEqual(c.simplify().__repr__(), '1/3')

    def test_is_simplified(self):
        a = Fraction(20, 150)
        b = Fraction(1, 3)
        self.assertFalse(a.is_simplified())
        self.assertTrue(a.simplify().is_simplified())
        self.assertTrue(b.is_simplified())

    def test__lt__(self):
        self.assertTrue((sorted([Fraction(1, 2), Fraction(1, 4)]) == [Fraction(1, 4), Fraction(1, 2)]))
        self.assertFalse(([Fraction(1, 2), Fraction(1, 4)] == [Fraction(1, 2), Fraction(1, 2)]))


if __name__ == '__main__':
    unittest.main()




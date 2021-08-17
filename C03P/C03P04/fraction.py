import math


class Fraction:

    def __init__(self, numerator, denominator):
        """
        Construct a new Fraction.
        If denominator = 0, raise ValueError.
        """
        if denominator == 0:
            raise ValueError

        self.numerator = numerator
        self.denominator = denominator
        self.gcd = math.gcd(self.numerator, self.denominator)

    def __str__(self):
        """
        Returns the string representation of self.
        """
        if self.numerator == 0:
            return '0'

        return f'{self.numerator}/{self.denominator}'

    def __repr__(self):
        """
        Returns the REPL representation of self.
        """
        if self.numerator == 0:
            return '0'

        return f'{self.numerator}/{self.denominator}'

    def __eq__(self, other):
        """
        Returns True/False, if self is equal to other.
        """
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        return False

    def __add__(self, other):
        """
        Returns new Fraction, that's the sum of self and other.
        """
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)

        first_numerator = self.numerator * other.denominator

        second_numerator = self.denominator * other.numerator

        denominator = self.denominator * other.denominator

        result_numerator = first_numerator + second_numerator

        if result_numerator == 0:
            return Fraction(0, 1)

        return Fraction(result_numerator, denominator)

    def __sub__(self, other):
        """
        Returns new Fraction, that's the subtraction of self and other.
        """
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)

        first_numerator = self.numerator * other.denominator

        second_numerator = self.denominator * other.numerator

        denominator = self.denominator * other.denominator

        result_numerator = first_numerator - second_numerator

        if result_numerator == 0:
            return Fraction(0, 1)

        return Fraction(result_numerator, denominator)

    def __mul__(self, other):
        """
        Returns new Fraction, that's the product of self and other.
        """
        if self.numerator == 0:
            return Fraction(0, 1)

        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def simplify(self):
        """
        Returns new Fraction, that's the simplification of self
        """
        return Fraction(int(self.numerator / self.gcd), int(self.denominator / self.gcd))

    def is_simplified(self):
        """
        Returns True/False, if self cannot be simplified further
        """
        if self.gcd == 1 or self.numerator == 0:
            return True
        return False

    def __lt__(self, other):
        if self.numerator / self.denominator < other.numerator / other.denominator:
            return True
        return False




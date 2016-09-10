import string
from unittest import TestCase

from nose.tools import istest

from nisteag.entropy import (
    EmptyTokenError,
    EntropyCalculator,
)


class EntropyCalculatorTest(TestCase):
    def setUp(self):
        self.calculator = EntropyCalculator()

    @istest
    def calculates_for_empty_token(self):
        result = self.calculator.calculate('')

        self.assertEqual(result, 0)

    @istest
    def calculates_for_single_ascii_character(self):
        result = self.calculator.calculate('a')

        self.assertEqual(result, 4)

    @istest
    def calculates_for_2_ascii_characters(self):
        result = self.calculator.calculate(string.printable[:2])

        self.assertEqual(result, 6)

    @istest
    def calculates_for_6_ascii_characters(self):
        result = self.calculator.calculate(string.printable[:6])

        self.assertEqual(result, 14)

    @istest
    def calculates_for_8_ascii_characters(self):
        result = self.calculator.calculate(string.printable[:8])

        self.assertEqual(result, 18)

    @istest
    def calculates_for_9_ascii_characters(self):
        result = self.calculator.calculate(string.printable[:9])

        self.assertEqual(result, 19.5)

    @istest
    def calculates_for_21_ascii_characters(self):
        result = self.calculator.calculate(string.printable[:21])

        self.assertEqual(result, 37)

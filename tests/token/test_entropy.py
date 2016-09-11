# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
    def calculates_for_single_ascii_upper_character(self):
        result = self.calculator.calculate('A')

        self.assertEqual(result, 4)

    @istest
    def calculates_for_2_ascii_characters(self):
        result = self.calculator.calculate(string.printable[:2])

        self.assertEqual(result, 6)

    @istest
    def calculates_for_3_ascii_characters(self):
        result = self.calculator.calculate(string.printable[:3])

        self.assertEqual(result, 8)

    @istest
    def calculates_for_4_ascii_characters(self):
        result = self.calculator.calculate(string.printable[:4])

        self.assertEqual(result, 10)

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
        token = (string.ascii_letters * 2)[:21]
        result = self.calculator.calculate(token)

        self.assertEqual(result, 37)

    @istest
    def calculates_for_single_unicode_character(self):
        result = self.calculator.calculate('á')

        self.assertEqual(result, 12.26)

    @istest
    def calculates_for_single_ascii_byte(self):
        result = self.calculator.calculate('a'.encode('ascii'))

        self.assertEqual(result, 4)

    @istest
    def calculates_for_single_utf8_byte(self):
        result = self.calculator.calculate('á'.encode('utf-8'))

        self.assertEqual(result, 12.26)

    @istest
    def calculates_for_single_latin1_byte(self):
        result = self.calculator.calculate('á'.encode('latin1'))

        self.assertEqual(result, 12.26)

    @istest
    def calculates_for_mixed_case(self):
        result = self.calculator.calculate('abcA')

        self.assertEqual(result, 12)

    @istest
    def calculates_for_small_mixed_case(self):
        result = self.calculator.calculate('abC')

        self.assertEqual(result, 8)

    @istest
    def calculates_for_lower_and_digit(self):
        result = self.calculator.calculate('abc1')

        self.assertEqual(result, 12)

    @istest
    def calculates_for_upper_and_digit(self):
        result = self.calculator.calculate('ABC1')

        self.assertEqual(result, 12)

    @istest
    def calculates_for_upper_and_special(self):
        result = self.calculator.calculate('ABC*')

        self.assertEqual(result, 12)

    @istest
    def calculates_for_lower_and_upper_and_special_and_number(self):
        result = self.calculator.calculate('aA*1')

        self.assertEqual(result, 12)

    @istest
    def calculates_for_mixed_case_5(self):
        result = self.calculator.calculate('Abcde')

        self.assertEqual(result, 15)

    @istest
    def calculates_for_mixed_case_9(self):
        result = self.calculator.calculate('Abcdefghi')

        self.assertEqual(result, 25.5)

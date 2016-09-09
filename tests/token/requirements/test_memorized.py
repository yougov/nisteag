from unittest import TestCase

from nose.tools import istest

from nisteag.token.requirements.memorized import (
    Level1Checker,
    Level2Checker,
    SmallPasswordError,
)


class Level1CheckerTest(TestCase):
    def setUp(self):
        self.checker = Level1Checker()

    @istest
    def checks_a_strong_password(self):
        self.checker.check('This Is a BIG and relev4nt passwurd!!!')

    @istest
    def fails_a_too_small_password(self):
        with self.assertRaises(SmallPasswordError):
            self.checker.check('12345')


class Level2CheckerTest(TestCase):
    def setUp(self):
        self.checker = Level2Checker()

    @istest
    def checks_a_strong_password(self):
        self.checker.check('This Is a BIG and relev4nt passwurd!!!')

    @istest
    def fails_a_too_small_password(self):
        with self.assertRaises(SmallPasswordError):
            self.checker.check('1234567')

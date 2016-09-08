from unittest import TestCase

from nose.tools import istest

from nisteag.token.requirements import (
    PasswordStrengthChecker,
    SmallPasswordError,
)


class PasswordStrengthCheckerTest(TestCase):
    def setUp(self):
        self.checker = PasswordStrengthChecker()

    @istest
    def checks_a_strong_password(self):
        self.checker.check('This Is a BIG and relev4nt passwurd!!!')

    @istest
    def fails_a_too_small_password(self):
        with self.assertRaises(SmallPasswordError):
            self.checker.check('1234567')

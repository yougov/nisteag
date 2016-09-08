MINIMUM_LENGTH = 8


class StrengthError(Exception):
    """Base exception class for strengh check failures."""


class SmallPasswordError(StrengthError):
    """Raised when the password is too small."""


class PasswordStrengthChecker(object):
    def check(self, password):
        if len(password) < MINIMUM_LENGTH:
            raise SmallPasswordError(
                'The password needs to be at least 8 characters long.')

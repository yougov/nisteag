class StrengthError(Exception):
    """Base exception class for strengh check failures."""


class SmallPasswordError(StrengthError):
    """Raised when the password is too small."""


class Level1Checker(object):
    MINIMUM_LENGTH = 6

    def check(self, password):
        if len(password) < self.MINIMUM_LENGTH:
            raise SmallPasswordError(
                'The password needs to be at least 8 characters long.')

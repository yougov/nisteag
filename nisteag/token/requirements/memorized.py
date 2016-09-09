class StrengthError(Exception):
    """Base exception class for strengh check failures."""


class SmallPasswordError(StrengthError):
    """Raised when the password is too small."""


class BaseMemorizedChecker(object):
    def _check_length(self, password):
        if len(password) < self.MINIMUM_LENGTH:
            raise SmallPasswordError(
                'The password needs to be at least {} characters long.'.format(
                    self.MINIMUM_LENGTH))

    def check(self, password):
        self._check_length(password)


class Level1Checker(BaseMemorizedChecker):
    MINIMUM_LENGTH = 6


class Level2Checker(BaseMemorizedChecker):
    MINIMUM_LENGTH = 8

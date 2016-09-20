"""Requirements for memorized tokens."""

import string

from nisteag.entropy import EntropyCalculator, EntropyError


class WeakTokenError(EntropyError):
    """Raised when the token is too weak."""


class BaseMemorizedChecker(object):
    MINIMUM_LENGTH = 0

    def __init__(self):
        self.calculator = EntropyCalculator()

    def check(self, token, dictionary=None, username=None):
        bits = self.calculator.calculate(token, dictionary, username)

        if bits < self._comparison_bits():
            raise WeakTokenError('Token is too weak.')

    def _comparison_bits(self):
        comparison_token = string.printable[:self.MINIMUM_LENGTH]
        return self.calculator.calculate(comparison_token)


class Level1Checker(BaseMemorizedChecker):
    MINIMUM_LENGTH = 6


class Level2Checker(BaseMemorizedChecker):
    MINIMUM_LENGTH = 8

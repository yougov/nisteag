"""Requirements for memorized tokens."""

from nisteag.entropy import EntropyCalculator, EntropyError


class WeakTokenError(EntropyError):
    """Raised when the token is too weak."""


class BaseMemorizedChecker(object):
    MINIMUM_ENTROPY = 0

    def __init__(self):
        self.calculator = EntropyCalculator()

    def check(self, token, dictionary=None, username=None):
        bits = self.calculator.calculate(token, dictionary, username)

        if bits < self.MINIMUM_ENTROPY:
            raise WeakTokenError('Token is too weak.')


class Level1Checker(BaseMemorizedChecker):
    MINIMUM_ENTROPY = 14


class Level2Checker(BaseMemorizedChecker):
    MINIMUM_ENTROPY = 18

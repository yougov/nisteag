"""Requirements for Memorized Secret Tokens.

See section 6.3.1.1. Single Token Authentication, table 6, page 51, of the NIST
document.

"""

from abc import ABCMeta

from nisteag.entropy import EntropyCalculator
from nisteag.errors import WeakTokenError


class BaseMemorizedChecker(object):
    __metaclass__ = ABCMeta

    MINIMUM_ENTROPY = 0

    def __init__(self, throttler=None):
        """Initializes the instance.

        :param nisteag.threats.throttling.BaseThrottler throttler:
            An optional throttler that can be used at token requirements check
            time. Default is `None`.

        """
        self.calculator = EntropyCalculator()
        self.throttler = throttler

    def check(self, token, dictionary=None, username=None):
        """Checks a token to make sure it meets the requirements.

        :param str token: The token for the calculation. May be a password, a
            pass-phrase and the like.
        :param sequence dictionary: An optional dictionary as a sequence,
            against which the token will be tested, if provided. If you opt by
            using it, provide a dictionary of at least 50,000 items.
            Default: `None`.
        :param str username: An optional username to be used for anagram
            checking. Default: `None`.

        """
        if self.throttler is not None:
            self.throttler.check(username, token)

        bits = self.calculator.calculate(token, dictionary, username)

        if bits < self.MINIMUM_ENTROPY:
            raise WeakTokenError('Token is too weak.')


class Level1Checker(BaseMemorizedChecker):
    MINIMUM_ENTROPY = 14


class Level2Checker(BaseMemorizedChecker):
    MINIMUM_ENTROPY = 18

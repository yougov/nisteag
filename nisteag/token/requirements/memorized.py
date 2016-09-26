"""Requirements for Memorized Secret Tokens.

See section 6.3.1.1. Single Token Authentication, table 6, page 51, of the NIST
document.

"""

from abc import ABCMeta, abstractmethod

from nisteag.entropy import EntropyCalculator, TokenError


class WeakTokenError(TokenError):
    """Raised when the token is too weak."""


class ThrottlerTokenError(TokenError):
    """Raised when the token is rejected by the throttler."""


class BaseThrottler(object):
    """Base class for implementation of throttling mechanisms.

    The only method that needs to be implemented is
    :meth:`BaseThrottler.check`.

    :throws ThrottlerTokenError: In case the throttler rejects the token - for
        instance if it's temporarily blocked.

    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def check(self, username, token):
        raise NotImplementedError()  # pragma: no cover


class NullThrottler(BaseThrottler):
    """A null throttler, i.e., it does not actually do anything.

    The check from this class always passes, it's used for experimentation or
    testing purposes only. Use it at your own risk.

    """

    def check(self, username, token):
        pass


class BaseMemorizedChecker(object):
    MINIMUM_ENTROPY = 0

    def __init__(self, throttler):
        """Initializes the instance.

        :param BaseThrottler throttler: The throttler that will be used for
            making sure that failed attempts are limited.

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
        self.throttler.check(username, token)

        bits = self.calculator.calculate(token, dictionary, username)

        if bits < self.MINIMUM_ENTROPY:
            raise WeakTokenError('Token is too weak.')


class Level1Checker(BaseMemorizedChecker):
    MINIMUM_ENTROPY = 14


class Level2Checker(BaseMemorizedChecker):
    MINIMUM_ENTROPY = 18

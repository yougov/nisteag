"""Requirements for memorized tokens."""

from nisteag.entropy import EntropyError


class SmallTokenError(EntropyError):
    """Raised when the token is too small."""


class BaseMemorizedChecker(object):
    def _check_length(self, token):
        if len(token) < self.MINIMUM_LENGTH:
            raise SmallTokenError(
                'The token needs to be at least {} characters long.'.format(
                    self.MINIMUM_LENGTH))

    def check(self, token):
        self._check_length(token)


class Level1Checker(BaseMemorizedChecker):
    MINIMUM_LENGTH = 6


class Level2Checker(BaseMemorizedChecker):
    MINIMUM_LENGTH = 8

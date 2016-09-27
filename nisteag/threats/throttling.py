"""Throttling mechanisms.

See section 8.2.3. Throttling Mechanisms, page 75, of the NIST document.

"""

from abc import ABCMeta, abstractmethod

from nisteag.errors import SecurityError


class ThrottlerError(SecurityError):
    """Raised when there's any issue caught by the throttler."""


class BaseThrottler(object):
    """Base class for implementation of throttling mechanisms.

    The only method that needs to be implemented is
    :meth:`BaseThrottler.check`.

    :throws ThrottlerError: In case the throttler rejects the token - for
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

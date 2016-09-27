"""Throttling mechanisms.

See section 8.2.3. Throttling Mechanisms, page 75, of the NIST document.

"""

import time
from abc import ABCMeta, abstractmethod
from collections import defaultdict, deque

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


class MemoryThrottler(BaseThrottler):
    """A very simple and naive memory-based throttler.

    This throttler was developed only as a concept; since it runs in memory,
    and application processes normally don't last too long, it will probably
    not make much sense to use it in production.

    If the checks reach 100 times in a period of until 30 days, it starts
    failing on further attempts, like recommended by the NIST document.

    Not thread-safe at all!

    """

    MAX_ATTEMPTS = 100
    ATTEMPT_WINDOW = 30 * 24 * 60 * 60

    def __init__(self):
        self.__users_data = defaultdict(self.__user_initial_data)

    def __user_initial_data(self):
        return deque([], self.MAX_ATTEMPTS)

    def check(self, username, token):
        user_data = self.__users_data[username]
        now = time.time()

        if len(user_data) == self.MAX_ATTEMPTS and (
                (now - user_data[0]) <= self.ATTEMPT_WINDOW):
            raise ThrottlerError('User reached maximum attempts.')

        user_data.append(now)

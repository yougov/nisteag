KEYBOARD_CHARS = 90
UNICODE_CHARS = 1114111


class EntropyError(Exception):
    """Base exception class for entropy errors."""


class EmptyTokenError(EntropyError):
    """Raised when the token is empty."""


class EntropyCalculator(object):
    def calculate(self, token):
        total = 0

        for i, char in enumerate(token):
            if i == 0:
                bits = 4
            elif i < 8:
                bits = 2
            elif i < 20:
                bits = 1.5
            else:
                bits = 1
            total += bits

        return total

import math

import chardet
import six


KEYBOARD_SIZE = 94
UNICODE_SIZE = 1114111


class EntropyError(Exception):
    """Base exception class for entropy errors."""


class EmptyTokenError(EntropyError):
    """Raised when the token is empty."""


class EntropyCalculator(object):
    def _get_alphabet_size(self, token):
        try:
            token.encode('ascii')
        except UnicodeEncodeError:
            return UNICODE_SIZE
        return KEYBOARD_SIZE

    def calculate(self, token):
        if not isinstance(token, six.text_type):
            token = self._decode_token(token)

        total = self._calculate_bits(token)

        size = self._get_alphabet_size(token)
        coef = math.log(size, 2) / math.log(KEYBOARD_SIZE, 2)

        return round(total * coef, 2)

    def _calculate_bits(self, token):
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

    def _decode_token(self, token):
        try:
            return token.decode('utf-8')
        except UnicodeDecodeError:
            charset = chardet.detect(token)
            return token.decode(charset['encoding'])

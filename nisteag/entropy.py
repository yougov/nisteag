import math
import string

import chardet
import six


KEYBOARD_SIZE = 94
UNICODE_SIZE = 1114111


ALL_SET = set(string.printable)
LOWER_SET = set(string.ascii_lowercase)
UPPER_SET = set(string.ascii_uppercase)
DIGIT_SET = set(string.digits)
SPECIAL_SET = ALL_SET - (LOWER_SET | UPPER_SET | DIGIT_SET)


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
        if not token:
            return 0

        if not isinstance(token, six.text_type):
            token = self._decode_token(token)

        bits = self._calculate_bits(token)

        size = self._get_alphabet_size(token)
        coef = math.log(size, 2) / math.log(KEYBOARD_SIZE, 2)

        bits += self._get_composition_additional(token)

        return round(bits * coef, 2)

    def _get_composition_additional(self, token):
        token_set = set(token)
        composition = -6

        for checking_set in (LOWER_SET, DIGIT_SET, UPPER_SET, SPECIAL_SET):
            if token_set & checking_set:
                composition += 6

        for c in token_set:
            if c not in ALL_SET:
                composition += 6
                break

        return composition

    def _calculate_bits(self, token):
        bits = 0

        for i, char in enumerate(token):
            if i == 0:
                char_bits = 4
            elif i < 8:
                char_bits = 2
            elif i < 20:
                char_bits = 1.5
            else:
                char_bits = 1
            bits += char_bits

        return bits

    def _decode_token(self, token):
        try:
            return token.decode('utf-8')
        except UnicodeDecodeError:
            charset = chardet.detect(token)
            return token.decode(charset['encoding'])

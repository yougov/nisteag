"""This module is related to token entropy calculation and the like.

See Appendix A of the NIST document (page 103) if you want to understand how
the calculation is done.

"""

import math
import string

import chardet
import six

from nisteag.errors import (
    DictionaryError,
    AnagramError,
)


KEYBOARD_SIZE = 94
UNICODE_SIZE = 1114111


ALL_SET = set(string.printable)
LOWER_SET = set(string.ascii_lowercase)
UPPER_SET = set(string.ascii_uppercase)
DIGIT_SET = set(string.digits)
SPECIAL_SET = ALL_SET - (LOWER_SET | UPPER_SET | DIGIT_SET)
SETS = sorted((LOWER_SET, UPPER_SET, DIGIT_SET, SPECIAL_SET))


MAX_COMPOSITION_BITS = 6
MAX_DICTIONARY_BITS = 6
MIN_DICT_USER_BITS = 10


class EntropyCalculator(object):
    """This class is used to calculate entropies for tokens."""

    def _get_alphabet_size(self, token):
        try:
            token.encode('ascii')
        except UnicodeEncodeError:
            return UNICODE_SIZE
        return KEYBOARD_SIZE

    def calculate(self, token, dictionary=None, username=None):
        """Calculates the entropy for a given token.

        :param str token: The token for the calculation. May be a password, a
            pass-phrase and the like.
        :param sequence dictionary: An optional dictionary as a sequence,
            against which the token will be tested, if provided. If you opt by
            using it, provide a dictionary of at least 50,000 items.
            Default: `None`.
        :param str username: An optional username to be used for anagram
            checking. Default: `None`.

        """

        if not token:
            return 0

        if dictionary and token in dictionary:
            raise DictionaryError('Token exists in the dictionary provided.')

        if username and sorted(username) == sorted(token):
            raise AnagramError('Token must not be an anagram of username.')

        if not isinstance(token, six.text_type):
            token = self._decode_token(token)

        bits = self._calculate_bits(token)

        size = self._get_alphabet_size(token)
        coef = math.log(size, 2) / math.log(KEYBOARD_SIZE, 2)

        bits += self._get_composition_additional(token)
        bits += self._get_dictionary_additional(token, dictionary)

        if username and dictionary:
            bits = max(bits, MIN_DICT_USER_BITS)

        return round(bits * coef, 2)

    def _get_dictionary_additional(self, token, dictionary):
        length = len(token)
        if not dictionary or length < 4 or length >= 20:
            return 0
        if length > 8:
            return MAX_DICTIONARY_BITS - (length - 8) / 2.0
        return min(length, MAX_DICTIONARY_BITS)

    def _get_composition_additional(self, token):
        token_set = set(token)
        token_length = len(token)
        composition = 0

        if self._is_composed(token_set) and token_length > 3:
            composition = min(token_length - 2, MAX_COMPOSITION_BITS)

        return composition

    def _is_composed(self, token_set):
        for i, first_set in enumerate(SETS):
            for j, second_set in enumerate(SETS):
                composes = (
                    i != j
                    and token_set & first_set
                    and token_set & second_set
                )
                if composes:
                    return True
        return False

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

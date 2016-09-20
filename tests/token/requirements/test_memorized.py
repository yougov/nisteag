# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest import TestCase

from nose.tools import istest

from nisteag.entropy import AnagramError, DictionaryError
from nisteag.token.requirements.memorized import (
    Level1Checker,
    Level2Checker,
    WeakTokenError,
)


class Level1CheckerTest(TestCase):
    def setUp(self):
        self.checker = Level1Checker()

    @istest
    def checks_a_strong_token(self):
        self.checker.check('This Is a BIG and relev4nt passwurd!!!')

    @istest
    def fails_a_too_weak_token(self):
        with self.assertRaises(WeakTokenError):
            self.checker.check('12345')

    @istest
    def checks_a_strong_unicode_token(self):
        self.checker.check('á1234')

    @istest
    def fails_an_existing_token(self):
        token = 'Some Exist1ng Tok3n!!!'

        with self.assertRaises(DictionaryError):
            self.checker.check(token, dictionary=['something', token])

    @istest
    def fails_an_anagram_token(self):
        token = 'This Is a BIG and relev4nt passwurd!!!'

        with self.assertRaises(AnagramError):
            self.checker.check(token, username=reversed(token))


class Level2CheckerTest(TestCase):
    def setUp(self):
        self.checker = Level2Checker()

    @istest
    def checks_a_strong_token(self):
        self.checker.check('This Is a BIG and relev4nt passwurd!!!')

    @istest
    def fails_a_too_weak_token(self):
        with self.assertRaises(WeakTokenError):
            self.checker.check('1234567')

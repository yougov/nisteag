from unittest import TestCase

from mock import patch
from nose.tools import istest

from nisteag.threats.throttling import MemoryThrottler, ThrottlerError


class MemoryThrottlerTest(TestCase):
    def setUp(self):
        self.throttler = MemoryThrottler()

    @istest
    def checks_once_for_username(self):
        self.throttler.check('john', 'some-token')

    @istest
    def throws_error_after_max_attempts(self):
        for i in range(100):
            self.throttler.check('john', 'some-token')

        with self.assertRaises(ThrottlerError):
            self.throttler.check('john', 'some-token')

    @istest
    @patch('nisteag.threats.throttling.time')
    def doesnt_throw_error_if_attempts_outside_window(self, mock_time):
        mock_time.time.side_effect = [
            i * self.throttler.ATTEMPT_WINDOW
            for i in range(101)
        ]

        for i in range(101):
            self.throttler.check('john', 'some-token')

    @istest
    def doesnt_throw_error_if_different_users(self):
        for i in range(101):
            self.throttler.check('john{}'.format(i), 'some-token')

    @istest
    @patch('nisteag.threats.throttling.time')
    def throws_error_after_window(self, mock_time):
        mock_time.time.side_effect = [
            i * self.throttler.ATTEMPT_WINDOW
            for i in range(101)
        ] + [
            i + (100 * self.throttler.ATTEMPT_WINDOW)
            for i in range(101, 201)
        ]

        for i in range(101):
            self.throttler.check('john', 'some-token')

        with self.assertRaises(ThrottlerError):
            for i in range(101, 201):
                self.throttler.check('john', 'some-token')

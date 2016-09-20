from unittest import TestCase

from mock import patch
from nose.tools import istest

from nisteag.scripts.checkers import check_entropy


class CheckEntropyTest(TestCase):
    @istest
    @patch('nisteag.scripts.checkers.print')
    @patch('nisteag.scripts.checkers.sys')
    def checks_entropy(self, mock_sys, mock_print):
        mock_sys.argv = ['check-entropy', 'abcd']

        check_entropy()

        mock_print.assert_called_once_with(10.0)

    @istest
    @patch('nisteag.scripts.checkers.print')
    @patch('nisteag.scripts.checkers.sys')
    @patch('nisteag.scripts.checkers.getpass')
    def checks_entropy_with_safe_pass(self, mock_pass, mock_sys, mock_print):
        mock_sys.argv = ['check-entropy']
        mock_pass.return_value = 'abcd'

        check_entropy()

        mock_print.assert_called_once_with(10.0)

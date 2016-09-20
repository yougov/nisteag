from __future__ import print_function

import sys
from getpass import getpass

from nisteag.entropy import EntropyCalculator


def check_entropy():
    calculator = EntropyCalculator()

    try:
        token = sys.argv[1]
    except IndexError:
        token = getpass()

    print(calculator.calculate(token))

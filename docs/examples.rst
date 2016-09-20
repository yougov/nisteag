Examples
========

Library
-------

Checking that a password meets the minimum requirements::

    from nisteag.token.requirements.memorized import BaseThrottler, Level1Checker


    class MyThrottler(BaseThrottler):
        def check(self, username, token):
            """Verify that the token hasn't failed too many times and too frequently."""


    checker = Level1Checker(MyThrottler())

    checker.check('This Is a b1g and r3l3v4nt passwrod!')
    checker.check('this')  # will fail, however.

    # also fails, since the token matches the provided word dictionary
    checker.check('known one', dictionary=['known one', 'something else'])

    # also fails, since it's an anagram of the username
    checker.check('silent', username='listen')

You can also just calculate the entropy directly, if you want::

    from nisteag.entropy import EntropyCalculator


    calculator = EntropyCalculator()
    calculator.calculate('abcd')  # returns 10.0


Command-line
------------

You can also check the entropy of a password from the command-line::

    $ check-entropy abcd
    10.0

    $ check-entropy  # will pick the password via user input

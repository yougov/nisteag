Overview
========

This package was built with the intention of implementing most of the
recommendations in NIST Special Publication 800-63-2, titled
"Electronic Authentication Guideline". This is the link for the document:
http://dx.doi.org/10.6028/NIST.SP.800-63-2

The main reason behind this implementation is to cover the need to check if
passwords or pass-phrases meet minimum requirements in the system that uses it;
Since "strong password" is mostly used in a subjective manner, I felt the need
of a more research-based way of determining how strong or weak a password is.
And this publication by NIST seemed to be the best resource available for this.

The first published version will contain checkers for levels 1 and 2 for
Memorized Secret Tokens, but the intention is to organically grow the package
and include implementation for other recommendations, and not only token
verification.

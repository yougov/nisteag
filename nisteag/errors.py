"""Core exceptions used in the package."""


class SecurityError(Exception):
    """Raised in case any security issue happens."""


class TokenError(SecurityError):
    """Base exception class for token errors."""


class WeakTokenError(TokenError):
    """Raised when the token is too weak."""


class EmptyTokenError(TokenError):
    """Raised when the token is empty."""


class DictionaryError(TokenError):
    """Raised when there's an error regarding the terms dictionary provided."""


class AnagramError(TokenError):
    """Raised when the token is an anagram of a username."""

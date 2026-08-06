#!/usr/bin/python3
"""Module that checks if a character is lowercase."""


def islower(c):
    """Check if a character is lowercase.

    Args:
        c: a single character

    Returns:
        True if c is lowercase, False otherwise
    """
    return 97 <= ord(c) <= 122

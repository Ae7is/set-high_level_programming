#!/usr/bin/python3
"""Module that removes a character at a given index from a string."""


def remove_char_at(str, n):
    """Return a copy of str with the character at index n removed.

    Args:
        str: the original string
        n: the index of the character to remove (C-style, non-negative)

    Returns:
        A new string with the character at index n removed,
        or the original string if n is out of valid range.
    """
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n + 1:]

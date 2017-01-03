#!/usr/bin/env python
"""
Contains common string-based tricks
"""


def is_all_unique(string):
    """
    Returns true if all the characters in a string are unique

    Currently case-insensitive
    """
    bit_vector = 0
    for ch in string.lower():
        char_bit_pos = ord(char) - ord('a')
        if bit_vector & (1 << char_bit_pos) != 0:
            return False
        bit_vector |= 1 << char_bit_pos
    return True

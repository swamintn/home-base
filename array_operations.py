#!/usr/local/bin/python
"""
A reminder/refresher about common python list operations
"""


def reverse(arr):
    """Reverse a list"""
    # Go from start to end with a step 1 
    return arr[::-1]


def create_2d_arr(m, n, init_element=None):
    """Create a 2-d array"""
    # m is the rows, n is the columns
    # (So n should be on the outer here)
    arr = [[init_element] * m] * n
    return arr



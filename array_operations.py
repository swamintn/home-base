#!/usr/local/bin/python
"""
A reminder/refresher about common python list operations
"""


def reverse(arr):
    """Reverse a list"""
    # Go from start to end with a step 1 
    return arr[::-1]


def create_2d_arr(rows, columns, init_element=None):
    """Create a 2-d array"""
    # rows should be the "outer" loop here
    arr = [[init_element for j in range(columns)] for i in range(rows)]
    return arr



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


def reverse_list_in_place(l):
    """Reverse a list in place"""
    # Go from start to half of list. Ok if we miss
    # middle element. Use negative indexing to reverse
    # Take care that negative indices start from -1 onwards
    for i in range(len(l) / 2):
        l[i], l[-(i+1)] = l[-(i+1)], l[i]


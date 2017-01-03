#!/usr/bin/env python
"""
Small tricks to efficiently do some mathematical operations
"""


def powers_of_2(num):
    """
    Splits a number into powers of 2
    """
    powers = []
    i = 1
    while i <= num:
        if i & num:
            powers.append(i)
        i = i << 1
    return powers


def find_power(n, p):
    """
    Computes n^p by spliting p into sum of 2s
    """
    my_res, pow_res, i = 1, n, 1
    while i <= p:
        if i & p:
            my_res = my_res * pow_res
        i = i << 1
        pow_res = pow_res * pow_res
    return my_res   


def digital_root(num):
    """
    Gets the result of adding up all the digits of num
    """
    # A well-known solution. Multiples of 9 will always sum upto 9 and so, have
    # a digital root of 9. The next 8 numbers before it will obviously have
    # digital roots 1-8. So, we only need to find how far it is from a multiple
    # of 9. A small catch here is that using modulo will give us values 0-8. So,
    # we subtract 1 from the number, find the remainder using modulo and re-add
    # 1.
    if num == 0:
        return 0
    return ((abs(num)-1) % 9) + 1


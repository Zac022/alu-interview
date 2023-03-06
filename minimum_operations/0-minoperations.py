#!/usr/bin/python3
"""
This module contains the function minOperations(n).
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to obtain n H's
    in a text file given that we can only copy all and paste.
    """
    if n <= 1:
        return 0
    i = 2
    operations = 0
    while i <= n:
        if n % i == 0:
            operations += i
            n //= i
        else:
            i += 1
    return operations


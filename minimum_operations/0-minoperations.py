
# #!/usr/bin/python3
"""
Module for minimum operations problem
"""


def minOperations(n):
    """
    Method to calculate the fewest number of operations needed to result in
    exactly n H characters in the file.
    """
    if n <= 1:
        return 0
    else:
        for i in range(2, n + 1):
            if n % i == 0:
                return minOperations(n // i) + i
        return n

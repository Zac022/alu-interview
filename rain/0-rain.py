#!/usr/bin/python3
"""
Module for computing the amount of rainwater that can be trapped on a terrain map
"""

def rain(walls):
    """
    Computes the amount of rainwater that can be trapped on a terrain map
    """
    if not walls or len(walls) < 3:
        return 0

    trapped = 0
    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]

    while left < right:
        if walls[left] < walls[right]:
            left_max = max(left_max, walls[left])
            trapped += left_max - walls[left]
            left += 1
        else:
            right_max = max(right_max, walls[right])
            trapped += right_max - walls[right]
            right -= 1

    return trapped


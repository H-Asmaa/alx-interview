#!/usr/bin/python3
"""
0x08. Making Change
"""


def makeChange(coins, total):
    """A function that determine the fewest number of coins
    needed to meet a given amount total."""
    if total <= 0:
        return 0
    coins = sorted(coins)[::-1]
    count = i = 0
    length = len(coins)
    while i < length:
        if not total:
            break
        if coins[i] <= total:
            total -= coins[i]
            count += 1
        else:
            i += 1
    if total:
        return -1
    return count

print(makeChange([65, 67, 8], 0))

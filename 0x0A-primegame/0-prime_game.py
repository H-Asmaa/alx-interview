#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def isPrime(n):
    """A function that determins if a number is prime."""
    if n == 2:
        return True
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """A function that determines the winner of the prime games."""
    ben_score = maria_score = 0
    for num in nums[:x]:
        turn = 0
        tmp_list = []
        for i in range(1, num + 1):
            tmp_list.append(i)
        for pick in tmp_list:
            if not isPrime(pick):
                continue
            turn = 1 - turn
        if turn:
            maria_score += 1
        else:
            ben_score += 1
    if maria_score > ben_score:
        return "Maria"
    elif maria_score < ben_score:
        return "Ben"
    else:
        return None

#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def isWinner(x, nums):
    """A function that determines the winner of the prime games."""
    turn = 0
    maria_score = ben_score = 0
    while nums:
        prime = None
        for num in nums:
            if num == 2:
                prime = num
                break
            if num < 2 or num % 2 == 0:
                continue
            for n in range(3, int(num**0.5) + 1, 2):
                if num % n == 0:
                    break
            prime = num
            break
        if prime is None:
            break
        nums.remove(prime)
        if turn:
            maria_score += 1
        else:
            ben_score += 1
        for n in nums[:]:
            if n % prime == 0:
                nums.remove(n)
        turn = 1 - turn
        x -= 1
    return "Maria" if maria_score > ben_score else "Ben"

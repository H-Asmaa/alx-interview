#!/usr/bin/python3
"""
0x09. Island Perimeter
"""


def island_perimeter(grid):
    """A function that calculates the island perimeter."""
    perimeter = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                count += 4
                if grid[row][col - 1]:
                    count -= 2
                if grid[row - 1][col]:
                    count -= 2
    return perimeter

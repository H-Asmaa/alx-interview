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
                perimeter += 4
                if grid[row][col - 1]:
                    perimeter -= 2
                if grid[row - 1][col]:
                    perimeter -= 2
    return perimeter

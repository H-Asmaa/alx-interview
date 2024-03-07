#!/usr/bin/python3
"""
0x09. Island Perimeter
"""


def island_perimeter(grid):
    """A function that calculates the island perimeter."""
    if isinstance(grid, list) and all(isinstance(sub, list) for sub in grid):
        if isinstance(grid, list):
            perimeter = 0
            for row in range(len(grid)):
                for col in range(len(grid[row])):
                    if grid[row][col]:
                        perimeter += 4
                        if col and grid[row][col - 1]:
                            perimeter -= 2
                        if row > 0 and grid[row - 1][col]:
                            perimeter -= 2
            return perimeter

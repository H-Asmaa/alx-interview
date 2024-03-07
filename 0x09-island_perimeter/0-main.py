#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__("0-island_perimeter").island_perimeter

if __name__ == "__main__":
    # Test case 1
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    print(island_perimeter(grid))
    print("Test case 6: Expected perimeter: 12")

    # Test case 2
    grid = [
        [0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    print(island_perimeter(grid))
    print("Test case 6: Expected perimeter: 24")

    # Test case 3
    grid = [
        [0, 0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
    print(island_perimeter(grid))
    print("Test case 6: Expected perimeter: 28")

    # Test case 4
    grid = [
        [0, 0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0],
    ]
    print(island_perimeter(grid))
    print("Test case 6: Expected perimeter: 28")

    # Test case 5
    grid = [
        [0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0],
    ]
    print(island_perimeter(grid))
    print("Test case 6: Expected perimeter: 38")

    # Test case 6
    grid1 = [[0, 1, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0]]
    print(island_perimeter(grid1))
    print("Test case 6: Expected perimeter: 16")

    # Test case 7
    grid2 = [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]
    print(island_perimeter(grid2))
    print("Test case 7: Expected perimeter: 8")

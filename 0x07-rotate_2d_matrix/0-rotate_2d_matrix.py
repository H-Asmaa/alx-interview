#!/usr/bin/python3
"""
0x07. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """A function that returns the transpose of a matrix."""
    n = len(matrix)
    length = n - 1
    line = 0
    while (n - 1):
        for i in range(line, n - 1):
            tmp = matrix[line][i]
            matrix[line][i] = matrix[length][line]
            matrix[length][line] = matrix[n - 1][length]
            matrix[n - 1][length] = matrix[i][n - 1]
            matrix[i][n - 1] = tmp
            length -= 1
        n -= 1
        length = n - 1
        line += 1

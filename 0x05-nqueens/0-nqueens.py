#!/usr/bin/python3
"""
0x05. N Queens
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)


class nQueens:
    """This is a nQueen class. Why do a class, IDK."""

    def __init__(self) -> None:
        self.colSet = set()
        self.posDig = set()
        self.negDig = set()
        self.results = []
        self.QueensPlacement = []
        self.board = [["."] * n for _ in range(n)]

    def checkInput(self, n):
        """A method that checks the validity of the input"""
        if not isinstance(n, int):
            print("N must be a number")
            exit(1)
        if n < 4:
            print("N must be at least 4")
            exit(1)
        self.backtrack(0)

    def backtrack(self, row):
        """A method that performs the backtracking algorithm"""
        if row == n:
            boardList = ["".join(row) for row in self.board]
            self.results.append(boardList)
            return
        for column in range(n):
            if (
                column in self.colSet
                or (row + column) in self.posDig
                or (row - column) in self.negDig
            ):
                continue

            self.board[row][column] = "Q"
            self.colSet.add(column)
            self.posDig.add(row + column)
            self.negDig.add(row - column)
            self.backtrack(row + 1)
            self.colSet.remove(column)
            self.posDig.remove(row + column)
            self.negDig.remove(row - column)
            self.board[row][column] = "."

    def displayResult(self, input):
        """A method that displays the results in as indexes."""
        self.QueensPlacement = []
        for result in input:
            queens = []
            for rowIndex, row in enumerate(result):
                for colIndex, elem in enumerate(row):
                    if elem == "Q":
                        queens.append([rowIndex, colIndex])
            self.QueensPlacement.append(queens)
        for queens in self.QueensPlacement:
            print(queens)


chess = nQueens()
chess.backtrack(0)
chess.displayResult(chess.results)

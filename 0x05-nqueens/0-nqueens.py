#!/usr/bin/python3
""" A solution for the N queens problem."""


import sys


def nqueens(N, m, chessboard):
    """ A method that solves the N queens problem."""
    for i in range(N):
        isController = False
        for j in chessboard:
            if (i == j[1]) or (i - j[1] == j[0] - m) or (m - i == j[0] - j[1]):
                isController = True
        if not isController:
            chessboard.append([m, i])
            if (N - 1) != m:
                nqueens(N, m + 1, chessboard)
            else:
                print(chessboard)
            del chessboard[-1]


if __name__ == "__main__":
    """main"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(int(sys.argv[1]), 0, [])

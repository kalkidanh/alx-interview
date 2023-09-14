#!/usr/bin/python3
""" Function that takes a 2D matrix and rotates it 90 degrees CW."""


def rotate_2d_matrix(matrix):
    """ Rotate the matrix 90 degrees CW."""
    length = len(matrix)
    for item in range(length // 2):
        fst, lst, tpose = item, length - 1 - item, 0
        for i in range(fst, lst):
            start = matrix[fst][i]
            matrix[fst][i] = matrix[lst - tpose][fst]
            matrix[lst - tpose][fst] = matrix[lst][lst - tpose]
            matrix[lst][lst - tpose] = matrix[i][lst]
            matrix[i][lst] = start
            tpose += 1

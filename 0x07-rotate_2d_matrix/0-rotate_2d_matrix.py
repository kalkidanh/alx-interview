#!/usr/bin/python3
""" Function that takes a 2D matrix and rotates it 90 degrees CW."""


def rotate_2d_matrix(matrix):
    """ Rotate the matrix 90 degrees CW."""
    length = len(matrix)

    """ Transposes the 2D  matrix."""
    for i in range(length):
        for j in range(i, length):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        """ Reverses each row."""
        for i in range(length):
            matrix[i] = matrix[i][::-1]

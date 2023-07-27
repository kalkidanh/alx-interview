#!/usr/bin/python3
""" Function to draw Pascal's Triangle """


def pascal_triangle(n):
    """Function to returns Pascal's triangle of givern height
    """
    p_triangle = [[] for row in range(n)]

    for row in range(n):
        for col in range(row + 1):
            if (col < row):
                if (col == 0):
                    p_triangle[row].append(1)
                else:
                    p_triangle[row].append(p_triangle[row - 1][col] +
                                           p_triangle[row - 1][col - 1])
            elif (col == row):
                p_triangle[row].append(1)
    return p_triangle

#!/usr/bin/python3
""" Function to draw Pascal's Triangle """


def pascal_triangle(n):
    """Function to returns Pascal's triangle of givern height
    """
    pascal_triangle = [[] for row in range(n)]

    for row in range(n):
        for col in range(row + 1):
            if (col < row):
                if (col == 0):
                    pascal_triangle[row].append(1)
                else:
                    pascal_triangle[row].append(pascal_triangle[row - 1][col] +
                                                pascal_triangle[row - 1][col - 1])
            elif (col == row):
                pascal_triangle[row].append(1)
    return pascal_triangle

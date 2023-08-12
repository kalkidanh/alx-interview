#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the minimum number of operations needed to get n number of H characters in the file.

    n: The number of H characters to achieve.
    Return: The minimum number of operations needed to achieve n H characters.
    """

    if n <= 1:
        return 0
    num_operations = 0
    minoper = 2
    while minoper <= n:
        if n % minoper == 0:
            num_operations += minoper
            n = n // minoper
            minoper -= 1
        minoper += 1
    return num_operations


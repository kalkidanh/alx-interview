#!/usr/bin/python3
""" Given a pile of coins, find the lowest combinations that make a sum."""


def makeChange(coins, total):
    """ Determine the fewest number of coins that add to a given total."""
    if total < 1:
        return 0

    minCoins = 0
    coins.sort()
    coins.reverse()

    for i in coins:
        change = int(total / i)
        total -= change * i
        minCoins += change
        if total == 0:
            return minCoins

    if total != 0:
        return -1

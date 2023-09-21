#!/usr/bin/python3
""" Given a pile of coins, find the fewest combinations that make a sum."""


def makeChange(coins, total):
    """ Determine the fewest number of coins that add to a given total."""
    if total <= 0:
        return 0
    min_coin = [0] + [float("inf")] * (total)
    for coin in coins:
        for i in range(coin, total + 1):
            min_coin[i] = min(min_coin[i], min_coin[i - coin] + 1)
    return min_coin[-1] if min_coin[-1] != float("inf") else -1

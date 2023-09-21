#!/usr/bin/python3
""" Given a pile of coins, determine the fewest possible combinations that make a sum."""

def makeChange(coins, total):
    """ Determine the fewest number of coins that add to a given total."""
    if total <= 0:
        return 0
    if total not in coins:
        return -1
    table = [0] * (total + 1)

    for i in range(1, total + 1):
        min_coins = float('inf')
        for coin in coins:
            if i - coin >= 0:
                min_coins = min(min_coins, table[i - coin] + 1)
                table[i] = min_coins
                return table[total]

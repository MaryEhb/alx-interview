#!/usr/bin/python3
"""
0. Change comes from within
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
    If total is 0 or less, return 0
    If total cannot be met by any number of coins you have, return -1
    """
    if not coins or len(coins) == 0:
        return -1
    if total <= 0:
        return 0

    inx_del = 0
    coins.sort(reverse=True)

    while inx_del != len(coins):
        count = 0
        for coin in coins[inx_del:]:
            while coin <= total:
                total -= coin
                count += 1
            if total == 0:
                return count

        inx_del += 1
    return -1

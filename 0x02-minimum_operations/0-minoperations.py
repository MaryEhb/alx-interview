#!/usr/bin/python3
'''0. Minimum Operations'''


def minOperations(n):
    '''In a text file, there is a single character H. Your text editor can
    execute only two operations in this file: Copy All and Paste. Given a
    number n, write a method that calculates the fewest number of
    operations needed to result in exactly n H characters in the file.'''

    if n <= 1:
        return 0
    if n % 3 == 0:
        return minOperations(n / 3) + 3
    if n % 2 == 0:
        return minOperations(n / 2) + 2
    return n

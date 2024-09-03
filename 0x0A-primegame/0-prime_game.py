#!/usr/bin/python3
"""0. Prime Game
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from
the set. The player that cannot make a move loses the game.
"""


def calcPrime(n):
    """returns list of primes to the given number included"""
    primList = []

    for num in range(2, n + 1):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if (num % i == 0):
                prime = False
                break
        if prime:
            primList.append(num)
    return primList


primesList = calcPrime(1000)


def isWinner(x, nums):
    """
    function calculate winner
    where x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    You cannot import any packages in this task
    """
    condition = (not x or x < 1 or not nums
                 or not isinstance(nums, list) or not len(nums))
    if condition:
        return None

    score = 0
    for i in range(x):
        n = nums[i]
        while n > 1:
            if n in primesList:
                if (primesList.index(n) + 1) % 2:
                    score += 1
                else:
                    score -= 1
                break
            n -= 1
        if n == 1:
            score += 1

    if score > 0:
        return 'Ben'
    if score < 0:
        return 'Maria'
    return None

#!/usr/bin/python3
"""0. Prime Game
Maria and Ben are playing a game. Given a set of consecutive integers
starting from 1 up to and including n, they take turns choosing a prime
number from the set and removing that number and its multiples from
the set. The player that cannot make a move loses the game.
"""


def calcPrime(n):
    """Returns a list of primes up to and including n."""
    primList = []
    for num in range(2, n + 1):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            primList.append(num)
    return primList


def primes_in_range(primesList, n):
    """Return a list of primes up to and including n."""
    return [p for p in primesList if p <= n]


def isWinner(x, nums):
    """
    Function to calculate the winner of the prime game.
    x: the number of rounds.
    nums: list of n values for each round.
    Return: name of the player that won the most rounds.
    """
    if x < 1 or not nums or len(nums) != x:
        return None

    primesList = calcPrime(1000)
    mariaWins = 0
    benWins = 0

    for n in nums:
        primesSet = primes_in_range(primesList, n)
        if not primesSet:
            benWins += 1
            continue

        isMariaTurn = True

        while primesSet:
            smallestPrime = primesSet.pop(0)
            primesSet = [p for p in primesSet if p % smallestPrime != 0]
            isMariaTurn = not isMariaTurn

        if isMariaTurn:
            benWins += 1
        else:
            mariaWins += 1

    if mariaWins > benWins:
        return "Maria"
    elif benWins > mariaWins:
        return "Ben"
    else:
        return None

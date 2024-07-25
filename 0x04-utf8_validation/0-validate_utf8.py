#!/usr/bin/python3
"""0. UTF-8 Validation"""


def validUTF8(data):
    """method that determines if a given data set represents
       a valid UTF-8 encoding"""

    def countOnes(n):
        count = 0
        for i in range(7, -1, -1):
            if n & (1 << i):
                count += 1
            else:
                break
        return count

    bytes_count = 0
    for i in data:
        if bytes_count == 0:
            bytes_count = countOnes(i)
            if bytes_count > 4 or bytes_count == 1:
                return False
        else:
            if countOnes(i) != 1:
                return False
            bytes_count -= 1
    return True

#!/usr/bin/python3
"""0. UTF-8 Validation"""


def validUTF8(data):
    """method that determines if a given data set represents
       a valid UTF-8 encoding"""
    for i in range(len(data)):
        if data[i] > 255 or data[i] < 0:
            return False
    return True

#!/usr/bin/python3
"""0. Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise"""
    n = len(matrix)
    rotated_matrix = []

    for i in range(n):
        temp = []
        for j in range(n - 1, -1, -1):
            temp.append(matrix[j][i])
        rotated_matrix.append(temp)

    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated_matrix[i][j]

#!/bin/python3
'''0x00. Pascal's Triangle'''

def pascal_triangle(n):
    '''
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    '''
    
    triangle = []
    
    if n > 0:
        for i in range(0, n):
            row = []
            for j in range (0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(triangle[i-1][j-1] + triangle[i-1][j])
            triangle.append(row)

    return triangle

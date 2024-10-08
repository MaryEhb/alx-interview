#!/usr/bin/python3
"""0. Island Perimeter"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    grid is a list of list of integers:
        - 0 represents water
        - 1 represents land
        - Each cell is square, with a side length of 1
        - Cells are connected horizontally/vertically (not diagonally).
        - grid is rectangular, with its width and height not exceeding 100
        - The grid is completely surrounded by water
        - There is only one island (or nothing).
        - The island doesn’t have “lakes” (water inside that isn’t
          connected to the water surrounding the island).
    """

    perimeter = 0
    width = len(grid[0])
    height = len(grid)

    for j in range(0, width):
        for i in range(0, height):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i + 1 == height or grid[i + 1][j] == 0:
                    perimeter += 1
                if j + 1 == width or grid[i][j + 1] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
    return perimeter

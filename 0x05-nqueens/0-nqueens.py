#!/usr/bin/python3
"""0. N queens"""
import sys


def nqueens(board_size, current_row, board):
    """Recursive function to solve the N-Queens problem."""
    for current_col in range(board_size):
        conflict = False
        for queen in board:
            queen_row, queen_col = queen
            if current_col == queen_col:
                conflict = True
                break
            if current_row - current_col == queen_row - queen_col:
                conflict = True
                break
            if current_col - queen_col == queen_row - current_row:
                conflict = True
                break
        if not conflict:
            board.append([current_row, current_col])
            if current_row != board_size - 1:
                nqueens(board_size, current_row + 1, board)
            else:
                print(board)
            board.pop()


def main():
    """main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n_str = sys.argv[1]
    if not n_str.isdigit():
        print('N must be a number')
        sys.exit(1)

    n = int(n_str)

    if not isinstance(n, int) or n < 4:
        print("N must be an integer and at least 4")
        sys.exit(1)

    nqueens(n, 0, [])


if __name__ == "__main__":
    main()

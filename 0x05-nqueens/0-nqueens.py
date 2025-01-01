#!/usr/bin/python3
"""N Queens puzzle solver - place N non-attacking queens on an NxN chessboard"""

import sys


def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    
    Args:
        board: 2D list representing the board
        row: Row to check
        col: Column to check
        n: Size of the board
        
    Returns:
        bool: True if safe to place queen, False otherwise
    """
    # Check this row on left side
    for j in range(col):
        if board[row][j] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                   range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1),
                   range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n, solutions):
    """
    Solve N Queens problem using backtracking
    
    Args:
        board: 2D list representing the board
        col: Current column
        n: Size of the board
        solutions: List to store solutions
        
    Returns:
        bool: True if solution found, False otherwise
    """
    if col >= n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, n, solutions) or res
            board[i][col] = 0

    return res


def print_solutions(n):
    """
    Initialize the board and print all solutions
    
    Args:
        n: Size of the board
    """
    # Initialize board
    board = [[0 for x in range(n)] for y in range(n)]
    solutions = []

    solve_nqueens(board, 0, n, solutions)

    # Print solutions
    for solution in solutions:
        print(solution)


def main():
    """Main function to handle input and start solving"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solutions(n)


if __name__ == "__main__":
    main()
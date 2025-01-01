#!/usr/bin/python3
""" this is the n-queen chess solution module"""
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed at board[row][col]."""
    # Check column leftwards
    if any(board[row][i] == 1 for i in range(col)):
        return False
    # Check upper diagonal leftwards
    if any(board[i][j] == 1 for i, j in zip(range(row, -1, -1),
                                            range(col, -1, -1))):
        return False
    # Check lower diagonal leftwards
    if any(board[i][j] == 1 for i, j in zip(range(row, n,  1),
                                            range(col, -1, -1))):
        return False
    return True


def solve_nq_util(board, col, n, solutions):
    if col == n:
        sol = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
        solutions.append(sol)
        return True
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            if solve_nq_util(board, col + 1, n, solutions):
                return True

            board[i][col] = 0
    return False


def solve_nq(n):
    """Solve the N-Queens problem for a given size."""
    if not isinstance(n, int):
        raise ValueError("N must be an integer.")
    if n < 4:
        raise ValueError("N must be at least  4.")
    board = [[0]*n for _ in range(n)]
    solutions = []
    solve_nq_util(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be an integer.")
        sys.exit(1)

    solutions = solve_nq(n)
    for solution in solutions:
        print([[i, j] for i, j in solution])

# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

import pprint
def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """
    # Initialize the quuens array that will be rteurned
    if n <= 0:
        return None

    queens = []

    if place_queens(0, queens, n):
        return queens
    else:
        return None


def place_queens(col, q_arr, n):
    """
    A helper function
    This is a recursive function
    """
    if col >= n:
        return True

    # Iterate through the rows and backtrack
    row = 0
    while row < n:
        q_arr.append([row, col])
        if is_safe(row, col, q_arr) and place_queens(col+1, q_arr, n):
            return True

        # backtrack
        q_arr.pop()
        row += 1

    return False

def is_safe(row, col, q_arr):
    """
    Helper function to check if the queen on the board is safe or not
    2 conditions
    1) No 2 queens should be placed on the same row
    2) No 2 queens should be placed on the same diagonal( slope should be 1)
    """
    for i in range(len(q_arr) - 1):
        r = q_arr[i][0]
        c = q_arr[i][1]

        if r == row:
            return False

        if abs(r - row) == abs(c - col):
            return False


    return True

pprint.pprint(solveNQueens(4))

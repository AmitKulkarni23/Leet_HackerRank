# Given a sudoku board, solve the problem
# Implement Sudoku solver

import collections
def solveSudoku(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # Credits -> https://leetcode.com/problems/sudoku-solver/solution/

    def get_box_index(row, col):
        return (row // 3) * 3 + col // 3

    def can_place_this_num(num, row, col):
        return not(num in rows[row] or num in cols[col] or num in boxes[get_box_index(row, col)])


    def place_number(num, row, col):
        # Increment the count
        rows[row][num] += 1
        cols[col][num] += 1
        boxes[get_box_index(row, col)][num] += 1
        board[row][col] = str(num)

    def remove_number(num, row, col):
        del rows[row][num]
        del cols[col][num]
        del boxes[get_box_index(row, col)][num]
        board[row][col] = "."

    def place_next_numbers(row, col):
        if row == N - 1 and col == N - 1:
            # We are done
            nonlocal sudoku_solved
            sudoku_solved = True
        else:
            if col == N - 1:
                # We have reached the last box in this row
                # We should move to the next row
                backtrack(row+1, 0)
            else:
                # We should move to the next column
                backtrack(row, col + 1)

    def backtrack(row = 0, col = 0):
        # If cell is empty
        if board[row][col] == ".":
            for num in range(1, 10):
                if can_place_this_num(num, row, col):
                    place_number(num, row, col)
                    place_next_numbers(row, col)

                    if not sudoku_solved:
                        remove_number(num, row, col)
        else:
            # This spot is occupied
            place_next_numbers(row, col)

    n = 3
    N = n * n
    rows = [collections.defaultdict(int) for _ in range(N)]
    cols = [collections.defaultdict(int) for _ in range(N)]
    boxes = [collections.defaultdict(int) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] != ".":
                num = int(board[i][j])
                place_number(num, i, j)


    # Now back track
    sudoku_solved = False
    backtrack()

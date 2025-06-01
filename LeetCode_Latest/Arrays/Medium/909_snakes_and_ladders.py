# https://leetcode.com/problems/snakes-and-ladders/description/

from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        def get_position(square):
            """
            Convert square number to (row, col) on the board
            """
            row_from_bottom = (square - 1) // n
            col_in_row = (square - 1) % n

            row = n - 1 - row_from_bottom  # because board starts from bottom

            if row_from_bottom % 2 == 0:  # left to right
                col = col_in_row
            else:  # right to left
                col = n - 1 - col_in_row
            
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (square_number, moves)

        while queue:
            square, moves = queue.popleft()
            for i in range(1, 7):  # roll dice
                next_square = square + i
                if next_square > n * n:
                    continue
                r, c = get_position(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]  # jump to snake/ladder

                if next_square == n * n:
                    return moves + 1

                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1  # not reachable
    
    # Time - O(n ^ 2) - there are at most n ^ 2 nodes - visit all nodes
    # Space - O(n ^ 2) - for visited

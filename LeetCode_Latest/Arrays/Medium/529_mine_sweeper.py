# https://leetcode.com/problems/minesweeper/description/

class Solution:
    def updateBoard(self, board, click):
        row, col = click
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        
        if board[row][col] == "E":
            adjacent_mines_count = self.adjacent_mines_count(board, row, col)
            if adjacent_mines_count > 0:
                board[row][col] = str(adjacent_mines_count)
            else:
                self.update_positions(board, row, col)
        
        return board

    
    def adjacent_mines_count(self, board, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(board) and 0 <= c < len(board[0]):
                if board[r][c] == "M":
                    count += 1
        return count
    
    def update_positions(self, board, row, col):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]

        board[row][col] = "B"

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == "E":
                count = self.adjacent_mines_count(board, r, c)
                if count > 0:
                    board[r][c] = str(count)
                else:
                    self.update_positions(board, r, c)

                

        
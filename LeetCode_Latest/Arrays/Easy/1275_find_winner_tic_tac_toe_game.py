# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/description/?

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        anti_diag = 0

        # Time - O(1)
        # Space - O(1)

        for i, (r, c) in enumerate(moves):
            player = 1 if i % 2 == 0 else -1  # A=+1, B=-1

            rows[r] += player
            cols[c] += player
            if r == c:
                # This is the diagonal
                diag += player
            if r + c == 2:
                # This is the anti-diagonal (the other diagonal)
                anti_diag += player

            # Check win
            if abs(rows[r]) == 3 or abs(cols[c]) == 3 or abs(diag) == 3 or abs(anti_diag) == 3:
                return "A" if player == 1 else "B"

        return "Draw" if len(moves) == 9 else "Pending"


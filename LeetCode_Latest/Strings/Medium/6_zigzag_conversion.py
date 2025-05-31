# https://leetcode.com/problems/zigzag-conversion/description/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Moving down from row 0 to row numRows - 1
        # Then up from row numRows - 2 back to row 1
        # Use an array of strings, one for each row.
        # Iterate through the characters of s.
        # Track:
            # Current row
            # Direction (down or up)
        # Append each character to the correct row based on the current direction.
        # Finally, concatenate all rows.

        if numRows == 1 or numRows >= len(s):
            return s

        # Initialize an array to hold each row
        rows = [''] * numRows
        curr_row = 0
        going_down = False

        for char in s:
            rows[curr_row] += char

            # Change direction if we hit the top or bottom
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down

            # Move up or down
            curr_row += 1 if going_down else -1

        return ''.join(rows)

        # Time - O(n) - iterate through the whole string
        # Space - O(n) - rows array


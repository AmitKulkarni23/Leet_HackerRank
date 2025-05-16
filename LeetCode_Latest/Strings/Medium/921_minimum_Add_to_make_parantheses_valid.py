# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # `balance` tracks the number of unmatched '(' we've seen so far.
        balance = 0
        # `insertions` counts the extra parentheses we must insert.
        insertions = 0

        # Scan through each character in the string exactly once
        for ch in s:
            if ch == '(':
                # We’ve got an extra '(', so increment our open-count
                balance += 1
            else:  # ch == ')'
                if balance > 0:
                    # We have a matching '(' to pair with this ')'
                    balance -= 1
                else:
                    # No '(' to match this ')', so we must insert one '(', i.e. one move
                    insertions += 1

        # After the scan, any remaining `balance` unmatched '(' each need a ')'
        insertions += balance

        return insertions

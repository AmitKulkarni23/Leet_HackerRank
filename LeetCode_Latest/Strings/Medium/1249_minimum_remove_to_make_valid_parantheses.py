# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/

# Thought Process:
# 1. There are same number of opening and closing parentheses in a valid string.
# Scanning from left to right there should be no closing parentheses before opening parentheses.
# We use a stack here
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Time Complexity - O(n) where n is the length of the string
        # Space Complexity - O(n) for the stack
        # Convert the string to a list of characters so we can mark removals in-place
        chars = list(s)
        # Stack to keep track of indices of unmatched '(' characters
        open_paren_stack = []

        # First pass: scan left to right and remove invalid ')'
        for i, ch in enumerate(chars):
            if ch == '(':
                # Push the index of every '(' onto the stack
                open_paren_stack.append(i)
            elif ch == ')':
                if open_paren_stack:
                    # There is a matching '(', so pop it and keep this ')'
                    open_paren_stack.pop()
                else:
                    # No matching '(', so this ')' is invalid—mark it for removal
                    chars[i] = ''

            # If it's a lowercase letter, we just leave it alone

        # Second pass: any '(' indices left in the stack didn't get matched
        # Remove them by marking their positions empty
        while open_paren_stack:
            idx_to_remove = open_paren_stack.pop()
            chars[idx_to_remove] = ''

        # Join the list back into a string, skipping all marked positions
        return ''.join(chars)

        
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

class Solution:
    def maxDepth(self, s: str) -> int:
        # Time - O(n); single pass
        # Space - O(1)
        max_depth = 0
        current_depth = 0

        for ch in s:
            if ch == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif ch == ')':
                current_depth -= 1

        return max_depth
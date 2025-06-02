# https://leetcode.com/problems/a-number-after-a-double-reversal/description/

class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # Helper function to reverse a number
        def reverse(n: int) -> int:
            # Convert to string, reverse, and convert back to int
            return int(str(n)[::-1])
        
        # First reverse
        reversed1 = reverse(num)
        # Second reverse
        reversed2 = reverse(reversed1)

        # Check if double reversed is same as original
        return reversed2 == num
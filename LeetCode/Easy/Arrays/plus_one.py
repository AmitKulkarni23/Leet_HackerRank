"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # inspired by one of the solution sin the discussion forum for this problem
        ans = 0
        for i in range(len(digits)):
            ans = ans * 10 + digits[i]

        return [int(x) for x in str(ans + 1)]

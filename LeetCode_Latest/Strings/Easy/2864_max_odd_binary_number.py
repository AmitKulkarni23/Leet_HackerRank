# https://leetcode.com/problems/maximum-odd-binary-number/description/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Time - O(n) for count
        
        ones = s.count('1')
        zeros = len(s) - ones

        # Put (ones - 1) 1's first, then all 0's, then one final 1 to make the number odd
        return '1' * (ones - 1) + '0' * zeros + '1'
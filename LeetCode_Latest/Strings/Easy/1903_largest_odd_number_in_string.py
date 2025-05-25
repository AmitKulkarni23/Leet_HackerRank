# https://leetcode.com/problems/largest-odd-number-in-string/description/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Any substring that ends at an odd digit is an odd number (as long as it starts at the beginning of num).

        # We just scan from right to left and find the rightmost odd digit — because if the entire number up to that point ends in an odd digit, it’s an odd number (and longer numbers are larger).
        
        # Scan from the end toward the start
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[:i + 1]
        return ""
        


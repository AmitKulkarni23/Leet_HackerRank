# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # Time - O(n)
        max_result = ""

        for i in range(len(number)):
            if number[i] == digit:
                candidate = number[:i] + number[i+1:]
                if candidate > max_result:
                    max_result = candidate

        return max_result
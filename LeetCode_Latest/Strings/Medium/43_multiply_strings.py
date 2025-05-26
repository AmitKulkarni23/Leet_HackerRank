# https://leetcode.com/problems/multiply-strings/description/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # We will follow basic school way of multiplying numbers 
        # O (m * n) -> where m and n are the length of the strings
        # O(m + n) -> result array

        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)

        # Maximum possible number of digits = m + n
        result = [0] * (m + n)

        # Multiply every digit in num1 with every digit in num2
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                mul = digit1 * digit2
                p1 = i + j      # carry goes here
                p2 = i + j + 1  # current digit goes here

                sum_ = mul + result[p2]
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10

        # Skip leading zeros
        result_str = ''.join(map(str, result)).lstrip('0')
        return result_str
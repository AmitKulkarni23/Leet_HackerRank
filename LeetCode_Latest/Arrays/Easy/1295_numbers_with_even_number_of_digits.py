# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0

        for item in nums:
            iteration_count = 0
            while item:
                item = item // 10
                iteration_count += 1
            if iteration_count % 2 == 0:
                result += 1

        return result
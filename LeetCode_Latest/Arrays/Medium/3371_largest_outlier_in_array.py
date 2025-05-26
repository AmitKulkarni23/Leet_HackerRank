# https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/description/

from collections import Counter


class Solution:
    def getLargestOutlier(self, nums) -> int:
        # Time - O(n) - iterating through the whole array
        # Space - O(n) for the Counter dictionary

        # total_sum = sum(nums)
        # x = sum of special numbers → one of the elements in the array
        # y = the outlier → the number we're trying to find

        # total_sum = x (sum) + y (outlier) + sum(special numbers) = x + y + x = 2x + y
        # y = total_sum - 2 * x
        # Compute y = total_sum - 2 * x
        # If y also exists in the array (at a different index), then it's a valid outlier
        # Track the maximum such y


        total = sum(nums)
        counter = Counter(nums)
        max_outlier = float('-inf')

        for x in nums:
            y = total - 2 * x
            if y in counter:
                # Ensure x and y are not the same index
                if x != y or counter[y] > 1:
                    max_outlier = max(max_outlier, y)

        return max_outlier
# https://leetcode.com/problems/monotonic-array/description/

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = decreasing = True
        # Initialize two flags
        # If either flag remains true at the end, then array is monotonic

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                decreasing = False
            if nums[i] < nums[i + 1]:
                increasing = False
        
        return increasing or decreasing

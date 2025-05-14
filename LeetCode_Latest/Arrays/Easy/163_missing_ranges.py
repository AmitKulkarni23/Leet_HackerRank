# https://leetcode.com/problems/missing-ranges/description/

class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):
        result = []
        
        if len(nums) == 0:
            return [[lower, upper]]
        
        # Check for the first element in the array
        if lower < nums[0]:
            result.append([lower, nums[0] - 1])
        
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] <= 1:
                continue
            result.append([nums[i] + 1, nums[i + 1] - 1])
        
        
        # Check for the last element in the array
        if upper > nums[-1]:
            result.append([nums[-1] + 1, upper])

        return result
        




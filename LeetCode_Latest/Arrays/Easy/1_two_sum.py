# https://leetcode.com/problems/two-sum/

class Solution:
    # Time: On(n) - iteration through the input list
    # Space: On(n) - for complement dictionary
    def twoSum(self, nums, target):
        final_dict = {}
        
        for idx, item in enumerate(nums):
            complement = target - item
            
            if complement in final_dict:
                return [final_dict[complement], idx]
            
            final_dict[item] = idx
        
sol_obj = Solution()
print(sol_obj.twoSum([2,7,11,15], 9))
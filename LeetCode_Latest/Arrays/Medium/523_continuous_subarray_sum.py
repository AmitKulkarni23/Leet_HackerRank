# https://leetcode.com/problems/continuous-subarray-sum/description/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Below is O(n^2) and it exceeds time
        # if len(nums) < 2:
        #     return False
        
        # for i in range(len(nums) - 1):
        #     result = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         result += nums[j]

        #         if (result / k) % 1 == 0:
        #             # Is an integer
        #             return True
        
        # return False

        ############
        # O(n) solution 
        remainder_index_map = {0: -1}  # Base case to handle sum from index 0
        prefix_sum = 0

        for idx, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder in remainder_index_map:
                # To ensure the case that length of subarray is 2
                if idx - remainder_index_map[remainder] >= 2:
                    return True
            else:
                remainder_index_map[remainder] = idx

        return False

        ############
            
  
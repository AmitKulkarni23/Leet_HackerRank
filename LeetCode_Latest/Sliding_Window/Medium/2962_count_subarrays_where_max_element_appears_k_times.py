# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

class Solution:
    from collections import Counter
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        Global Max Element:
        The only element that matters is the maximum element in nums. Let's call it max_val.

        Valid Subarray:
        A subarray is valid if:
            - The maximum in that subarray is max_val, AND
            - max_val appears at least k times in that subarray.

        So, we only care about ranges where:
        All elements are ≤ max_val

        Count of max_val in that range is ≥ k

        Note: Loop through the array and keep a sliding window [left, right] such that: The elements are all ≤ max_val

        Keep track of how many times max_val appears in the window
        For each valid window where count_max ≥ k, all subarrays ending at right and starting from any index i in [left, right] where count_max from i to right is still ≥ k are valid.
        '''
        max_val = max(nums)
        n = len(nums)
        left = 0
        count = 0
        max_freq = 0
        result = 0

        for right in range(n):
            if nums[right] == max_val:
                count += 1

            # Shrink window until the count of max_val is less than k
            while count >= k:
                if nums[left] == max_val:
                    count -= 1
                left += 1
            
            # All subarrays ending at `right` and starting before `left` are valid
            # counts how many subarrays end at right and are valid
            result += left

        return result

        # Time - O(n) - 1 pass
        # Space - O(1)

        
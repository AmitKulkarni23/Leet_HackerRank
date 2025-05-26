# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/

from collections import defaultdict
class Solution:
    def maxOperations(self, nums, k: int) -> int:
        count = 0
        freq = defaultdict(int)

        for num in nums:
            complement = k - num
            if freq[complement] > 0:
                # If complement exists in the map, 
                # simply remove it from the map
                freq[complement] -= 1
                count += 1
            else:
                # If complement doesn't exists in the map, add the current number to the map
                freq[num] += 1

        return count
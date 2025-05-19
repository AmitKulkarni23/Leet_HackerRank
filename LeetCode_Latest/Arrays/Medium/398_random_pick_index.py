# https://leetcode.com/problems/random-pick-index/description/


from collections import defaultdict
import random
from typing import List


"""
The solution below precomputes the indices in a Hashmap and returns the result
"""
class Solution:
    # Time: O(n)
    # Space: O(n)
    def __init__(self, nums: List[int]):
        self.index_map = defaultdict(list)
        for i, num in enumerate(nums):
            self.index_map[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.index_map[target])
    

# Reservoir Sampling
# Note: The above hashmap suolution takes O(n) space, but we can do it in O(1) space
# Imagine you're given a very large data stream or a huge list of unknown or massive size, and you want to:
# Pick one or more items randomly with equal probability, but you can't store the entire data in memory.
# This is where Reservoir Sampling comes in.

class Solution:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        result = -1
        count = 0

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # The below line of code is the key to reservoir sampling
                # It ensures that each occurrence of the target has an equal chance of being selected
                # The probability of selecting the i-th occurrence is 1/count
                if random.randint(1, count) == 1:
                    result = i

        return result


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# https://leetcode.com/problems/diagonal-traverse-ii/

from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag_dict = defaultdict(list)

        for i in range(len(nums)):
            # The rows are jagged; Meaning, you can't use m * n as the martix's dimension
            for j in range(len(nums[i])):
                # Collect rows top-down
                diag_dict[i + j].append(nums[i][j])
            
        result = []
        for key in sorted(diag_dict.keys()):
            result.extend(reversed(diag_dict[key]))  # reverse each diagonal
        return result
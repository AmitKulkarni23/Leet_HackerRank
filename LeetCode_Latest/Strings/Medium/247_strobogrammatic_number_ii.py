# https://leetcode.com/problems/strobogrammatic-number-ii/description/

from collections import deque
from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        pairs = [('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')]

        if n % 2 == 0:
            queue = deque([""])
        else:
            queue = deque(["0", "1", "8"])
        
        curr_len = 1 if n % 2 else 0

        while curr_len < n:
            next_level = deque()
            for num in queue:
                for a, b in pairs:
                    if curr_len + 2 == n and a == '0':
                        continue  # avoid leading zero

                    # Why a + num + b works and not something like a + b + num or num + a + b; a + num + b preserves the symmetry -> Wraps valid mirror pair around existing structure
                    next_level.append(a + num + b)
            queue = next_level
            curr_len += 2
        
        return list(queue)

        # Time Complexity:
        # Valid digit pairs:
        # ('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6') → 5 options
        # Each recursive step builds numbers of length k from numbers of length k - 2 by inserting one of the 5 pairs on both ends.

        # Core Insight:
        # At each recursive level (moving outward), we have up to 5 choices to wrap around each of the shorter strings.
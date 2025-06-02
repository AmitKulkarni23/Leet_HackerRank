# https://leetcode.com/problems/assign-cookies/description/

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Time - O(m log m + n log n)
        # Space - O(1)
        
        g.sort()
        s.sort()
        
        i = 0
        j = 0
        
        while i < len(g) and j < len(s):
            # Note: You can give the child at most one cookie only
            # Even if you had remaining cookies you can't give it to the child
            if s[j] >= g[i]:
                i += 1
            j += 1
        
        return i
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        max_candies = max(candies)

        for candy in candies:
            if candy + extraCandies >= max_candies:
                output.append(True)
            else:
                output.append(False)
        
        return output
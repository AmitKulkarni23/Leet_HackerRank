# https://leetcode.com/problems/friends-of-appropriate-ages/description/

from collections import Counter
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = Counter(ages) # O(n) time and O(n) space
        total_requests = 0
        unique_ages = list(count.keys())

        # Time - O(m ^ 2) where m is the unique number of ages
        for ageA in unique_ages:
            for ageB in unique_ages:
                if ageB <= 0.5 * ageA + 7:
                    continue
                if ageB > ageA:
                    continue
                if ageB > 100 and ageA < 100:
                    continue

                # Computes total number of friend requests from all people of age ageA to all people of age ageB.
                requests = count[ageA] * count[ageB]

                
                if ageA == ageB:
                    requests -= count[ageA]

                total_requests += requests

        return total_requests
  
  
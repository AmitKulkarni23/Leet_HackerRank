# https://leetcode.com/problems/buildings-with-an-ocean-view/description/

class Solution:
    def findBuildings(self, heights):
        # Time: O(N) - run through the whole loop and also reverse takes O(N)
        # Space: O(1)

        result = [len(heights) - 1] # Last building always has an ocean view

        # Capture the amx seen until now
        max_seen = heights[-1]

        for idx in range(len(heights) - 2, -1, -1):
            if heights[idx] > max_seen:
                result.append(idx)
                max_seen = heights[idx]
        
        result.reverse()
        return result


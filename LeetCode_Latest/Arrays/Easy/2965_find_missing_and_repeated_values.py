# https://leetcode.com/problems/find-missing-and-repeated-values/description/

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # Time: O(n ^ 2)
        # Space: O(n ^ 2)
        counter_dict = {}
        for i in range(1, (len(grid) * len(grid)) + 1):
            counter_dict[i] = 0
        
        for item in grid:
            for num in item:
                counter_dict[num] = counter_dict.get(num, 0) + 1
        

        for item in counter_dict:
            if counter_dict[item] == 2:
                a = item
            
            if counter_dict[item] == 0:
                b = item
        
        return [a, b]


# Time Complexity: O(n^2) - we need to iterate through the grid to count occurrences of each number
# Space Complexity: O(n^2) - we are storing counts of numbers in a dictionary
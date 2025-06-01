# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort by end time
        intervals.sort(key=lambda x: x[1])
        
        # Step 2: Greedy selection of non-overlapping intervals
        end = float('-inf')
        count = 0

        for start, finish in intervals:
            if start >= end:
                end = finish  # no overlap, we keep it
            else:
                count += 1  # overlap, we remove this one

        return count

        # Time O(n log n)
        # Input: [[1,2],[2,3],[3,4],[1,3]]
        # Sorted: [[1,2],[1,3],[2,3],[3,4]]
        # Keep [1,2], skip [1,3] (overlaps), keep [2,3], keep [3,4] → Remove 1
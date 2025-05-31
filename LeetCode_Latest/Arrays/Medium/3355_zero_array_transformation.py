# https://leetcode.com/problems/zero-array-transformation-i/description/

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        # What is the diff array?
        # tracks how many times a position is "eligible to be decremented" by 1 — i.e., how many queries cover this index.
        diff = [0] * (n + 1)

        for l, r in queries:
            diff[l] += 1
            # Why r + 1? -> r + 1 indicates that such an index is not convered by either l, r
            diff[r + 1] -= 1

        # What is freq array?
        # the total number of queries covering it must be ≥ nums[i]. Otherwise, we won't be able to bring that value down to 0.

        # How many queries cover index i
        # → This tells us how many times we can decrement index i.
        # This is needed because:
        # If nums[i] = 3, we need at least 3 queries that cover i, so we can decrement i three times. If we only have 2 such queries, we can’t zero out that position.


        total_coverage = 0
        for i in range(n):
            total_coverage += diff[i] # accumulate how many times this index was covered
            if total_coverage < nums[i]: # if not enough, we can't make it zero
                return False

        return True

        # Time - O (n + q) where n -> len(nums); q -> length of queries
        # Space - O(n) - diff array and freq array
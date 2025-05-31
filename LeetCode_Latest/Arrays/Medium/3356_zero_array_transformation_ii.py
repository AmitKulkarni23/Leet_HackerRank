# https://leetcode.com/problems/zero-array-transformation-ii/description/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # Same as https://leetcode.com/problems/zero-array-transformation-i/description/
        # Submission - https://leetcode.com/problems/zero-array-transformation-i/submissions/1647148571/

        n = len(nums)
        
        def is_possible(k):
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val
            
            total_coverage = 0
            for i in range(n):
                total_coverage += diff[i] # accumulate how many times this index was covered
                if total_coverage < nums[i]: # if not enough, we can't make it zero
                    return False
            return True
        
        # Binary search
        # Why binary search? - The problem is "Find the minimum index where a condition becomes true"
        # Monotonic behavior → as k increases, the property "can make all nums[i] zero" goes from False to True and stays True.

        left, right = 0, len(queries)
        
        while left < right:
            mid = (left + right) // 2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if is_possible(left) else -1

    # Time - O(log Q * (Q + N))
    # Space - O (N)
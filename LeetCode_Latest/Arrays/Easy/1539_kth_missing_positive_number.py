# https://leetcode.com/problems/kth-missing-positive-number/description/

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # O(log n) -> Binary Search
        # O(1)

        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            # This is the main logic
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                # move right, because we haven’t skipped enough numbers yet
                left = mid + 1
            else:
                # move left, because we may have skipped too many numbers already
                right = mid - 1

        # left is the number of elements in arr before the k-th missing number
        # So the answer is left + k
        return k + left
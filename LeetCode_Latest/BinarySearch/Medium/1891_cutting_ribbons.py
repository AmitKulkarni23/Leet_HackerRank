# https://leetcode.com/problems/cutting-ribbons/


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        # This is a binary search problem
        # Key - rather searching for the maximum possible ribbon length x such that you can cut at least k ribbons of length x.
        # You're trying to maximize x, the length of each ribbon piece.

        # For a given candidate length x, check:
            # Can we cut at least k ribbons of length x from the input?

        # This check is monotonic:
        # If x is possible, then all values smaller than x are also possible.
        # If x is not possible, then all values larger than x are also impossible.

        # Time - O(n × log(max)) where n = len(ribbons) and max = max(ribbons)
        # Space - O(1)

        def can_cut(length):
            count = 0
            for ribbon in ribbons:
                count += ribbon // length
            return count >= k

        left, right = 1, max(ribbons)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_cut(mid):
                result = mid  # candidate for answer
                left = mid + 1
            else:
                right = mid - 1

        return result


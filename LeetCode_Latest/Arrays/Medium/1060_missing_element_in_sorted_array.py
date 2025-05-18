# https://leetcode.com/problems/missing-element-in-sorted-array/

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # O(n) solution
        # """
        # Linear scan over each pair nums[i], nums[i+1]:
        #   - gap = nums[i+1] - nums[i] - 1
        #   - if k <= gap: the answer is nums[i] + k
        #   - else: k -= gap and continue
        # If we exhaust all gaps, it lies beyond the last element.
        # """
        # n = len(nums)
        # for i in range(n - 1):
        #     # how many numbers are strictly between nums[i] and nums[i+1]?
        #     gap = nums[i+1] - nums[i] - 1
        #     if k <= gap:
        #         # the kᵗʰ missing in this gap is nums[i] + k
        #         return nums[i] + k
        #     k -= gap

        # # if not found in any gap, it’s beyond nums[-1]
        # return nums[-1] + k

        # O(log(n)) solution
        n = len(nums)

        # Helper: how many numbers are missing up to index i?
        def missing(i: int) -> int:
            return nums[i] - nums[0] - i

        # If k is beyond all missing before the last element
        total_missing = missing(n - 1)
        if k > total_missing:
            # We need to go past nums[-1]
            return nums[-1] + (k - total_missing)

        # Binary search for first index where missing(idx) >= k
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if missing(mid) < k:
                lo = mid + 1
            else:
                hi = mid

        # Now lo is the smallest index with missing(lo) ≥ k
        # The previous index lo-1 has missing(lo-1) < k
        prev_missing = missing(lo - 1)
        # We need (k - prev_missing) more numbers after nums[lo-1]
        return nums[lo - 1] + (k - prev_missing)
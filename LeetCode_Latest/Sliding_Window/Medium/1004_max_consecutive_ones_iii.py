# https://leetcode.com/problems/max-consecutive-ones-iii
# Same as https://leetcode.com/problems/longest-repeating-character-replacement/
# Same as https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/


class Solution:
    def longestOnes(self, nums, k: int) -> int:
        # Sliding Window
        # Expand the window to include elements while the number of zeros in the window ≤ k
        # If zeros exceed k, shrink the window from the left
        # Track the maximum window length

        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # shrink window from the left

            max_len = max(max_len, right - left + 1)

        return max_len

        # Time O(n)
        # Space O(1)
# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
# Same as https://leetcode.com/problems/max-consecutive-ones-iii
# Same as https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Intuition 
        # Pick a target value x
        # Try to increase numbers before it to become x
        # Count the cost (number of increments needed)

        # Approach
        # Sort the array
        # Use Sliding Window
            # Window - nums[left:right+1]
            # Try to make all values in that window equal to nums[right]
            # Cost = (nums[right] * window_size) - sum(window)
            # If cost > k shrink the window from the left
        # Keep track of maximum window you can afford

        nums.sort()
        left = 0
        total = 0
        max_freq = 0

        for right in range(len(nums)):
            total += nums[right]

            # Cost to make all nums[left:right+1] == nums[right]
            # Why is this the cost? - 

            # nums[right] * (window_size) is the total sum you'd get if all values were equal to nums[right]
            # sum(window) is the actual current sum
            # The difference is the number of increments needed to raise all numbers to nums[right]

            while nums[right] * (right - left + 1) - total > k:
                total -= nums[left]
                left += 1

            # Why keep track of this?
            # we track the length of the longest subarray (window) where we can make all elements equal to nums[right] with at most k increments.
            max_freq = max(max_freq, right - left + 1)

        return max_freq

        # Time - O(n log n)
        # Space - O(1)




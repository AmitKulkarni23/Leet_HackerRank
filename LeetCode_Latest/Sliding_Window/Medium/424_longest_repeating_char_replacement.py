# https://leetcode.com/problems/longest-repeating-character-replacement/

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window
        # Same as https://leetcode.com/problems/max-consecutive-ones-iii
        # Same as https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
        count = defaultdict(int)
        left = 0
        max_count = 0  # count of the most frequent character in the window
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            # Check if the window is valid
            if (right - left + 1) - max_count > k:
                # This means window is invalid
                # Shrink left
                count[s[left]] -= 1
                left += 1  # shrink the window

            max_len = max(max_len, right - left + 1)

        return max_len
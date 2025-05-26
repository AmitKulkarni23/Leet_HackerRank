# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        count = defaultdict(int)
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # Shrink the window until we have at most 2 distinct characters
            while len(count) > 2:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1  # shrink window from the left

            # Update max length of valid window
            max_len = max(max_len, right - left + 1)

        return max_len

        # Time - O(n)
        # Space - O(1)
        
# https://leetcode.com/problems/minimum-deletions-for-at-most-k-distinct-characters/description/

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        # Time Complexity - O(n) -> counting frequencies; sorting is constant time becuase we have only lowercase caharacters
        # Space - O(n)
        freq = Counter(s)
        if len(freq) <= k:
            return 0

        # Sort character frequencies in ascending order
        sorted_freqs = sorted(freq.values())
        deletions = 0
        remove_count = len(freq) - k

        for i in range(remove_count):
            deletions += sorted_freqs[i]

        return deletions
# https://leetcode.com/problems/group-shifted-strings/description/

from collections import defaultdict
class Solution:
    def groupStrings(self, strings):
        """
        Idea: Two strings belong to the same shifting sequence if the difference between adjacent characters in their strings is the same modulo 26.

        Example for the get_sgnature() method down below
        "abc" -> [1,1] (b-a=1, c-b=1)
        "bcd" -> [1,1] (c-b=1, d-c=1)
        "az" -> [25] (z-a=-1 ≡ 25 mod 26)
        """
        def get_signature(s):
            if len(s) == 1:
                return ()  # singleton string, no shift
            return tuple((ord(s[i+1]) - ord(s[i])) % 26 for i in range(len(s)-1))

        groups = defaultdict(list)
        for s in strings:
            sig = get_signature(s)
            groups[sig].append(s)

        return list(groups.values())      
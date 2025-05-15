# https://leetcode.com/problems/valid-word-abbreviation/description


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        n, m = len(word), len(abbr)

        while i < n and j < m:
            if abbr[j].isalpha():
                # letter must match exactly
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
            else:
                # parse a positive integer with no leading zeros
                if abbr[j] == '0':
                    return False  # leading zero or zero-length
                num = 0
                while j < m and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num  # skip that many chars in word

        # Both pointers must reach the end simultaneously
        return i == n and j == m
                
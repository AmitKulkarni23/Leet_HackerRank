# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Step 1: Convert letters to their corresponding alphabet positions
        digit_str = ''
        for ch in s:
            position = ord(ch) - ord('a') + 1  # 'a' ➝ 1, ..., 'z' ➝ 26
            digit_str += str(position)         # Concatenate as string, not integer

        # Step 2: Repeat the digit-sum transformation k times
        for _ in range(k):
            digit_str = str(sum(int(d) for d in digit_str))

        return int(digit_str)
        
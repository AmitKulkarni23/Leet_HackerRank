# https://leetcode.com/problems/guess-number-higher-or-lower/description

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = low + (high - low) // 2
            if guess(mid) == 0:
                return mid
            
            if guess(mid) == -1:
                high = mid - 1
            else:
                low = mid + 1
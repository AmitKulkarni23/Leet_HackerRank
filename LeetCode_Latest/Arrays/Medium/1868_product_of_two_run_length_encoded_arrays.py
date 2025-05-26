# https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/description/

from typing import List


class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        freq1 = freq2 = 0
        val1 = val2 = 0

        while i < len(encoded1) and j < len(encoded2):
            if freq1 == 0:
                val1, freq1 = encoded1[i]
            if freq2 == 0:
                val2, freq2 = encoded2[j]

            # Minimum frequency to process
            # Why minimum? - You’re trying to multiply elements in order, and you can only match up as many pairs as the smaller of the two current runs allows.
            f = min(freq1, freq2)
            prod = val1 * val2

            # Merge with previous if same value
            if res and res[-1][0] == prod:
                res[-1][1] += f
            else:
                res.append([prod, f])

            # Subtract the portion we just used for this run
            freq1 -= f
            freq2 -= f

            # Advance to the next if current is fully exhausted
            if freq1 == 0:
                i += 1
            if freq2 == 0:
                j += 1

        return res
        

# https://leetcode.com/problems/count-largest-group/description/

from collections import defaultdict
class Solution:
    def countLargestGroup(self, n: int) -> int:
        count_map = defaultdict(int)

        for i in range(1, n + 1):
            s = self.digit_sum(i)
            count_map[s] += 1

        max_size = max(count_map.values())
        return sum(1 for v in count_map.values() if v == max_size)

    def digit_sum(self, x: int) -> int:
        total = 0
        while x > 0:
            total += x % 10
            x //= 10
        return total

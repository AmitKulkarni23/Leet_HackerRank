# https://leetcode.com/problems/first-bad-version/description/

class Solution:
    def firstBadVersion(self, n: int):
        low = 1
        high = n

        while low < high:  # We use "<" instead of "<=" to avoid unnecessary checks.
            # WHy low < high instead of low <= high? - we want teh termination condition to end on one single element
            # With low < high - the loop will terminate when low == high. This gurantees that we are left with exactly one element to inspect which is the first bad version
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid  # If mid is bad, the first bad version is at mid or before mid
            else:
                low = mid + 1  # If mid is not bad, the first bad version is after mid

        return low  # At the end of the loop, low will be the first bad version

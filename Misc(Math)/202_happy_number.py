# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its digits,
#  and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1. Those numbers for
# which this process ends in 1 are happy numbers.
#
# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    Credits -> https://leetcode.com/problems/happy-number/discuss/144154/Python-solution
    """

    # Create a set
    visited = set()

    # We will add all those numbers whose addition of square of integers do not resut in 1
    # into this so as to avoid cacluation for the same number repeatedly

    while 1:
        num = 0
        while n > 0:
            num = num + (n % 10) ** 2
            n = n // 10

        if num in visited:
            # Means we have already done the operation for this number
            return False
        if num == 1:
            return True

        visited.add(num)
        n = num

    return False

print(isHappy(29))

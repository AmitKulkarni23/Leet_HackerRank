# Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
#
# Example 1:
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# Example 2:
# Input: 3
# Output: False

import math

# Runtime -> 203ms
def judgeSquareSum(c):
    """
    :type c: int
    :rtype: bool
    """

    # Credits -> https://leetcode.com/problems/sum-of-square-numbers/solution/

    # Idea : Check if c - a^2 is a perfect square

    # Time Complexity -> Iterate sqrt(c) to find a
    # We take log(c) time to find sqrt(c)
    # Therefore time complexity = sqrt(c) * log(c)

    for a in range(int(math.sqrt(c)) + 1):
        b = math.sqrt(c - (a * a))
        if b % 1 == 0.0:
            return True

Runtime -> 115 ms
def judgeSquareSumBinarySearch(c):
    """
    :type c: int
    :rtype: bool
    Credits -> https://leetcode.com/submissions/detail/161800386/
    """

    l,r = 0, int(math.sqrt(c))
    while l <= r:
        mid = l*l + r*r
        if mid < c:
            l += 1
        elif mid > c:
            r -= 1
        else:
            return True
    return False

print(judgeSquareSum(5))

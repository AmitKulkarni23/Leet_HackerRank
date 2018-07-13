# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
#
# Example 1:
#
# Input: [5,7]
# Output: 4
# Example 2:
#
# Input: [0,1]
# Output: 0


def rangeBitwiseAnd(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    # Credits -> https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/56729/Bit-operation-solution(JAVA)  
    # Corner case
    if m == 0:
        return 0

    count = 1
    while m != n:
        # Right shift m and n
        m = m >> 1
        n = n >> 1
        count = count << 1

    return m * count

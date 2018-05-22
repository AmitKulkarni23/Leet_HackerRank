# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
#
# Given two integers x and y, calculate the Hamming distance.
#
# Note:
# 0 ≤ x, y < 231.
#
# Example:
#
# Input: x = 1, y = 4
#
# Output: 2
#
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
#
# The above arrows point to positions where the corresponding bits are different.

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    # Stratgey: We will do an XOR x ^ y and count the number of 1s in the result
    result = x ^ y
    count = 0
    while result:
        result &= result - 1
        count += 1

    return count

print(hammingDistance(1, 4))

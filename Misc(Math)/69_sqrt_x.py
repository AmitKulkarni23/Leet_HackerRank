# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """

    # Newton-Raphson method
    r = x
    while r * r - x > 0:
        # For truncated decimal part
        r = (r + x // r) // 2

        # For non-truncated decimal part
        r = (r + x / r) / 2

    return r

print(mySqrt(10))

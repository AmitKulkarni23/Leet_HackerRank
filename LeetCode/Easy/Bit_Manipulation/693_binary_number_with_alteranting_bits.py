# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
#

# Example 1:
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101

# Example 2:
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.

# Example 3:
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.

# Example 4:
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.

# Space Complexity: O(1)
# Time Complexity : O(1)

def hasAlternatingBits(n):
    """
    :type n: int
    :rtype: bool
    """
    n, rem = divmod(n , 2)

    while n:
        if n % 2 == rem:
            return False

        n, rem = divmod(n, 2)

    return True

n = 11
print(hasAlternatingBits(n))

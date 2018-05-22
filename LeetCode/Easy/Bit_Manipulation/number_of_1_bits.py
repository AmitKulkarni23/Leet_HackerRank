# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
#
# Example 1:
#
# Input: 11
# Output: 3
# Explanation: Integer 11 has binary representation 00000000000000000000000000001011
# Example 2:
#
# Input: 128
# Output: 1
# Explanation: Integer 128 has binary representation 00000000000000000000000010000000


# ALGORITHM: Brian Kernighan’s Algorithm
# Subtraction of 1 from a number toggles all the bits (from right to left) till the rightmost set
#  bit(including the righmost set bit). So if we subtract a number by 1 and do bitwise & with itself (n & (n-1)),
#  we unset the righmost set bit. If we do n & (n-1) in a loop and count the no of times loop executes we get the set bit count.
# Beauty of the this solution is number of times it loops is equal to the number of set bits in a given integer.

def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1

    return count

# Examples:
n = 128
print(hammingWeight(n))

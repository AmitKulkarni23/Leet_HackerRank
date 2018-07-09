# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
#
# Example:
# For num = 5 you should return [0,1,1,2,1,2].
#
# Follow up:
#
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """

    # Initialize an empty list
    result = []

    for i in range(num+1):
        # Call a helper function
        result.append(count_1s(i))

    return result


def count_1s(n):
    """
    Helper function which counts the number of set bits in binary representation of a number
    """
    count = 0

    if n == 0:
        return 0

    while n:
        n = n & (n-1)
        count += 1

    return count

print(countBits(7))

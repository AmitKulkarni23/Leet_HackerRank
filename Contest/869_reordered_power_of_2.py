# Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.
#
# Return true if and only if we can do this in a way such that the resulting number is a power of 2.
#
#
#
# Example 1:
#
# Input: 1
# Output: true
# Example 2:
#
# Input: 10
# Output: false
# Example 3:
#
# Input: 16
# Output: true
# Example 4:
#
# Input: 24
# Output: false
# Example 5:
#
# Input: 46
# Output: true
#
#
# Note:
#
# 1 <= N <= 10^9

import itertools
import collections

def reorderedPowerOf2(N):
    """
    :type N: int
    :rtype: bool
    """

    # Check if the given number itself is a power of 2
    if is_power_of_2(N):
        print("Given number itself is a power of 2")
        return True

    l = str(N)
    x = itertools.permutations(list(l))


    result_list = []
    for item in x:
        if item[0][0] != "0":
            result_list.append(int("".join(item)))

    # print(result_list)
    return any(is_power_of_2(x) for x in result_list)

def is_power_of_2(n):
    """
    Function to chcek if given number is power of 2
    """
    return n and not (n & (n-1))


def best_leet_code_sol(N):
    """
    :type N: int
    :rtype: bool
    """
    # Credits -> https://leetcode.com/problems/reordered-power-of-2/solution/
    # We can check whether two numbers have the same digits by comparing the count of their digits.
    # For example, 338 and 833 have the same digits because they both have exactly two 3's and one 8.
    #
    # Since Ncould only be a power of 2 with 9 digits or less ( 2 ** 30 > 10 ^ 9)
    # we can just check whether N has the same digits as any of these possibilities.

    # Create a counter object
    my_counter = collections.Counter(str(N))
    return any(my_counter == collections.Counter(str(2 ** i)) for i in range(31))

# Examples
z = 46
print(reorderedPowerOf2(z))
print(best_leet_code_sol(z))

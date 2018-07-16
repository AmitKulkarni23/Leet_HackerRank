# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, .
# .. is a 0, which is part of the number 10.


def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    # Credits -> https://leetcode.com/problems/nth-digit/discuss/88417/4-liner-in-Python-and-complexity-analysis

    # Time Complexity -> O(logn)
    # Space COmplexity -> O(logn) ( extra space for the string)
    # Explanation:
    # 1 - 9 -> There are 9 1-digit numbers
    # 10 - 99 -> There are 90 2-digit numbers
    # 100 - 99 -> There are 990 3 -digit numbers
    #

    # Start from base = 9
    # len = 1, start = 1

    # On each iteration of the while loop( while loop goes until n > len * base)
    # start = start * 10
    # base = base * 10
    # len++
    # Step 2 : Find the range(start of the range will be stored in the start variable)
    # Step 3: Calcualte the actual number and the index that we want to find
    # Return the character at the index of the actual number

    # Why are we using n - 1 -> zero based index

    start = 1
    base = 9
    len = 1

    # print("Initial n = ", n)
    while n > len * base:
        n = n - len * base
        len += 1
        start = start * 10
        base = base * 10

    # print("start = ", start)
    # print("Now n = ", n)
    target = start + (n - 1) / len
    # print("The actual number is ", target)
    remainder = (n - 1) % len
    return str(target)[remainder]

print(findNthDigit(2886))

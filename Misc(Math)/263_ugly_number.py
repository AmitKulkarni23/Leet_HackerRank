# Write a program to check whether a given number is an ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
#
# Example 1:
#
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:
#
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# Example 3:
#
# Input: 14
# Output: false
# Explanation: 14 is not ugly since it includes another prime factor 7.


def isUgly(num):
    """
    :type num: int
    :rtype: bool
    """
    if num == 0 or num == 1:
        return True

    if num < 0:
        return False

    if num % 2 == 0:
        return isUgly(num // 2)
    elif num % 3 == 0:
        return isUgly(num // 3)
    elif num % 5 == 0:
        return isUgly(num // 5)
    else:
        return False


def iterative_leet_code_sol(num):
    """
    :type num: int
    :rtype: bool
    """
    if (num <= 0):
        return False

    while ((num != 1)):
        if (num % 2 != 0 and num % 3 != 0 and num % 5 != 0):
            return False
        if (num % 2 == 0):
            num /= 2
        if (num % 3 == 0):
            num /= 3
        if (num % 5 == 0):
            num /= 5

    return True

print(isUgly(0))
print(isUgly(6))
print(isUgly(14))
print(isUgly(21))
print(isUgly(-10))
print(isUgly(8))

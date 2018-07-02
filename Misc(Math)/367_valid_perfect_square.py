# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
# Input: 16
# Returns: True
# Example 2:
#
# Input: 14
# Returns: False

def isPerfectSquare(num):
    """
    :type num: int
    :rtype: bool
    """

    # Credits -> https://www.geeksforgeeks.org/check-number-is-perfect-square-using-additionsubtraction/
    i = 1
    sum_odd_numbers = 0
    while sum_odd_numbers < num:
        sum_odd_numbers += i
        i += 2

        if sum_odd_numbers == num:
            return True

    return False


def best_leet_code_sol(num):
    """
    :type num: int
    :rtype: bool
    """

    if num == 0 or num == 1:
        return True

    if num < 0:
        # No square root for negative numbers
        return False
        
    # Use Newton Raphson method
    r = num
    while r * r - num > 0:
        r = ( r + num / r) / 2
    return r * r == num


print(isPerfectSquare(16))

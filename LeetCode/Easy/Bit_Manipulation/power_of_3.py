def power_of_3_math(n):
    """
    :type n: int
    :rtype: bool
    """
    import math
    # n = 3 ^ i
    # i = log3(n)
    # i = log10(n) / log10(3)
    # return (math.log(n, 10) / math.log(3, 10)) % 1 == 0;


def isPowerOfThree_integer_limitation(n):
    """
    :type n: int
    :rtype: bool
    """
    # Integer limitation
    # We know that the max integer number held is 3 ^ 19
    # There if the given number completely divides 3 ^ 19, then return true

    return n > 0 and ( 3 ** 19 % n) == 0

def isPowerOfThree_recursive(n):
    """
    :type n: int
    :rtype: bool
    """
    # print n
    if n < 1:
        return False
    if n == 1:
        return True
    if n%3:
        return False
    return self.isPowerOfThree(n/3)

print(power_of_3_math(81 * 9))
print(power_of_3_math(45))

# Write a program to calculate pow(x,n)
# Given two integers x and n, write a function to compute xn. We may assume that x and n are small and overflow doesn’t happen.


def power(x, y):
    """
    Function that cacluates x ^ y
    Can work for -ve y
    """
    temp = 0.0
    if y == 0:
        # Anything raised to 0 is 1
        return 1

    temp = power(x, int(y / 2))
    if y  % 2 == 0:
        # If it is an even power
        return temp * temp
    else:
        # Odd power
        if y > 0:
            return x * temp * temp
        else:
            return (temp * temp) / x


def power_iterative(x, n):
    """
    Iterative solution for finding pow(x, n)
    """
    res = 1.0

    if n < 0:
        x = 1 / x

    while n != 0:
        # If n is odd
        if n & 1:
            res = res * x

        n = int(n / 2)
        x = x * x

    return res
# Examples:
x = 2.0
y = -2
print(power(x, y))
print(power_iterative(x, y))

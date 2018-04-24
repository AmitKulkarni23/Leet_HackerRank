"""
Python program to check if ith bit is set in the binary representation of a given number

To check if the ith bit is set or not (1 or not), we can use AND operator
And the given number with 2^i. In 2 ^ i only the ith bit is set.
All the other bits are zero.
If numb & ( 2 ^ i) returns a non-zero number then the ith bit in the given number is set



How to get 2 ^ i. Use the left -shift operator <<( i.e 1 << i)
"""


def ith_bit_set(numb, i):
    """
    Method to check if the ith bit is set in a given number
    :param numb: integer
    :param i: integer i
    :return: true, iff the ith bit is set in teh given number

    Example: N = 20 = {10100}2  => ith_bit_set(20, 2) returns True
    """

    if numb & (1 << i):
        return True

    return False


print(ith_bit_set(20, 2))

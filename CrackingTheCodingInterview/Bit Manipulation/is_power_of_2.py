"""
Python program to check if a given number is power of 2

Design Strategy: A given number is a power of 2 if that (numb) & (numb -1) == 0
where number is represented in binary form

Pythonic way to convert a number into its binary form is bin(numb)
"""


def is_power_of_2(numb):
    """
    Method to check if a given number is a power of 2 or not
    :param numb: a +ve integer
    :return: true, iff the number is power of 2
    """

    return not (numb & numb-1)


print(is_power_of_2(256))
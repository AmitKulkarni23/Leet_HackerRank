"""
Program to count teh number of 1s in the binary representation of a given number


Running time: number of 1s in the binary representation of the number
Use teh relationship between (numb) and (numb - 1)

In (numb -1) -> the rightmost 1 and the bits right to it are flipped
For example:
4 -> 100
3 -> 011

By reducing the given number numb = numb & (numb - 1)
We are storing in number, we are reducing the given numb to a number containing ones 1less than than the
number of ones present in its previous state
"""


def count_numb_of_1s(numb):
    """
    Count the number of 1s in the given integer
    :param numb: an integer
    :return: number of 1s in the binary form of numb

    Example: 23 = {10111}2
    """
    count = 0
    while numb:
        numb = numb & (numb -1)
        count += 1

    return count


print(count_numb_of_1s(23))


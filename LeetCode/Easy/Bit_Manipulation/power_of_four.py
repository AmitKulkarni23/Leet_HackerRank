# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
def isPowerOfFour(self, num):
    """
    :type num: int
    :rtype: bool
    """
    # return bool(num == (num & -num) and num.bit_length() %2)
    if num <= 0:
        return False

    return bool((num & (num -1)) == 0 and num.bit_length() % 2)

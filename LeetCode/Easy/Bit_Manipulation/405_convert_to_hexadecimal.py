# Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed integer.
# You must not use any method provided by the library which converts/formats the number to hex directly.
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"

def toHex(num):
    """
    :type num: int
    :rtype: str
    """
    # Credits -> https://leetcode.com/problems/convert-a-number-to-hexadecimal/discuss/145650/20ms-python-solution-100-beat
    # Create a dictinary to hold mapping of numbes and cahracters
    my_dict = {
                10: 'a',
                11: 'b',
                12: 'c',
                13: 'd',
                14: 'e',
                15: 'f'}

    if num < 0:
        # If the given number is negative
        num = 0xffffffff + num + 1

    result_list = []
    res = 0

    # Note: my_dict.get(key, default = None)
    # # Returns a defualt value if the key is not found

    while  num >= 16:
        res = num%16
        num = num/16
        result_list = [my_dict.get(res, "%s" % res)] + result_list


    result_list = [my_dict.get(num, "%s" % num)] + result_list
    return ''.join(x for x in result_list)


# Examples:
print(toHex(10))

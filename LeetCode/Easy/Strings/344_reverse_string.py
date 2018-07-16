# Write a function that takes a string as input and returns the string reversed.
#
# Example:
# Given s = "hello", return "olleh".

def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    # Method 1:
    # use for loop
    # This gave me Memory Limit Exceeded
    x = ""
    for i in s:
        x = i + x

    return x

    # Method 2
    # Recursion
    # if len(s) == 0:
    #     return s
    # else:
    #     return reverseString(s[1:]) + s[0]

    # ACCEPTED ON LEETCODE
    # LOWEST TIME
    # Method 3:
    # using slice index
    # return s[::-1]

    # Method 4:
    # Using reversed
    # s = "".join(reversed(s))
    # return s
print(reverseString("abc def"))

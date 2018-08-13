# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is represented as a string.
#
# Example 1:
#
# Input:  "69"
# Output: true
# Example 2:
#
# Input:  "88"
# Output: true
# Example 3:
#
# Input:  "962"
# Output: false

# Runtime -> 20ms
def isStrobogrammatic(num):
    """
    :type num: str
    :rtype: bool
    """
    # Credits -> https://leetcode.com/problems/strobogrammatic-number/discuss/67203/1-liners-Python

    return all(c + d in "69 96 88 11 00" for c,d in zip(num, num[::-1]))

# Runtime -> 16ms
def isStrobogrammatic_best_leetcode_sol(num):
    """
    :type num: str
    :rtype: bool
    """
    sd = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}

    for i in xrange(len(num)/2+1):
        if num[i] in sd and sd[num[i]]==num[-1-i]:
            continue
        else:
            return False

    return True

# Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.
#
# Please note that the string does not contain any non-printable characters.
#
# Example:
#
# Input: "Hello, my name is John"
# Output: 5

def countSegments(s):
    """
    :type s: str
    :rtype: int
    """
    # Credits: https://leetcode.com/problems/number-of-segments-in-a-string/solution/
    count = 0

    for i in range(len(s)):
        if (i == 0 or s[i-1] == " ") and s[i] != " ":
            count += 1

    return count

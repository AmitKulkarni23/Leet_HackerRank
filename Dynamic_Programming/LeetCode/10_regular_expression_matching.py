# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
# Example 5:
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    s_len = len(s)
    p_len = len(p)

    if s_len == 0 and p_len == 0:
        return True

    # Create a cache
    cache = [[False for _ in range(p_len + 1)] for _ in range(s_len + 1)]

    # Empty string and empty pattern is a match
    cache[0][0] = True
    
    # Populate 0th row( 0th column is already populated)
    # If pattern is a* or a*b* then cache[i][j] = True
    for i in range(1, p_len + 1):
        if p[i-1] == "*":
            cache[0][i] = cache[0][i-2]

    # Iterate through the text and the pattern
    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):

            # First condition
            if s[i - 1] == p[j - 1] or p[j -1] == ".":
                cache[i][j] = cache[i-1][j-1]
            # Check for *
            elif p[j - 1] == "*":
                # Check for 0 occurrences
                if cache[i][j-2]:
                    cache[i][j] = True

                elif s[i - 1] == p[j-2] or p[j-2] == ".":
                    cache[i][j] = cache[i-1][j]

    return cache[-1][-1]


# Examples
# s = "aab"
# p = "c*a*b"

s = "mississippi"
p = "mis*is*p*."
print(isMatch(s, p))

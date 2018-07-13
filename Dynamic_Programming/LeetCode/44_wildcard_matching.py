# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
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
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false


def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    # Credits -> https://www.youtube.com/watch?v=3ZDZ-N0EPV0
    s_len = len(s)
    p_len = len(p)

    if s_len == 0 and p_len == 0:
        return True

    if p_len == 0:
        return False
    # We need to eliminate consecutive **
    # For instance a**b**c => a*b*c

    is_first = True
    pattern_list = []
    for i in range(p_len):
        if p[i] == "*":
            if is_first:
                pattern_list.append(p[i])
                is_first = False
        else:
            pattern_list.append(p[i])
            is_first = True

    new_p = "".join(pattern_list)
    np_len = len(new_p)

    # Create a cache
    cache = [[False for _ in range(np_len + 1)] for _ in range(s_len + 1)]

    cache[0][0] = True

    # Fill the first row
    if new_p[0] == "*" and len(pattern_list) > 0:
        cache[0][1] = True


    # Now iterate through s and p
    for i in range(1, s_len + 1):
        for j in range(1, np_len + 1):

            if s[i-1] == new_p[j-1] or new_p[j-1] == "?":
                cache[i][j] = cache[i-1][j-1]

            elif new_p[j-1] == "*":
                cache[i][j] = cache[i-1][j] or cache[i][j-1]


    return cache[-1][-1]

def best_leetcode_sol(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """

    #if not p or len(p) == 0:
    #    return True

    ss, pp = 0, 0
    match, star = -1, -1

    while (ss < len(s)):
        if pp < len(p) and (s[ss] == p[pp] or p[pp] == '?'):
            ss += 1
            pp += 1
        elif pp < len(p) and p[pp] == '*':
            star = pp
            pp += 1
            match = ss
        elif star != -1:
            pp = star + 1
            match += 1
            ss = match
        else:
            return False

    while (pp < len(p)):
        if p[pp] != '*':
            return False
        pp += 1

    return True

# Examples
s = "aaaa"
p = "************a"

print(isMatch(s, p))

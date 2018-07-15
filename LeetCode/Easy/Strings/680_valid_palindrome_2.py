# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
#
# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.


def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    if s == s[::-1]:
        # The given string itself is a palindrome
        return True

    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            # Then we can do one insertion or deletion
            return is_palin(s, start+1, end) or is_palin(s, start, end-1)
        start += 1
        end -= 1

    return True


def is_palin(s, start, end):
    """
    Helper function which returns whether a given string is plaindrome or not
    """

    while start < end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True

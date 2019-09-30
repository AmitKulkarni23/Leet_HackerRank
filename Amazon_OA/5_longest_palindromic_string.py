# https://leetcode.com/problems/longest-palindromic-substring/

def longestPalindrome(s: str) -> str:
    # Credits -> https://leetcode.com/problems/longest-palindromic-substring/discuss/2954/Python-easy-to-understand-solution-with-comments-(from-middle-to-two-ends). by user kanhar22

    # Idea: Expand around the center of the palindrom
    # How many centers? -> 2n - 1
    # For example the palindrome "abba" center is between 2 b's.
    # Consider the string "abc". Possible centers are ('a'), (between 'ab'), ('b'), (between 'bc'), ('c')
    # Keep moving and keep moving right until the substring is not a palindrome

    # 2n - 1 centers. Expanding around each center could take O(n) time
    # Time - O(n ^ 2)
    # Space - O(1)

    res = ""

    for i in range(len(s)):
        odd = expand_around_center(i, i, s)
        even = expand_around_center(i, i + 1, s)

        res = max(odd, even, res, key=len)

    return res


def expand_around_center(left, right, s):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left + 1: right]
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid palindrome.
#
# Example 1:
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:
#
# Input: "race a car"
# Output: false

# Runtime - 73ms
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    final_str = [ch for ch in s if ch.isalnum()]
    return final_str == final_str[::-1]

# Runtime 50ms
def best_leet_code_sol(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower()
    s = filter(str.isalnum, str(s))
    # ''.join([i for i in s if i.isalpha() or i .isdigit()])
    return s == s[::-1]
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("aa"))
print(isPalindrome("b"))
print(isPalindrome("bbc"))
print(isPalindrome(",."))

# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # If teh lenghts of 2 strings are different then they cannot be anagrams
    if len(s) != len(t):
        return False

    # Create a list containing of length 26
    my_table = [0] * 26

    # Put everything present in string s in a dictionary
    for item in s:
        my_table[ord(item) - ord('a')] += 1

    # Iterate through the t string
    for item in t:
        my_table[ord(item) - ord('a')] -= 1
        if my_table[ord(item) - ord('a')] < 0:
            return False

    return True

def best_leet_code_sol(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    l = 'abcdefghijklmnopqrstuvwxyz'
    for i in l:
        if(s.count(i) != t.count(i)):
            return False
    return True

# Test Examples
s = "anagram"
t = "nagaram"
print(isAnagram(s, t))


x = "rat"
y = "car"
print(isAnagram(x, y))

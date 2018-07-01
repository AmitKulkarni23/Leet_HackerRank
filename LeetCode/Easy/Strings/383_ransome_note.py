# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """

    mag = list(magazine)

    for ch in ransomNote:
        if ch in mag:
            mag.remove(ch)
        else:
            return False

    return True

def best_leetcode_sol(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """

    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True
# Examples:
print(best_leetcode_sol("a", "b"))
print(best_leetcode_sol("aa", "ab"))
print(best_leetcode_sol("aa", "aab"))

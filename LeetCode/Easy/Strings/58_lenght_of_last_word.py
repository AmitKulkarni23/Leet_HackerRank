# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5

# Runtime : 33ms
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """

    if not s:
        return 0

    word_count = 0
    no_real_char = True

    for ch in s[::-1]:
        if ch == " " and no_real_char:
            continue
        if ch != " ":
            word_count += 1
            no_real_char = False
        else:
            break

    return word_count

# Runtime : 29ms
def best_leet_code_sol(s):
    """
    :type s: str
    :rtype: int
    """
    # string.split -> Gives us a list of words separated by " "
    split = s.split()
    if len(split) == 0:
        return 0
    return len(split[-1])
print(lengthOfLastWord("a "))

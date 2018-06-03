# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
#
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".

def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    s_list = []
    t_list = []
    for x in S:
        if x != "#":
            s_list.append(x)
        else:
            if s_list:
                s_list.pop()
    for y in T:
        if y != "#":
            t_list.append(y)
        else:
            if t_list:
                t_list.pop()
    return "".join(s_list) == "".join(t_list)

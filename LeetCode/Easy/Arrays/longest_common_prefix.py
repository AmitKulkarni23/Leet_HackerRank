# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

# Examples:
# Input: ["flower","flow","flight"]
# Output: "fl"
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    # Design Stratgey: Iterate through all the elements present in the strs list
    # Compare the first characters in each of them.
    # If they are the same store this character in a string & move on to teh second character..
    # If not, break out of it

    if strs:
        shortest_str = min(strs, key=len)
        for i, char in enumerate(shortest_str):
            for other_str in strs:
                if other_str[i] != char:
                    return shortest_str[:i]

        return shortest_str
    else:
        return ""

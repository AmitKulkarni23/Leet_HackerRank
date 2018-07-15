# Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
#
# Substrings that occur multiple times are counted the number of times they occur.
#
# Example 1:
# Input: "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
#
# Notice that some of these substrings repeat and are counted the number of times they occur.
#
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:
# Input: "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
# Note:
#
# s.length will be between 1 and 50,000.
# s will only consist of "0" or "1" characters.

# Time Complexity -> O(n)
# Space COmplexity -> O(n)
def countBinarySubstrings_approach1(s):
    """
    :type s: str
    :rtype: int
    """
    # Credits -> https://leetcode.com/problems/count-binary-substrings/solution/

    # Create groups
    # The first element in the string is a group by itself
    groups = [1]


    # Now iterate through the string
    for i in range(1, len(s)):
        # If it is the same same character as previous icrement the count
        if s[i-1] == s[i]:
            # Increment the last groups count
            groups[-1] += 1
        else:
            # Create a new group
            groups.append(1)

    # Now we have got the groups
    # How to calculate th answer
    # The maximum length of 0s and ones can be min(groups[i], groups[i])
    # Because the binary digits to teh left or right must change and our answer
    # can never be larger

    ans = 0
    for i in range(len(groups) - 1):
        ans += groups[i] + groups[i+1]

# Time Complexity -> O(n)
# Space COmplexity -> O(1)
def countBinarySubstrings_approach2(s):
    """
    :type s: str
    :rtype: int
    """
    # Credits -> https://leetcode.com/problems/count-binary-substrings/solution/

    # Similar to approach 1
    # Maintain the count variables

    prev = 0
    cur = 1

    ans = 0

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cur += 1
        else:
            ans += min(prev, cur)
            prev = cur
            cur = 1


    return ans + min(prev, cur)

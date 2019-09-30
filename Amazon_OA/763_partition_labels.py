# A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that
# each letter appears in at most one part, and return a list of integers representing the size of these parts.

# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

######################################################################################

def partitionLabels(S):
    # Credits -> https://leetcode.com/problems/partition-labels/discuss/113259/Java-2-pass-O(n)-time-O(1)-space-extending-end-pointer-solution

    # Time - > O(n)
    # Space -> O(1)

    # Create a list that stores the index of the last occurrence of the character
    char_map = [0] * 26

    for i, ch in enumerate(S):
        char_map[ord(ch) - ord('a')] = i

    start, last = 0, 0
    result = []

    for i, ch in enumerate(S):
        last = max(last, char_map[ord(ch) - ord('a')])

        if last == i:
            # This is the index where this is character last occurs.
            # We need a split point here.
            # Append the lenght of the substring to result
            result.append(last - start + 1)

            # A new start
            start = last + 1

    return result

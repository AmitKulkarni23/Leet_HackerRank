# In a string S of lowercase letters, these letters form consecutive groups of the same character.
#
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
#
# The final answer should be in lexicographic order.
# Example 1:
#
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
# Example 2:
#
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
# Example 3:
#
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
def largeGroupPositions(S):
    """
    :type S: str
    :rtype: List[List[int]]
    """
    if len(S) < 3:
        return []
    #Index varaiables
    i = 0
    j = 1

    # The final list that wll be returned
    final_list = []

    # A boolean varaibale that is set to true as soon as a contiguous
    # array is found of any size
    contig = False


    while i < j:
        if S[i] == S[j]:
            # keep on incrementing j until we find a mismatch
            j += 1
            contig = True

        # Corner condition
        # Since we are incrementing j above
        # need to check for array index out of bounds
        if j >= len(S):
            if contig and (j - i >= 3):
                final_list.append([i, j - 1])
                return final_list
            else:
                return final_list

        # Now we have reached the end point
        if S[i] != S[j]:
            if contig and (j - i >= 3):
                # That means there was a contiguous sub-array
                # Doing a j - 1 becuase j was already 1 step ahead of i and was incremented
                # an additional time ( j += 1) in the above if condition
                final_list.append([i, j - 1])
                i = j - 1
                j = i + 1
                contig = False

            else:
                # There was no contiguous array
                i = j
                j = i + 1


        if i == len(S) - 1:
            # We have reached the end of the array
            # There is no need to append anything
            break

    return final_list

S = "abbxxxxzzy"
S1 = "abc"
S2 = "abcdddeeeeaabbbcd"
S3 = "aaa"
S4 = "aaab"
print(largeGroupPositions(S2))

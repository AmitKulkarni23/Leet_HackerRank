# S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
#
# S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.
#
# Return any permutation of T (as a string) that satisfies this property.
#
# Example :
# Input:
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
# Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.
#
#
# Note:
#
# S has length at most 26, and no character is repeated in S.
# T has length at most 200.
# S and T consist of lowercase letters only.

import collections
def customSortString(S, T):
    """
    :type S: str
    :type T: str
    :rtype: str
    """

    # Credits -> https://leetcode.com/problems/custom-sort-string/solution/
    # IDEA: 1) Write to our answer elements of T that occur in S, in order of S
    # 2) Second write -> Write all elements of T to our that we previously did not write

    # First step -> maintain count of elements occurring in T
    count = collections.Counter(T)

    answer = []

    # Iterate through thecharacters in S
    for c in S:
        answer.append(count[c] * c)

        # make count[c] = 0, to indicate that we do no nned to write this to our
        # answer anymore
        count[c] = 0


    # Second write operation
    for k in count:
        answer.append(k * count[k])

    # Return the list converted to a string
    return "".join(answer)

# Examples:
S = "cba"
T = "abcd"

print(customSortString(S, T))

# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.
#
#
#
# Example 1:
#
# Input: A = "ab", B = "ba"
# Output: true
# Example 2:
#
# Input: A = "ab", B = "ab"
# Output: false
# Example 3:
#
# Input: A = "aa", B = "aa"
# Output: true
# Example 4:
#
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:
#
# Input: A = "", B = "aa"
# Output: false
#
#
# Note:
#
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.

########################################

def buddyStrings(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """
    # Time Complexity: O(N)
    # Space COmplexity : O(1)

    # Credits -> https://leetcode.com/problems/buddy-strings/solution/

    # If suppose A == B
    # Then there should be atleast 1 occurrence of a character that occurs twice

    # If A != B
    # A and B will be buddy strings if there is mismatch in 2 indices only

    # Suppose we switch the ith and jth indices in A
    # then the following must be true

    # A[i] = B[j] and A[j] = B[i]

    if len(A) != len(B):
            return False

    my_set = set()

    if A == B:
        for a in A:
            if a in my_set:
                return True
            my_set.add(a)
        # There are no 2 occurrences of any character
        return False

    else:
        # Create a temp array
        temp = []

        for c1, c2 in zip(A, B):
            if c1 != c2:
                temp.append((c1, c2))

        if len(temp) >= 3:
            return False

        # If len(temp) == 2 check for the condition A[i] = B[j] and A[j] = B[i]
        return len(temp) == 2 and temp[0] == temp[1][::-1]

# Examples:
A = "aaaaaaabc"
B = "aaaaaaacb"
print(buddyStrings(A, B))

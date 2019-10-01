# https://leetcode.com/discuss/interview-question/370157
# Time - O(n)
# Space -> O(n)
# Solution Credits -> https://leetcode.com/playground/j9sVKJaQ

# Approach - https://leetcode.com/problems/subarrays-with-k-different-integers/discuss/235235/C%2B%2BJava-with-picture-prefixed-sliding-window
# if substring [left, right] contains K unique elements and the first "prefix" number of  charcters appear in the subarray
# [left + prefix, right] then we have a total of 1 + prefix valid substrings

# Example:
# "pqpqs"
# First 2 characters "pq" (left = 0, right = 2) appear in the the subarray "pqs" ( here prefix = 2, left = 2, right = 5 )
# Valid substrings => "pq", "qp", "pq" ( 1 + prefix valid substrings )

# Use 2 pointers to iterate through the string
# [left, right]
# Use a sliding window approach
# back of the window is right, front of the window is left

# The front of teh window is moved so that s[left] appears only once
# We shrinking our window maintaining the same number of elements

# Maintain a dictionary that counts the number of times a character appears in the window
# After we add a new character to the window, try to remove as many as possible characters from the front.
# so that the character at front appears only once.

# If we collected k different/unique chars then we have 1 + prefix valid substrings

# If we reached k + 1 chars, remove one char from left and reset the prefix to 0 as we are starting a new sequence.


def findSubstring(m, k):
    A = list(m)
    left, right = 0, 0

    num_count = {}
    distinct = 0
    result = 0
    prefix = 0

    while right < len(A):
        if A[right] in num_count and num_count[A[right]] != 0:
            # Such a character is already present
            num_count[A[right]] += 1
        else:
            # First occurrence of such a character
            distinct += 1
            num_count[A[right]] = 1

        if distinct > k:
            num_count[A[left]] -= 1
            prefix = 0
            distinct -= 1
            left += 1

        while num_count[A[left]] > 1:
            num_count[A[left]] -= 1
            left += 1
            prefix += 1

        if distinct == k:
            result += 1 + prefix

        right += 1

    return result

print(findSubstring("pqpqs", 2))
print(findSubstring("aabab", 3))
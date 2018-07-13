# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Time COmplexity : O(n) -> Iterating only once through the array
# Space Complexity : O(n) -> USed cache

def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """

    # Credits -> https://leetcode.com/problems/decode-ways/discuss/30358/Java-clean-DP-solution-with-explanation
    # Credits -> https://www.youtube.com/watch?v=RgrCL-wU110
    str_len = len(s)

    # Corner cases
    if str_len == 0:
        return 0

    # Create a cache
    cache = [0] * (str_len + 1)

    # if there was an empty string, there is only way 1 to decode it
    cache[0] = 1

    # Now if the string begins with 0
    if s[0] == 0:
        cache[1] = 0
    else:
        cache[1] = 1

    # Now iterate through the string and populate teh cache
    for i in range(2, str_len + 1):
        first = int(s[i-1])
        second = int(s[i-2] + s[i-1])

        if first >= 1 and first <= 9:
            cache[i] += cache[i-1]

        if second >= 10 and second <= 26:
            cache[i] += cache[i-2]

    # Finally return
    return cache[str_len]
# Examples
input = "1234"
print(numDecodings(input))

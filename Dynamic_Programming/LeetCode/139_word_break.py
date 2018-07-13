# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
# Note:
#
# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

import pprint
def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    # Credits -> https://www.youtube.com/watch?v=WepWFGxiwRs
    # Credits -> https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/BreakMultipleWordsWithNoSpaceIntoSpace.java

    word_len = len(s)

    # Create a cache
    cache = [[False for _ in range(word_len)] for _ in range(word_len)]

    # Matrix that will be used to print the actual words
    # print_matrix = [[-1 for _ in range(word_len)] for _ in range(word_len)]

    # Fill the matrix in bottom up manner
    for l in range(1, word_len + 1):
        for i in range(word_len - l + 1):
            j = i + l - 1

            temp_word = s[i:j+1]

            # If temp_word is in dictionary
            # cache[i][j] = True
            if temp_word in wordDict:
                cache[i][j] = True
                continue

            # If not
            # Find k such that T[i][k] and T[i+1][j] is true
            for k in range(i+1, j+1):
                if cache[i][k-1] and cache[k][j]:
                    cache[i][j] = True
                    break

    # pprint.pprint(cache)
    return cache[0][-1]

def best_leet_code_sol(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    l = len(s)
    dp = [False for i in range(l+1)]
    dp[0] = True
    for i in range(1, l+1):
        for w in wordDict:
            if len(w)<=i and dp[i-len(w)] and s[i-len(w):i] == w:
                dp[i] = True
                break

    print(dp)
    return dp[l]

# Examples
# s = "leetcode"
# wordDict = ["leet", "code"]

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]

# print(wordBreak(s, wordDict))
print(best_leet_code_sol(s, wordDict))

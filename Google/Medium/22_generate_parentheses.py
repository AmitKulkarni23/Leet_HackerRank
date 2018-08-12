# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    # Credits -> https://leetcode.com/problems/generate-parentheses/solution/

    # Put up an opening bracket if we have one of n places left
    # Put up closing bracket if it doesn't exceed the number of opening brackets
    ans = []
    backtrack(ans, n)
    return ans


def backtrack(ans, N, S="", left=0, right=0):
    """
    This is the helper function
    """
    if len(S) == 2*N:
        # This is our base case
        ans.append(S)
        return

    if left < N:
        backtrack(ans, N, S + "(", left + 1, right)

    if right < left:
        backtrack(ans, N, S + ")", left, right + 1)


#Examples
print(generateParenthesis(3))
